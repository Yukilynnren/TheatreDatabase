from flask import Flask, render_template, request
import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'root',
    #'password': 'love',
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

# choose name to check customer profile
@app.route("/profile")
def profile():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("SELECT * from `Customer`")
    customers=cursor.fetchall()
    cnx.close()
    return render_template('profile.html', customers = customers)

# specific customer profile
@app.route("/choose", methods=["POST"])
def customer():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    select_stmt = ("SELECT * from `Customer` WHERE idCustomer=%s ")
    data = (request.form['idCustomer'],)
    cursor.execute(select_stmt, data)
    customers=cursor.fetchall()
    cnx.close()
    return render_template('customerprofile.html',customers = customers)

# choose name to check customer history
@app.route("/history")
def history():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("SELECT * from `Customer`")
    customers=cursor.fetchall()
    cnx.close()
    return render_template('history.html', customers = customers)

# specific customer profile
@app.route("/choose1", methods=["POST"])
def cushistory():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    select_stmt = ("SELECT MovieName,Rating from `Movie` join `Customer` join `Attend` join `Showing` WHERE idCustomer=%s AND Customer.idCustomer=Attend.Customer_idCustomer AND Movie.idMovie=Showing.Movie_idMovie AND Showing.idShowing=Attend.Showing_idShowing")
    data = (request.form['idCustomer'],)
    cursor.execute(select_stmt, data)
    customers=cursor.fetchall()
    cnx.close()
    return render_template('customerhistory.html',customers = customers)


# movie
@app.route("/movie")
def moivepage():
    return render_template('movie.html')

@app.route("/addmovie")
def addmoivepage():
    return render_template('addmovie.html')

# add a movie (ID, name, year)
@app.route("/submit", methods=["POST"])
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

# delete a movie by name


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)