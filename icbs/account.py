class Account:
    def __init__(self, amount, iban_number, owner):
        self.amount = amount
        self.iban_number = iban_number
        self.owner = owner

    def __str__(self):
        return f'Account number {self.iban_number} owned by {self.owner}'

    def cash_transaction(self, transaction_type, amount):
        print(f'Amount before transaction is {self.amount}')
        if transaction_type == 'WITHDRAW':
            print(f'Withdrawing {amount} from account number {self.iban_number}')
            self.amount -= amount
        elif transaction_type == 'DEPOSIT':
            print(f'Depositing {amount} to account number {self.iban_number}')
            self.amount += amount
        else:
            raise NameError("Unsupported cash transaction")
        print(f'New amount is {self.amount}\n')

    def print_transactions_list(self):
        raise NotImplementedError

    def print_account_balance(self):
        print(f'Account balance for account {self.iban_number} is {self.amount}\n')
