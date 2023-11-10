 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a database to store the stamps
stamps = []

# Home page
@app.route('/')
def index():
    return render_template('index.html', stamps=stamps)

# Add a new stamp
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        stamp = request.form.get('stamp')
        stamps.append(stamp)
        return redirect(url_for('index'))
    return render_template('add.html')

# Edit an existing stamp
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        stamp = request.form.get('stamp')
        stamps[id] = stamp
        return redirect(url_for('index'))
    return render_template('edit.html', stamp=stamps[id])

# Delete a stamp
@app.route('/delete/<int:id>')
def delete(id):
    del stamps[id]
    return redirect(url_for('index'))

# View the stamps
@app.route('/view')
def view():
    return render_template('view.html', stamps=stamps)

# Search for stamps
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        stamp = request.form.get('stamp')
        results = [stamp for stamp in stamps if stamp.lower().find(stamp.lower()) != -1]
        return render_template('search.html', results=results)
    return render_template('search.html')

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
    <ul>
        {% for stamp in stamps %}
            <li>{{ stamp }}</li>
        {% endfor %}
    </ul>
    <a href="/add">Add a new stamp</a>
</body>
</html>


HTML code for add.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Add a new stamp</title>
</head>
<body>
    <h1>Add a new stamp</h1>
    <form action="/add" method="post">
        <input type="text" name="stamp" placeholder="Stamp name">
        <input type="submit" value="Add">
    </form>
</body>
</html>


HTML code for edit.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Edit a stamp</title>
</head>
<body>
    <h1>Edit a stamp</h1>
    <form action="/edit/{{ stamp.id }}" method="post">
        <input type="text" name="stamp" value="{{ stamp.name }}">
        <input type="submit" value="Save">
    </form>
</body>
</html>


HTML code for view.html

html
<!DOCTYPE html>
<html>
<head>
    <title>View stamps</title>
</head>
<body>
    <h1>View stamps</h1>
    <ul>
        {% for stamp in stamps %}
            <li>{{ stamp }}</li>
        {% endfor %}
    </ul>
</body>
</html>


HTML code for search.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Search for stamps</title>
</head>
<body>
    <h1>Search for stamps</h1>
    <form action="/search" method="post">
        <input type="text" name="stamp" placeholder="Stamp name">
        <input type="submit" value="Search">
    </form>
    <ul>
        {% for result in results %}
            <li>{{ result }}</li>
        {% endfor %}
    </ul>
</body>
</html>
