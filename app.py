from flask import Flask ,render_template

app=Flask(__name__)

NOTES=[{
  'id':1,
  'Subject':'Mathematics',
'Topics':'Linear_Equation_in_two_variable',
  'link':'http',
  'Board':'CBSE'
},
       {
  'id':2,
  'Subject':'Mathematics',
'Topics':'Polynomials',
  'link':'http',
  'Board':'CBSE'
},
       {
  'id':3,
  'Subject':'Science',
'Topics':'Electricity',
  'link':'http',
  'Board':'CBSE'
}
  
]
 

@app.route("/")
def hello_world():
  return render_template('home.html',notes=NOTES)

if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)
  