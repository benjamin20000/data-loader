from fastapi import FastAPI
from  .mysql_connector import init_db, init_table, select_table
app = FastAPI()


@app.get("/")
def read_root():
    init_db()
    init_table()
    res = select_table()

    return {"res": res}


