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
    def get(self):  # Controller that collects and sends data to  view model
        p = FormPage()
        p.inputs = [['city', 'text', 'City'], ['state', 'text', 'State'], ['Submit', 'submit']]

        if self.request.GET: #only if there is a city and state in the url
            #get info from the API and creates model
            hm = HouseModel()
            hm.city = self.request.GET['city']
            hm.state = self.request.GET['state']
            hm.callApi()

            # takes data from model class and then sends it to the view class
            hv = HouseView()
            hv.housedo = hm.houses
            p._body = hv.content

        self.response.write(p.print_out())


class HouseView(object):
    def __init__(self):  # creates output from API call
        self.__housedo = []
        self.__content = '<br/>'



#don't ever mess with this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
