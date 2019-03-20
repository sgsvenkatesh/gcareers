import requests
import json
import time

url = "https://careers.google.com/api/jobs/jobs-v1/search/?company=Google&company=YouTube&hl=en_US&jlo=en_US&location=United%20States&q=&sort_by=relevance&page="

page = 1
results = []

while True:
    print("requesting page " + str(page))

    resp = requests.get(url + str(page))
    resp_json = resp.json()

    if resp_json.get("jobs"):
        results += resp_json["jobs"]
        page = resp_json["next_page"]
    else:
        break

    if int(page) % 10 == 0:
        time.sleep(1)

with open("./raw-data/jobs-list.json", 'w') as outfile:
    json.dump(results, outfile, indent=4)