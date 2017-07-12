import requests
from flask import Flask, render_template, request, Response
import redis

from twilio_handler import Messages

application = Flask(__name__)


@application.route("/")
def home():
	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	title = str(r.get("hk:title"))
	img_src = r.get("hk:img")
	status = str(r.get("hk:status"))
	return render_template("home.html",
							title=title,
							img_src=img_src,
							status=status)


@application.route("/update", methods=["POST"])
def update():
	m = Messages()

	body = request.form
	_from = body['From']
	msg_body = body['Body']
	
	if 'MediaUrl0' in body:
		media = body['MediaUrl0']
	else:
		media = None
	
	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	instructions = ["status", "pic", "title", "numbers"]

	allowed_numbers = r.get("hk:numbers")

	if _from in allowed_numbers.split(","):
		updates = 0
		
		if media:
			try:
				headers = {
					"Authorization": "Client-ID cbd22022907d26a"
				}
				form_data = {
					"image": media
				}
				image_uri = requests.post("https://api.imgur.com/3/upload",
											headers=headers,
											data=form_data).json()['data']['link']
			except Exception as e:
				print(e)
				return m.display_message("Whoops, that image didn't work. Maybe try a different one.")
			else:
				r.set("hk:img", image_uri)
				return m.display_message(m.success)
	
		for line in msg_body.split("\n"):
			content = line.split("=")
			if content[0].strip().lower() in instructions:
				if content[0].strip().lower() == "status":
					r.set("hk:status", content[1].strip())
					updates = updates + 1
				elif content[0].strip().lower() == "title":
					r.set("hk:title", content[1].strip())
					updates = updates + 1
				elif content[0].strip().lower() == "numbers":
					numbers = r.get("hk:numbers")
					numbers = numbers + "," + content[1].strip()
					r.set("hk:numbers", numbers)
					updates = updates + 1
		if updates:
			response = m.display_message(m.success)
		else:
			response = m.display_message(m.instructions)
	else:
		response = m.display_message(m.numbers)
	return Response(response, mimetype='text/xml')

if __name__ == "__main__":
	application.run(host='0.0.0.0')
