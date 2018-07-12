# coding: utf-8

import logging
import json
import time
import datetime


from flask_restplus import Resource
from app.rest.api import api
from app.rest.analytics.serializers import stats_serializer
from app.analytics.analytics import AnalyticsController

log = logging.getLogger(__name__)
ns = api.namespace('Analytics', description='Get statistics users information in your notifiCRM account')


@ns.route('/get_user_information')
class Stats(Resource):

    @api.expect(stats_serializer, validate=True)
    def get(self):
        post_mail = AnalyticsController()
        return post_mail.controller(**api.payload)


@ns.route('/get_leads')
class Stats1(Resource):

    @api.expect(stats_serializer, validate=True)
    def get(self):
        post_mail = AnalyticsController()
        return post_mail.controller(**api.payload)

@ns.route('/get_view_trend')
class Stats2(Resource):

    @api.expect(stats_serializer, validate=True)
    def get(self):
        post_mail = AnalyticsController()
        return post_mail.controller(**api.payload)

@ns.route('/get_click_trend')
class Stats3(Resource):

    @api.expect(stats_serializer, validate=True)
    def get(self):
        post_mail = AnalyticsController()
        return post_mail.controller(**api.payload)

@ns.route('/create_predictive_model')
class Stats4(Resource):

    @api.expect(stats_serializer, validate=True)
    def post(self):
        post_mail = AnalyticsController()
        return post_mail.controller(**api.payload)

@ns.route('/create_descriptive_model')
class Stats5(Resource):

    @api.expect(stats_serializer, validate=True)
    def post(self):
        post_mail = AnalyticsController()
        return post_mail.controller(**api.payload)

@ns.route('/create_regression_model')
class Stats6(Resource):

    @api.expect(stats_serializer, validate=True)
    def post(self):
        post_mail = AnalyticsController()
        return post_mail.controller(**api.payload)


@ns.route('/create_report')
class Stats7(Resource):

    @api.expect(stats_serializer, validate=True)
    def post(self):
        post_mail = AnalyticsController()
        return post_mail.controller(**api.payload)

@ns.route('/create_summary')
class Stats8(Resource):

    @api.expect(stats_serializer, validate=True)
    def post(self):
        post_mail = AnalyticsController()
        return post_mail.controller(**api.payload)


