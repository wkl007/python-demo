from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    user_id = Column(String(20), ForeignKey('user.id'))


engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')

DBSession = sessionmaker(bind=engine)

# session = DBSession()
# new_user = User(id='2', name='Bob')
# session.add(new_user)
# session.commit()
# session.close()

session2 = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session2.query(User).filter(User.id == '2').one()
print(type(user), user.name)
session2.close()
