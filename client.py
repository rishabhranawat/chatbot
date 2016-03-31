import requests
import json
print requests.post("http://localhost:5000", data = json.dumps({"hello":"there"}))

