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
    date_joined= db.Column(db.DateTime, default=datetime.utcnow)
    email =  db.Column(db.String(100), nullable=False )
    group =  db.Column(db.String(100))


    def __repr__(self):
        return '<Contact %r>' % self.id




#url request path to homepage
@app.route('/', methods=['POST', 'GET'])
def Index():
    all_contacts = Contact.query.all()
    return render_template("index.html", contacts= all_contacts)

#Add Contact
@app.route('/add', methods=['POST', 'GET']) #get information and post to database
def add():
    if request.method == 'POST':
        firstname= request.form['first-name']
        lastname= request.form['last-name']
        email= request.form['email']
        phone= request.form['phone']
        group= request.form['inputGroup']
        date= request.form['date']

        new_contact = Contact(firstname, lastname, email, phone, group, date)

        try:
            db.session.add(new_contact)
            db.session.commit()

        flash("Contact saved")

        return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)