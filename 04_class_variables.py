#==========================Assignment:
'''
Create a class Bank with a class variable bank_name. 
Add a class method change_bank_name(cls, name) that allows changing the bank name. 
Show that it affects all instances.
'''

class Bank:
    bank_name = "Public Bank"
    print(f"Initial Bank Name: {bank_name}")

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

Bank.change_bank_name("National Bank")
print(f"Second Bank Name: {Bank.bank_name}")

Bank.change_bank_name("Private Bank")
print(f"Third Bank Name: {Bank.bank_name}")



print("=" * 80)


# ----------------Input from user----------------
class Bank:
    bank_name = "National Bank"
    print(f"--------First bank Name: {bank_name}---------")

    @classmethod
    def chnage_bank_name(cls, name):
        cls.bank_name = name

Bank.chnage_bank_name(input("Enter the new name of Bank: "))
print(f"--------Second bank Name: {Bank.bank_name}---------")

Bank.chnage_bank_name(input("Enter the new name of Bank: "))
print(f"--------Third bank Name: {Bank.bank_name}---------")