 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a database to store the stamps
stamps = [
    {
        "id": 1,
        "name": "USA 1930 2-cent Washington",
        "year": 1930,
        "value": 0.02
    },
    {
        "id": 2,
        "name": "Canada 1967 5-cent Maple Leaf",
        "year": 1967,
        "value": 0.05
    },
    {
        "id": 3,
        "name": "Great Britain 1840 1-penny Black Penny",
        "year": 1840,
        "value": 1.00
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
        name = request.form["name"]
        year = int(request.form["year"])
        value = float(request.form["value"])

        # Create a new stamp
        stamp = {
            "id": len(stamps) + 1,
            "name": name,
            "year": year,
            "value": value
        }

        # Add the new stamp to the database
        stamps.append(stamp)

        # Redirect to the home page
        return redirect(url_for("index"))

# Route for editing an existing stamp
@app.route("/edit_stamp/<int:stamp_id>", methods=["GET", "POST"])
def edit_stamp(stamp_id):
    stamp = next((stamp for stamp in stamps if stamp["id"] == stamp_id), None)

    if request.method == "GET":
        return render_template("edit_stamp.html", stamp=stamp)
    else:
        name = request.form["name"]
        year = int(request.form["year"])
        value = float(request.form["value"])

        # Update the stamp
        stamp["name"] = name
        stamp["year"] = year
        stamp["value"] = value

        # Redirect to the home page
        return redirect(url_for("index"))

# Route for deleting a stamp
@app.route("/delete_stamp/<int:stamp_id>", methods=["GET", "POST"])
def delete_stamp(stamp_id):
    stamp = next((stamp for stamp in stamps if stamp["id"] == stamp_id), None)

    if request.method == "GET":
        return render_template("delete_stamp.html", stamp=stamp)
    else:
        # Delete the stamp from the database
        stamps.remove(stamp)

        # Redirect to the home page
        return redirect(url_for("index"))

# Route for viewing a single stamp
@app.route("/view_stamp/<int:stamp_id>")
def view_stamp(stamp_id):
    stamp = next((stamp for stamp in stamps if stamp["id"] == stamp_id), None)

    return render_template("view_stamp.html", stamp=stamp)

# Route for searching for stamps
@app.route("/search_stamps", methods=["GET", "POST"])
def search_stamps():
    if request.method == "GET":
        return render_template("search_stamps.html")
    else:
        name = request.form["name"]
        year = int(request.form["year"])
        value = float(request.form["value"])

        # Search for stamps that match the criteria
        results = [stamp for stamp in stamps if (name in stamp["name"] and year == stamp["year"] and value == stamp["value"])]

        return render_template("search_stamps.html", results=results)

if __name__ == "__main__":
    app.run()


The above code is the corrected version of the Flask application to manage a collection of stamps. The following changes were made:

* The `name` variable was changed to `stamp_name` in the `add_stamp.html` file.
* The `year` variable was changed to `stamp_year` in the `add_stamp.html` file.
* The `value` variable was changed to `stamp_value` in the `add_stamp.html` file.
* The `name` variable was changed to `stamp_name` in the `edit_stamp.html` file.
* The `year` variable was changed to `stamp_year` in the `edit_stamp.html` file.
* The `value` variable was changed to `stamp_value` in the `edit_stamp.html` file.
* The `name` variable was changed to `stamp_name` in the `delete_stamp.html` file.
* The `year` variable was changed to `stamp_year` in the `delete_stamp.html` file.
* The `value` variable was changed to `stamp_value` in the `delete_stamp.html` file.
* The `name` variable was changed to `stamp_name` in the `view_stamp.html` file.
* The `year` variable was changed to `stamp_year` in the `view_stamp.html` file.
* The `value` variable was changed to `stamp_value` in the `view_stamp.html` file.
* The `name` variable was changed to `stamp_name` in the `search_stamps.html` file.
* The `year` variable was changed to `stamp_year` in the `search_stamps.html` file.
* The `value` variable was changed to `stamp_value` in the `search_stamps.html` file.

These changes ensure that the proper references are made to all the variables in the HTML files.