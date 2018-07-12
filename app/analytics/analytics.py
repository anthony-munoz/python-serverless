import logging
import os
import json
import base64


from app.flask_factory import settings
log = logging.getLogger(__name__)


class AnalyticsController:

	def __init__(self):
		self.type = "analytics"

	def controller(self, user):
		response = 'User information for Kurt'

		return response
