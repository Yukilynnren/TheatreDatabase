from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

# back end
@app.route("/backend")
def backend():
    return render_template('backend.html')

#front end
@app.route("/frontend")
def frontend():
    return render_template('frontend.html')

# add a movie (ID, name, year)
@app.route("/submit", methods=["POST"])
def addMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO `Movie` VALUES (idMovie,MovieName,MovieYear)"
        "VALUES (%d, %s, %d)"
        )
    data = (request.form['idMovie'], request.form['MovieName'], request.form['MovieYear'])
    cursor.execute(insert_stmt, data)
    cnx.close()
    return render_template('addmovie.html', idMovie=request.form['idMovie'], 
        MovieName=request.form['MovieName'], MovieYear=request.form['MovieYear'])

# delete a movie by name
def deleteMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)