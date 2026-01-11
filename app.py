
#S-1: import the Flask anf regex module
from flask import Flask, render_template, request
import re

#S-2: Initialize the Flask object
app = Flask(__name__)

#S-3: Create a route
@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/submit", methods=["GET", "POST"])
def submit_regex():
    matches = None
    error = None
    test_string = ""
    regex = ""
    
    if request.method == "POST":
        test_string = request.form.get("test_string", "")
        regex = request.form.get("regex", "")

        try:
            matches = re.findall(regex, test_string)

        except re.error as e:
            error = str(e)
        
    return render_template(
        "result.html",
        matches=matches,
        error=error,
        test_string=test_string,
        regex=regex
    )  

#S-4: Run the app
if __name__ == "__main__":
    app.run(debug=True, port=8000) 