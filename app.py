from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Inisialisasi list untuk menyimpan to-do items
todo_list = []

@app.route('/')
def index():
    # Meneruskan data ke template dengan indeks sudah di-enumerate
    return render_template('index.html', todo_list_with_index=enumerate(todo_list))

@app.route('/add', methods=['POST'])
def add():
    # Ambil data dari form
    item = request.form.get('item')
    # Tambahkan item ke list
    todo_list.append(item)
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        # Ambil data dari form
        new_item = request.form.get('new_item')
        # Ubah item pada indeks tertentu
        todo_list[index] = new_item
        return redirect(url_for('index'))
    else:
        return render_template('edit.html', index=index, item=todo_list[index])

@app.route('/delete/<int:index>')
def delete(index):
    # Hapus item dari list berdasarkan indeks
    del todo_list[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)