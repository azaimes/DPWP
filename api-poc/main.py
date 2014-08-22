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





# don't ever mess with this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
