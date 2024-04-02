# technically nothing is private in Python

# the __ prefix makes the variable/method private(technically not private but hidden)

class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        self.__menu()

    def get_pin(self):
        return self.__pin
    
    def set_pin(self, pin):
        self.__pin = pin

    def __menu(self):
        user_input = int(input("""
            Hello! Welcome to the ATM
            1. Enter 1 to create pin
            2. Enter 2 to check balance
            3. Enter 3 to deposit money
            4. Enter 4 to withdraw money
            5. Enter 5 to exit
            """))
        
        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.check_balance()
        elif user_input == 3:
            self.deposit()
        elif user_input == 4:
            self.withdraw()
        elif user_input == 5:
            print("Thank you for using the ATM")
        else:
            print("Invalid input. Please try again")
            self.__menu()

    def create_pin(self):
        self.__pin = input("Create your 4 digit pin: ")
        print("Pin created successfully")
        self.__menu()

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp != self.__pin:
            print("Invalid pin")
        else:
            print(f"Your balance is {self.__balance}")
        self.__menu()

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp != self.__pin:
            print("Invalid pin")
        else:
            amount = int(input("Enter the amount you want to deposit: "))
            self.__balance += amount
            print("Amount deposited successfully")
        self.__menu()

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp != self.__pin:
            print("Invalid pin")
        else:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount > self.__balance:
                print("Insufficient balance")
            else:
                self.__balance -= amount
                print("Amount withdrawn successfully")
        self.__menu()

icici = Atm()
# print(icici._Atm__balance)
# you can access the hidden variables/methods using the _ClassName__variableName or _ClassName__methodName() syntax