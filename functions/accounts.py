class Account:
    def __init__(self):
        self.accounts = []
    def add_account(self):
        ac_name = input("Enter name: ")
        deposit = int(input("Enter deposit amount: "))
        unique_id = int(input("Enter unique number in 6 digit: "))
        id = len(self.accounts + 1)
        self.accounts.append({'id':id,'name':ac_name,'deposit':deposit,'unique':unique_id})
        print("Account added successfully..")
    def get_account(self,ac_name):
        for val in self.accounts:
            if val['name'] == ac_name:
                uniqueness = input("Enter unique_id: ")
                if uniqueness == val['unique']:
                    print(f"id : {val['id']}")
                    print(f"deposit : {val['deposit']}")
                else:
                    print("You got wrong pin try next time")
    #delete , update , to text file , connection to database also, request response with html 