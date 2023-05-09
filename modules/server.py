#!/usr/bin/env python
""" Server/API class.

Class for the HIAS IoT Agent server/API.

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
import os
import requests
import time

from modules.AbstractServer import AbstractServer

from flask import Flask, request, Response

class server(AbstractServer):
	""" Server/API class.

	Class for the HIAS IoT Agent server/API.
	"""

	def start(self):
		""" Starts the server. """

		app = Flask(self.helpers.credentials["iotJumpWay"]["name"])

		@app.route('/Inference', methods=['POST'])
		def Inference():
			""" Responds to HTTP POST requests. """

			self.mqtt.publish("States", {
				"Type": "Prediction",
				"Name": self.helpers.credentials["iotJumpWay"]["name"],
				"State": "Processing",
				"Message": "Processing data"
			})

			query = request.json
			response = self.model.predict(query["query"], "answer")

			self.mqtt.publish("States", {
				"Type": "Prediction",
				"Name": self.helpers.credentials["iotJumpWay"]["name"],
				"State": "Classified",
				"Message": response
			})

			return Response(response=json.dumps(response, indent=4, sort_keys=True),
					status=200, mimetype="application/json")

		app.run(host=self.helpers.credentials["server"]["ip"],
				port=self.helpers.credentials["server"]["port"])
