from bottle import Bottle, run, \
     template, debug, static_file

import os, sys

dirname = os.path.abspath(os.path.dirname(__file__))

app = Bottle()
debug(True)

@app.route('/static/<filename:re:.*\.css>')
def send_css(filename):
    print("Sending", filename, dirname)
    return static_file(filename, root=dirname+'/static/asset/css')

@app.route('/static/<filename:re:.*\.js>')
def send_js(filename):
    print("Sending", filename, dirname)
    return static_file(filename, root=dirname+'/static/asset/js')

@app.route('/')
def index():
    data = {"developer_name":"Tarun Lalwani",
            "developer_organization":""}
    return template('index', data = data)

@app.route('/tarun/')
def tarun():
    data = {"developer_name":"Tarun Lalwani",
            "developer_organization":""}
    return template('index', data = data)


if __name__ == "__main__":
    run(app, host='localhost', port = 8080)
