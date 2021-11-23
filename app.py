from flask import Flask, render_template , url_for
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
@app.route('/')
@app.route('/home', methods=['POST', 'GET']) #get information and post to database
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)