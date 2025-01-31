from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    grupo = "IDSG803"
    lista = ["Juan", "Pedro", "Mario"]
    return render_template("index.html", grupo=grupo, lista=lista)


@app.route("/OperaBas", methods=["GET", "POST"])
def operas():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        resul = int(num1) + int(num2)
        resul = int(resul)
    return render_template("OperaBas.html", resul=resul)


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
    app.run(debug=True, port=300)
