import sqlite3

conn = sqlite3.connect("Contacts.db")

cursor = conn.cursor()

def menu():
    print("----MENU----")
    print("1. CREATE A TABLE")
    print("2. ADD A NEW NUMBER")
    print("3. DELETE A NUMBER")
    print("4. SEARCH FOR A NUMBER")

    choice = input("Enter your choice (1-4): ")
    return choice

while True:
    choice = menu()
    if choice == "1":
        cursor.execute("CREATE TABLE CONTACTS (Name text, Number integer)")
        print("Table created successfully!")
    elif choice == "2":
        
