import sqlite3

conn = sqlite3.connect("Contacts.db")

cursor = conn.cursor()

def menu():
    print("----MENU----")
    print("1. CREATE A TABLE")
    print("2. ADD A NEW NUMBER")
    print("3. DELETE A NUMBER")
    print("4. SEARCH FOR A NUMBER")
    print("5. EXIT")

    choice = int(input("Enter your choice (1-4): "))
    return choice

while True:
    choice = menu()
    if choice == 1:
        cursor.execute("CREATE TABLE CONTACTS (Name text, Number string)")
        print("Table created successfully!")
    elif choice == 2:
        name = input("Enter the name: ")
        number = int(input("Enter the number: "))
        cursor.execute("INSERT INTO CONTACTS VALUES (?,?)", (name, number))
        conn.commit()
        print("Number added successfully!")
    elif choice == 3:
        name = input("Enter the name to delete: ")
        cursor.execute("DELETE FROM CONTACTS WHERE Name =?", (name,))
        conn.commit()
        print("Number deleted successfully!")
    elif choice == 4:
        name = input("Enter name to be searched:")
        cursor.execute("SELECT Name, Number FROM CONTACTS WHERE Name =?", (name,))
        print(cursor.fetchall())
    elif choice == 5:
        print("Exiting...")
        break
    

    
   

