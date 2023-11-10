 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a database to store the stamps
stamps = [
    {
        "id": 1,
        "country": "United States",
        "year": 1930,
        "theme": "Presidents"
    },
    {
        "id": 2,
        "country": "Canada",
        "year": 1967,
        "theme": "Centenary of Confederation"
    },
    {
        "id": 3,
        "country": "Great Britain",
        "year": 1840,
        "theme": "Penny Black"
    }
]

# Define the routes
@app.route("/")
def index():
    return render_template("index.html", stamps=stamps)

@app.route("/add_stamp", methods=["GET", "POST"])
def add_stamp():
    if request.method == "GET":
        return render_template("add_stamp.html")
    else:
        country = request.form["country"]
        year = request.form["year"]
        theme = request.form["theme"]
        new_stamp = {
            "id": len(stamps) + 1,
            "country": country,
            "year": year,
            "theme": theme
        }
        stamps.append(new_stamp)
        return redirect(url_for("index"))

@app.route("/edit_stamp/<int:stamp_id>", methods=["GET", "POST"])
def edit_stamp(stamp_id):
    stamp = stamps[stamp_id - 1]
    if request.method == "GET":
        return render_template("edit_stamp.html", stamp=stamp)
    else:
        country = request.form["country"]
        year = request.form["year"]
        theme = request.form["theme"]
        stamp["country"] = country
        stamp["year"] = year
        stamp["theme"] = theme
        return redirect(url_for("index"))

@app.route("/delete_stamp/<int:stamp_id>")
def delete_stamp(stamp_id):
    stamp = stamps[stamp_id - 1]
    stamps.remove(stamp)
    return redirect(url_for("index"))

@app.route("/view_stamp/<int:stamp_id>")
def view_stamp(stamp_id):
    stamp = stamps[stamp_id - 1]
    return render_template("view_stamp.html", stamp=stamp)

@app.route("/search_stamps", methods=["GET", "POST"])
def search_stamps():
    if request.method == "GET":
        return render_template("search_stamps.html")
    else:
        country = request.form["country"]
        year = request.form["year"]
        theme = request.form["theme"]
        results = []
        for stamp in stamps:
            if (country and stamp["country"] == country) or \
               (year and stamp["year"] == year) or \
               (theme and stamp["theme"] == theme):
                results.append(stamp)
        return render_template("search_stamps.html", results=results)

if __name__ == "__main__":
    app.run()
