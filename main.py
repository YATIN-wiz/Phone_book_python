import sqlite3

conn = sqlite3.connect("Contacts.db")

cursor = conn.cursor()

# Create table if not exists
cursor.execute("CREATE TABLE IF NOT EXISTS CONTACTS (Name text, Number string, Relation text)")

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
        relation = input("Enter relation:")
        cursor.execute("INSERT INTO CONTACTS VALUES (?,?,?)", (name, number, relation))
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
        result = cursor.fetchall()
        for rec in result:
            print("Name:",rec[0], "Number:",rec[1])

    elif choice == 4:
        print("Exiting...")
        break


    
   

