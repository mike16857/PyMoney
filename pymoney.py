money = int(input('How much money do you have? '))

flag = True
entries = []

while flag:
    action = input('What do you want to do (add / view / delete / exit)? ')

    if action == 'add':
        entry = input('Add an expense or income record with description and amount:\ndesc1 amt1, desc2 amt2, desc3 amt3, ...\n').split(',')
        for i in entry:
            entries.append(tuple(i.split()))
            money += int(i.split()[1])
        # print(entries)
        # print(money)

    elif action == 'view':
        print('Here are your expense and income records:')
        print('Description     Amount')
        print('=============== ======')
        for item, amount in entries:
            print(f'{item:15} {amount:6}')
        print('=============== ======')
        print(f'Now you have {money} dollars.\n')
        
    elif action == 'delete':
        entry_to_delete = tuple(input('Enter an expense or income record you want to delete with description and amount:\n').split())
        if entry_to_delete not in entries:
            print('Record not found.')
        else:
            num = entries.count(entry_to_delete)
            if num == 1:
                entries.remove(entry_to_delete)
                money -= int(entry_to_delete[1])
            else:
                print(f'{num} identical records found.')
                n = int(input('How many records do you want to delete? '))
                if n > num:
                    print('Invalid input, please try again.')
                else:
                    for i in range(n):
                        entries.remove(entry_to_delete)
                        money -= int(entry_to_delete[1])
        print(entries)
        print(money)

    elif action == 'exit':
        flag = False
        break

    else:
        print('Invalid input, please try again.')

    # item, change = input('Add an expense or income record with   description and amount:\n').split()
    # change = int(change)
    # if item == 'q':
    #     flag = False
    #     break
    # balance = money + change
    # print('Now you have %d dollars.' %(balance))
    # money = balance