from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from EC2 + Docker!"}

@app.get("/db-check")
def db_check():
    try:
        conn = psycopg2.connect(os.getenv('DAtABASE_URL'))
        return {"db_status":"connected"}
    except Exception as e:
        return {"db_status":"error","detail":str(e)}