from httpbin import sendDataHttpbin

data = {
    'UserName':'Anton',
    'Status':'On'
}

sendDataHttpbin(data)