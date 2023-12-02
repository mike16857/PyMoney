import sys

################## Class definition ##################
class Record:
    """Represent a record."""
    def __init__(self, category, description, amount):
        """Construct a record entry."""
        self._category = category
        self._description = description
        self._amount = int(amount)
    
    @property
    def category(self):
        """Category of the entry."""
        return self._category

    @property
    def description(self):
        """Description of the entry."""
        return self._description
    
    @property
    def amount(self):
        """The amount of the entry."""
        return self._amount
    
    def cmp(self, Rcd):
        """Compare two Record entries.
           Return True if the two are identical, False if not.
        """
        if self.category == Rcd.category and self.description == Rcd.description and self.amount == Rcd.amount:
            return True
        else:
            return False
    

class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self):
        """Constructor of Records instance."""
        try:
            fh = open('records_oop.txt', 'r')
            print('Welcome Back!')
            init_money = int(fh.readline())
            st = ''
            tmp2 = fh.readlines()
            if not tmp2:    
                rcd = []
            else:
                for tp in tmp2:
                    st += tp
                rcd = [eval(s) for s in st.split('\n')] # Turn string into executable code
            fh.close()
        
        except FileNotFoundError:  # No original record file
            try:
                init_money = int(input('How much money do you have? '))

            except ValueError:  # User inputs a string that cannot be converted to integer
                sys.stderr.write('Invalid value for money. Set to 0 by default.\n') 
                init_money = 0

            rcd = []

        except:  # Record in the file does not match the format
            sys.stderr.write('Invalid format in records_oop.txt. Deleting the contents.\n')
            open('records_oop.txt','w').close()

            try:
                init_money = int(input('How much money do you have? '))

            except ValueError:  # User inputs a string that cannot be converted to integer
                sys.stderr.write('Invalid value for money. Set to 0 by default.\n') 
                init_money = 0

            rcd = []

        self._initial_money = init_money
        self._records = []
        for member in rcd:
            self._records.append(Record(member[0], member[1], member[2])) 

        return
    
    def add(self, rcd, ctgies):
        """Add one or multiple entries to 'records'.
           Validity of a category of each entry will be checked individually.
        """
        fail_count = 0
        try:
            entry_to_add = rcd.split(',')
            for i in entry_to_add:
                member = tuple(i.split())
                if len(member) != 3:
                    raise IndexError
                member_record = Record(member[0], member[1], member[2])

                if ctgies.is_category_valid(member_record.category):
                    self._records.append(member_record)
                    self._initial_money += member_record.amount
                else:
                    fail_count += 1
                    print(f'The specified category "{member_record.category}" is not in the category list.')
            
            if fail_count != 0:
                print(f'You can check the category list by command "view categories".\nFail to add {fail_count} record(s).')
            

        except IndexError:  # Input string does not follow the format
            sys.stderr.write('The format of a record should be like this: meal breakfast -50.\nFail to add a record.\n')
        
        except ValueError:  # The third string of a record, after splitting, cannot be converted to an integer
            sys.stderr.write('Invalid value for money.\nFail to add a record.\n')

    def view(self):
        """Print all the records and report the balance."""
        print('Here are your expense and income records:')
        print('Index  Category        Description           Amount') 
        print('=====  =============== ====================  ======')

        for i, member in enumerate(self._records):
            print(f'{i:<5d}  {member.category:<15s} {member.description:<20s}  {member.amount:<6d}')    

        print('=====  =============== ====================  ======')
        print(f'Now you have {self._initial_money} dollars.')  
        
    def delete(self, input_entry):
        """Delete the specified record from self._records.
           Validity of the category of the specified record will be checked first.
        """
        if len(self._records) == 0:   # Check if there is record 
            print('Currently no record, go and add some records.')
            return 

        input_entry = tuple(input_entry.split())

        if len(input_entry) != 3:
            print('Invalid format. Fail to delete a record.')  # Input format is invalid
            return

        entry_to_delete = Record(input_entry[0], input_entry[1], input_entry[2])
        
        # if entry_to_delete not in self._records:
        #     print('Record not found. Fail to delete a record.')  # The specified record does not exist
        #     return
        flag = False
        for i in self._records:
            flag = entry_to_delete.cmp(i)
            if flag == True: 
                break
        
        if flag == False:
            print('Record not found. Fail to delete a record.')  # The specified record does not exist
            return            

        else:
            tmp = []
            for i in range(len(self._records)):
                if entry_to_delete.cmp(self._records[i]):
                # if self._records[i] == entry_to_delete: 
                    # tmp += [i]
                    tmp.append(i)
        
            if len(tmp) == 1:
                print(f'You deleted {self._records[tmp[0]].category}, {self._records[tmp[0]].description}, {self._records[tmp[0]].amount}')
                self._initial_money -= self._records[tmp[0]].amount
                self._records.remove(self._records[tmp[0]])

            else:
                print(f'{len(tmp)} identical records found. Which are')
                for i in tmp:
                    print(f'Entry #{i}')

                n = int(input('Which one do you want to delete? '))

                while (n not in tmp):
                    if n == -1: # Quit delete mode 
                        break
                    print('Invalid input, please try again.')   # The specified record does not exist 
                    n = int(input('Which one do you want to delete? '))
                else:
                    print(f'You deleted {self._records[n].category}, {self._records[n].description}, {self._records[n].amount}')
                    self._initial_money -= self._records[n].amount
                    del(self._records[n])
        
        return 
    
    def find(self, target_categories, category):
        """Print the records whose category is in the specified category and all its subcategories
           and report the total amount of money of the listed records.
        """
        to_print_money = 0
        if target_categories == []:
            print('No such category.')
            return
        
        to_print = filter(lambda r: r.category in target_categories, self._records)

        print(f'Here\'s your expense and income records under category "{category}":')
        print('Category        Description           Amount') 
        print('=============== ====================  ======')

        for member in to_print:
            print(f'{member.category:<15s} {member.description:<20s}  {member.amount:<6d}')
            to_print_money += member.amount

        print('=============== ====================  ======')
        print(f'The total amount above is {to_print_money} dollars.') 

    def save(self):
        """Save the record data into 'records_oop.txt' before exiting the program."""
        tmp_ls = []
        with open('records_oop.txt', 'w') as fh:
            fh.write(f'{self._initial_money}\n')

            for i in self._records:
                tmp = (i.category, i.description, i.amount)
                tmp_ls.append(tmp)
            fh.writelines('\n'.join([str(s) for s in tmp_ls]))


