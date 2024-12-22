import sqlite3
from xml.dom.minidom import Document

# Подключение к базе данных
conn = sqlite3.connect('space_exploration.db')
cursor = conn.cursor()

# Запрос всех космических миссий
cursor.execute("SELECT * FROM space_missions")
missions = cursor.fetchall()

# Создание XML документа
doc = Document()
root = doc.createElement("missions")
doc.appendChild(root)

# Добавление данных о миссиях в XML
for mission in missions:
    mission_element = doc.createElement("mission")
    root.appendChild(mission_element)
    
    id_element = doc.createElement("id")
    id_element.appendChild(doc.createTextNode(str(mission[0])))
    mission_element.appendChild(id_element)

    name_element = doc.createElement("name")
    name_element.appendChild(doc.createTextNode(mission[1]))
    mission_element.appendChild(name_element)

    date_element = doc.createElement("date")
    date_element.appendChild(doc.createTextNode(mission[2]))
    mission_element.appendChild(date_element)

    # Запрос названия планеты по ID
    cursor.execute("SELECT name FROM planets WHERE id = ?", (mission[3],))
    planet = cursor.fetchone()  # Получаем имя планеты
    planet_name = planet[0] if planet else "Unknown"  # Если планета не найдена, ставим "Unknown"

    planet_element = doc.createElement("target_planet")
    planet_element.appendChild(doc.createTextNode(planet_name))
    mission_element.appendChild(planet_element)

    astronauts_element = doc.createElement("astronauts_involved")
    astronauts_element.appendChild(doc.createTextNode(mission[4]))
    mission_element.appendChild(astronauts_element)

# Сохранение XML в файл
with open("missions.xml", "w") as f:
    f.write(doc.toprettyxml())

# Закрытие соединения
conn.close()

print("Data exported to XML successfully!")
