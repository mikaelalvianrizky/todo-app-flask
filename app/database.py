from app import db

def getAllKegiatan() -> list:
    """Reads all tasks listed in the todo table
    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("SELECT * FROM Kegiatan ORDER BY id DESC").fetchall()
    conn.close()
    todoList = []
    for result in query_results:
        kegiatan = {
            "id": result[0],
            "task": result[1],
        }
        todoList.append(kegiatan)

    return todoList

def create(judul):
    conn = db.connect()
    conn.execute(f"INSERT INTO Kegiatan (judul) VALUES ('{judul}')")
    conn.close()

def update(id, judulBaru):
    conn = db.connect()
    conn.execute(f"UPDATE Kegiatan SET judul='{judulBaru}' WHERE id={id}")
    conn.close()

def findKegiatan(id):
    conn = db.connect()
    query_results = conn.execute(f"SELECT * FROM Kegiatan WHERE id={id}")
    conn.close()
    for result in query_results:
        kegiatan = {
            "id": result[0],
            "task": result[1],
        }

    return kegiatan

def delete(id):
    conn = db.connect()
    conn.execute(f"DELETE FROM kegiatan WHERE id={id}")
    conn.close()