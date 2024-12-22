import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('space_exploration.db')
cursor = conn.cursor()

# Вставка данных о астронавтах
cursor.execute("INSERT INTO astronauts (name, nationality, birth_date, space_missions_count) VALUES ('Yuri Gagarin', 'Russian', '1934-03-09', 1)")
cursor.execute("INSERT INTO astronauts (name, nationality, birth_date, space_missions_count) VALUES ('Neil Armstrong', 'American', '1930-08-05', 1)")
cursor.execute("INSERT INTO astronauts (name, nationality, birth_date, space_missions_count) VALUES ('Valentina Tereshkova', 'Russian', '1937-03-06', 1)")

# Вставка данных о планетах
cursor.execute("INSERT INTO planets (name, description, diameter, distance_from_sun) VALUES ('Earth', 'The third planet from the Sun, home to life.', 12742, 149.6)")
cursor.execute("INSERT INTO planets (name, description, diameter, distance_from_sun) VALUES ('Mars', 'The fourth planet from the Sun, known as the Red Planet.', 6779, 227.9)")
cursor.execute("INSERT INTO planets (name, description, diameter, distance_from_sun) VALUES ('Jupiter', 'The largest planet in the Solar System.', 139820, 778.6)")

# Вставка данных о космических миссиях
cursor.execute("INSERT INTO space_missions (mission_name, mission_date, target_planet_id, astronauts_involved, mission_description) VALUES ('Vostok 1', '1961-04-12', 1, 'Yuri Gagarin', 'First human spaceflight to orbit Earth')")
cursor.execute("INSERT INTO space_missions (mission_name, mission_date, target_planet_id, astronauts_involved, mission_description) VALUES ('Apollo 11', '1969-07-16', 1, 'Neil Armstrong, Buzz Aldrin, Michael Collins', 'First manned mission to land on the Moon')")
cursor.execute("INSERT INTO space_missions (mission_name, mission_date, target_planet_id, astronauts_involved, mission_description) VALUES ('Venera 7', '1970-12-15', 2, 'No astronauts', 'First successful landing on Venus')")

# Подтверждение изменений и закрытие соединения
conn.commit()
conn.close()

print("Data inserted successfully!")
