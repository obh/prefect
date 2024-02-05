import time

import httpx
from prefect import flow
import requests
from datetime import datetime
from models import models

# @flow(log_prints=True)
# def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
#     url = f"https://api.github.com/repos/{repo_name}"
#     response = httpx.get(url)
#     response.raise_for_status()
#     repo = response.json()
#     print(f"{repo_name} repository statistics 🤓:")
#     print(f"Stars 🌠 : {repo['stargazers_count']}")
#     print(f"Forks 🍴 : {repo['forks_count']}")


@flow(flow_run_name="test-run")
def get_data():
    #print(cred, time)
    keys = fetch_keys(1848)
    time.sleep(5)
    url = "https://api.cashfree.com/pg/recon"
    headers = {
        'x-client-id': keys[0],
        'x-client-secret': keys[1],
        'x-api-version': '2022-09-01'
    }
    payload = {
        "filters": {
            "start_date": "2023-07-20T00:00:00Z",
            "end_date": "2023-07-30T00:00:00Z"
        },
        "pagination": {
            "limit": 10
        }
    }
    print(url, headers, payload)
    response = requests.post(url, headers=headers, json=payload)
    print(response)


def fetch_keys(merchantId: int):
    return "1848d0ce8441fb8ffa258bc98481", "f7cbcd7ba238c4f85a4083c39f9386be33de1214"


if __name__ == "__main__":
    # get_repo_info.serve(name="my-first-deployment")
    get_data.serve(name="my-second-deployment")

