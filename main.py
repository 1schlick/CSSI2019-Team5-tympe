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
        end_template = jinja_current_dir.get_template("/templates/Game.html")
        self.response.write(end_template.render())
        threading.Timer(20,post).start()

    def gameOver(self):
        self.points = self.render.get("points")
        #score = Score(int(points))
        #score.put()
        #topScores = Score.query().order(Score.score).fetch(1)
        dict = {"points": self.points}
        #        "1": topScores[0],
        #        "2": topScores[1],
        #        "3": topScores[2],
        #        "4": topScores[3],
        #        "5": topScores[4]}
        end_template = jinja_current_dir.get_template("/templates/Scores.html")
        self.response.write(end_template.render(dict))

    def post(self):
        end_template = jinja_current_dir.get_template("/templates/Welcome.html")
        self.response.write(end_template.render())

class score(webapp2.RequestHandler):
    def get(self):
        dict = {"points": 67}
        end_template = jinja_current_dir.get_template("/templates/Scores.html")
        self.response.write(end_template.render(dict))

    def post(self):
        start_template = jinja_current_dir.get_template("/templates/Welcome.html")
        self.response.write(start_template.render())

app = webapp2.WSGIApplication([
    ('/welcome', welcome),
    ('/game', game),
    ('/score', score)
], debug=True)
