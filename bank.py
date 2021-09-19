class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def balanceInquiry(self):
        print("Your balance is : 2000")

    def cashWithdrawl(self,amount):
        newAmount = 2000-amount
        print("Your withdrawed: " + str(amount)+ " , " + "Your remaining balance is: " + str(newAmount))
def main():
    name = input("What is your name?")
    print("Hello" + " " + name)
    cardNumber = input("Insert your card number: ")
    pin = input("Enter your pin: ")
    new_user= Atm(cardNumber,pin)

    print("Choose you activity:")
    print("1.Balance Inquiry")
    print("2.Cash Withdrawl")
    activity = int(input("Enter your choice: "))

    if(activity==1):
        new_user.balanceInquiry()
    elif(activity==2):
        amount = int(input("Enter the amount: "))
        new_user.cashWithdrawl(amount)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()
 
