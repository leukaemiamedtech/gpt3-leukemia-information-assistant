#!/usr/bin/env python
""" Abstract class representing a HIAS AI Model.

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
import time

from abc import ABC, abstractmethod

class AbstractModel(ABC):
	""" Abstract class representing a HIAS AI Model.

	This object represents a HIAS AI Model. HIAS AI Models are used by AI Agents
	to process incoming data.
	"""

	def __init__(self, helpers):
		"Initializes the AbstractModel object."
		super().__init__()

		self.helpers = helpers
		self.confs = self.helpers.confs

		os.environ["KMP_BLOCKTIME"] = "1"
		os.environ["KMP_SETTINGS"] = "1"
		os.environ["KMP_AFFINITY"] = "granularity=fine,verbose,compact,1,0"
		os.environ["OMP_NUM_THREADS"] = str(
			self.helpers.confs["agent"]["cores"])

		self.addr = "http://" + self.helpers.credentials["server"]["ip"] + \
			':'+str(self.helpers.credentials["server"]["port"]) + '/Inference'

		self.headers = {
			'content-type': 'application/json',
			'Authorization': 'Bearer ' + self.helpers.confs["openai"]["key"],
		}

		self.helpers.logger.info("Model class initialization complete.")

	@abstractmethod
	def predict(self, prompt, typeof):
		""" Gets a prediction. """
		pass
