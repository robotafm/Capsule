# Примеры взяты отсюда: https://ru.wikibooks.org/wiki/SQLAlchemy

from sqlalchemy import create_engine
# Создать БД sqlite в оперативной памяти:
engine = create_engine('sqlite:///:memory:', echo=False) # echo -> печать SQL запросов

# # sqlite://<nohostname>/<path>
# # where <path> is relative:
# engine = create_engine('sqlite:///foo.db')
# # Unix/Mac - 4 initial slashes in total
# engine = create_engine('sqlite:////absolute/path/to/foo.db')

# # Windows
# engine = create_engine('sqlite:///C:\\path\\to\\foo.db')

# # Windows alternative using raw string
# engine = create_engine(r'sqlite:///C:\path\to\foo.db')

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()
users_table = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
    Column('password', String)
)

metadata.create_all(engine)

class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

from sqlalchemy.orm import mapper  #достать "Отобразитель" из пакета с объектно-реляционной моделью
print(mapper(User, users_table))  # и отобразить. Передает класс User и нашу таблицу
user = User("Вася", "Василий", "qweasdzxc")
print(user)  #Напечатает <User('Вася', 'Василий', 'qweasdzxc'>
print(user.id)  #Напечатает None

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

# Добавление одной записи:
vasiaUser = User("vasia", "Vasiliy Pypkin", "vasia2000")
session.add(vasiaUser)

ourUser = session.query(User).filter_by(name="vasia").first()

# Добавление нескольких записей:
session.add_all([User("kolia", "Cool Kolian[S.A.]","kolia$$$"), 
                 User("zina", "Zina Korzina", "zk18")])   #добавить сразу пачку записей

vasiaUser.password = "-=VP2001=-"   #старый пароль был таки ненадежен

# Сохранение всех изменений в БД, поле чего откат невозможен:
session.commit()

vasiaUser.name = 'Vaska'

fake_user = User('fakeuser', 'Invalid', '12345')
session.add(fake_user)

print(session.query(User).filter(User.name.in_(['Vasko', 'fakeuser'])).all())

# Откат вернёт БД в состояние после ближайшего commit():
session.rollback()

print (vasiaUser.name, fake_user in session)

print(session.query(User).filter(User.name.in_(['vasia', 'fakeuser'])).all())

# Можно получать значения из БД, отсортированные по столбцу:
for instance in session.query(User).order_by(User.id): 
    print(instance.name, instance.fullname)

# Результаты возвращаются в виде кортежей, которым можно давать имена:
for name, fullname in session.query(User.name, User.fullname): 
    print(name, fullname)

# Или так:
for row in session.query(User, User.name).all(): 
   print(row.User, row.name)

# Можно использовать label() для скалярных атрибутов и aliased() для классов:
from sqlalchemy.orm import aliased
user_alias = aliased(User, name='user_alias')
for row in session.query(user_alias, user_alias.name.label('name_label')).all(): 
   print(row.user_alias, row.name_label)

# Использование срезов массивов Pyton для получения части данных:
for u in session.query(User).order_by(User.id)[1:2]: 
   print("Результат:", u)

# Обращение к конкретному полю name:
for name in session.query(User.name).filter_by(fullname='Cool Kolian[S.A.]'): 
   print(name)

# Также можно создать фильтр такого типа:
for name in session.query(User.name).filter(User.fullname=='Cool Kolian[S.A.]'):
   print(name)
