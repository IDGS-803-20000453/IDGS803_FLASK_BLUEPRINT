import flask
from Alumnos.route import alumnos
from Directivos.route import dir
from Maestros.route import maestros

app = flask.Flask(__name__)
app.config['DEBUG']=True


@app.route("/", methods=['GET'])
def home():
    return flask.jsonify({'Datos':'Home'})

app.register_blueprint(alumnos)
app.register_blueprint(dir)
app.register_blueprint(maestros)

if __name__ == '__main__':
    app.run()