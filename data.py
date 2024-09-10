import mysql.connector, os, dotenv
from dotenv import load_dotenv
load_dotenv()

password = os.getenv("PASS")

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = password,
  database = "users"
)

cursor = db.cursor()