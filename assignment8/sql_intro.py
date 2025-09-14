import sqlite3

def add_subscriber(cursor, name, address):
  try:
    cursor.execute("INSERT INTO Subscribers (name, address) VALUES (?, ?)", (name, address))
  except sqlite3.IntegrityError:
    print(f"{name} at {address} is already in the database.")

def add_publisher(cursor, name):
  try:
    cursor.execute("INSERT INTO Publishers (name) VALUES (?)", (name,))
  except sqlite3.IntegrityError:
    print(f"{name} is already in the database.")

def add_magazine(cursor, name, publisher_name):
  cursor.execute("SELECT * FROM Publishers WHERE name = ?", (publisher_name,))
  results = cursor.fetchall()
  if len(results) > 0:
    publisher_id = results[0][0]
  else:
    print(f"There was no publisher named {publisher_name}.")
    return

  try:
    cursor.execute("INSERT INTO Magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
  except sqlite3.IntegrityError:
    print(f"{name} is already in the database.")

def add_subscription(cursor, subscriber_name, subscriber_address, magazine_name):
  cursor.execute("SELECT * FROM Subscribers WHERE name = ? AND address = ?", (subscriber_name, subscriber_address))
  results = cursor.fetchall()
  if len(results) > 0:
    subscriber_id = results[0][0]
  else:
    print(f"There was no subscriber named {subscriber_name} at {subscriber_address}.")
    return

  cursor.execute("SELECT * FROM Magazines WHERE name = ?", (magazine_name,))
  results = cursor.fetchall()
  if len(results) > 0:
    magazine_id = results[0][0]
  else:
    print(f"There was no magazine named {magazine_name}.")
    return

  cursor.execute("SELECT * FROM Subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
  results = cursor.fetchall()
  if len(results) > 0:
    print(f"Subscriber {subscriber_name} is already subscribed to magazine {magazine_name}.")
    return

  cursor.execute("INSERT INTO Subscriptions (subscriber_id, magazine_id) VALUES (?, ?)", (subscriber_id, magazine_id))


with sqlite3.connect("../db/magazines.db") as conn:
  conn.execute("PRAGMA foreign_keys = 1")
  cursor = conn.cursor()

  # Create tables
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS Subscribers (
      subscriber_id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      address TEXT NOT NULL,
      UNIQUE (name, address)
    )
  """)

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS Publishers (
      publisher_id INTEGER PRIMARY KEY,
      name TEXT NOT NULL UNIQUE
    )
  """)

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS Magazines (
      magazine_id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      publisher_id INTEGER,
      FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id),
      UNIQUE (name, publisher_id)
    )
  """)

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS Subscriptions (
      subscription_id INTEGER PRIMARY KEY,
      magazine_id INTEGER,
      subscriber_id INTEGER,
      expiration_date DATE DEFAULT (DATE('now', '+1 year')),
      FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id),
      FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id)
    )
  """)

  print("Tables created successfully or already exist.")

  # Insert sample data into tables

  add_subscriber(cursor, "Alice", "123 Main St")
  add_subscriber(cursor, "Bob", "456 Tiger Ln")
  add_subscriber(cursor, "Charlie", "789 Candyland Dr")

  add_publisher(cursor, "Pets International")
  add_publisher(cursor, "Inert Hobbies")
  add_publisher(cursor, "News and Stuff")

  add_magazine(cursor, "Cats Cats Cats", "Pets International")
  add_magazine(cursor, "Dogs Dogs Dogs", "Pets International")
  add_magazine(cursor, "Snakesss", "Pets International")
  add_magazine(cursor, "Rocks Monthly", "Inert Hobbies")
  add_magazine(cursor, "Sitting Digest", "Inert Hobbies")
  add_magazine(cursor, "World on Fire", "News and Stuff")

  add_subscription(cursor, "Alice", "123 Main St", "Dogs Dogs Dogs")
  add_subscription(cursor, "Alice", "123 Main St", "World on Fire")
  add_subscription(cursor, "Bob", "456 Tiger Ln", "Cats Cats Cats")
  add_subscription(cursor, "Bob", "456 Tiger Ln", "Rocks Monthly")
  add_subscription(cursor, "Charlie", "789 Candyland Dr", "Sitting Digest")
  add_subscription(cursor, "Charlie", "789 Candyland Dr", "Snakesss")

  cursor.execute("SELECT * FROM Subscribers")
  print("Subscribers:")
  for row in cursor.fetchall():
    print(row)

  cursor.execute("SELECT * FROM Magazines ORDER BY name")
  print("Magazine (Alpha):")
  for row in cursor.fetchall():
    print(row)

  cursor.execute("SELECT * FROM Magazines" \
                " JOIN Publishers ON Magazines.publisher_id = Publishers.publisher_id" \
                " WHERE Publishers.name = 'Pets International'")
  print("Pets International Magazines:")
  for row in cursor.fetchall():
    print(row)

  conn.commit()

  print("all done!")

