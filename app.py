from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        with open("feedback.txt", "a") as f:
            f.write(f"Name: {name}\nMessage: {message}\n---\n")
        return render_template("feedback.html", thank_you=True, name=name)
    return render_template("feedback.html", thank_you=False)

if __name__ == "__main__":
    app.run(debug=True)
