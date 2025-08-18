from fastapi import FastAPI
from  .mysql_connector import init_db, init_table, select_table
app = FastAPI()

init_db()
init_table()


@app.get("/")
def read_root():
    res = select_table()
    return {"res": res}


