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
            <label>Name</label><input type="text" name="user" />
            <label>Email</label><input type="text" name="email" /><br>
            <label>Address</label><input type="text" name="address" />
            <label>City</label><input type="text" name="city" />
            <label>State</label><input type="text" name="state" /><br>
        '''
        page_close = '''
    </body>
</html>'''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
