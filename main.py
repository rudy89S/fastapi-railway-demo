from fastapi import FastAPI
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI + Railway works!"}

@app.on_event("startup")
def connect_db():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_PUBLIC_URL"))
        cursor = conn.cursor()
        cursor.execute("SELECT current_database();")
        db = cursor.fetchone()
        print(f" Connected to database: {db[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f" Database connection failed: {e}")

