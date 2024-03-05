from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Inisialisasi list untuk menyimpan to-do items
todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add():
    # Ambil data dari form
    item = request.form.get('item')
    # Tambahkan item ke list
    todo_list.append(item)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    # Hapus item dari list berdasarkan indeks
    del todo_list[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
