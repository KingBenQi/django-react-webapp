# Set up
## Backend

### create new environment for the app
python3 -m venv env 

### activate the env
source env/bin/activate

### install the requirement dependencies
pip install -r requirements.txt

### create the backend
django-admin startproject backend
cd backend

### create new directory for custom
python manage.py startapp api

### run the server
python manage.py runserver

----------------

## Frontend

### start
npm create vite@latest frontend -- --template react

### install package
npm install axios react-router-dom jwt-decode
---------------

# Questions to figure
1. load_dotenv()
2. JWT (json web tokens)
    act as the permissons or authentication everytime we access a website
