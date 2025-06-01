import mysql.connector
import schedule
import time

def sync():
    print("[*] Running snapshot sync...")

    src = mysql.connector.connect(
        host=os.environ['SRC_DB_HOST'],
        user=os.environ['SRC_DB_USER'],
        password=os.environ['SRC_DB_PASS'],
        database=os.environ['SRC_DB_NAME']
    )

    dest = mysql.connector.connect(
        host=os.environ['DEST_DB_HOST'],
        user=os.environ['DEST_DB_USER'],
        password=os.environ['DEST_DB_PASS'],
        database=os.environ['DEST_DB_NAME']
    )

    src_cursor = src.cursor()
    dest_cursor = dest.cursor()

    dest_cursor.execute("DROP TABLE IF EXISTS user_snapshot")
    dest_cursor.execute("CREATE TABLE user_snapshot (id INT PRIMARY KEY, name VARCHAR(255))")

    src_cursor.execute("SELECT id, name FROM users")
    for (id, name) in src_cursor.fetchall():
        dest_cursor.execute("INSERT INTO user_snapshot (id, name) VALUES (%s, %s)", (id, name))

    dest.commit()
    src.close()
    dest.close()
    print("[✓] Sync complete")

schedule.every(10).seconds.do(sync)

if __name__ == "__main__":
    import os
    sync()  # initial sync
    while True:
        schedule.run_pending()
        time.sleep(1)
