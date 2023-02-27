import getch
from requests import post

print('hello world')
url = "http://homeassistant.local:8123/api/services/script/turn_on"
headers = {"Authorization": "Bearer TOKEN"}

while (1):
    char = getch.getch()
    if (char == 'a'):
        print('Button 1')
        data = {"entity_id": "script.button_1"}
        response = post(url, headers=headers, json=data)
    if (char == 'b'):
        print('Button 2')
        data = {"entity_id": "script.button_2"}
        response = post(url, headers=headers, json=data)
    print(char)
    print(response.text)
