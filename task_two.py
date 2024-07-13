import os

def list_directory():
    files = []
    dirs = []
    for item in os.listdir():
        if os.path.isfile(item):
            files.append(item)
        else:
            dirs.append(item)
    return files, dirs

def save_directory_listing():
    files, dirs = list_directory()
    with open('listdir.txt', 'w') as file:
        file.write('files: ' + ', '.join(files) + '\n')
        file.write('dirs: ' + ', '.join(dirs) + '\n')

def main():
    while True:
        print("\n1. Просмотр содержимого рабочей директории")
        print("2. Сохранить содержимое рабочей директории в файл")
        print("3. Выйти")
        choice = input("Выберите опцию: ")

        if choice == '1':
            files, dirs = list_directory()
            print("Файлы:")
            for f in files:
                print(f"  {f}")
            print("Папки:")
            for d in dirs:
                print(f"  {d}")
        elif choice == '2':
            save_directory_listing()
            print("Содержимое рабочей директории сохранено в listdir.txt")
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

main()
