from flask import Flask, request 

app = Flask(__name__)

@app.after_request
def apply_header(response):
    response.headers["backend"] = "true"
    return response

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    app.logger.critical(request.headers)
    return "Yeah Nah"
