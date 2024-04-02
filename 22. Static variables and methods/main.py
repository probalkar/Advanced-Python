# static variable : A variable that is shared among all instances of a class. It is defined outside the constructor and is accessed using the class name.

# static method : A method that is shared among all instances of a class. It is defined using the @staticmethod decorator.

class Atm:

    # static variable
    __counter = 0

    def __init__(self):
        # instance variables
        self.__pin = ""
        self.__balance = 0
        Atm.__counter += 1
        self.sno = Atm.__counter

        # self.__menu()

    # getter for counter
    @staticmethod
    def get_counter():
        return Atm.__counter
    
    # setter for counter
    @staticmethod
    def set_counter(new_counter):
        if type(new_counter) != int:
            raise ValueError("Counter must be an integer")
        else:
            Atm.__counter = new_counter

    # getter for pin
    def get_pin(self):
        return self.__pin
    
    # setter for pin
    def set_pin(self, new_pin):
        if type(new_pin) != str and len(new_pin) != 4:
            raise ValueError("Pin must be a string")
        else:
            self.__pin = new_pin

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
            # self.__menu()

    def create_pin(self):
        self.__pin = input("Create your 4 digit pin: ")
        print("Pin created successfully")
        # self.__menu()

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp != self.__pin:
            print("Invalid pin")
        else:
            print(f"Your balance is {self.__balance}")
        # self.__menu()

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp != self.__pin:
            print("Invalid pin")
        else:
            amount = int(input("Enter the amount you want to deposit: "))
            self.__balance += amount
            print("Amount deposited successfully")
        # self.__menu()

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
        # self.__menu()

icici = Atm()
axis = Atm()
hdfc = Atm()
sbi = Atm()
print(Atm.get_counter())
print(icici.sno)
print(axis.sno)
print(hdfc.sno)
print(sbi.sno)