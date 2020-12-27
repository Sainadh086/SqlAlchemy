from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:////home/varshan/Documents/auto_ml/db.sqlite', echo = True)
meta = MetaData()

students = Table(
   'students', meta,
   Column('name', String(50)),
   Column('reg_no', Integer, primary_key = True),
   Column('group_name', String(50)),
)
meta.create_all(engine)
