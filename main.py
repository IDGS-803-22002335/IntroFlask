from flask import Flask, render_template, request
import forms
from flask import g
from flask_wtf.csrf import CSRFProtect
from flask import flash
app = Flask(__name__)
app.secret_key = "Esta es la clave secreta"
csrf = CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def index():
    grupo = "IDSG803"
    lista = ["Juan", "Pedro", "Mario"]
    print("Index 2")
    print(f"Hola {g.nombre}")
    return render_template("index.html", grupo=grupo, lista=lista)


@app.before_request
def before_request():
    g.nombre = "Mario"
    print(' Before request 1')


@app.after_request
def after_request(response):
    print(' After request 3')
    return response


@app.route("/Alumnos", methods=["GET", "POST"])
def alumnos():
    mat = ''
    nom = ''
    edad = ''
    correo = ''
    ape = ''

    # Va a optener los valores de la clase UserForm
    alumno_clase = forms.UserForm(request.form)
    # no deja pasar si todas las validaciones no se cumplan
    if request.method == "POST" and alumno_clase.validate():
        mat = alumno_clase.matricula.data
        nom = alumno_clase.nombre.data
        ape = alumno_clase.apellidos.data
        edad = alumno_clase.edad.data
        correo = alumno_clase.email.data
        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("Alumnos.html", form=alumno_clase, mat=mat, nom=nom, ape=ape, edad=edad, correo=correo)


@app.route("/OperaBas", methods=["GET", "POST"])
def operas():
    resul = ""
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        opcion = request.form.get("Opcion")

        if opcion == "Suma":
            resul = int(num1) + int(num2)
        elif opcion == "Resta":
            resul = int(num1) - int(num2)
        elif opcion == "Multiplicar":
            resul = int(num1) * int(num2)
        elif opcion == "Dividir":
            resul = int(num1) / int(num2)

        resul = int(resul)
    return render_template("OperaBas.html", resul=resul)


@app.route("/cinePolis", methods=["GET", "POST"])
def cine():
    nombre, cantidad, tarjeta, boletos = "", 0, "", 0
    alerta, descuento = "", 0.0
    cantidadaPagar = 0

    if request.method == "POST":

        nombre = request.form.get("nombre")

        cantidad = request.form.get("compradores", "0")
        tarjeta = request.form.get("Opcion")
        boletos = request.form.get("boletos")
        cantidad = int(cantidad)
        boletos = int(boletos)

        cantidadaPagar = 0.0

        # Calcular los boletos que se pueden comprar
        boletoxpersona = 7
        boletoxpersona *= cantidad
        if boletos <= boletoxpersona:

            if boletos > 5:
                cantidadaPagar = 12 * boletos
                descuento = cantidadaPagar * 0.15
                cantidadaPagar -= descuento
            elif 3 <= boletos <= 5:
                cantidadaPagar = 12 * boletos
                descuento = cantidadaPagar * 0.10
                cantidadaPagar -= descuento
            else:
                cantidadaPagar = 12*boletos
            if tarjeta == "Si":
                descuentotarjeta = cantidadaPagar * 0.10
                cantidadaPagar -= descuentotarjeta

        else:
            alerta = "¡¡Solo se pueden comprar 7 boletos por persona!!"

    return render_template("cine.html", cantidadaPagar=cantidadaPagar, nombre=nombre, tarjeta=tarjeta, cantidad=cantidad, boletos=boletos, alerta=alerta)


@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return f"La suma de {num1} y {num2} es {num1,num2, int(num1) + int(num2)}"


@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")


@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")


@app.route("/hola")
def hola():
    return "Hola!!!"


@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}!!!"


@app.route("/numero/<int:n>")
def numero(n):
    return "Numero {}".format(n)


@app.route("/user/<string:user>/<int:id>")
def username(user, id):
    return f"Nombre: {user} ID: {id}!!!"


@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es: {}!!!".format(n1+n2)


@app.route("/default")
@app.route("/default/<string:nom>")
def func(nom="pedro"):
    return "El nombre de Nom es "+nom


@app.route("/form1")
def form1():
    return '''
          <form>
          <br>
          <label>Nombre</label>
          <input type="text" name="nombre" placeholder = "Nombre">
          </br>
          <label>Nombre</label>
          <input type="text" name="nombre" placeholder = "Nombre">
          </form>
       '''


if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True, port=300)
