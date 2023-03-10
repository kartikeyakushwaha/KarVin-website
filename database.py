from sqlalchemy import create_engine,text
import os



db_connection_string=os.environ['DB_CONNECTION_STRING']



engine=create_engine(
  db_connection_string,
connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})


def load_notes_from_db():
  with engine.connect() as conn:
   result = conn.execute(text("select * from notes"))

  note = []
  for row in result.all():
    note.append(row._mapping)
  return note


def load_note_from_db(id):
  with engine.connect() as conn:
    query="SELECT * FROM notes WHERE id = {}".format(id)
    result =conn.execute(text(query))
    
  rows=result.all()
  if len(rows)==0:
      return None
  else:
    return (rows[0]._mapping)
#---------------------------------------------
