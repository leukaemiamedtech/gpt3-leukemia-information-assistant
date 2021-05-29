#!/usr/bin/env python
""" Class representing a HIAS AI Model.

Represents a HIAS AI Model. HIAS AI Models are used by AI Agents to process
incoming data.

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

from modules.AbstractModel import AbstractModel


class model(AbstractModel):
	""" Class representing a HIAS AI Model.

	This object represents a HIAS AI Model. HIAS AI Models are used by AI Agents
	to process incoming data.
	"""

	def predict(self, prompt, typeof):
		""" Gets a prediction. """

		if typeof == "answer":
			return self.openai_http_request_answer(prompt)
		if typeof == "completion":
			return self.openai_http_request_complete(prompt)

	def openai_http_request_answer(self, prompt):
		""" Sends request to the inference API endpoint. """

		response = requests.post(
					self.helpers.confs["openai"]["url"] + "/answers", json={
						"documents": [],
						"model": self.helpers.confs["openai"]["engine"],
						"question": prompt,
						"examples_context": "In 2020, almost 500,000 new patients were diagnosed with leukemia all over the world and approximately 312,000 individuals died with this disease.",
						"examples": [["How many people were diagnosed with leukemia in 2020?", "In 2020, almost 500,000 new patients were diagnosed with leukemia all over the world."], ["How many people died from leukemia in 2020?", "In 2020, approximately 312,000 individuals died with this disease."]],
						"max_tokens": self.helpers.confs["openai"]["max_tokens"],
						"temperature": self.helpers.confs["openai"]["temperature"],
						"stop": ["\n"]
					}, headers=self.headers)

		response = json.loads(response.text)

		return response["answers"][0]

	def openai_http_request_complete(self, prompt):
		""" Sends request to the inference API endpoint. """

		response = requests.post(
			self.helpers.confs["openai"]["url"] + "/engines/" +
							self.helpers.confs["openai"]["engine"] + "/completions", json={
								"prompt": prompt,
								"max_tokens": self.helpers.confs["openai"]["max_tokens"],
								"temperature": self.helpers.confs["openai"]["temperature"],
								"top_p": self.helpers.confs["openai"]["top_p"],
								"frequency_penalty": self.helpers.confs["openai"]["frequency_penalty"],
								"presence_penalty": self.helpers.confs["openai"]["presence_penalty"],
								"stop": ["\n"]
							}, headers=self.headers)

		response = json.loads(response.text)

		return response["choices"][0]["text"]
