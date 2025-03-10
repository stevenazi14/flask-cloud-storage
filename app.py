from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage simulation
files = []
next_id = 1

@app.route("/", methods=["GET", "POST"])
def index():
    global next_id
    if request.method == "POST":
        filename = request.form.get("filename")
        if filename:
            files.append({"id": next_id, "name": filename})
            next_id += 1
        return redirect(url_for("index"))
    return render_template("index.html", files=files)

@app.route("/update/<int:file_id>", methods=["GET", "POST"])
def update(file_id):
    file = next((f for f in files if f["id"] == file_id), None)
    if not file:
        return redirect(url_for("index"))
    if request.method == "POST":
        new_name = request.form.get("new_name")
        if new_name:
            file["name"] = new_name
        return redirect(url_for("index"))
    return render_template("update.html", file=file)

@app.route("/delete/<int:file_id>")
def delete(file_id):
    global files
    files = [f for f in files if f["id"] != file_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
