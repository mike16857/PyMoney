money = int(input('How much money do you have? '))

flag = True
entries = []
tmp = [] # record the index of the entry to be deleted

while flag:
    action = input('What do you want to do (add / view / delete / exit)? ')

    if action == 'add':
        entry_to_add = input('Add an expense or income record with description and amount:\ndesc1 amt1, desc2 amt2, desc3 amt3, ...\n').split(',')

        for i in entry_to_add:
            entries.append(tuple(i.split()))
            money += int(i.split()[1])
        # print(entries)
        # print(money)

    elif action == 'view':
        print('Here are your expense and income records:')
        print('Index    Description     Amount')
        print('=====    ==============  ======')

        for i, (item, amount) in enumerate(entries):
            print(f'{i:<5d}    {item:15s} {int(amount):<6d}')

        print('=====    ==============  ======')
        print(f'Now you have {money} dollars.\n')
        
    elif action == 'delete':
        entry_to_delete = tuple(input('Enter an expense or income record you want to delete with description and amount: ').split())

        if entry_to_delete not in entries:
            print('Record not found.')
        else:
            for i in range(len(entries)):
                if entries[i] == entry_to_delete: 
                    tmp += [i]

            if len(tmp) == 1:
                entries.remove(entry_to_delete)
                money -= int(entry_to_delete[1])

            else:
                print(f'{len(tmp)} identical records found. Which are')
                for i in tmp:
                    print(f'Entry #{i}')

                n = int(input('Which one do you want to delete? '))

                while (n not in tmp):
                    print('Invalid input, please try again.')
                    n = int(input('Which one do you want to delete? '))
                else:
                    del(entries[n])
                    money -= int(entry_to_delete[1])
        
        tmp = []
            

    elif action == 'exit':
        flag = False
        break

    else:
        print('Invalid input, please try again.')
