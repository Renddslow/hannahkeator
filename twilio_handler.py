import random
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom


class Messages:
	success_messages = [
		"Good job, Hannah! Your updates have been made!",
		"Wow, look at you changing the world one update at a time!",
		"Congrats, that thing you wrote is now a thing!",
		"You've got it! Consider it done!"
	]
	success = random.choice(success_messages)
	
	numbers = "It doesn't look like your number is allowed to update Hannah's site. You'll have to ask Hannah for access. Don't worry, she'll know what to do."
	
	instructions = "Woops, that's not a command we recognize. Available commands include:\ntitle\npic\nstatus\nnumbers"
	

	def display_message(self, message):
		response = Element('Response')
		message_tag = SubElement(response, 'Message')
		message_tag.text = message
		return self.prettify(response)

	
	def prettify(self, message):
		rough_string = tostring(message, 'utf-8', method='xml')
		reparsed = minidom.parseString(rough_string)
		return reparsed.toprettyxml(indent="  ")
