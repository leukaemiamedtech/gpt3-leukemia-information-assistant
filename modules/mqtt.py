#!/usr/bin/env python
""" HIAS iotJumpWay MQTT module

This module connects devices, applications, robots  and other softwares to the
HIAS iotJumpWay MQTT Broker.

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
"""

import json
import os

import paho.mqtt.client as pmqtt


class mqtt():
	"""iotJumpWay MQTT connection."""

	def __init__(self,
			  helpers,
			  client_type,
			  configs):
		""" Initializes the class. """

		self.configs = configs
		self.client_type = client_type

		self.helpers = helpers
		self.program = "HIAS iotJumpWay MQTT module"

		self.mqtt_config = {}
		self.module_topics = {}

		self.agent = [
			'host',
			'port',
			'location',
			'zone',
			'entity',
			'name',
			'un',
			'up'
		]

		self.helpers.logger.info(self.program + " initialization complete.")

	def configure(self):

		# Checks required parameters
		self.client_id = self.configs['name']
		for param in self.agent:
			if self.configs[param] is None:
				raise ConfigurationException(param + " parameter is required!")

		# Sets MQTT connection configuration
		self.mqtt_config["tls"] = "/etc/ssl/certs/DST_Root_CA_X3.pem"
		self.mqtt_config["host"] = self.configs['host']
		self.mqtt_config["port"] = self.configs['port']

		# Sets MQTT topics
		self.module_topics["statusTopic"] = '%s/Agents/%s/%s/Status' % (
			self.configs['location'], self.configs['zone'], self.configs['entity'])

		# Sets MQTT callbacks
		self.commandsCallback = None

		self.helpers.logger.info(
					"iotJumpWay " + self.client_type + " connection configured.")

	def start(self):

		self.mClient = pmqtt.Client(client_id=self.client_id, clean_session=True)
		self.mClient.will_set(self.module_topics["statusTopic"], "OFFLINE", 0, False)
		self.mClient.tls_set(self.mqtt_config["tls"], certfile=None, keyfile=None)
		self.mClient.on_connect = self.on_connect
		self.mClient.on_message = self.on_message
		self.mClient.on_publish = self.on_publish
		self.mClient.on_subscribe = self.on_subscribe
		self.mClient.username_pw_set(
			str(self.configs['un']), str(self.configs['up']))
		self.mClient.connect(self.mqtt_config["host"], self.mqtt_config["port"], 10)
		self.mClient.loop_start()

		self.helpers.logger.info(
					"iotJumpWay " + self.client_type + " connection started.")

	def on_connect(self, client, obj, flags, rc):

		self.helpers.logger.info(
			"iotJumpWay " + self.client_type + " connection successful.")
		self.helpers.logger.info("rc: " + str(rc))

		self.statusPublish("ONLINE")

	def statusPublish(self, data):

		self.mClient.publish(self.module_topics["statusTopic"], data)
		self.helpers.logger.info("Published to " + self.client_type + " status.")

	def on_subscribe(self, client, obj, mid, granted_qos):

		self.helpers.logger.info("iotJumpWay " + self.client_type + " subscription")

	def on_message(self, client, obj, msg):

		splitTopic = msg.topic.split("/")
		connType = splitTopic[1]

		topic = splitTopic[4]

		self.helpers.logger.info(msg.payload)
		self.helpers.logger.info("iotJumpWay " + connType +
								 " " + topic + " communication received.")

		if topic == 'Commands':
			if self.commandsCallback == None:
				self.helpers.logger.info(
							connType + " comands callback required (commandsCallback) !")
			else:
				self.commandsCallback(msg.topic, msg.payload)

	def publish(self, channel, data):

		channel = '%s/Agents/%s/%s/%s' % (self.configs['location'],
			self.configs['zone'], self.configs['entity'], channel)

		self.mClient.publish(channel, json.dumps(data))
		self.helpers.logger.info("Published to " + channel)
		return True

	def subscribe(self, application=None, channelID=None, qos=0):

		channel = '%s/#' % (self.configs['location'])
		self.mClient.subscribe(channel, qos=qos)
		self.helpers.logger.info("-- Agent subscribed to all channels")
		return True

	def on_publish(self, client, obj, mid):
		self.helpers.logger.info("Published: "+str(mid))

	def on_log(self, client, obj, level, string):
		print(string)

	def disconnect(self):
		self.statusPublish("OFFLINE")
		self.mClient.disconnect()
		self.mClient.loop_stop()
