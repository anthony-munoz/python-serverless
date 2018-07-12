import json
from flask_restplus import fields
from app.router import api


context_example = {
        "title": 'Welcome',
        "content": 'We are pleased to have you on board!',
        "action_content": 'More information in our web application.',
        "action_title": 'nFusz',
        "action_url": 'https://nfusz.com',
        "action_text": 'Your CRM platform',
    }


stats_serializer = api.model('Resource', {
    'user': fields.String(required=True, description='client user ID', example="12"),
})
