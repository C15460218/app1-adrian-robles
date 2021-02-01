from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
Bootstrap(app)

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:marcopolo123@localhost:5432/escolares'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://zyezsomlktdsre:0b63209efcb819e744bc93c1e8959f278e815ca87771068ece6031eee6848d0a@ec2-54-196-1-212.compute-1.amazonaws.com:5432/d6s3529jvhbpdk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Alumno(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(30))


@app.route('/', methods=['GET','POST'])
def index():
    print("index")
    if request.method == "POST":
        print("request")
        campo_nombre = request.form['nombre']
        campo_apellido = request.form['apellido']
        alumno = Alumno(nombre=campo_nombre,apellido=campo_apellido)
        db.session.add(alumno)
        db.session.commit()
        mensaje="Alumno Registrado"
        return redirect(url_for('index'))
    lista = ["Acerca","Nosotros","Contacto","Preguntas Frecuentes"]
    return render_template("index.html",variable = lista)
    #return redirect(url_for('acerca'))

@app.route('/eliminar/<id>')
def eliminar(id):
    eAlumno = Alumno.query.filter_by(id=int(id)).delete()
    db.sesion.commit()
    return redirect(url_for('acerca'))

@app.route('/editar/<id>')
def editar(id):
    ralumno = Alumno.query.filter_by(id=int(id)).first()
    return render_template('editar.html', alumno = ralumno)

@app.route('/actualizar', methods=['GET','POST'])
def actualizar():
   if request.method == 'POST':
       cons = Alumno.query.get(request.form['id'])
       cons.nombre = request.form['nombreE']
       cons.apellido = request.form['apellidoE']
       db.session.commit()
       return redirect(url_for('acerca'))

@app.route('/acerca')
def acerca():
    consulta = Alumno.query.all()
    print(consulta)
    return render_template("acerca.html",variable=consulta)

if __name__ == "__main__":
    app.run(debug=True)