import json

import requests

url = "http://liwei:123@127.0.0.1:8888/jenkins/job/Interface_26_jmx/api/json"
ret = requests.get(url)
print(json.dumps(ret.json(), indent=2))
