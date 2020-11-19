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
                increaseTasksCounters(item['completed'], usersTasks[item['userId']])
            else:
                increaseTasksCounters(item['completed'], usersTasks[item['userId']])
                
        uniqueUsers = len(users)
        return [uniqueUsers, usersTasks, 1]
    else:
        uniqueUsers = {}
        usersTasks = {}
        return [uniqueUsers, usersTasks, -1]

def increaseTasksCounters(isTaskCompleted, userTasks):
    if isTaskCompleted == True:
        userTasks['completedTasks'] += 1
    userTasks['tasks'] += 1