class Categories:
    """Maintain the category list and provide some methods."""
    def __init__(self):
        """Valid categories to this program."""
        self._categories = ['expense', 
                                ['food', 
                                    ['meal', 'snack', 'drink'], 
                                 'transportation', 
                                    ['bus', 'railway']], 
                            'income', 
                                ['salary', 
                                 'bonus']]

    def view(self, ctgies = None, level = 0):
        """List out all the valid categories."""
        if ctgies is None:
            ctgies = self._categories

        for ct in ctgies:
            if type(ct) == list:
                self.view(ct, level + 1)
            else:
                s = ''
                s += '  ' * level
                s += f'- {ct}'
                print(s)

    def is_category_valid(self, in_ctg, ctgies = None):
        """Check if a category is valid to this program."""
        if ctgies is None:
            ctgies = self._categories

        found = False
        for ct in ctgies:
            if type(ct) == list:
                found = self.is_category_valid(in_ctg, ct)
            elif found:
                return True
            else:
                if in_ctg == ct:
                    return True
                
        return found

    def find_subcategories(self, category):
        """Find and return the target category and all its subcategories in a list."""
        def find_subcategories_gen(category, categories, found = False):
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) and type(categories[index + 1]) == list:
                        # When the target category is found,
                        # recursively call this generator on the subcategories
                        # with the flag set as True.
                        yield from find_subcategories_gen(category, categories[index + 1], True)
            else:
                if categories == category or found:
                    yield categories
        
        return [i for i in find_subcategories_gen(category, self._categories)]
    # def find_subcategories(self, category, categories = None):
    #     """Find and return the target category and all its subcategories in a list."""
    #     if categories is None:
    #         categories = self._categories

    #     if type(categories) == list:
    #         for v in categories:
    #             p = self.find_subcategories(category, v)
    #             if p == True:
    #                 index = categories.index(v)
    #                 if index + 1 < len(categories) and type(categories[index + 1]) == list:
    #                     return self._flatten(categories[index:index + 2])
    #                 else:
    #                     # return only itself if no subcategories
    #                     return [v]
    #             if p != []:
    #                 return p
                
    #     return True if categories == category else [] # return [] instead of False if not found
    
    # def _flatten(self, L):
    #     if type(L) == list:
    #         result = []
    #         for child in L:
    #             result.extend(self._flatten(child))
    #         return result
    #     else:
    #         return [L]


################## Main program ##################
categories = Categories()
records = Records()

while True:
    command = input('\nWhat do you want to do (add / view / delete / view categories / find / exit)? ')
    if command == 'add':
        record = input('Add some expense or income records with category, description, and amount (separate by spaces):\ncat1 desc1 amt1, cat2 desc2 amt2, cat3 desc3 amt3, ...\n')
        records.add(record, categories)

    elif command == 'view':
        records.view()

    elif command == 'delete':
        delete_record = input('Enter an expense or income record you want to delete with its category, description and amount (separate by spaces): cat desc amt\n')
        records.delete(delete_record)

    elif command == 'view categories':
        categories.view()

    elif command == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        records.find(target_categories, category)

    elif command == 'exit':
        records.save()
        break

    else:
        sys.stderr.write('Invalid command. Try again.\n')