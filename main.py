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
import webapp2
import cgi


page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>CaesarCode</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>

"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

# caesar.py

ALPHABET_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphabet_position(letter):
    alphabet = ALPHABET_LOWERCASE if letter.islower() else ALPHABET_UPPERCASE
    return alphabet.index(letter)

def rotate_char(char, rotation):
    if not char.isalpha():
        return char

    alphabet = ALPHABET_LOWERCASE if char.islower() else ALPHABET_UPPERCASE
    new_pos = (alphabet_position(char) + rotation) % 26
    return alphabet[new_pos]

def encrypt(text, rotation):
    answer = ""
    for char in text:
        answer += rotate_char(char, rotation)
    return answer



        # a form for adding new movies
rot_form = """
    <form action = "/code" method="post">
        <label style="font-size: 32pt">
            Caesar Code
        </label>
        <br>
        <label>
            Rotation
            <br>
            <input type="text" name="rot" value=""/>
            <br>
        </label>
        <label>
            Phrase to be coded
            <br>
            <input name="phrase" " value="%(code)s">
            <br>
        <label>

        <input type="submit" value="submit"/>
    </form>
    """
        # combine all the pieces to build the content of our response
        #main_content =  rot_form
        #response = page_header + main_content + page_footer
        #self.response.write(response)

class index(webapp2.RequestHandler):
    """ Handles requests coming in to '/'
        e.g. www.caesar.com/
    """
    def write_form(self, code =""):
        self.response.write(rot_form % {"code":code})

    def get(self):
        self.write_form()

class CaesarCode(webapp2.RequestHandler):
    """ Handles requests coming in to '/code'
        e.g. www.caesar.com/code
    """
    def write_form(self, code =""):
        self.response.write(rot_form % {"code":code})

    def post(self):
        rotCode = int(self.request.get("rot"))
        phraseCode = self.request.get("phrase")
        newCode = cgi.escape(encrypt(phraseCode, rotCode))
        self.write_form(newCode)

        #response = page_header + "<p>" + cgi.escape(newCode, quote=True) + "</p>" + page_footer
        #self.response.write(response)

app = webapp2.WSGIApplication([
        ('/', index),
        ('/code', CaesarCode)
        ], debug=True)
