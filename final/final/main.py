'''
Name: Adam Zaimes
Date: 8/28/2014
Class: DPWP
Assignment: Final
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
