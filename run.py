from contactsapp import app


#checks if run.py file has executed directly and not imported
if __name__== '__main__':
    app.run(debug=True)