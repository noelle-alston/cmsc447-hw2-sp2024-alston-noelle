import sqlite3
from flask import Flask, render_template, request, url_for, redirect

# FOLLOWED VR SOFT TECH and DIGITAL OCEAN TUTORIALS
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    conn = sqlite3.connect('database.db') 
    cur = conn.cursor() 
    cur.execute('SELECT * FROM database') 
  
    data = cur.fetchall() 
    return render_template('home.html', data=data)

@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method=='POST':
        new_name =request.form['name']
        new_id =request.form['id']
        new_points =request.form['points']
        con=sqlite3.connect("database.db")
        cur=con.cursor()
        cur.execute("INSERT OR IGNORE INTO database(name, real_id, points) VALUES (?,?, ?)",(new_name,new_id,new_points))
        con.commit()
        return redirect(url_for("home"))
    return render_template("create.html")

@app.route('/delete/<string:entry>', methods=['GET'])
def delete(entry):
    con=sqlite3.connect("database.db")
    cur=con.cursor()
    cur.execute("DELETE FROM database WHERE entry_num=?",(entry, ))
    con.commit()
    return redirect(url_for("home"))

@app.route('/update/<string:entry>', methods=['POST', 'GET'])
def update(entry):
    if request.method=='POST':
        new_name =request.form['name']
        new_id =request.form['id']
        new_points =request.form['points']
        conn=sqlite3.connect("database.db")
        cur=conn.cursor()
        cur.execute("UPDATE OR IGNORE database set name=?, real_id=?, points=? where entry_num=?", (new_name, new_id, new_points, entry))
        conn.commit()
        return redirect(url_for("home"))
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cur=conn.cursor()
    cur.execute('SELECT * FROM database WHERE entry_num=?', (entry, ))
    data=cur.fetchone()
    return render_template("update.html", data=data)    

if __name__ == '__main__':
    app.run(debug=True, threaded=True)