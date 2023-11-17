import random
friend_count = int(input("Enter the number of friends joining (including you):"))
if friend_count <= 0:
    print("No one is joining for the party")
else:
    friend_list = {}
    i = 1
    print("Enter the name of every friend (including you), each on a new line")
    while i <= friend_count:
        friend_list.update({input(): 0.0})
        i += 1
    print("Enter the total bill value:")
    bill = float(input())
    split = round(bill / friend_count, 2)
    for key in friend_list:
        friend_list.update({key: split})
    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    if lucky == 'No':
        print('No one is going to be lucky')
        print(friend_list)
    else:
        lucky_friend = random.choice(list(friend_list.keys()))
        print(f'{lucky_friend} is the lucky one!')
        split = round(bill / (friend_count-1), 2)
        for key in friend_list:
            friend_list.update({key: split})
        friend_list.update({lucky_friend: 0})
        print(friend_list)