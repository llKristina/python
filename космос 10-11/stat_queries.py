import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('space_exploration.db')
cursor = conn.cursor()

# Статистический запрос 1: Получение всех астронавтов
cursor.execute("SELECT * FROM astronauts")
astronauts = cursor.fetchall()
print("All Astronauts:")
for astronaut in astronauts:
    print(astronaut)

# Статистический запрос 2: Получение всех планет
cursor.execute("SELECT name, description FROM planets")
planets = cursor.fetchall()
print("\nAll Planets:")
for planet in planets:
    print(f"{planet[0]} - {planet[1]}")

# Статистический запрос 3: Получение информации о космических миссиях
cursor.execute('''SELECT space_missions.mission_name, space_missions.mission_date, planets.name, space_missions.astronauts_involved
                  FROM space_missions
                  JOIN planets ON space_missions.target_planet_id = planets.id''')
missions = cursor.fetchall()
print("\nAll Space Missions:")
for mission in missions:
    print(f"Mission '{mission[0]}' on {mission[1]} targeting planet {mission[2]} with astronauts {mission[3]}")

# Закрытие соединения
conn.close()
