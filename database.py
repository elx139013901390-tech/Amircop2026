import sqlite3

db = sqlite3.connect("bot.db", check_same_thread=False)
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS warns(
    chat_id INTEGER,
    user_id INTEGER,
    warns INTEGER DEFAULT 0,
    PRIMARY KEY(chat_id, user_id)
)
""")
db.commit()


def add_warn(chat_id, user_id):
    cur.execute("SELECT warns FROM warns WHERE chat_id=? AND user_id=?", (chat_id, user_id))
    row = cur.fetchone()

    if row:
        warns = row[0] + 1
        cur.execute(
            "UPDATE warns SET warns=? WHERE chat_id=? AND user_id=?",
            (warns, chat_id, user_id)
        )
    else:
        warns = 1
        cur.execute(
            "INSERT INTO warns(chat_id,user_id,warns) VALUES(?,?,?)",
            (chat_id, user_id, warns)
        )

    db.commit()
    return warns
