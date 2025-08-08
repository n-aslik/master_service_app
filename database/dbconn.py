import psycopg2 # type: ignore

def async_get_db():
    connect=psycopg2.connect(dbname="master_servicesdb",host="localhost",user="postgres",password="aasl8998",port="5432")
    return connect
    
    


    

