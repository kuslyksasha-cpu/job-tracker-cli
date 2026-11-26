import db


def show_menu():
    print("\n====================")
    print("1. add")
    print("2. show")
    print("3. change status")
    print("4. delete")
    print("0. exit")
    print("====================\n")

def add_vacancy():
    db.add_vacancy(company=input("company name:\n"), position=input("position:\n"))

def show_vacancies():
    rows = db.get_all_vacancies()
    if not rows:
        print("list is empty")
    else:
        for r in rows:
            print(f"{r[0]}. {r[1]} - {r[2]} [{r[3]}]")

def update_status():
    try:
        vacancy_id = int(input("position ID:\n"))
    except ValueError as e:
        print(f"{e} - can't use symbols or letters")
        return
    new_status = input("new status:\n")
    updated = db.update_vacancy_status(vacancy_id, new_status)
    if updated == 0:
        print("ID doesn't exist")
    else:
        print("status changed")

def delete_vacancy():
    try:
        vacancy_id = int(input("position ID:\n"))
    except ValueError as e:
        print(f"{e} - can't use symbols or letters")
        return
    deleted = db.delete_vacancy(vacancy_id)
    if deleted == 0:
        print("ID doesn't exist")
    else:
        print("deleted successfully")

def main():

    db.init_db()

    while True:

        show_menu()

        choice = input()

        if choice == "1":
            add_vacancy()
        elif choice == "2":
            show_vacancies()
        elif choice == "0":
            break
        elif choice == "3":
            update_status()
        elif choice == "4":
            delete_vacancy()
        else:
            print("unknown command")

if __name__ == "__main__":
    main()