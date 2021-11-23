from sys import excepthook
from flask import Flask, render_template , url_for , redirect , request , flash
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)

# for app to recognize and connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)

#database instance
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False )
    lastname = db.Column(db.String(100), nullable=False )
    phonenumber =  db.Column(db.String(), nullable=False)
    email =  db.Column(db.String(100), nullable=False )
    group =  db.Column(db.String(100))


    def __init__(self, firstname, lastname, phonenumber, email, group):
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber
        self.email = email
        self.group = group




#url request path to homepage
@app.route('/')
def index():
    contacts = Contact.query.all()
    render_template("index.html", contacts=contacts)


#adding contact
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        firstname= request.form['first-name']
        lastname= request.form['last-name']
        email= request.form['email']
        phonenumber= request.form['phone']
        group= request.form['group']

        new_contact = Contact(firstname, lastname, phonenumber, email, group)
        db.session.add(new_contact)
        db.session.commit()
        flash("Contact saved")
        return redirect(url_for('index'))

#deleting contact
@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    contact_to_delete = Contact.query.get(id)
    db.session.delete(contact_to_delete)
    db.session.commit()
    flash("Contact deleted")
    
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)