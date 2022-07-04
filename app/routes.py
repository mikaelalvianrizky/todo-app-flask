from flask import redirect, render_template, request, jsonify, url_for, request
from app import app, database

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': # Create
        judul = request.form['judul']
        database.create(judul)
        return redirect(url_for('index'))

    todo = database.getAllKegiatan()
    return render_template("content/index.html", todo=todo)

@app.route('/detail/<int:task_id>', methods=['GET', 'POST'])
def detail(task_id):
    kegiatan = database.findKegiatan(task_id)
    return render_template("content/detail.html", kegiatan=kegiatan)

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
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

@app.route('/api', methods=['GET'])
def indexJson():
    todo = database.getAllKegiatan()
    return jsonify(todo)

@app.route('/api/<int:task_id>', methods=['GET'])
def detailJson(task_id):
    kegiatan = database.findKegiatan(task_id)
    return jsonify(kegiatan)

@app.route('/api/create', methods=['POST'])
def createJson():
    try:
        judul = request.json['judul']
        database.create(judul)
        return {
            'response': 'Kegiatan baru berhasil ditambahkan',
            'status':201
        }
    except:
        return {
            'response': 'Kegiatan baru gagal ditambahkan, silakan coba beberapa saat kemudian',
            'status':404
        }

@app.route('/api/edit/<int:task_id>', methods=['POST'])
def editJson(task_id):
    try:
        judul = request.json['judul']
        kegiatan = database.findKegiatan(task_id)
        if kegiatan['task'] != judul:    
            database.update(task_id, judul)
            return {
                'response': 'Kegiatan baru berhasil diubah',
                'status':201
            }
        else:
            return {'status': 204} # No Changes
    except:
        return {
            'response': 'Kegiatan baru gagal diubah, silakan coba beberapa saat kemudian',
            'status':404
        }

@app.route('/api/delete/<int:task_id>', methods=['DELETE'])
def deleteJson(task_id):
    try:
        database.delete(task_id)
        return {
            'response': 'Kegiatan berhasil dihapus',
            'status':200
        }
    except:
        return {
            'response': 'Kegiatan gagal dihapus, silakan coba beberapa saat kemudian',
            'status':404
        }
