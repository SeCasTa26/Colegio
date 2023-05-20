from contacts import contacts

from app import app

app.register_blueprint(contacts)

# starting the app
if __name__ == "__main__":
    app.run(port=8080, debug=True)