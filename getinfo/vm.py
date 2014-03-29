import requests
import json

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
auth = {"auth": {"tenantName": "admin", "passwordCredentials": {"username": "admin", "password": "admin"}}}
r = requests.post("http://10.1.0.208:5000/v2.0/tokens", headers=headers, data = json.dumps(auth))
print r.text
print r.headers
print 'token:', json.loads(r.text)['access']['token']['id']
headers['X-Auth-Token'] = json.loads(r.text)['access']['token']['id']
headers['User-Agent'] = 'python-keystoneclient'
r = requests.get("http://10.1.0.208:35357/v2.0/tenants", headers=headers)
print r.text
print headers



for tenant in  json.loads(r.text)['tenants']:
  print tenant['name'] == 'admin'
  if tenant['name'] == 'admin':
    print tenant
    r = requests.get("http://10.1.0.208:8774/v2/%s/servers/detail" %(tenant['id']), headers=headers, params={'all_tenants': '1'})
    print "http://10.1.0.208:8774/v2/%s/servers/detail" %(tenant['id'])
    print r.text
    break



