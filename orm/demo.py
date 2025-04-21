from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Step 1: Setup
Base = declarative_base()
engine = create_engine('sqlite:///mydb.db')  # this creates a file called mydb.db
Session = sessionmaker(bind=engine)
session = Session()

# Step 2: Create a simple table (class)
class User(Base):
    __tablename__ = 'users'  # table name in the database

    id = Column(Integer, primary_key=True)
    name = Column(String)

# Step 3: Create the table in the database
Base.metadata.create_all(engine)

# Step 4: Add a new user
user1 = User(name="Piseth")
session.add(user1)
session.commit()

# Step 5: Read all users
all_users = session.query(User).all()
for user in all_users:
    print(user.id, user.name)
