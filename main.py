import webapp2
import os
import jinja2
import random



jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



class welcome(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("Welcome.html")
        self.response.write(start_template.render())

    def post(self):
        f = open("words.txt", "r")
        fl = []

        for x in f:
            fl.append(x)

        randWord = fl[random.randint(0,999)]
        dict = {"word": randWord}
        end_template = jinja_current_dir.get_template("Game.html")
        self.response.write(end_template.render(dict))

class game(webapp2.RequestHandler):
    def get (self):
        


app = webapp2.WSGIApplication([
    ('/', welcome),
    ('/game', game)
], debug=True)
