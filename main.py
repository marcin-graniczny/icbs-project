from icbs.account import Account
from icbs.bank import Bank
from icbs.customer import Customer

customer1 = Customer('Jan', 'Kowalski')
account1 = Account(100, 'PL40109024025249592124718384', customer1)

customer2 = Customer('Adam', 'Nowak')
account2 = Account(500, 'PL05109024021887523769458146', customer2)


def example():
    account1.cash_transaction('DEPOSIT', 300)
    account1.cash_transaction('WITHDRAW', 200)
    account1.cash_transaction('DEPOSIT', 150)
    account1.print_account_balance()

    print_line()

    account2.cash_transaction('DEPOSIT', 300)
    account2.cash_transaction('DEPOSIT', 300)
    account2.print_account_balance()


def bug_1():
    # Popsuty bankomat wywołuje metodę w taki sposób:
    account2.cash_transaction('WITΗDRAW', 200)

    # Sprawny bankomat wywołuje metodę w taki sposób:
    account2.cash_transaction('WITHDRAW', 200)


def bug_2():
    account1.print_account_balance()
    account1.cash_transaction('DEPOSIT', -100)
    account1.print_account_balance()


def bug_3():
    account1.print_account_balance()
    account1.cash_transaction('WITHDRAW', 100000)
    account1.print_account_balance()


def dev_1():
    account1.print_transactions_list()


def dev_2():
    clients_dict = {
        '0000000001': {'name': 'Jan', 'surname': 'Kowalski'},
        '0000000002': {'name': 'Anna', 'surname': 'Nowak'}
    }

    accounts_dict = {
        '3769458146': {'amount': 1000, 'iban_number': 'PL05109024021887523769458146', 'owner': '0000000001'},
        '3769458147': {'amount': 2000, 'iban_number': 'PL05109024021887523769458147', 'owner': '0000000002'}
    }

    bank = Bank()
    bank.import_clients(clients_dict)
    bank.import_accounts(accounts_dict)

    bank.money_transfer_transaction(100, bank.accounts['3769458147'], bank.accounts['3769458146'])
    bank.print_transaction_list_for_all_accounts()


def print_line():
    print('#' * 100 + '\n')


if __name__ == '__main__':
    example()
    print_line()

    # bug_1()
    # bug_2()
    # bug_3()
    # dev_1()

    dev_2()
    print_line()
