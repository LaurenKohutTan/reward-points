import os

from flask import request, send_file

from app import app

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def asset(path):
    path = os.path.join('../static', request.path[1:])

    try:
        return send_file(path)
    except IsADirectoryError:
        return send_file(os.path.join(path, 'index.html'))
    except FileNotFoundError:
        return '404: Not Found', 404
