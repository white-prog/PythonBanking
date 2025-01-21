from functions import accounts

def main():
    print("BANKING SYSTEM")
    print("1.add account")
    print("2.get account")

    first_acnt = accounts.Account()
    while True:
        inp = input("Enter S to Exit : ")
        if inp == 'S':
            print("Thank you")
            break
        operation = int(input("Enter number: "))
        if operation == 1:
            first_acnt.add_account()
        elif operation == 2:
            first_acnt.get_account()
            



if __name__ == "__main__":
    main()