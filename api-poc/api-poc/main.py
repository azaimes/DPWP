'''
Name: Adam Zaimes
Date: 8/21/2014
Class: DPWP
Assignment: Proof of Concept
'''


import webapp2
import urllib2
from xml.dom import minidom



class MainHandler(webapp2.RequestHandler):
    def get(self):
        fp = FormPage()
        fp.inputs = [['city', 'text', 'City'], ['state', 'text', 'State'], ['Submit', 'submit']]

        if self.request.GET: 

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
