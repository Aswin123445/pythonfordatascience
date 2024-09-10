name_prompt='please enter user name: '
poll_prompt='please type the polling: '
exit_prompt='is ther more user to poll y/n: '
#creating a empty dictionary
dict={}

#setting flag
flag=True

while flag:
    #taking polling user data
    name=input(name_prompt)
    poll=input(poll_prompt)

    #adding poll to the dictionary
    dict[name]=poll

    #asking to exit the loop
    checker=input(exit_prompt)

    #conditional checking
    flag=False if checker == 'n' else flag
    