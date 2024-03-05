# Copyright (c) 2024 Ika Nurfitriani

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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