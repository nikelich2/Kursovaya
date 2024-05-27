from flask import Flask, render_template
import pandas as pd
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # Подключение к базе данных и загрузка данных
    conn = sqlite3.connect('ad_campaigns.db')
    metrics = pd.read_sql_query("SELECT * FROM metrics", conn)
    conn.close()

    # Преобразование DataFrame в список словарей для передачи в шаблон
    metrics_dict = metrics.to_dict(orient='records')
    return render_template('index.html', metrics=metrics_dict)

if __name__ == '__main__':
    app.run(debug=True)
