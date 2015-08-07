from google.appengine.ext.webapp import template
import webapp2


class Handler(webapp2.RequestHandler):
    def get(self):
        self.response.write(template.render("template.html", {}))


app = webapp2.WSGIApplication([
    ("/", Handler)
], debug=True)
