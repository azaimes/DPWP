'''
Name: Adam Zaimes
Date: 8/14/14
Class: DPWP
Assignment: Lab 2 Server Side Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):#begining of page
        heading = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Lab 2 Server Side Form</title>
        <link type="text/css" rel="stylesheet" href="/css/style.css"   />
    </head>
    <body>
        <div class="wrapper">'''
        #provides the form for input
        page_form = '''<form method="GET">

            <fieldset>
                <h1>Signup for Classy Coders Today!</h1>
                <label class="field">Name</label><input class="textBox" type="text" name="user" /><br>
                <label class="field">Email</label><input class="textBox" type="text" name="email" /><br>
                <label class="field">Address</label><input class="textBox" type="text" name="address" /><br>
                <label class="field">City</label><input class="textBox" type="text" name="city" /><br>
                <label class="field">State</label><input class="textBox" type="text" name="state" /><br>
                <label class="field">Zip Code</label><input class="textBox" type="text" name="zipcode" /><br>
                <label class="mail">Receive mailing</label><select name="mail">
                    <option value="yes">Yes</option>
                    <option value="no">No</option>
                    </select><br>
                <label class="mail">Agree to terms</label><input type="checkbox" name="terms" value="agree" /><br>
                <div class="submitButton">
                <input type="submit" value="Submit" /><br>
                </div>
            </fieldset>
        '''
        # output is presented here after form submission
        page_body = '''
        <div class="top"><h1> Thank you, {user}</h1>
            <h2>Your information has been saved!</h2>
            <p>Name: {user}</p>
            <p>Email: {email}</p>
            <p>Address: {address} {city}, {state} {zipcode}
        </div>
        '''
        #end of page
        page_close = '''
        </form>
        </wrapper>
    </body>
</html>'''
        #script to collect data from form and process
        if self.request.GET:
            user = self.request.GET['user']
            email = self.request.GET['email']
            address = self.request.GET['address']
            city = self.request.GET['city']
            state = self.request.GET['state']
            zipcode = self.request.GET['zipcode']
            mail = self.request.GET['mail']
            terms = self.request.GET['terms']
            page_body = page_body.format(**locals())
            self.response.write(heading + page_body + page_close) #shows form on page load
        else:
            self.response.write(heading + page_form + page_close) #shows results from form


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
