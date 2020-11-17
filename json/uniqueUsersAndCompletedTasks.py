import json
import requests


def uniqueUsersAndCompletedTasks():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    if response.status_code != 404:
        result = json.loads(response.text)
        users = {}
        usersTasks = {}

        for item in result:
            users[item['userId']] = item['userId']
            if item['userId'] not in usersTasks:
                usersTasks[item['userId']] = {'tasks':0, 'completedTasks':0}
                if item['completed'] == True:
                    usersTasks[item['userId']]['completedTasks'] += 1 
                usersTasks[item['userId']]['tasks'] += 1
            else:
                if item['completed'] == True:
                    usersTasks[item['userId']]['completedTasks'] += 1 
                usersTasks[item['userId']]['tasks'] += 1
            
        uniqueUsers = len(users)
        return [uniqueUsers, usersTasks, 1]
    else:
        uniqueUsers = {}
        usersTasks = {}
        return [uniqueUsers, usersTasks, -1]
