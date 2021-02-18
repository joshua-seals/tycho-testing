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

logger = logging.getLogger (__name__)

def test_start_system_resource(mocker, system_request, client, request):
    print (f"{request.node.name}")
    response = {
        "status": "success",
        "result": {
            "name": "jupyter-ds-caa94baea8a849d89e427bd78cad17eb",
            "sid": "caa94baea8a849d89e427bd78cad17eb",
            "containers": {
                "jupyter-datascience": {
                    "ip_address": "127.0.0.1",
                    "port-1": 32661
                }
            }
        },
        "message": "Started system jupyter-ds-caa94baea8a849d89e427bd78cad17eb"
    }

    # Making a system request, storing in tycho_system
    # What does it need to be asserted to match up to???
    tycho_system = system_request()
    result = tycho_system['result']
    jupyter = result['containers']['jupyter-datascience']

    assert tycho_system.status == 'success'
    assert tycho_system.name == result['name']
    assert tycho_system.identifier == result['sid']
    assert tycho_system.services[0].ip_address == jupyter['ip_address']
    assert tycho_system.services[0].port == jupyter['port-1']
    assert tycho_system.message == response['message']

def test_delete_system_resource(mocker, system_request, client, request):
    print(f"{request.node.name}")
    response = {
        "status": "success",
        "result": {
            #not sure what to put here
        }
    }

    tycho_system = 

def test_status_system_resource(mocker, system_request, client, request):
    print(f"{request.node.name}")