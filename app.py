from flask import Flask
app = Flask(__name__)

from flask import request
import operations

@app.get("/add")
def add():
    """return query terms summed"""
    a = float(request.args['a'])
    b = float(request.args['b'])

    return str(operations.add(a, b))

@app.get("/sub")
def sub():
    """return query terms subtracted"""
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(operations.sub(a, b))
