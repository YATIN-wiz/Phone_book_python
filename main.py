import sqlite3

conn = sqlite3.connect("Contacts.db")

cursor = conn.cursor()

# Create table if not ex
cursor.execute("CREATE TABLE IF NOT EXISTS CONTACTS (Name text, Number string)")

def menu():
    print("----MENU----")
    print("1. ADD A NEW NUMBER")
    print("2. DELETE A NUMBER")
    print("3. SEARCH FOR A NUMBER")
    print("4. EXIT")

    choice = int(input("Enter your choice (1-4): "))
    return choice

while True:
    choice = menu()
    if choice == 1:
        name = input("Enter the name: ")
        number = int(input("Enter the number: "))
        cursor.execute("INSERT INTO CONTACTS VALUES (?,?)", (name, number))
        conn.commit()
        print("Number added successfully!")
    elif choice == 2:
        name = input("Enter the name to delete: ")
        cursor.execute("DELETE FROM CONTACTS WHERE Name =?", (name,))
        conn.commit()
        print("Number deleted successfully!")
    elif choice == 3:
        name = input("Enter name to be searched:")
        cursor.execute("SELECT Name, Number FROM CONTACTS WHERE Name =?", (name,))
        print(cursor.fetchall())
    elif choice == 4:
        print("Exiting...")
        break


    
   

