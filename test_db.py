from db import get_db_connection

conn = get_db_connection()

if conn and conn.is_connected():
    print("SUCCESS: Database connected successfully!")
    conn.close()
else:
    print("FAILED: Could not connect to the database.")