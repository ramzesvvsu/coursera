class Value():
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = int(value - value*instance.commission)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission




def main():
    new_account = Account(0.1)
    new_account.amount = 100

    print(new_account.amount)

if __name__ == '__main__':
    main()


