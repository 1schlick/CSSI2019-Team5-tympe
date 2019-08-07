import webapp2
import os
import jinja2
import random
import threading

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class welcome(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("/templates/Welcome.html")
        self.response.write(start_template.render())

    def post(self):
        end_template = jinja_current_dir.get_template("/templates/Game.html")
        self.response.write(end_template.render())

class game(webapp2.RequestHandler):
    def get(self):
        while true:
            if self.render.get("word") == "Game Over":
                end_template = jinja_current_dir.get_template("/templates/Scores.html")
                self.response.write(end_template.render())

class score(webapp2.RequestHandler):
    def get(self):
        dict = {"points": self.render.get("points"),
                "score": int(self.render.get("points"))/60.0}
        end_template = jinja_current_dir.get_template("/templates/Scores.html")
        self.response.write(end_template.render(dict))

app = webapp2.WSGIApplication([
    ('/', welcome),
    ('/game', game),
    ('/score', score)
], debug=True)
