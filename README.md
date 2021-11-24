
# Digital Product School Challenge Assessment

Name: Yvette Nuerkie Nartey
Program: Software Engineering
21.11.2021

## 🚀 Project Overview

An application where users can maintain their contacts. The application follows CRUD operations and utilizes a database to handle the storage.
Users can add a new contact, see all contacts from database, and also delete contact.  

## Project Architecture and Workflow

Flask Web Framework is used. It also uses the Model-View-Controller(MVC) Design Pattern.

## 🚀 Project Set Up

1. **Installing Main Development Dependencies and Requirements**

- Package manager [Python 3.8.6 pip](https://www.python.org/)
- Code Editor [Visual Studio Code](https://code.visualstudio.com/)
- Version Control[Git](https://git-scm.com/)
- Database [SQLAlchemy](https://www.sqlalchemy.org/)

2.**Virtual Environment**

- Create environment

    ```bash
    mkdir contactsapp
    cd contactsapp
    python -m venv venv
    ```

- Activate environment

    ```bash
    source ./venv/Scripts/activate
    ```

- Install Flask and SQLAlchemy flask extension

 ```bash
$pip install Flask
$pip install Flask-SQLAlchemy //database
 ```

3.**Setup Directory**

 ```shell
    contapp/
      ├
      ├── static/
      ├── templates/
      ├── app.py
      ├── models.py
      ├── routes.py
      └── README.md
```

This application’s code is organized using these directories and files:

- static/ contains the application’s static files(CSS, JS).
- templates/ contains the application’s templates(HTML).
- models.py contains the definition of the application’s models.
- main.py contains the application logic.
- routes.py contains the application routes path

4.**Setting up Model and Database**
Create database instance from SQLAlchemy, write a frunction that represents our model and connect to our application using sqlite3 by adding to configuration

5.**Restructure Project**

NB: Create a package file of the entire application to make it as an executable to install. (__init__.py). This solves the issue of circular imports.

6.**Templates and Static Content**
    - base page which all pages extend from
    - an index page which displays contacts
    - css styles
    - form-input component.

```bash
    $pip install flask-wtf
    $pip install wtforms
```

Create SECRET KEY for application as user will submit information to the database and to make information secure.
Validators used for form input

7.**CRUD**
Write functions to describe the various functionalities (Add, Read, Delete)

9.**Pushing to GitHub**
    -Store folders and files to not include in repository in .gitignore before pushing to Github

10.**Deploy**
Run with Production Server

```bash
    $pip install waitress
    $ waitress-serve --call 'contactsapp:create_app'
```

### Deploy to Heroku

11.**💫 Site URL**

Site is now running at <https://cmanagemt.herokuapp.com/>

12.**References**

- [Flask](https://strapi.io/documentation/developer-docs/latest/getting-started/introduction.html)

- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
