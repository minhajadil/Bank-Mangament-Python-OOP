class Bank:
    def __init__(self):
        self.users = []
        self.balance = 0
        self.loan_give = 0
        self.loan_option = True

    def create_user(self, name, email, address, types):
        ac_number = len(self.users)+1
        user = User(name, email, address, types, ac_number)
        self.users.append(user)
        print(f'Account for {name} is created successfully')

    def delete_user(self, ac_number):
        for user in self.users:
            if user.ac_number == ac_number:
                delete = user
                break

        print(f'Account of {delete.name} is deleted successfully')
        self.users.remove(delete)

    def check_user(self):
        for user in self.users:
            print(
                f'User name : {user.name} AC Number :{user.ac_number} Email :{user.email}')

    def check_balance(self):
        print(f'Total Balance : {self.balance}')

    def loan_given(self):
        print(f'Total loan given : {self.loan_give}')

    def loan_on(self):
        self.loan_option = True
        print(f'Loan option turned on successfully')

    def loan_off(self):
        print(f'Loan option is turned off successfully')
        self.loan_option = False


class User:
    def __init__(self, name, email, address, types, ac_number):
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0
        self.type = types
        self.ac_number = ac_number
        self.number_of_loan = 0
        self.history = []
        self.deposits = 0

    def check_balance(self):
        print(f'Total balance : {self.balance}')

    def check_transactions(self):
        for i, ele in enumerate(self.history):
            print(f'{i+1}.{ele}')

    def take_loan(self, amount):
        if bank.loan_option == False:
            print('The bank is not giving any loan at this moment')
        elif self.number_of_loan > 2:
            print('Sorry,the limit of loan has exceeded')
        else:
            if bank.balance-(self.balance+amount) >= 0:
                self.balance += amount
                self.number_of_loan += 1
                # bank.balance -= amount
                bank.loan_give += amount
                print(f'Loan {amount} is added to your account')
                self.history.append(f'Loan Taken :{amount}')

            else:
                print(f'Sorry, It is not possible to give such amount of money')

    def transfer_amount(self, amount, ac_number):
        flag = False
        for user in bank.users:
            if (user.ac_number == ac_number):
                other = user
                flag = True
        if flag == True:
            if self.balance >= amount:
                other.balance += amount
                self.balance -= amount
                self.deposits -= amount
                self.history.append(f'Transfered {amount} to {ac_number}')
                other.history.append(
                    f'Received {amount} from {self.ac_number}')
                print(f'Transfered {amount} to {ac_number} successfully')

            else:
                print(f'Not enough money')
        else:
            print(f'Account does not Exist')

    def deposit(self, amount):
        self.balance += amount
        bank.balance += amount
        self.deposits += amount
        print(f'Deposited {amount} to your account')
        self.history.append(f'Deposit : {amount}')

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Withdrawal amount exceeded")
        else:
            if self.deposits > amount and amount > bank.balance:
                print('The bank is bankrupt')

            elif amount <= bank.balance:
                self.balance -= amount
                bank.balance -= amount
                print(f'Withdrawed {amount} succesfully')
                self.history.append(f'Withdraw : {amount}')
            elif self.deposits < amount:
                print('The loan cant be withdrawn at this moment')


bank = Bank()

# replica
# checked at 18th october,2023 3:26 AM
# everything is working properly

while 1:
    first_input = input("""
Options:
1.Admin 
2.User 
3.Exit    
""")
    if first_input == '3':
        break
    if first_input == '1':
        while True:
            Admin_input = input("""
Welcome Admin 
Options :
1.Create Account
2.Delete Account 
3.See Accounts
4.Bank Balance 
5.Loan balance
6.Turn on the Loan feature
7.Turn off the Loan feature
8.Exit 
""")
            if Admin_input == '1':
                name = input("Name: ")
                email = input("Email: ")
                address = input("Address: ")
                types = input("Type: ")
                bank.create_user(name, email, address, types)
            if Admin_input == '2':
                ac_number = input("Account Number: ")
                ac_number = int(ac_number)
                bank.delete_user(ac_number)
            if Admin_input == '3':
                print("The list of the users: ")
                bank.check_user()

            if Admin_input == '4':
                bank.check_balance()
            if Admin_input == '5':
                bank.loan_given()
            if Admin_input == '6':
                bank.loan_on()
            if Admin_input == '7':
                bank.loan_off()
            if Admin_input == '8':
                break

    if first_input == '2':
        while 1:
            ac_input = input(""""
Enter Account Number :     
""")
            if ac_input.isdigit() == False:
                break
            ac_input = int(ac_input)
            flag = False
            for user in bank.users:
                if user.ac_number == ac_input:
                    flag = True
                    current_ac = user

            if flag == False:
                print(f'Invalid Account number')
                break
            else:
                print(f'Welcome {current_ac.name} !')
                while 1:
                    user_input = input(
                        """Options :
1.Deposit 
2.Withdraw
3.Check Balance
4.Check Trx History
5.Transfer       
6.Loan
7.Exit
""")
                    if user_input == '7':
                        break
                    if user_input == '1':
                        cash_amount = input("Input Amount:")
                        cash_amount = int(cash_amount)
                        current_ac.deposit(cash_amount)
                    if user_input == '2':
                        cash = input("Input Amount :")
                        cash = int(cash)
                        current_ac.withdraw(cash)
                    if user_input == '3':
                        current_ac.check_balance()
                    if user_input == '4':
                        print("Transactions :")
                        current_ac.check_transactions()
                    if user_input == '5':
                        cash = input("Enter amount :")
                        receiver = input("Input Receiver AC:")
                        cash = int(cash)
                        receiver = int(receiver)
                        current_ac.transfer_amount(cash, receiver)
                    if user_input == '6':
                        cash = input("Input Amount :")
                        cash = int(cash)
                        current_ac.take_loan(cash)
