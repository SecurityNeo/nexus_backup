import requests
from common.constants import NEXUS_COMPONENTS_URL


def assemble_components(items):
    data = []
    for _, item in enumerate(items):
        for index, asset in enumerate(item):
            data.append({"downloadUrl": asset["downloadUrl"], "path": asset["path"], "md5": asset["md5"]})
    return data


def iterate_get_components(token=None):
    url = NEXUS_COMPONENTS_URL + "&continueToken=" + token
    response = requests.get(url)
    components = response.json()
    return components


def grab_components():
    components = []
    response = requests.get(NEXUS_COMPONENTS_URL)
    rsp = response.json()
    items = rsp['items']
    component = assemble_components(items)
    components.extend(component)
    while True:
        if rsp['continueToken']:
            data = iterate_get_components(rsp['continueToken'])
            items = data['items']
            component = assemble_components(items)
            components.extend(component)
            if data['continueToken']:
                rsp['continueToken'] = data['continueToken']
            else:
                break
    return components


