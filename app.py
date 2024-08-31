from flask import Flask, render_template, request, redirect, url_for
from models import db, Dogs

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Creamos la base de datos
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/adopción")
def perritos():
    perrito = 'Zeus'
    perrito_2 = 'Nala'
    #return "Hola, aquí le puedes dar un nuevo hogar a lindos perritos"
    return render_template("perritos.html", perrito=perrito,perrito_2=perrito_2)

@app.route("/tamaños")
def tamaños():
    return "Tenemos de todos los tamaños elige el que más te guste :)"

@app.route("/nuevos_perritos")
def nuevos_perritos():
    return render_template("nuevos_perritos.html")

@app.route("/guardar_informacion", methods = ["POST"])
def guardar_informacion():
    name = request.form["name"]
    color = request.form["color"]
    race = request.form["race"]
    age = request.form["age"]
    new_dog = Dogs(
        name = name,
        color = color,
        race = race,
        age = age
    )
    db.session.add(new_dog)
    db.session.commit()
    return render_template("perritos.html")


app.run(port=3000)

#tarea: buscar un tema para la página web

#Serif
#Times New Roman: font-family: "Times New Roman", Times, serif;
#Georgia: font-family: Georgia, serif;
#Garamond: font-family: Garamond, serif;
#Palatino: font-family: Palatino, serif;
#Sans-Serif
#Arial: font-family: Arial, Helvetica, sans-serif;
#Verdana: font-family: Verdana, Geneva, sans-serif;
#Tahoma: font-family: Tahoma, Geneva, sans-serif;
#Trebuchet MS: font-family: "Trebuchet MS", Helvetica, sans-serif;
#Monospace
#Courier New: font-family: "Courier New", Courier, monospace;
#Lucida Console: font-family: "Lucida Console", Monaco, monospace;
#Consolas: font-family: Consolas, monospace;
#Cursive
#Comic Sans MS: font-family: "Comic Sans MS", cursive, sans-serif;
#Caveat: font-family: Caveat, cursive;
#Fantasy
#Papyrus: font-family: Papyrus, fantasy;
#Impact: font-family: Impact, fantasy;

#cantidad = db.Column(db.Integer)
#nombre = db.Column(db.String(100))
#total = db.Column(db.Float)
#disponible = db.Column(db.Boolean)
#fecha = db.Column(db.Date)
#timestamp = db.Column(db.DateTime)

#db.Integer: Para números enteros.
#db.String(length): Para cadenas de texto, donde length especifica la longitud máxima de la cadena.
#db.Float: Para números de punto flotante.
#db.Boolean: Para valores booleanos (True/False).
#db.Date: Para fechas.
#db.DateTime: Para fechas y horas.



