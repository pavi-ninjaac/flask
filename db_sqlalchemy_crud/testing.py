import psycopg2
import psycopg2.extras
def connect():
    c=psycopg2.connect("host=localhost dbname=flask-bick user=postgres password=ninja1pd2ac3")
    return c
def get_all_thinks():
    con=connect()
    #for dictionary cursor
    cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #cur=con.cursor()
    cur.execute("select version();")
    record=cur.fetchone()
    print("we are conected to the {}".format(record))
    '''
    create_que=" create table bick.bick(brand varchar(20),id integer) ;"
    cur.execute(create_que)
    print("table cratede successfully")
    '''
    cur.execute('insert into bick.bick (brand,id) values(%s,%s)',('pavi',3))
    print("successfully inserted")
    #commit is so important to do make things chanced in databse
    con.commit()
    #normal cursor
    cur.execute("select * from bick.bick;")
    #dictionary cursure

    bick=cur.fetchall()
    cur.close()
    con.close()
    for bi in bick:
         print(bi['brand'])
if __name__=="__main__":
    res=    get_all_thinks()
    print(res)
