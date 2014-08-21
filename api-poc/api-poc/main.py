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
            hm.state = self.request.GET['state']  # gets state from form
            hm.call_api()

            hv = HouseView()
            hv.houseget = hm.houses
            fp._body = hv.content

        self.response.write(fp.print_out())


class HouseView(object):  # shows user page and data recieved from api
    def __init__(self):
        self.__houseget = []
        self.__content = '<br/>'

    def returned(self):
        for do in self.__houseget:
            self.__content += '<p>Here is the information you requested for houses located in ' + do.city + ', ' \
                              + do.state + '</p>'
            self.__content += '<p>Select a link to see more information about this neighborhood</p><p><ul> \
                                <li><a href="' + do.for_sale + '">For Sale</a></li>' \
                                '<li><a href="' + do.fsbo + '">For Sale By Owner</a></li>' \
                                '<li><a href="' + do.foreclosure + '">Foreclosures</a></li>' \
                                '<li><a href="' + do.recently_sold + '">Recently Sold</a></li>' \
                                '<li><a href="' + do.affordability + '">Area Affordability</a></li></ul><br/>'

    @property
    def content(self):
        return self.__content

    @property
    def houseget(self):
        pass

    @houseget.setter
    def houseget(self, arr):
        self.__houseget = arr
        self.__returned()


class HouseModel(object):  # gets data from zillow
    def __init__(self):
        self.__url = "http://www.zillow.com/webservice/GetDemographics.htm?zws-id=X1-ZWz1b4fgi6xnuz_9hc6e&state="
        self.__city = ''
        self.__state = ''
        self.__xmldoc = ''

    def call_api(self):
        request = urllib2.Request(self.__url + self.__state + "&city" + self.__city)

        opener = urllib2.build_opener()

        result = opener.open(request)  # gets info from api

        self.__xmldoc = minidom.parse(result)  # parses the xml

        self._houses = []
        house = HouseData()
        house.city = self.__xmldoc.getElementsByTagName('city')[1].firstChild.nodeValue
        house.state = self.__xmldoc.getElementsByTagName('state')[1].firstChild.nodeValue
        house.for_sale = self.__xmldoc.getElementsByTagName('forSale')[0].firstChild.nodeValue
        house.fsbo = self.__xmldoc.getElementsByTagName('forSaleByOwner')[0].firstChild.nodeValue
        house.foreclosure = self.__xmldoc.getElementsByTagName('foreclosures')[0].firstChild.nodeValue
        house.recently_sold = self.__xmldoc.getElementsByTagName('recentlySold')[0].firstChild.nodeValue
        house.affordability = self.__xmldoc.getElementsByTagName('affordability')[0].firstChild.nodeValue
        self._houses.append(house)

    @property
    def houses(self):
        return self._houses

    @property
    def city(self):
        pass

    @property
    def state(self):
        pass

    @city.setter
    def city(self, cty):
        self.__city = cty

    @state.setter
    def state(self, ste):
        self.__state = ste


class HouseData(object):  # all the info gotten from the classes
    def __init__(self):
        self.city = ''
        self.state = ''
        self.for_sale = ''
        self.fsbo = ''
        self.foreclosure = ''
        self.recently_sold = ''
        self.affordability = ''














#never touch this!!!
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
