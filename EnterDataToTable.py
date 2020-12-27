#Refer the steps from Google Keep
#Doc :-https://docs.sqlalchemy.org/en/13/orm/tutorial.html

from sqlalchemy import create_engine

#Importing create_engine for connecting to database


'''
Syntax for connecting to various types of databases
Basic Format:- dialect+driver://username:password@host:port/database

You can refer at https://docs.sqlalchemy.org/en/13/core/engines.html#sqlalchemy.create_engine

#Here I am using SQL lite
'''
from sqlalchemy.ext.declarative import declarative_base
#for mapping the database


from sqlalchemy import Column, Integer, String,Sequence
Base = declarative_base()
class Student(Base):
    __tablename__ = 'students'

    name = Column(String(50))
    reg_no = Column(Integer,Sequence('student_reg_no_seq'),primary_key = True)
    group_name = Column(String(50))
    

    def __repr__(self):
        return "<Student(name='%s', reg_no='%s')>" %(self.name,self.reg_no)


if __name__ == '__main__':
    #Creating a DataBase


    print("**Table**")
    print(Student.__table__)

    #Now we enter data to the table

    std1 = Student(name='Sai', reg_no='123456', group_name='CSE')
    std2 = Student(name='Yogesh',reg_no='123457', group_name='EEE')
    std3 = Student(name='Balaji', reg_no='123458', group_name='IT')

    #Here we adding student data but it is not pushed to the database

    #Creating a session and adding our data to database
    engine = create_engine('sqlite:////home/varshan/Documents/auto_ml/db.sqlite', echo=True)
    from sqlalchemy.orm import sessionmaker
    Session_maker = sessionmaker(bind=engine)
    Session = Session_maker()
    try:
        Session.add(std1) #For adding a single row

        Session.add_all([std2,std3]) #for adding Mulitple rows at once
    except:
        print("The data you want to enter already exists")
    #To check our data we do a small query
    #here we filtering the data based on Group name
    q = Session.query(Student).filter_by(group_name='CSE')
    print("Displaying the query data")
    print(q)
    
    std3.name = 'Mastan'
    #if we want to update anything in the row
    print("Dirty session",Session.dirty) #to know the changes in any column
    
    #To know the new changes
    print("New session details", Session.new)

    #To save the changes to database we use commit
    Session.commit()

    print("Succesfully connected and added data to the database")


