from rethinkdb import RethinkDB
from rethinkdb.errors import ReqlOpFailedError
from contextlib import suppress

r = RethinkDB()

print("Loading database connection...")
conn = r.connect("rdb", 28015)

with suppress(ReqlOpFailedError):
    r.db_create("haste").run(conn)
with suppress(ReqlOpFailedError):
    r.db("haste").table_create("uploads").run(conn)

print("DONE SCRIPT")
