
from requests import post

url = "http://homeassistant.local:8123/api/services/script/turn_on"
headers = {"Authorization": "Bearer TOKEN"}


def getch():
    import sys
    import tty
    import termios
    old_settings = termios.tcgetattr(0)
    new_settings = old_settings[:]
    new_settings[3] &= ~termios.ICANON
    try:
        termios.tcsetattr(0, termios.TCSANOW, new_settings)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(0, termios.TCSANOW, old_settings)
    return ch

response = ''

while (1):
    char = getch()
    if (char == '1'):
        print('Button 1')
        data = {"entity_id": "script.button_1"}
        response = post(url, headers=headers, json=data)
    if (char == '2'):
        print('Button 2')
        data = {"entity_id": "script.button_2"}
        response = post(url, headers=headers, json=data)
    if (char == '3'):
        print('Button 3')
        data = {"entity_id": "script.button_3"}
        response = post(url, headers=headers, json=data)
    if (char == '4'):
        print('Button 4')
        data = {"entity_id": "script.button_4"}
        response = post(url, headers=headers, json=data)
    if (char == '5'):
        print('Button 5')
        data = {"entity_id": "script.button_5"}
        response = post(url, headers=headers, json=data)
    if (char == '6'):
        print('Button 6')
        data = {"entity_id": "script.button_6"}
        response = post(url, headers=headers, json=data)
    if (char == '7'):
        print('Button 7')
        data = {"entity_id": "script.button_7"}
        response = post(url, headers=headers, json=data)
    if (char == '8'):
        print('Button 8')
        data = {"entity_id": "script.button_8"}
        response = post(url, headers=headers, json=data)
    if (char == '9'):
        print('Button 9')
        data = {"entity_id": "script.button_9"}
        response = post(url, headers=headers, json=data)
    if (char == '0'):
        print('Button 0')
        data = {"entity_id": "script.button_0"}
        response = post(url, headers=headers, json=data)
    if (char == '+'):
        print('Button Plus')
        data = {"entity_id": "script.button_plus"}
        response = post(url, headers=headers, json=data)
    if (char == '-'):
        print('Button Minus')
        data = {"entity_id": "script.button_minus"}
        response = post(url, headers=headers, json=data)
    if (char == '*'):
        print('Button Mult')
        data = {"entity_id": "script.button_multiply"}
        response = post(url, headers=headers, json=data)
    if (char == '/'):
        print('Button Div')
        data = {"entity_id": "script.button_divide"}
        response = post(url, headers=headers, json=data)
    print(char)
    if (response != ''): print(response.text)
