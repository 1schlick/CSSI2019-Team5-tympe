import webapp2
import os
import jinja2
import random
import threading


class Score():
    def __init__(num):
        score = num

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
            if self.render.get("#word") == "Game Over":
                points = self.render.get("#points")
                score = Score(int(points))
                score.put()
                topScores = Score.query().order(Score.score).fetch(5)


                end_template = jinja_current_dir.get_template("/templates/Scores.html")
                self.response.write(end_template.render())

class score(webapp2.RequestHandler):
    def get(self):
        end_template = jinja_current_dir.get_template("/templates/Scores.html")
        self.response.write(end_template.render())

app = webapp2.WSGIApplication([
    ('/', welcome),
    ('/game', game),
    ('/score', score)
], debug=True)
