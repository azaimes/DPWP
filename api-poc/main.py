import webapp2
import urllib2  # import python classes to make things work
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['zip', 'text', 'Zip Code'],['Submit', 'submit']]  # input field data that is submitted to api
        self.response.write(p.print_out())

        if self.request.GET:  # this only will work if there is a zip code in the text field which is sent to the url
            zip = self.request.GET['zip']
            url = "http://www.zillow.com/webservice/GetDemographics.htm?zws-id=X1-ZWz1b4eovrcw7f_a1050&zip="+zip
            request = urllib2.Request(url)  # puts the request together

            opener = urllib2.build_opener()  # uses urllib2 to get the url

            result = opener.open(request)  # gets the result from the url

            xmldoc = minidom.parse(result)  # xml parsing going on here
            print xmldoc

            self.response.write(xmldoc.getElementsByTagName('city')[0].firstChild.nodeValue)
            self.response.write(xmldoc.getElementsByTagName('zip')[0].firstChild.nodeValue)


class Page(object):  # html is added here
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>API POC</title>
    </head>
    <body>'''

        self._body = 'Search for a home:'
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''


    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        self.__inputs = arr
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            try:
                self._form_inputs += '" placeholder="' + item[2]+'" />'
            except:
                self._form_inputs += '" />'

    def print_out(self):  # puts it all together so it can be put on the page
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close

#  if you touch this a kitten will die
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)