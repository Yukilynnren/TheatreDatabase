from flask import Flask, render_template, request
import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'root',
    'password': 'love',
    'database': 'MovieTheatre'
}

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

# back end
@app.route("/backend")
def backend():
    return render_template('backend.html')

# front end
@app.route("/frontend")
def frontend():
    return render_template('frontend.html')

# movie
@app.route("/movie")
def moivepage():
    return render_template('movie.html')

# add movie
@app.route("/addmovie")
def addmoivepage():
    return render_template('addmovie.html')

@app.route("/addMovie", methods=["POST"])
def addMovie():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO `Movie` (idMovie,MovieName,MovieYear)"
        "VALUES (%s, %s, %s)"
        )
    data = (request.form['idMovie'], request.form['MovieName'], request.form['MovieYear'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('addmovie.html', idMovie=request.form['idMovie'], 
        MovieName=request.form['MovieName'], MovieYear=request.form['MovieYear'])

# delete movie
@app.route("/deletemovie")
def deletemoivepage():
    return render_template('deletemovie.html')

@app.route("/deleteMovie", methods=["POST"])
def deleteMovie():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    delete_stmt = (
        "DELETE FROM `Movie` WHERE MovieName=%s" #single value
        )
    data = (request.form['MovieName'],) # force string to become tupple
    cursor.execute(delete_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('deletemovie.html', MovieName=request.form['MovieName'])

# update movie
@app.route("/updatemovie")
def updatemoivepage():
    return render_template('updatemovie.html')

@app.route("/updateMovie", methods=["POST"])
def updateMovie():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    insert_stmt = (
        "UPDATE `Movie` SET (idMovie,MovieName,MovieYear)"
        "VALUES (%s, %s, %s)"
        )
    data = (request.form['idMovie'], request.form['MovieName'], request.form['MovieYear'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('updatemovie.html', idMovie=request.form['idMovie'], 
        MovieName=request.form['MovieName'], MovieYear=request.form['MovieYear'])

# list movie
@app.route("/listmovie")
def listmoivepage():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("SELECT * from Movie")
    cursor.execute(query)
    movies=cursor.fetchall()
    cnx.close()
    return render_template('listmovie.html', movies=movies)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)