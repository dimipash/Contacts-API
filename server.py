from flask import Flask

app = Flask(__name__)

contacts = [
    {"id": "1", "name": "Ivan", "phone": "12345678"},
    {"id": "2", "name": "Georgi", "phone": "22345678"},
    {"id": "3", "name": "Petar", "phone": "32345678"},
    {"id": "4", "name": "Misho", "phone": "42345678"},
]


@app.get("/contacts")
def list_contacts():
    return contacts


@app.get("/contacts/<id>")
def read_single_contact(id):
    for contact in contacts:
        if contact["id"] == id:
            return contact

    return "That contact does not exists"


if __name__ == "__main__":
    app.run(debug=True)
