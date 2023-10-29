#!/usr/bin/python3
'''create a route /status'''
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False, methods=['GET'])
def status():
    '''returns a json file'''
    return {"status": "OK"}
