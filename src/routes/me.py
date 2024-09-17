from app import app

@app.route('/api/me')
def me():
    return "me"