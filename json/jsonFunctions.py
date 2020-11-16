import json
import requests

def openJSON(link):
    response = requests.get(link)
    result = json.loads(response.text)
    return result


def saveJSONtoFile():
    data = openJSON("https://jsonplaceholder.typicode.com/todos")
    fo = open('dataJSON.json', 'wt')
    fo.write(json.dumps(data, indent=2))
    fo.close()


def uniqueUsers():
    try:
        with open('dataJSON.json', 'r') as f:
            data = json.loads(f.read())
        
        users = {}

        for item in data:
            users[item['userId']] = item['userId']

        uniqueUsers = len(users.items())
    
        return [uniqueUsers, 1]

    except Exception:
        uniqueUsers = {}
        return [uniqueUsers, -1]
        

def originalTasks():
    try:
        with open('dataJSON.json', 'r') as f:
            data = json.loads(f.read())

        usersTasks = {}

        for item in data:
            usersTasks[item['userId']] = {'tasks':0, 'completedTasks':0}
        
        for item in data:
            if item['completed'] == True:
                usersTasks[item['userId']]['completedTasks'] += 1
            usersTasks[item['userId']]['tasks'] += 1
        
        return [usersTasks, 1]

    except Exception:
        usersTasks = {}
        return [usersTasks, -1]

