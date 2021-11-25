from flask import Flask, request

app = Flask(__name__)

@app.after_request
def apply_header(response):
    response.headers["backend"] = "true"
    return response

@app.route('/', defaults={'u_path': ''}, methods = ['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:u_path>')
def catch_all(u_path):
    app.logger.critical(request.headers)
    app.logger.critical(request.data)
    app.logger.critical(request.args)
    app.logger.critical(request.form)
    app.logger.critical(request.endpoint)
    app.logger.critical(request.method)
    app.logger.critical(request.remote_addr)
    return ("Yeah Nah", 418)
