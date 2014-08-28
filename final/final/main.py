'''
Name: Adam Zaimes
Date: 8/28/2014
Class: DPWP
Assignment: Final
'''
import webapp2
import urllib2  # python classes and code needed to requesting info, receiving, and opening
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self): # Controller that collects and sends data to  view model
        p = FormPage()
        p.inputs = [['city', 'text', 'City'],['state', 'text', 'State'],['Submit', 'submit']]

#don't ever mess with this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
