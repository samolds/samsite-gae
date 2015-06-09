import webapp2
import settings
from controllers import home
from controllers import greet
from controllers import admin


app = webapp2.WSGIApplication([
  ('/', home.Home),
  ('/greet', greet.Greet),
  ('/admin', admin.Admin),
], debug=settings.DEBUG)
