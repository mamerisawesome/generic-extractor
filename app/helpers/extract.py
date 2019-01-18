import requests as fetch
from bs4 import BeautifulSoup
import soupsieve as sv

class EmptyUrlError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class MalformedSchemaUrlError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class InvalidUrlError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class NoTargetError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

def extract_page(url=None, root="", targets=[]):
    if not url:
        raise EmptyUrlError("URL cannot be empty for extraction")

    if not root and not targets:
        raise NoTargetError("No targets are available for extraction")

    try:
        data = fetch.get(url)
    except requests.exceptions.MissingSchema:
        raise MalformedSchemaUrlError("The URL cannot be used: {}".format(url))
    except requests.exceptions.ConnectionError:
        raise InvalidUrlError("Provide a valir URL: {}".format(url))

    soup = BeautifulSoup(data.text, 'html.parser')
    containers = soup.select(root)
    extracted = {}
    for parent in containers:
        for target in targets:
            extracted[target["name"]] = parent.select_one(target["el"])

    return { "data": extracted }

if __name__ == "__main__":
    import json
    data = {
        "url": "http://www.yamaha-motor.com.ph/product/",
        "root": "pro-details-left",
        "target": [
            { "name": "iamge", "el": "img" },
            { "name": "name", "el": ".product-name" },
            { "name": "price", "el": ".product-price" }
        ]
    }

    res = extract_page(**data)
    return json.dumps(res)
