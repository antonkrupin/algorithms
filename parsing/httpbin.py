import json
import requests


def sendDataHttpbin(data):
    sendData = requests.post('http://httpbin.org/post', data=data)
    if sendData.status_code == 200:
        return 1
    else:
        return -1