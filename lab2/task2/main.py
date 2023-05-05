def pars_command():

print('Welcome to my own set!!!')
username=input('Enter username: ')
print (f'Hello, {username}!')
print ('Type command or \'help\ to get info about available commands.')
is_working = True
while is_working:
    command, args = parse_command()