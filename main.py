 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a database to store the stamps
stamps = []

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Add a new stamp
@app.route('/add_stamp', methods=['POST'])
def add_stamp():
    stamp = request.form.get('stamp')
    stamps.append(stamp)
    return redirect(url_for('index'))

# Edit an existing stamp
@app.route('/edit_stamp/<stamp_id>', methods=['POST'])
def edit_stamp(stamp_id):
    stamp = request.form.get('stamp')
    stamps[stamp_id] = stamp
    return redirect(url_for('index'))

# Delete a stamp
@app.route('/delete_stamp/<stamp_id>')
def delete_stamp(stamp_id):
    del stamps[stamp_id]
    return redirect(url_for('index'))

# View all stamps
@app.route('/view_stamps')
def view_stamps():
    return render_template('view_stamps.html', stamps=stamps)

# Search for stamps
@app.route('/search_stamps', methods=['POST'])
def search_stamps():
    search_term = request.form.get('search_term')
    results = [stamp for stamp in stamps if search_term in stamp]
    return render_template('view_stamps.html', stamps=results)

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
    <form action="/add_stamp" method="post">
        <label for="stamp">Stamp:</label><br>
        <input type="text" id="stamp" name="stamp"><br><br>
        <input type="submit" value="Add Stamp">
    </form>
    <form action="/edit_stamp/<stamp_id>" method="post">
        <label for="stamp">Stamp:</label><br>
        <input type="text" id="stamp" name="stamp"><br><br>
        <input type="submit" value="Edit Stamp">
    </form>
    <form action="/delete_stamp/<stamp_id>" method="post">
        <input type="submit" value="Delete Stamp">
    </form>
    <a href="/view_stamps">View Stamps</a>
    <a href="/search_stamps">Search Stamps</a>
</body>
</html>


HTML code for view_stamps.html

html
<!DOCTYPE html>
<html>
<head>
    <title>View Stamps</title>
</head>
<body>
    <h1>View Stamps</h1>
    <ul>
        {% for stamp in stamps %}
            <li>{{ stamp }}</li>
        {% endfor %}
    </ul>
    <a href="/">Home</a>
</body>
</html>


HTML code for search_stamps.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Search Stamps</title>
</head>
<body>
    <h1>Search Stamps</h1>
    <form action="/search_stamps" method="post">
        <label for="search_term">Search Term:</label><br>
        <input type="text" id="search_term" name="search_term"><br><br>
        <input type="submit" value="Search">
    </form>
    <a href="/">Home</a>
</body>
</html>
