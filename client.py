#!/usr/bin/env python
""" HIAS AI Agent Client.

Sends data to the HIAS AI Agent server.

MIT License

Copyright (c) 2023 Peter Moss Leukaemia MedTech Research CIC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files(the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Contributors:
- Adam Milton-Barker

"""

import json
import requests
import string
import sys
import time

from modules.helpers import helpers


class client():
    """ HIAS AI Agent Client

    Sends data to the HIAS AI Agent server.
    """

    def __init__(self):
        """ Initializes the class. """

        self.helpers = helpers("Client")

        self.apiUrl = "http://" + self.helpers.credentials["server"]["ip"] + ":" + str(
            self.helpers.credentials["server"]["port"]) + "/Inference"
        self.headers = {"content-type": 'application/json'}

        self.helpers.logger.info("Client ready")

    def call(self, data):
        """ Initializes the class. """

        self.helpers.logger.info("Sending string for classification...")
        response = requests.post(self.apiUrl, data=json.dumps(data),
                                 headers=self.headers)
        client.helpers.logger.info("Response: "+str(response.text))

if __name__ == "__main__":

    if len(sys.argv) < 1:
        print("You must provide an argument")
        exit()

    client = client()
    client.call({"query": str(sys.argv[1])})
