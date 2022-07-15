# import
import json

import gistyc

# Initiate the GISTyc class with the auth token
gist_api = gistyc.GISTyc(auth_token="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")

# Create a GIST with the sample file
#response_data = gist_api.create_gist(file_name="./update_gist.py")

gist_list = gist_api.get_gists()

print(json.dumps(gist_list, indent=4, sort_keys=True))

"""
HTTP Reuests has following parameters:
1)Request URL
2)Header Fields
3)Parameter
4)Request body
"""
"""


#!/usr/bin/env python

import requests
import json
# import
import gistyc

# Initiate the GISTyc class with the auth token
gist_api = gistyc.GISTyc(auth_token=AUTH_TOKEN)

# Create a GIST with the sample file
response_data = gist_api.create_gist(file_name=FILEPATH)
GITHUB_API="https://api.github.com"
API_TOKEN='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'# 'your_token_goes_here'

#form a request URL
url= "https://gist.github.com/RainXculiva/1e58a86113806f3a0afa7ac748d45ca9?file=gistfile1.txt" #GITHUB_API+"/gists"
print("Request URL: %s"%url)

#print headers,parameters,payload
headers={'Authorization':'token %s'%API_TOKEN}
params={'scope':'gist'}
payload={"description":"GIST created by python code","public":True,"files":{"python request module":{"content":"Python requests has 3 parameters: 1)Request URL\n 2)Header Fields\n 3)Parameter \n4)Request body"}}}

#make a requests
res=requests.post(url,headers=headers,params=params,data=json.dumps(payload))

#print response --> JSON
print(res.status_code)
print(res.url)
print(res.text)
j=json.loads(res.text)

# Print created GIST's details
for gist in range(len(j)):
    print("Gist URL : %s"%(j['url']))
    print("GIST ID: %s"%(j['id']))
    
    
"""