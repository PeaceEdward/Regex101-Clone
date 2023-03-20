from flask import Flask, request, render_template
import re

# create a flask object
app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("request_form.html")


@app.route("/", methods=["POST"])
def regex_match():
    text_string = request.form.get("text_string")
    regex_pattern = request.form.get("regex_pattern")

    match = re.findall(regex_pattern, text_string)
    length=len(match)
    return render_template("results.html", matches=match,length=length)


if __name__ == "__main__":
    app.run(debug=True)
