import sqlite3

# Function to create the database and table if they don't exist
def create_database():
    conn = sqlite3.connect('dates.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dates (
            id INTEGER PRIMARY KEY,
            date TEXT,
            event TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to add a new date
def add_date(date):
    conn = sqlite3.connect('dates.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO dates (date) VALUES (?)', (date,))
    conn.commit()
    conn.close()

# Function to update an existing date
def update_date(date_id, new_date):
    conn = sqlite3.connect('dates.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE dates SET date = ? WHERE id = ?', (new_date, date_id))
    conn.commit()
    conn.close()

# Function to delete a date
def delete_date(date_id):
    conn = sqlite3.connect('dates.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM dates WHERE id = ?', (date_id,))
    conn.commit()
    conn.close()

# Function to retrieve all dates
def load_dates():
    conn = sqlite3.connect('dates.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, date FROM dates')
    dates = cursor.fetchall()
    conn.close()
    return dates

# 

# Create the database and table
create_database()

# Load existing dates from the database
delete_date(6)

existing_dates = load_dates()
print("these are the existing database dates ",existing_dates)




#root.mainloop()
