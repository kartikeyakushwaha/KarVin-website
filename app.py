from flask import Flask ,render_template
from database import load_notes_from_db,load_note_from_db



app=Flask(__name__)



 

@app.route("/")
def hello_world():
  note=load_notes_from_db()
  return render_template('home.html',notes=note)
  

@app.route("/note/<id>")
def show_note(id):
  note=load_note_from_db(id)
  if not note:
    return "Not Found",404
  return render_template('notes_page.html', notes=note)




if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)
  