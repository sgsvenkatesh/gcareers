import requests
import json 
from urllib.parse import quote_plus
import time
import os

def crawl_full_desc():
    url = "https://careers.google.com/api/jobs/jobs-v1/jobs/get/?job_name="
    count = 1802

    with open('./raw-data/jobs-list.json') as results_obj:
        results = json.load(results_obj)

        for result in results:
            print("requesting for job " + str(count))
            job_id = quote_plus(result.get("job_id"))

            resp = requests.get(url + str(job_id))
            resp_json = resp.json()

            with open("./raw-data/full-desc/job-" + str(count) + ".json", 'w') as outfile:
                json.dump(resp_json, outfile, indent=4)

            count += 1

            if count % 10 == 0:
                time.sleep(2)

    print("Saved jobs " + str(count))

crawl_full_desc()