import traceback
import logging
from app.flask_factory import settings
from flask import Blueprint
from flask_cors import CORS
from app.rest.api import api
from app.rest.analytics.api import ns as analytics_namespace


log = logging.getLogger(__name__)


def _configure_namespaces(api):
	"""
		Add more namespaces HERE
	"""
	#email
	api.add_namespace(analytics_namespace)


def configure_api(flask_app):
	blueprint = Blueprint('api', __name__)
	api.init_app(blueprint)
	_configure_namespaces(api)
	CORS(flask_app)
	flask_app.register_blueprint(blueprint)
