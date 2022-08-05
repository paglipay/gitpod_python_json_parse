# import pandas as pd
import json

# import OS module
import os
import requests
from pprint import pprint

# defining the api-endpoint
API_ENDPOINT = "https://paglipay-dtree.herokuapp.com/start/111"


# data to be sent to api
data = {
    "jobs": [
        {
            "import": "Key"
        },
        {
            "True": [
                {
                    "import": "RequestsObj"
                },
                {
                    "open": {
                        "ip": "http://corp.paglipay.info:5003/start",
                        "jobs": [
                            {
                                "import": "Key"
                            },
                            {
                                "True": [
                                    {
                                        "import": "RequestsObj"
                                    },
                                    {
                                        "open": {
                                            "ip": "http://192.168.2.213:5000/start",
                                            "jobs": [
                                                {
                                                    "import": "Key"
                                                },
                                                {
                                                    "True": [
                                                        {
                                                            "import": "FileObj"
                                                        },
                                                        [
                                                            {
                                                                "open": "C:/Users/Paul Aglipay/Desktop/json_services/261figueroa.sw00f1.json"
                                                            },
                                                            {
                                                                "open": "C:/Users/Paul Aglipay/Desktop/json_services/720hilgard.sw00f2.json"
                                                            }
                                                        ]
                                                    ]
                                                }
                                            ]
                                        }
                                    },
                                    {
                                        "True": "end"
                                    }
                                ]
                            }
                        ]
                    }
                },
                {
                    "True": "end"
                }
            ]
        }
    ]
}

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, json=data)

# pprint(f"Status Code: {r.status_code}, Response: {r.json()}")

keysList = list(r.json().keys())
pprint(keysList)
# # Get the list of all files and directories
# path = "C:\\Users\\Paul Aglipay\\Desktop\\json_services"
# dir_list = os.listdir(path)
# services = []
# service_types = {}
# for fname in dir_list:
#     # print(fname)
#     with open('C:\\Users\\Paul Aglipay\\Desktop\\json_services\\' + fname, 'r') as f:
#         data = json.load(f)

#     # Output: {'name': 'Bob', 'languages': ['English', 'French']}
#     # print(data)
#     for s in data:
#         services.append({"id": fname, "service": s['description']})
#         s_desc = s['description']
#         # desc_list = [
#         #     'interface',
#         #     'dhcp',
#         #     'ospf',
#         #     'bgp'
#         # ]
#         desc_list = [
#             'interface',
#             'dhcp',
#             'ospf',
#             'bgp',
#             'nat',
#             '.*Power Supply.*',
#             'sensor.*Module Temperature Sensor$',
#             'sensor.*Bias Current Sensor',
#             'sensor.*Receive Power Sensor',
#             'sensor.*Supply Voltage Sensor',
#             'sensor.*Transmit Power Sensor',
#             'catv',
#             'cpu.*CPU.*',
#             '.*CpucardPwrCon Rail.*',
#             '.*DOM Temperature Sensor for Ethernet.*',
#             '.*DOM Voltage Sensor for Ethernet.*',
#             '.*DOM .* Power Sensor for Ethernet.*',
#             '.*DOM .* Bias Sensor for Ethernet.*',
#             '.*powerSupply.*Input voltage sensor.*',
#             '.*powerSupply.*Output current sensor.*',
#             'portInterfaceCard',
#             'powerEntryModule'
#         ]

#         import re

#         for d in desc_list:
#             if (re.search(d, s_desc)):
#                 s_desc = d

#         # for d in desc_list:
#         #     if (d in s_desc):
#         #         s_desc = d

#         if s_desc not in service_types:
#             service_types[s_desc] = []

#         service_types[s_desc].append(fname)


# keysList = list(service_types.keys())

# list_service_types = []
# for kl in keysList:
#     list_service_types.append({"id": kl, "count": len(service_types[kl])})

# print(services)

# df = pd.DataFrame(list_service_types)
# df.to_excel('C:\\Users\\Paul Aglipay\\Desktop\\Nagios monitored device services list.xlsx')
