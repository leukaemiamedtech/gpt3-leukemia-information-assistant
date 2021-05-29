#!/usr/bin/env python
""" HIAS AI Agent.

HIAS AI Agents process data using local AI models and communicate
with HIAS IoT Agents using the MQTT protocol.

MIT License

Copyright (c) 2021 Asociación de Investigacion en Inteligencia Artificial
Para la Leucemia Peter Moss

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

import sys

from abc import ABC, abstractmethod

from modules.AbstractAgent import AbstractAgent

from modules.helpers import helpers
from modules.server import server
from modules.model import model


class agent(AbstractAgent):
	""" OpenAI Leukemia Information Assistant HIAS AI Agent

	Represents a HIAS AI Agent that processes data
	using the OpenAI Leukemia Information Assistant.
	"""

	def set_model(self):

		self.model = model(self.helpers)

	def server(self):
		""" Loads the API server """

		self.mqtt_start()

		self.set_model()
		self.server = server(self.helpers, self.model, self.model_type, self.mqtt)
		self.server.start()

	def inference(self, prompt, typeof):
		""" Loads model and classifies test data locally """

		response = self.model.predict(prompt, typeof)
		self.helpers.logger.info(response["answers"][0])

	def signal_handler(self, signal, frame):
		self.helpers.logger.info("Disconnecting")
		self.mqtt.disconnect()
		sys.exit(1)


agent = agent()


def main():

	if len(sys.argv) < 2:
		agent.helpers.logger.error("You must provide an argument")
		exit()
	elif sys.argv[1] not in agent.helpers.confs["agent"]["params"]:
		agent.helpers.logger.error("Mode not supported! server, answer or completion")
		exit()

	mode = sys.argv[1]

	if mode == "answer":
		if len(sys.argv) < 3:
			agent.helpers.logger.error("You must provide an input")
			exit()
		agent.set_model()
		agent.inference(sys.argv[2], "answer")

	elif mode == "completion":
		if len(sys.argv) < 3:
			agent.helpers.logger.error("You must provide an input")
			exit()
		agent.set_model()
		agent.inference(sys.argv[2], "completion")

	elif mode == "server":
		agent.set_model()
		agent.server()


if __name__ == "__main__":
	main()
