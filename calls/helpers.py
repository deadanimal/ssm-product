import requests
from xml.etree import ElementTree

import xmltodict
import pprint
import json

from calls.services.get_basic_comp_prof import (
    get_basic_company_profile
)

def call_middleware(service_name, request_json):

    url = "http://integrasistg.ssm.com.my/InfoService/1"
    headers = {
        'content-type': "text/xml;charset=UTF-8",
        'authorization': "U1NNUHJvZHVrfDIwMjAtMDgtMjlUMDU6MDY6MDFafENwcEI0TVF3YTlIdXVQWm85aGgzeG10bVBFNzBBTjQvRTJXVUpuY25RbjA9"
    }

    
    json_response = get_basic_company_profile(url, headers, 'registration_number', 'check_digit')
    return json_response
