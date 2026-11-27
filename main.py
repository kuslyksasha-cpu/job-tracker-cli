import db

STATUSES = ("applied", "test task", "interview", "offer", "rejected")

def show_menu():
    print("\n====================")
    print("1. add")
    print("2. show")
    print("3. change status")
    print("4. delete")
    print("5. search by company")
    print("6. filter by status")
    print("7. statistics")
    print("0. exit")
    print("====================\n")

def search_vacancies():
    rows = db.search_by_company(query=input("company name:\n"))
    print_vacancies(rows)

def filter_vacancies():
    for i, status in enumerate(STATUSES, start=1):
        print(f"{i}. {status}")
    try:
        status_choice = int(input("status number:\n"))
    except ValueError:
        print("invalid status number")
        return
    if not 1 <= status_choice <= len(STATUSES):
        print("invalid status number")
        return
    status = STATUSES[status_choice - 1]
    rows = db.filter_by_status(status)
    print_vacancies(rows)

def show_stats():
    stats = db.get_stats()
    if not stats:
        print("list is empty")
    else:
        total = sum(count for _, count in stats)
        print(f"Total: {total}")
        for status, count in stats:
            print(f"{status}: {count}")

def print_vacancies(rows):
    if not rows:
        print("list is empty")
    else:
        for r in rows:
            print(f"{r[0]}. {r[1]} - {r[2]} {r[3]} [{r[4]}] {r[5]}")

def add_vacancy():
    db.add_vacancy(company=input("company name:\n"), position=input("position:\n"), url=input("Job URL (optional):\n").strip() or "-")

def show_vacancies():
    rows = db.get_all_vacancies()
    print_vacancies(rows)

def update_status():
    try:
        vacancy_id = int(input("position ID:\n"))
    except ValueError as e:
        print(f"{e} - can't use symbols or letters")
        return
    for i, status in enumerate(STATUSES, start=1):
        print(f"{i}. {status}")
    try:
        status_choice = int(input("new status number:\n"))
    except ValueError:
        print("invalid status number")
        return
    if not 1 <= status_choice <= len(STATUSES):
        print("invalid status number")
        return
    new_status = STATUSES[status_choice - 1]
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
        elif choice == "5":
            search_vacancies()
        elif choice == "6":
            filter_vacancies()
        elif choice == "7":
            show_stats()
        else:
            print("unknown command")

if __name__ == "__main__":
    main()