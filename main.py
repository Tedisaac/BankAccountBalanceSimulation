from users import Users


class Bank:
    users = []

    def __init__(self):
        self.users.append(Users('Wanjiru', 0))
        self.users.append(Users('Linda', 0))
        self.users.append(Users('Juma', 0))
        print("Welcome to your bank of choice.")

    def selectFromDict(self, options, name):
        index = 0
        indexValidList = []
        print('Select an ' + name + '(1-5):')
        for optionName in options:
            index = index + 1
            indexValidList.extend([options[optionName]])
            print(str(index) + ') ' + optionName)
        inputValid = False
        while not inputValid:
            inputRaw = input(name + ': ')
            inputNo = int(inputRaw) - 1
            if inputNo > -1 and inputNo < len(indexValidList):
                selected = indexValidList[inputNo]
                inputValid = True
                break
            else:
                print('Please select a valid ' + name + ' number')

        return selected

    def chooseUser(self):
        name = input("Input your username: ")
        if name == self.users[0].name:
            self.name = self.users[0].name
            self.amount = self.users[0].amount
            self.welcomeMessage()
        elif name == self.users[1].name:
            self.name = self.users[1].name
            self.amount = self.users[1].amount
            self.welcomeMessage()
        elif name == self.users[2].name:
            self.name = self.users[2].name
            self.amount = self.users[2].amount
            self.welcomeMessage()
        else:
            print("User does not exist")
            self.chooseUser()

    def welcomeMessage(self):
        print("Hello " + self.name + ", your account balance is : ")
        print(self.amount)
        self.chooseService()

    def chooseService(self):
        options = {}
        options['Deposit'] = 'deposit'
        options['Withdraw'] = 'withdraw'
        options['Transfer'] = 'transfer'
        options['Switch Account'] = 'switch'
        options['Exit'] = 'exit'
        option = self.selectFromDict(options, 'option')
        if option == 'deposit':
            self.deposit()
        elif option == 'withdraw':
            self.withdraw()
        elif option == 'transfer':
            self.transfer()
        elif option == 'switch':
            self.switchUser()
        elif option == 'exit':
            print("Thank you for choosing our service :)")
        else:
            print("Invalid Choice. Please choose a number from 1-5")
            self.chooseService()

    def switchUser(self):
        name = input("Input new username : ")
        if name == self.name:
            print("You cannot switch to the same account")
            self.switchUser()
        elif name == self.users[0].name or name == self.users[1].name or name == self.users[2].name:
            if name == self.users[0].name:
                self.name = name
                self.amount = self.users[0].amount
                print(self.name)
                self.welcomeMessage()
            elif name == self.users[1].name:
                self.name = name
                self.amount = self.users[1].amount
                print(self.name)
                self.welcomeMessage()
            elif name == self.users[2].name:
                self.name = name
                self.amount = self.users[2].amount
                print(self.name)
                self.welcomeMessage()
        else:
            print("Invalid account. Please ensure you have typed the name correctly.")
            self.switchUser()

    def deposit(self):
        amount = float(input("Input the deposit amount: "))
        self.amount = self.amount + amount
        if self.name == self.users[0].name:
            self.users[0].amount = self.amount
        elif self.name == self.users[1].name:
            self.users[1].amount = self.amount
        elif self.name == self.users[2].name:
            self.users[2].amount = self.amount
        print("Deposit successful")
        print("Your new account balance is : ")
        print(self.amount)
        self.chooseService()

    def withdraw(self):
        amount = float(input("Input the withdrawal amount: "))
        if self.amount >= amount:
            self.amount = self.amount - amount
            if self.name == self.users[0].name:
                self.users[0].amount = self.amount
            elif self.name == self.users[1].name:
                self.users[1].amount = self.amount
            elif self.name == self.users[2].name:
                self.users[2].amount = self.amount
            print("Withdrawal successful")
            print("Your new account balance is : ")
            print(self.amount)
            self.chooseService()
        else:
            print("You have insufficient funds to make this withdrawal")
            self.chooseService()

    def transfer(self):
        tuser = input("Input the receiver name: ")
        if tuser == self.name:
            print("You cannot send funds to the same user")
            self.transfer()
        elif tuser == self.users[0].name or tuser == self.users[1].name or tuser == self.users[2].name:
            tamount = float(input("Input transfer amount: "))
            if self.amount >= tamount:
                self.amount = self.amount - tamount
                if self.name == self.users[0].name:
                    self.users[0].amount = self.amount
                elif self.name == self.users[1].name:
                    self.users[1].amount = self.amount
                elif self.name == self.users[2].name:
                    self.users[2].amount = self.amount
                if tuser == self.users[0].name:
                    self.users[0].amount = self.users[0].amount + tamount
                    print("Transfer successful")
                    print("Your new account balance is : ")
                    print(self.amount)
                    self.chooseService()
                elif tuser == self.users[1].name:
                    self.users[1].amount = self.users[1].amount + tamount
                    print("Transfer successful")
                    print("Your new account balance is : ")
                    print(self.amount)
                    self.chooseService()
                elif tuser == self.users[2].name:
                    self.users[2].amount = self.users[2].amount + tamount
                    print("Transfer successful")
                    print("Your new account balance is : ")
                    print(self.amount)
                    self.chooseService()
            else:
                print("You have insufficient funds to make the transfer")
                self.chooseService()
        else:
            print("Invalid user. The user does not seem to exist")
            self.transfer()


acc = Bank()
acc.chooseUser()
