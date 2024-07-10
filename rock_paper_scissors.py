import random

def play(user_p,computer_p):

    computer=random.choice(['s','p','r'])
    if user==computer:
        print('Is\'s a tie.')
        return user_p,computer_p

    if is_win(user,computer):
        print('It\'s your point.')
        return user_p+1,computer_p

    print('It\'s my point.')
    return user_p,computer_p+1

def is_win(user,computer):
    if (user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
        return True


def win(user_p,computer_p):
    if user_p>computer_p:
        return True


flag=True
user_p=0
computer_p=0

while flag==True:
    user=input('What is your choice?\n"r" for rock, "s" for scissors, "p" for paper, "c" to close:\n').lower()
    if user!='c':
        user_p,computer_p=play(user_p,computer_p)
    else:
        flag=False

if win(user_p,computer_p):
    print(f'You won!!! user={user_p} , computer={computer_p}')

else:
    print(f'I won user={user_p} , computer={computer_p}') 
