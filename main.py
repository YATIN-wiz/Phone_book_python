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
    print("4. VIEW ALL THE CONTACTS")
    print("5. TO VIEW THE CONTACTS OF A PARTICULAR RELATION ")
    print("6. EXIT")

    choice = int(input("Enter your choice (1-6): "))
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
        result = cursor.execute("DELETE FROM CONTACTS WHERE Name =?", (name,))
        conn.commit()
        print(result.rowcount)
        if result.rowcount == 0:
            print("Name not found!")
        else:
            print("Number deleted successfully!")

    elif choice == 3:
        name = input("Enter name to be searched:")
        cursor.execute("SELECT Name, Number, Relation FROM CONTACTS WHERE Name =?", (name,))
        result = cursor.fetchall()
        for rec in result:
            print("Name:",rec[0],"-->", "Number:",rec[1],"-->" ,"Relation:", rec[2])

    elif choice == 4:
        cursor.execute("SELECT * FROM CONTACTS")
        result = cursor.fetchall()
        for rec in result:
            print("Name:",rec[0],"-->","Number:",rec[1],"-->","Relation:",rec[2])

    elif choice == 5:
        relation = input("Enter relation to be searched:")
        cursor.execute("SELECT Name, Number, Relation FROM CONTACTS WHERE Relation =?", (relation,))
        result = cursor.fetchall()
        for rec in result:
            print("Name:",rec[0],"-->","Number:",rec[1],"-->","Relation:",rec[2])
    

    elif choice == 6:
        print("Exiting...")
        break


    
   

