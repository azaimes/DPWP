import webapp2
import urllib2  # import python classes to make things work
from xml.dom import minidom


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['zip', 'text', 'Zip Code'], ['Submit', 'submit']]  # input field data that is submitted to api
        self.response.write(p.print_out())

        if self.request.GET:  # this only will work if there is a zip code in the text field which is sent to the url
            zip = self.request.GET['zip']  # pulls data from api
            url = "http://www.zillow.com/webservice/GetDemographics.htm?zws-id=X1-ZWz1b4fgi6xnuz_9hc6e" + zip
            request = urllib2.Request(url)  # puts the request together

            opener = urllib2.build_opener()  # uses urllib2 to get the url

            result = opener.open(request)  # gets the result from the url

            xmldoc = minidom.parse(result)  # parse xml
            print xmldoc

            self.response.write(xmldoc.getElementsByTagName('city')[0].firstChild.nodeValue)
            self.response.write(xmldoc.getElementsByTagName('zip')[0].firstCild.nodeValue)


class Page(object):  # sets up the page structure
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Proof of Concept</title>
    </head>
    <body>'''

        self._body = 'SEARCH'
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._footer


class FormPage(object):
    def __init__(self):
        super(FormPage, self).__init__()
        self._form_open = '<form method="GET"'
        self._form_close = '</form>'
        self._inputs = []
        self._form_inputs = ''

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        for item in arr:




# don't ever mess with this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
