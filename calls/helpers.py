import requests
from xml.etree import ElementTree

import xmltodict
import pprint
import json

from calls.services.get_basic_comp_prof import (
    get_basic_company_profile
)

from calls.services.get_fin2 import get_fin2

def call_middleware(service_name, registration_number):

    url = "http://integrasistg.ssm.com.my/InfoService/1"
    headers = {
        'content-type': "text/xml;charset=UTF-8",
        'authorization': "U1NNUHJvZHVrfDIwMjAtMDktMDEgMTA6MzU6MDB8SnlnU1pUL055RlNKSnRXSk01TXF1a29QV1ZNQXQwRjcrRk5aeUkwV2I0bz0="
    }

    if service_name == 'getCompProfile':
        json_response = get_basic_company_profile(url, headers, registration_number)
    elif service_name == 'getFin2':
        json_response = get_fin2(url, headers, registration_number)
    return json_response
