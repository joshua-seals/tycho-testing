import sys
sys.path.append('/home/mattb523/tycho')

import os
import json
import logging
import pytest
import yaml
from tycho.client import TychoClient
from tycho.test.lib import client
from tycho.test.lib import system
from tycho.test.lib import system_request
from unittest import mock

from tycho.actions import StartSystemResource
from tycho.actions import TychoResource

logger = logging.getLogger (__name__)

def test_start_system_resource(mocker, system_request, client, request):
    print (f"{request.node.name}")
    response = {
        "status": "success",
        "result": {
            "name": "jupyter-ds-caa94baea8a849d89e427bd78cad17eb",
            "sid": "caa94baea8a849d89e427bd78cad17eb",
        },
        "message": "Started system jupyter-ds-caa94baea8a849d89e427bd78cad17eb"
    }

    # Making a system request, storing in tycho_system
    tycho_system = StartSystemResource().post(system_request)

    result = response["result"]
    
    assert tycho_system['status'] == response['status']
    assert tycho_system['name'] == result['name']
    assert tycho_system['sid'] == result['sid']
    assert tycho_system['message'] == response['message']

def test_delete_system_resource(mocker, system_request, client, request):
    print(f"{request.node.name}")
    # response = {
    #     "status": "success",
    #     "result": {
    #         #result
    #     }
    #     "message": "Deleted system ..."
    # }

    # tycho_delete = DeleteSystemResource().post(system_request)

    # result = response['result']

    # assert tycho_delete['status'] == response['status']
    # assert tycho_delete['name'] == result['name']
    # assert tycho_delete['sid'] == result['sid']
    # assert tycho_delete['message'] == response['message']


def test_status_system_resource(mocker, system_request, client, request):
    print(f"{request.node.name}")
