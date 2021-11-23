from flask import  render_template , url_for , redirect , request , flash

from contactsapp import app
from contactsapp.models import Contact
from contactsapp import db

#url request path to homepage
@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)


#adding contact
@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        name= request.form['name']
        phonenumber= request.form['phone']
        email= request.form['email']
        group= request.form['group']

        new_contact = Contact(name, email, phonenumber, group)
        db.session.add(new_contact)
        db.session.commit()
        flash("Contact saved")
        return redirect(url_for('index'))

#deleting contact
@app.route('/delete/<id>/', methods= ['GET', 'POST'])
def delete(id):
    contact_to_delete = Contact.query.get(id)
    db.session.delete(contact_to_delete)
    db.session.commit()
    flash("Contact deleted")
    
    return redirect(url_for('index'))

