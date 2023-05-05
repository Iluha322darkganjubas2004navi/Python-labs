import container
import re

while True:
    username = input("Enter username: ")
    if not re.findall(r'\b[A-z]\w+\b', username):
        print('Incorrect name.')
    else:
        container = container.Container(username)
        break

while True:
    command = input('> ').split()
    match command[0]:
        case 'add':
            container.add(*command[1:])
        case 'remove':
            container.remove(command[1])
        case 'find':
            container.find(*command[1:])
        case 'list':
            container.list()
        case 'grep':
            if len(command) == 3 and (command[2].lower() == 'true' or command[2].lower() == 'false'):
                if command[2].lower() == 'true':
                    container.grep(command[1], True)
                else:
                    container.grep(command[1], False)
            elif len(command) == 2:
                container.grep(command[1])
            else:
                print('You entered the wrong command.')
        case 'save':
            container.save()
        case 'load':
            container.load()
        case 'switch':
            container.switch(command[1])
        case _:
            print('Such command not supported')