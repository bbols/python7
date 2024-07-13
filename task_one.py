import os

BALANCE_FILE = 'balance.txt'
HISTORY_FILE = 'history.txt'

def read_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, 'r') as file:
            return float(file.read().strip())
    return 0.0

def write_balance(balance):
    with open(BALANCE_FILE, 'w') as file:
        file.write(str(balance))

def read_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as file:
            return file.readlines()
    return []

def write_history(history):
    with open(HISTORY_FILE, 'w') as file:
        file.writelines(history)

def main():
    balance = read_balance()
    history = read_history()

    while True:
        print("\n1. Показать баланс")
        print("2. Пополнить счет")
        print("3. Купить что-то")
        print("4. Показать историю покупок")
        print("5. Выйти")
        choice = input("Выберите опцию: ")

        if choice == '1':
            print(f"Текущий баланс: {balance}")
        elif choice == '2':
            amount = float(input("Введите сумму пополнения: "))
            balance += amount
            print(f"Ваш новый баланс: {balance}")
        elif choice == '3':
            item = input("Введите название покупки: ")
            cost = float(input("Введите стоимость покупки: "))
            if cost <= balance:
                balance -= cost
                history.append(f"{item}: {cost}\n")
                print(f"Вы купили {item} за {cost}. Остаток на счету: {balance}")
            else:
                print("Нед§остаточно средств на счету.")
        elif choice == '4':
            print("История покупок:")
            for entry in history:
                print(entry.strip())
        elif choice == '5':
            write_balance(balance)
            write_history(history)
            print("Данные сохранены. Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

main()
