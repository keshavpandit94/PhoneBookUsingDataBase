#Phonebook with connect DataBase SQlite3 Project
import sqlite3

con = sqlite3.connect("Create_DB_Using_Proj//phone_book.db")

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contact (
            name TEXT NOT NULL,
            number INTEGER  NOT NULL 
    )     
''')

def show_all_contact():
    cursor.execute("SELECT * FROM contact")
    print("\n")
    print("*"*50)
    for row in cursor.fetchall():
        print(row)

def add_new_contact(name, number):
    cursor.execute("INSERT INTO contact (name, number) VALUES (?,?)", (name,number))
    print("\nSuccessfully added contact!")
    con.commit()

def delete_contact():
    cursor.execute("DELETE FROM contact WHERE name = ?", (name))
    print("Sucessfuly delete contact!")
    con.commit()
    show_all_contact()
    

def main ():
    while True :
        print("\nPhone Book :")
        print("1. Show all contact")
        print("2. Add new contact")
        print("3. Delete contact")
        print("Exit ")
        
        choice = int(input ("Enter the your choice: "))
        
        if choice == 1 :
            show_all_contact()
        
        elif choice == 2 :
            name = input("Enter the name: ")
            number = input("Enter the number")
            add_new_contact(name, number)
            
        elif choice == 3:
            show_all_contact()
            name = input("Enter the name: ")
            delete_contact(name)
        elif choice == 4:
            print("Exit the application")
            break;
        else:
            print("Invalid input, Please try again")
        
                


if __name__ == "__main__":
    main()             