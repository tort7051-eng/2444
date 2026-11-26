import sqlite3

# Створюємо (або відкриваємо) базу даних AnimalKingdom.db
conn = sqlite3.connect("AnimalKingdom.db")
cursor = conn.cursor()

# 1. Створення таблиці Animals
cursor.execute("""
CREATE TABLE IF NOT EXISTS Animals (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    "Назва звіра" TEXT NOT NULL,
    "Тип звіра" TEXT NOT NULL
)
""")

# Очищаємо таблицю перед повторним запуском (щоб записи не дублювалися)
cursor.execute("DELETE FROM Animals")

# 2. Вставка п'яти записів
animals = [
    ("Лев", "Ссавець"),
    ("Крокодил", "Плазун"),
    ("Орел", "Птах"),
    ("Морська черепаха", "Плазун"),
    ("Мавпа", "Ссавець"),
]

cursor.executemany(
    'INSERT INTO Animals ("Назва звіра", "Тип звіра") VALUES (?, ?)',
    animals,
)

# 3. Зміна назви "Орел" на "Сокіл"
cursor.execute(
    'UPDATE Animals SET "Назва звіра" = ? WHERE "Назва звіра" = ?',
    ("Сокіл", "Орел"),
)

conn.commit()

# 4. Вибірка всіх звірів типу "Ссавець"
print("--- Усі ссавці ---")
cursor.execute('SELECT * FROM Animals WHERE "Тип звіра" = ?', ("Ссавець",))
for row in cursor.fetchall():
    print(row)

# 5. Виведення всіх записів про звірів
print("\n--- Усі записи в таблиці Animals ---")
cursor.execute("SELECT * FROM Animals")
for row in cursor.fetchall():
    print(row)

conn.close()