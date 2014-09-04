'''
Name: Adam Zaimes
Date: 8/28/2014
Class: DPWP
Assignment: API
'''
import webapp2
import urllib2 #python classes and code needed to requesting info, receiving, and opening
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    # This class is the controller and is collecting and sending the information from the view to the model class
    def get(self):
        p = FormPage()
        p.inputs = [['city', 'text', 'City'],['state', 'text', 'State'],['Submit', 'submit']]

        if self.request.GET: #only if there is a city and state in the url
            #get info from the API and creates model
            hm = HouseModel()
            hm.city = self.request.GET['city']
            hm.state = self.request.GET['state']
            hm.callApi()

            #taking the data from the model class and send it to the view class
            hv = HouseView()
            hv.housedo = hm.houses
            p._body = hv.content

        self.response.write(p.print_out())


class HouseView(object):
    # This class is creating what the user will view and shows the information from the API call
    def __init__(self):
        self.__housedo = []
        self.__content = '<br/>'

    def update(self):  # displays to the user the response from the api output as html then rendered by the browser
        for do in self.__housedo:
            self.__content += "<p>Showing information for houses in: <br/><h2>" + do.city + ", " + do.state + "</h2></p>"
            self.__content += '<p>Use the links below to find out more information about this area</p><p><ul><li><a href="' + do.for_sale + '">For Sale</a></li><li><a href="' + do.owner_sale + '">For Sale By Owner</a></li><li><a href="' + do.foreclosure + '">Foreclosures</a></li><li><a href="' + do.recently_sold + '">Recently Sold</a></li><li><a href="' + do.affordability + '">Area Affordability</a></li><p class="footer">Home Value In This Area: <strong>' + do.home_value + '</strong><br/>Property Tax In This Area: <strong>' + do.property_tax + '</strong></p>'

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
    # This class is where the data is fetched, parsed, and sorted from the Zillow API
    def __init__(self):  # provides the url for the api with the key
        self.__url = "http://www.zillow.com/webservice/GetDemographics.htm?zws-id=X1-ZWz1b49raz7yff_3jtqm&state="
        self.__city = ''
        self.__state = ''
        self.__xmldoc = ''

    def callApi(self):
        #assemble the request
        request = urllib2.Request(self.__url + self.__state + "&city=" + self.__city)

        #use the urllib2 library to create an object to get the url
        opener = urllib2.build_opener()

        #use the url to get a result - requesting info from the API
        result = opener.open(request)

        #parse the XML
        self.__xmldoc = minidom.parse(result)

        self._houses = []  # gets the data from the xml
        house = HouseData()
        house.city = self.__xmldoc.getElementsByTagName('city')[1].firstChild.nodeValue
        house.state = self.__xmldoc.getElementsByTagName('state')[1].firstChild.nodeValue
        house.for_sale = self.__xmldoc.getElementsByTagName('forSale')[0].firstChild.nodeValue
        house.owner_sale = self.__xmldoc.getElementsByTagName('forSaleByOwner')[0].firstChild.nodeValue
        house.foreclosure = self.__xmldoc.getElementsByTagName('foreclosures')[0].firstChild.nodeValue
        house.recently_sold = self.__xmldoc.getElementsByTagName('recentlySold')[0].firstChild.nodeValue
        house.affordability = self.__xmldoc.getElementsByTagName('affordability')[0].firstChild.nodeValue
        house.home_value = self.__xmldoc.getElementsByTagName('value')[2].firstChild.nodeValue
        house.property_tax = self.__xmldoc.getElementsByTagName('value')[26].firstChild.nodeValue
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
    def city(self, c):
        self.__city = c

    @state.setter
    def state(self, s):
        self.__state = s


class HouseData(object):
    #  This object holds all of the data that is fetched from the model class and show by the view class
    def __init__(self):
        self.city = ''
        self.state = ''
        self.for_sale = ''
        self.owner_sale = ''
        self.foreclosure = ''
        self.recently_sold = ''
        self.affordability = ''
        self.home_value = ''
        self.property_tax = ''


class Page(object):
    # This class is holding the main page information and skeleton
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>House Hunter</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <div class="wrapper">
            <header>House Hunter</header>
             <div class="main">'''

        self._body = ''
        self._close = '''
             </div>
             <div class="image">
                <img src="images/house.png" />
             </div>
       </div>
    </body>
</html>'''

    def print_out(self):  # tells python to print the html
        return self._head + self._body + self._close


class FormPage(Page):  # creates the form html open/close tags
    def __init__(self):
        super(FormPage, self).__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''

    @property
    def inputs(self):
        pass

    @inputs.setter  # creates the input fields for the form and gathers the data entered
    def inputs(self, arr):
        self.__inputs = arr
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            try:
                self._form_inputs += '" placeholder="' + item[2]+'" />'
            except:
                self._form_inputs += '" />'

    def print_out(self):  # outputs the main page 
        return self._head + "<h1>Find Your Dream Home</h1><p>Fill out the city and state you want to look in:</p>" + self._form_open + self._form_inputs + self._form_close + self._body +  self._close

# don't even think of touching this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)