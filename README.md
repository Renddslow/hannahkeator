# HannahKeator.org
This is a simple single page site for a friend of mine to have some level of web presence that she can update via SMS.

## Getting Started
HannahKeator.org runs on Python with [Redis](https://redis.io/topics/quickstart) as a simple db. You will need to have both installed to proceed.

### Prerequisites
You will need to have a virtual environment setup to run the app

`sudo apt-get install virtualenv`


### Installing

The repository comes complete with the virtualenv with all of our dependencies already installed. We are using the following depenencies:
- [Flask](http://flask.pocoo.org/)
- [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)
- [redis](https://pypi.python.org/pypi/redis)

So all we have to do is pop on into the virtual environment

`source env/bin/activate

and run `python app.py` to get things going.
