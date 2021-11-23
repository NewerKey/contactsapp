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
    first_name = db.Column(db.String(100), nullable=False )
    last_name = db.Column(db.String(100), nullable=False )
    phone_number =  db.Column(db.Integer(), nullable=False)
    email =  db.Column(db.String(100), nullable=False )
    group =  db.Column(db.String(100))


    def __repr__(self):
        return '<Contact %r>' % self.id




#url request path to homepage
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        firstname= request.form['first-name']
        lastname= request.form['last-name']
        email= request.form['email']
        phone= request.form['phone']
        group= request.form['group']

        new_contact = Contact(firstname, lastname, email, phone, group)
        db.session.add(new_contact)
        db.session.commit()
        flash("Contact saved")
        return redirect('/')

    else:
        all_contacts = Contact.query.all()
        return render_template("index.html", contacts= all_contacts)




#deleting contact
@app.route('/delete/<int:id>')
def delete(id):
    contact_to_delete = Contact.query.get_or_404(id)
    try:
        db.session.delete(contact_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that contact'

if __name__ == "__main__":
    app.run(debug=True)