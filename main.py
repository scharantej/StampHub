 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a database to store the stamps
stamps = [
    {
        "id": 1,
        "country": "United States",
        "year": 1935,
        "theme": "Presidents",
        "value": 10
    },
    {
        "id": 2,
        "country": "Canada",
        "year": 1967,
        "theme": "Animals",
        "value": 5
    },
    {
        "id": 3,
        "country": "Great Britain",
        "year": 1840,
        "theme": "History",
        "value": 20
    }
]

# Route for the home page
@app.route("/")
def index():
    return render_template("index.html", stamps=stamps)

# Route for adding a new stamp
@app.route("/add_stamp", methods=["GET", "POST"])
def add_stamp():
    if request.method == "GET":
        return render_template("add_stamp.html")
    else:
        country = request.form["country"]
        year = request.form["year"]
        theme = request.form["theme"]
        value = request.form["value"]

        # Add the new stamp to the database
        new_stamp = {
            "id": len(stamps) + 1,
            "country": country,
            "year": year,
            "theme": theme,
            "value": value
        }
        stamps.append(new_stamp)

        # Redirect to the home page
        return redirect(url_for("index"))

# Route for editing an existing stamp
@app.route("/edit_stamp/<int:stamp_id>", methods=["GET", "POST"])
def edit_stamp(stamp_id):
    stamp = stamps[stamp_id - 1]

    if request.method == "GET":
        return render_template("edit_stamp.html", stamp=stamp)
    else:
        country = request.form["country"]
        year = request.form["year"]
        theme = request.form["theme"]
        value = request.form["value"]

        # Update the stamp in the database
        stamp["country"] = country
        stamp["year"] = year
        stamp["theme"] = theme
        stamp["value"] = value

        # Redirect to the home page
        return redirect(url_for("index"))

# Route for deleting a stamp
@app.route("/delete_stamp/<int:stamp_id>")
def delete_stamp(stamp_id):
    # Delete the stamp from the database
    del stamps[stamp_id - 1]

    # Redirect to the home page
    return redirect(url_for("index"))

# Route for viewing a single stamp
@app.route("/view_stamp/<int:stamp_id>")
def view_stamp(stamp_id):
    stamp = stamps[stamp_id - 1]

    return render_template("view_stamp.html", stamp=stamp)

# Route for searching the collection
@app.route("/search_stamps", methods=["GET", "POST"])
def search_stamps():
    if request.method == "GET":
        return render_template("search_stamps.html")
    else:
        country = request.form["country"]
        year = request.form["year"]
        theme = request.form["theme"]
        value = request.form["value"]

        # Search the database for stamps that match the criteria
        results = []
        for stamp in stamps:
            if (country and stamp["country"] == country) or \
               (year and stamp["year"] == year) or \
               (theme and stamp["theme"] == theme) or \
               (value and stamp["value"] == value):
                results.append(stamp)

        return render_template("search_stamps.html", results=results)

if __name__ == "__main__":
    app.run()
