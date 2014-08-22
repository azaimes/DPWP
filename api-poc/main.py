import webapp2
import urllib2  # import python classes to make things work
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    p = FormPage()
    p.inputs = [['zip', 'text', 'Zip Code'], ['Submit', 'submit']]  # input field data that is submitted to api
    self.response.write(p.print_out())




# don't ever mess with this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
