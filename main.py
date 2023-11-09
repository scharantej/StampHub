 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a database to store the stamps
stamps = []

# Home page
@app.route('/')
def index():
    return render_template('index.html', stamps=stamps)

# Add a new stamp
@app.route('/add', methods=['POST'])
def add():
    stamp = request.form.get('stamp')
    stamps.append(stamp)
    return redirect(url_for('index'))

# Edit an existing stamp
@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    stamp = request.form.get('stamp')
    stamps[id] = stamp
    return redirect(url_for('index'))

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
@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    results = [stamp for stamp in stamps if query in stamp]
    return render_template('search.html', results=results)

if __name__ == '__main__':
    app.run()


main.py file:


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a database to store the stamps
stamps = []

# Home page
@app.route('/')
def index():
    return render_template('index.html', stamps=stamps)

# Add a new stamp
@app.route('/add', methods=['POST'])
def add():
    stamp = request.form.get('stamp')
    stamps.append(stamp)
    return redirect(url_for('index'))

# Edit an existing stamp
@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    stamp = request.form.get('stamp')
    stamps[id] = stamp
    return redirect(url_for('index'))

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
@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    results = [stamp for stamp in stamps if query in stamp]
    return render_template('search.html', results=results)

if __name__ == '__main__':
    app.run()
