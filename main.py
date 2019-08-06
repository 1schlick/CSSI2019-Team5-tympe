import webapp2
import os
import jinja2
import random



jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

text = open("words.txt", "r")
list = []

for x in text:
    list.append(x)

class welcome(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("/templates/Welcome.html")
        self.response.write(start_template.render())

    def post(self):
        dict = {"randWord": list[random.randint(0,999)]}
        end_template = jinja_current_dir.get_template("/templates/Game.html")
        self.response.write(end_template.render(dict))

class game(webapp2.RequestHandler):
    correct = True
    def get(self):
        if self.correct:
            self.randWord = list[random.randint(0,999)]
        self.userWord = self.request.get("userWord")

    def post(self):
        if self.randWord == self.userWord:
            self.correct = True
        else:
            self.correct = False
        end_template = jinja_current_dir.get_template("/templates/Game.html")
        self.response.write(end_template.render(self.dict))


app = webapp2.WSGIApplication([
    ('/', welcome),
    ('/game', game)
], debug=True)
