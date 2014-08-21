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

        if self.request.GET:  # only works if there is a city and state in the form fields
            hm = HouseModel()
            hm.city = self.request.GET['city']  # gets city from form
            hm.state = self.request.GET['state'] # gets state from form
            hm.callApi()

            hv = HouseView()
            hv.housedo = hm.houses
            fp._body = hv.content

        self.response.write(fp.print_out())

class


#never touch this!!!
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
