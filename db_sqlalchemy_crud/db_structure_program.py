import psycopg2
def connect():
    c=psycopg2.connect("host=localhost dbname=flask-bick user=postgres password=ninja1pd2ac3")
    return c
def get_all_thinks():
    con=connect()
    cur=con.cursor()
    cur.execute("select version();")
    record=cur.fetchone()
    print("we are conected to the {}".format(record))
    '''
    create_que=" create table bick.bick(brand varchar(20),id integer) ;"
    cur.execute(create_que)
    print("table cratede successfully")
    '''
    cur.execute("select * from bick.table_bick;")
    bick=cur.fetchall()
    cur.close()
    con.close()
    return bick
