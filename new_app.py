import sqlalchemy
from sqlalchemy import text
engine = sqlalchemy.create_engine("mysql+pymysql://root:Kunal_root1@localhost/prac_db")
with engine.connect() as connection:
    result = connection.execute(text("select * from prac_table"))
    print(result.all())
    for row in result:
        print("username:", row.firstname)