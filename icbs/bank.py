from icbs.account import Account
from icbs.customer import Customer


class Bank:
    def __init__(self):
        self.clients = {}
        self.accounts = {}

    def import_clients(self, clients_dict):
        for client_number, client in clients_dict.items():
            self.clients[client_number] = Customer(name=client['name'], surname=client['surname'])

    def import_accounts(self, accounts_dict):
        for acc_number, acc in accounts_dict.items():
            account = Account(amount=acc['amount'], owner=self.clients[acc['owner']], iban_number=acc['iban_number'])
            self.accounts[acc_number] = account

    @staticmethod
    def money_transfer_transaction(amount, from_account, to_account):
        if amount < 0:
            raise ValueError("Amount below 0")

        if amount > from_account.amount:
            raise ValueError("Transaction failed due to not enough money")

        from_account.amount -= amount
        to_account.amount += amount
        from_account.transaction_list.append(('CREDIT', amount, to_account.iban_number))
        to_account.transaction_list.append(('DEBIT', amount, from_account.iban_number))

    def print_transaction_list_for_account(self, iban):
        self.accounts[iban[-10:]].print_transactions_list()

    def print_transaction_list_for_all_accounts(self):
        for acc_num, acc in self.accounts.items():
            self.print_transaction_list_for_account(acc.iban_number)
