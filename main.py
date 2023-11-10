 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a database to store the stamps
stamps = []

# Add a new stamp to the collection
@app.route('/add_stamp', methods=['GET', 'POST'])
def add_stamp():
    if request.method == 'POST':
        stamp = request.form.get('stamp')
        stamps.append(stamp)
        return redirect(url_for('view_stamps'))
    return render_template('add_stamp.html')

# Edit an existing stamp in the collection
@app.route('/edit_stamp/<stamp_id>', methods=['GET', 'POST'])
def edit_stamp(stamp_id):
    stamp = stamps[int(stamp_id)]
    if request.method == 'POST':
        stamp = request.form.get('stamp')
        stamps[int(stamp_id)] = stamp
        return redirect(url_for('view_stamps'))
    return render_template('edit_stamp.html', stamp=stamp)

# Delete a stamp from the collection
@app.route('/delete_stamp/<stamp_id>')
def delete_stamp(stamp_id):
    del stamps[int(stamp_id)]
    return redirect(url_for('view_stamps'))

# View all of the stamps in the collection
@app.route('/view_stamps')
def view_stamps():
    return render_template('view_stamps.html', stamps=stamps)

# Search for stamps in the collection
@app.route('/search_stamps', methods=['GET', 'POST'])
def search_stamps():
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        results = [stamp for stamp in stamps if search_term in stamp]
        return render_template('search_stamps.html', results=results)
    return render_template('search_stamps.html')

if __name__ == '__main__':
    app.run()


HTML code for index.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Stamp Collection</title>
</head>
<body>
    <h1>Stamp Collection</h1>
    <a href="/add_stamp">Add a new stamp</a>
    <a href="/view_stamps">View all stamps</a>
    <a href="/search_stamps">Search for stamps</a>
</body>
</html>


HTML code for add_stamp.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Add a new stamp</title>
</head>
<body>
    <h1>Add a new stamp</h1>
    <form action="/add_stamp" method="post">
        <label for="stamp">Stamp:</label><br>
        <input type="text" id="stamp" name="stamp"><br><br>
        <input type="submit" value="Add stamp">
    </form>
</body>
</html>


HTML code for edit_stamp.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Edit a stamp</title>
</head>
<body>
    <h1>Edit a stamp</h1>
    <form action="/edit_stamp/{{ stamp_id }}" method="post">
        <label for="stamp">Stamp:</label><br>
        <input type="text" id="stamp" name="stamp" value="{{ stamp }}"><br><br>
        <input type="submit" value="Edit stamp">
    </form>
</body>
</html>


HTML code for view_stamps.html

html
<!DOCTYPE html>
<html>
<head>
    <title>View all stamps</title>
</head>
<body>
    <h1>View all stamps</h1>
    <ul>
        {% for stamp in stamps %}
            <li>{{ stamp }}</li>
        {% endfor %}
    </ul>
</body>
</html>


HTML code for search_stamps.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Search for stamps</title>
</head>
<body>
    <h1>Search for stamps</h1>
    <form action="/search_stamps" method="post">
        <label for="search_term">Search term:</label><br>
        <input type="text" id="search_term" name="search_term"><br><br>
        <input type="submit" value="Search">
    </form>
    {% if results %}
        <ul>
            {% for stamp in results %}
                <li>{{ stamp }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
