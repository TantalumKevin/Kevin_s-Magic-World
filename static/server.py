from flask import Flask, request, render_template
import json
 
app = Flask("listen", template_folder="./")

@app.route("/<filename>")
def file(filename):
    return render_template(filename)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5500)