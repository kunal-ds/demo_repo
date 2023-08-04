import sqlalchemy

def get_sql_connection():
    conn = None
    try:
        conn = sqlalchemy.create_engine("mysql+pymysql://root:Kunal_root1@localhost/prac_db")
    except BaseException as b:
        print(b[1])
    finally:
        return conn
def close_sql_resources(channel,conn):
    try:
        if channel:
            channel.close()
    except BaseException as b:
        print(b[1])
    try:
        if conn:
            conn.close()
    except BaseException as b:
        print(b[1])

def add_product():
    req_list = []
    insert_querry = f'''Insert into record_table values(
    {req_list[1]},{req_list[2]}
    )'''
    conn = get_sql_connection()
    if conn:
        try:
            channel = conn.cursor()
            channel.execute(insert_querry)
            conn.commit()
        except BaseException as b:
            print(b[1])
        finally:
            close_sql_resources(channel,conn)
    else:
        return "Invalid request"
    
def get_all_product():
    all_data_list = []
    get_all_querry = f'''SELECT * from prac_table'''
    conn = get_sql_connection()
    if conn:
        try:
            channel = conn.cursor()
            channel.execute(get_all_querry)
            conn.commit()
        except BaseException as b:
            print(b[1])
        finally:
            close_sql_resources(channel,conn)
            return
    else:
        return "Invalid request"

get_all_product()

