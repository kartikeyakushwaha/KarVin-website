from flask import Flask ,render_template

app=Flask(__name__)

NOTES=[{
  'id':1,
  'Subject':'Mathematics',
'Topics':'Linear_Equation_in_two_variable',
  'link':'https://docs.google.com/presentation/d/1ReeT1l0DwpjtLfJKscTUCP2WpawG_uqCfWC-k4sidEA/edit?usp=share_link',
  'Board':'CBSE'
},
       {
  'id':2,
  'Subject':'Mathematics',
'Topics':'Polynomials',
  'link':'https://drive.google.com/file/d/14DxFK-hSUnlBGea_llWyqm-MrIXMBHTC/view?usp=share_link',
  'Board':'CBSE'
},
       {
  'id':3,
  'Subject':'Science',
'Topics':'Electricity',
  'link':'https://docs.google.com/presentation/d/1BoT_sbplWiqh7M0A5idB2K1pSkSjAYOCpVPPkq--Kb4/edit?usp=share_link',
  'Board':'CBSE'
}
  
]
 

@app.route("/")
def hello_world():
  return render_template('home.html',notes=NOTES)

if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)
  