from flask import redirect, render_template, request, jsonify, url_for
from app import app, database

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': # Create
        judul = request.form['judul']
        database.create(judul)
        return redirect(url_for('index'))

    todo = database.getAllKegiatan()
    return render_template("content/index.html", todo=todo)

@app.route('/update/<int:task_id>', methods=['POST', 'GET'])
def update(task_id):
    if request.method == 'POST':
        judul = request.form['judulBaru']
        database.update(task_id, judul)
        return redirect(url_for('index'))
        
    kegiatan = database.findKegiatan(task_id)
    return render_template("content/edit.html", kegiatan=kegiatan)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    database.delete(task_id)
    return redirect(url_for('index'))