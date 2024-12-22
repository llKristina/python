from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Функция для получения данных из базы данных
def get_db_data(query, params=()):
    conn = sqlite3.connect('space_exploration.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    # Получаем все космические миссии с помощью SELECT-запроса
    missions = get_db_data("SELECT * FROM space_missions")
    return render_template('index.html', missions=missions)

@app.route('/book', methods=['POST'])
def book():
    astronaut_name = request.form['name']
    astronaut_nationality = request.form['nationality']
    astronaut_birth_date = request.form['birth_date']
    mission_id = request.form['mission_id']
    
    # Вставка нового астронавта и бронирования с помощью SELECT-запроса
    conn = sqlite3.connect('space_exploration.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO astronauts (name, nationality, birth_date, space_missions_count) VALUES (?, ?, ?, ?)", 
                   (astronaut_name, astronaut_nationality, astronaut_birth_date, 1))
    conn.commit()
    astronaut_id = cursor.lastrowid
    cursor.execute("UPDATE space_missions SET astronauts_involved = IFNULL(astronauts_involved, '') || ?, mission_date = CURRENT_DATE WHERE id = ?", 
                   (f" {astronaut_name}", mission_id))
    conn.commit()
    conn.close()
    
    return f"Booking confirmed for astronaut {astronaut_name}"

# Страница с информацией о астронавтах
@app.route('/astronauts')
def astronauts():
    astronauts_data = get_db_data("SELECT * FROM astronauts")
    return render_template('astronauts.html', astronauts=astronauts_data)

# Страница с информацией о миссиях
@app.route('/missions')
def missions():
    missions_data = get_db_data('''SELECT space_missions.mission_name, space_missions.mission_date, planets.name, space_missions.astronauts_involved
                                   FROM space_missions
                                   JOIN planets ON space_missions.target_planet_id = planets.id''')
    return render_template('missions.html', missions=missions_data)

# Страница с информацией о планетах
@app.route('/planets')
def planets():
    planets_data = get_db_data("SELECT * FROM planets")
    return render_template('planets.html', planets=planets_data)

if __name__ == '__main__':
    app.run(debug=True)
