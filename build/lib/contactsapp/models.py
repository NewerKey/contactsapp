from contactsapp import db

#database instance
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False )
    email =  db.Column(db.String(100), nullable=False )
    phonenumber =  db.Column(db.String(), nullable=False)
    group =  db.Column(db.String(100))


    def __init__(self, name, phonenumber, email, group):
        self.name = name
        self.email = email
        self.phonenumber = phonenumber
        self.group = group

