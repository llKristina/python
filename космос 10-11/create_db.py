import sqlite3

# Подключение к базе данных (если базы нет, она будет создана)
conn = sqlite3.connect('space_exploration.db')
cursor = conn.cursor()

# Создание таблицы астронавтов
cursor.execute('''CREATE TABLE IF NOT EXISTS astronauts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    nationality TEXT,
                    birth_date TEXT,
                    space_missions_count INTEGER
                )''')

# Создание таблицы планет
cursor.execute('''CREATE TABLE IF NOT EXISTS planets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    diameter REAL,
                    distance_from_sun REAL
                )''')

# Создание таблицы космических миссий
cursor.execute('''CREATE TABLE IF NOT EXISTS space_missions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    mission_name TEXT NOT NULL,
                    mission_date TEXT,
                    target_planet_id INTEGER,
                    astronauts_involved TEXT,
                    mission_description TEXT,
                    FOREIGN KEY (target_planet_id) REFERENCES planets (id)
                )''')

# Подтверждение изменений и закрытие соединения
conn.commit()
conn.close()

print("Database and tables for space exploration created successfully!")
