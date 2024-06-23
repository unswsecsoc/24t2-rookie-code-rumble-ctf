from flask import Flask, request
import jwt
import json

JWT_SECRET = "QVXN9xBkaZzUTi8rix2m9C22iB0CiIJLKn52PWLKfuuYHpQujB"

app = Flask(__name__)

@app.route("/flag", methods=["GET"])
def flag():
  token = request.cookies.get("token")
  userObj = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])

  if "username" not in userObj or "isAdmin" not in userObj:
    return "Sorry, your user object is malformed - it must have a username and isAdmin field"

  if userObj["isAdmin"]:
    return "BEGINNER{i_t0ld_y0u_n0t_t0_7ru5t_u53r_1npu7}"
  
  return f"Sorry, you are not an admin - here is the JSON object encoded in your token: {userObj}"

@app.route("/generate_user_token", methods=["POST"])
def generateUserToken():
  username = request.form.get("username")
  userObjString = f'{{ "isAdmin" : false, "username" : "{username}" }}'
 
  try:
    userObj = json.loads(userObjString)
    token = jwt.encode(userObj, JWT_SECRET, algorithm="HS256")
  except:
    return "Failed to construct a JWT token with your input :("

  return token

@app.route("/", methods=["GET"])
def index():
  return """
Welcome to the Simple Flag Storage (SFS) service!
You can send a POST request to /generate_user_token with a `username` parameter to generate a JWT token for your user account.
[ADMIN ONLY] You can send a GET request to /flag using a cookie of "token=<admin token>" to retrieve the super secret flag.
"""
