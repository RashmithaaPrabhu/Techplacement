from flask import Flask, render_template, request, redirect, url_for
import os
import json

# File path for storing contacts
CONTACTS_FILE = "contacts.json"

app = Flask(__name__)

# Function to load contacts from a file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save contacts to a file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Route to display all contacts
@app.route('/')
def index():
    contacts = load_contacts()
    return render_template('index.html', contacts=contacts)

# Route to add a new contact
@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        # Load contacts and add the new one
        contacts = load_contacts()

        if not phone.isdigit() or "@" not in email:
            return "Invalid phone number or email."

        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)

        return redirect(url_for('index'))

    return render_template('add_contact.html')

# Route to search for a contact
@app.route('/search', methods=['GET', 'POST'])
def search_contact():
    if request.method == 'POST':
        name = request.form['name']
        contacts = load_contacts()
        contact = contacts.get(name)
        if contact:
            return render_template('search_result.html', name=name, contact=contact)
        else:
            return "No contact found for " + name
    return render_template('search_contact.html')

# Route to update a contact
@app.route('/update', methods=['GET', 'POST'])
def update_contact():
    contacts = load_contacts()

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        # Validate phone number and email format
        if not phone.isdigit() or "@" not in email:
            return "Invalid phone number or email format."

        if name in contacts:
            contacts[name] = {"phone": phone, "email": email}
            save_contacts(contacts)
            return redirect(url_for('index'))
        else:
            return f"No contact found for {name}."

    # Handling the GET request when user is looking for a contact to update
    name = request.args.get('name')
    contact = contacts.get(name)
    return render_template('update_contact.html', contact=contact)

if __name__ == '__main__':
    app.run(debug=True)
