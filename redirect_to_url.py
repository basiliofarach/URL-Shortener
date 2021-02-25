import os
import database_url
import sqlite3
from flask import Flask, render_template, redirect, url_for


app=Flask(__name__)

@app.route('/')
def initial():
    return redirect('/home')

@app.route('/home')
def home():
    return "This is just a test"

@app.route('/xyz.com/'+'<input_url>', methods = ['GET'])
def redirect_url(input_url):
    input = 'xyz.com/'+str(input_url)
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM shortened_urls WHERE new_url=?",(input,))
    rows = cur.fetchall()
    if rows == []:
        cur.execute("SELECT * FROM shortened_urls WHERE orig_url=?",(input,))
        rows = cur.fetchall()
    conn.close()
    try:
        if rows[0][2] == input:
            destinated_url=rows[0][1]
            return redirect('/'+destinated_url) #For redirect out of the program add: redirect('http//:'+destinated_url)
        elif rows[0][1] == input:
            return('This is the redirected address')
    except:
        return('The address that you specified is not on our database')



if __name__=="__main__":
    app.run(debug=True)
