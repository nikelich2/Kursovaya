import sqlite3

conn = sqlite3.connect('ad_campaigns.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE campaigns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    start_date TEXT,
    end_date TEXT
)
''')

cursor.execute('''
CREATE TABLE metrics (
    id INTEGER PRIMARY KEY,
    campaign_id INTEGER,
    date TEXT,
    impressions INTEGER,
    clicks INTEGER,
    cost REAL,
    conversions INTEGER,
    FOREIGN KEY (campaign_id) REFERENCES campaigns (id)
)
''')


cursor.executemany('''
INSERT INTO campaigns (name, start_date, end_date)
VALUES (?, ?, ?)
''', [
    ('Campaign 1', '2024-01-01', '2024-01-31'),
    ('Campaign 2', '2024-02-01', '2024-02-28'),
    ('Campaign 3', '2024-03-01', '2024-03-31')
])


cursor.executemany('''
INSERT INTO metrics (campaign_id, date, impressions, clicks, cost, conversions)
VALUES (?, ?, ?, ?, ?, ?)
''', [
    (1, '2024-01-01', 1000, 50, 100.0, 5),
    (1, '2024-01-02', 1200, 60, 120.0, 6),
    (2, '2024-02-01', 2000, 100, 200.0, 10),
    (3, '2024-03-01', 1500, 75, 150.0, 7)
])

# Сохранение изменений и закрытие соединения

conn.commit()
conn.close()
