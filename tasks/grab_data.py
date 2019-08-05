import requests
from common.constants import NEXUS_COMPONENTS_URL


def grab_components():
    response = requests.get(NEXUS_COMPONENTS_URL)
    items = response.json()['items']
    data = []
    for _, item in enumerate(items):
        for index, asset in enumerate(item):
            data.append({"downloadUrl": asset["downloadUrl"], "path": asset["path"], "md5": asset["md5"]})
    return data

