# Rest-app
# Objective

Build a simple REST API using Flask that can Create, Read, Update, and Delete (CRUD) user data.
This project demonstrates API development fundamentals for the internship assignment.

# Tech Stack

- Python 3.x

- Flask (micro web framework)

- cURL / Postman (for testing)

- Anaconda environment (newsenv)

# Project Structure

Rest-app/
- rest.py              # Main Flask application
- requirements.txt     # Dependencies (Flask)
- README.md            # Project documentation

# Setup & Installation
1️ Clone this repository
git clone https://github.com/<your-username>/rest-app.git
cd rest-app

2️ Create and activate environment (Anaconda users)
conda create -n newsenv python=3.12 -y
conda activate newsenv


(If conda init fails, you can use full path like this instead:)

& C:/Users/reddy/anaconda3/envs/newsenv/python.exe -m pip install flask

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Run the Application
python rest.py


You’ll see:

 * Running on http://127.0.0.1:5000/


Open your browser → http://127.0.0.1:5000/

# API Endpoints
🔹 Home

GET /

{ "message": "Welcome to User Management API" }

🔹 Create User

POST /users

Body (JSON):

{
  "name": "Alice",
  "email": "alice@example.com"
}


Response:

{
  "id": "1",
  "name": "Alice",
  "email": "alice@example.com"
}

🔹 Get All Users

GET /users

Response:

[
  {
    "id": "1",
    "name": "Alice",
    "email": "alice@example.com"
  }
]

🔹 Get Single User

GET /users/<id>
Example: /users/1

🔹 Update User

PUT /users/<id>

Body (JSON):

{
  "name": "Alice Updated",
  "email": "newalice@example.com"
}

🔹 Delete User

DELETE /users/<id>

Response:

{ "message": "User deleted" }

# Testing
Using cURL
# Create user
curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d "{\"name\":\"Bob\",\"email\":\"bob@example.com\"}"

# Get users
curl http://127.0.0.1:5000/users

# Using Postman

- Open Postman

- Select method (GET/POST/PUT/DELETE)

- Enter URL: http://127.0.0.1:5000/users

- For POST/PUT, go to Body → raw → JSON and enter request data
