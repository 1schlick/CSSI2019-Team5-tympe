import webapp2
import os
import jinja2

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class thingy(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("Welcome.html")
        self.response.write(start_template.render())

    def post(self):
        end_template = jinja_current_dir.get_template("Game.html")
        self.response.write(end_template.render())

app = webapp2.WSGIApplication([
    ('/', thingy)
], debug=True)
