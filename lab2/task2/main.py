Commands ='''
* help - show all commands
* add <key> [key, …] – add one or more elements to the container (if the element is already in there then don’t add);
* remove <key> – delete key from container;
* find <key> [key, …] – check if the element is presented in the container, print each found or “No such elements” if nothing is;
* list – print all elements of container;
* grep <regex> – check the value in the container by regular expression, print each found or “No such elements” if nothing is;
* save - save container to file
* switch – switches to another user.
* exit - leave from program
'''
def parse_command():
    user_input=input('').split(maxsplit=1)

    if len(user_input) == 0:
        print('Input must be not empty')

    command = user_input[0]
    arguments = ''
    if len(user_input)>1:
        arguments = user_input[1]
    return command, arguments



print('Welcome to my own set!!!')
username=input('Enter username: ')
print (f'Hello, {username}!')
print ('Type command or \'help\ to get info about available commands.')
is_working = True
while is_working:
    command, args = parse_command()