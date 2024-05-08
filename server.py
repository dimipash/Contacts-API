from flask import Flask, request

app = Flask(__name__)

next_id = 5

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

@app.post('/contacts')
def create_contact():
   global next_id 

   new_contact = {
      "id": f'{next_id}',
      "name": request.json['name'],
      "phone": request.json['phone'],
   }

   contacts.append(new_contact)

   next_id += 1
   
   return new_contact

@app.put('/contacts/<id>')
def update_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            contact['name'] = request.json['name'] if 'name' in request.json else contact['name']
            contact['phone'] = request.json['phone'] if 'phone' in request.json else contact['phone']
            return contact
    
    return 'There is no contact with that id!'

if __name__ == "__main__":
    app.run(debug=True)
