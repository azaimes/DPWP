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

    def update(self):
        for do in self.__housedo:  # provides basic framework for users view
            self.__content += "<p>Showing results for houses in: <br/><h2>" + do.city + ", " + do.state + "</h2></p>"
            self.__content += '<p>Find all the essential data on homes within your search area using the links below.</p><p><ul><li><a href="' + do.for_sale + '">For Sale</a></li><li><a href="' + do.owner_sale + '">For Sale By Owner</a></li><li><a href="' + do.foreclosure + '">Foreclosures</a></li><li><a href="' + do.recently_sold + '">Recently Sold</a></li><li><a href="' + do.affordability + '">Area Affordability</a></li><p class="footer">Home Value In This Area: <strong>' + do.home_value + '</strong><br/>Property Tax In This Area: <strong>' + do.property_tax + '</strong></p>'

    @property
    def content(self):
        return self.__content

    @property
    def housedo(self):
        pass

    @housedo.setter
    def housedo(self, arr):
        self.__housedo = arr
        self.update()


class HouseModel(object):
    def __init__(self):  # provides api information for data retrieval parsing and sorting
        self.__url = "http://www.zillow.com/webservice/GetDemographics.htm?zws-id=X1-ZWz1b49raz7yff_3jtqm&state="
        self.__city = ''
        self.__state = ''
        self.__xmldoc = ''

     def callApi(self):
        request = urllib2.Request(self.__url + self.__state + "&city=" + self.__city)  # assembles the request for the api

        opener = urllib2.build_opener()  # uses urllib2 and creates obj to get url

        result = opener.open(request)  # request data from api from url provided

        self.__xmldoc = minidom.parse(result)  # parses XML

        


#don't ever mess with this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
