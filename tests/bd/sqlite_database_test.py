import sqlite3 as sl
import pandas as pd

con = sl.connect('my-test.db')

con.execute("""
    CREATE TABLE USER (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
    );
    """)

sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'

data = [
    (1, 'Alice', 21),
    (2, 'Bob', 22),
    (3, 'Chris', 23)
]

con.executemany(sql, data)

data = con.execute("SELECT * FROM USER WHERE age <= 22")
for row in data:
    print(row)

df_skill = pd.DataFrame({
    'user_id': [1,1,2,2,3,3,3],
    'skill': ['Network Security', 'Algorithm Development', 'Network Security', 'Java', 'Python', 'Data Science', 'Machine Learning']
})

df_skill.to_sql('SKILL', con)

df = pd.read_sql('''
    SELECT s.user_id, u.name, u.age, s.skill 
    FROM USER u LEFT JOIN SKILL s ON u.id = s.user_id
''', con)

df.to_sql('USER_SKILL', con)

вata = con.execute("SELECT * FROM USER WHERE age <= 22")
for row in data:
    print(row)

data = con.execute("SELECT * FROM USER_SKILL WHERE age <= 22")
for row in data:
    print(row)

data = con.execute("SELECT * FROM USER_SKILL")
for row in data:
    print(row)

