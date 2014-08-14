#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
'''
Name: Adam Zaimes
Date: 8/14/14
Class: DPWP
Assignment: Lab 2 Server Side Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        heading = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Lab 2 Server Side Form</title>
    </head>
    <body>'''
        page_body = '''<form methord="GET">
            <fieldset>
                <label>Name</label><input type="text" name="user" />
                <label>Email</label><input type="text" name="email" /><br>
                <label>Address</label><input type="text" name="address" />
                <label>City</label><input type="text" name="city" />
                <label>State</label><input type="text" name="state" /><br>
                <label>Receive mailing</label><select name="mail">
                    <option value="yes">Yes</option>
                    <option value="no">No</option>
                    </select>
                <label>Agree to terms</label><input type="checkbox" name="terms" value="agree" />
            </fieldset>
        '''
        page_close = '''
        </form>
    </body>
</html>'''
        if self.request.GET:
            user = self.request.GET['user']
            email = self.request.GET['email']
            address = self.request.GET['address']
            city = self.request.GET['city']
            state = self.request.GET['state']
            self.response.write(heading + user + ' ' + email + ' ' + page_body + page_close)
        else:
            self.response.write(heading + page_body + page_close)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
