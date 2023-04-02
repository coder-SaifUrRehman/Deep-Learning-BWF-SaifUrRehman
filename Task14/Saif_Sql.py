import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="MOCK_DATA.sql"
)

query = 'SELECT * FROM people'  # Read data from "MOCK_DATA" table
df = pd.read_sql(query, conn)
print(df)
