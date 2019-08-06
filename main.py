import webapp2
import os
import jinja2
import random



jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

text = open("test.txt", "r")
list = []

for x in text:
    list.append(x)

score = 0

class welcome(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("/templates/Welcome.html")
        self.response.write(start_template.render())

    def post(self):
        global score
        score = 0
        dict = {"randWord": list[0],
                "score": 0}
        end_template = jinja_current_dir.get_template("/templates/Game.html")
        self.response.write(end_template.render(dict))

class game(webapp2.RequestHandler):
    randWord = ""
    userWord = ""



    def post(self):
        self.randWord = list[0]
        self.userWord = self.request.get("userWord")
        if self.randWord == "word":
            global score
            score += 1

        dict = {"randWord": self.randWord,
                "score": str(score)}
        end_template = jinja_current_dir.get_template("/templates/Game.html")
        self.response.write(end_template.render(dict))


app = webapp2.WSGIApplication([
    ('/', welcome),
    ('/game', game)
], debug=True)
