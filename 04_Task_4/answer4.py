from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from psycopg2 import sql

app = Flask(__name__)


def create_table():
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        user="postgres",
        password="Extensa@5210",
        database="library_exam_db"
    )
    cursor = conn.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Readers (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


create_table()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

    
        if not name or '@' not in email:
            error_message = "Invalid data. Please make sure to enter a name and a valid email address."
            return render_template('index.html', error_message=error_message)

       
        try:
            conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        user="postgres",
        password="Extensa@5210",
        database="library_exam_db"
            )
            cursor = conn.cursor()
            insert_query = sql.SQL('INSERT INTO Readers (name, email) VALUES ({}, {})').format(
                sql.Literal(name),
                sql.Literal(email)
            )
            cursor.execute(insert_query)
            conn.commit()
            return redirect(url_for('index'))
        except psycopg2.Error as e:
            error_message = f"Database error: {str(e)}"
            return render_template('index.html', error_message=error_message)
        finally:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)