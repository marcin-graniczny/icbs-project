from icbs.account import Account
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


def print_line():
    print('#' * 100 + '\n')


if __name__ == '__main__':
    example()
    print_line()

    bug_1()
