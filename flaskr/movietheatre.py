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
    data = (request.form['MovieName'],) # force string to become tuple
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
    update_stmt = (
        "UPDATE `Movie` SET MovieName=%s, MovieYear=%s WHERE idMovie=%s"
        )
    data = (request.form['MovieName'], request.form['MovieYear'], request.form['idMovie'])
    cursor.execute(update_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('updatemovie.html', idMovie=request.form['idMovie'], 
        MovieName=request.form['MovieName'], MovieYear=request.form['MovieYear'])

# list movie
@app.route("/listmovie")
def listmoivepage():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("SELECT * from `Movie` ORDER BY MovieName")
    cursor.execute(query)
    movies=cursor.fetchall()
    cnx.close()
    return render_template('listmovie.html', movies=movies)


# genre
@app.route("/genre")
def genrepage():
    return render_template('genre.html')

# add genre
@app.route("/addgenre")
def addgenrepage():
    return render_template('addgenre.html')

@app.route("/addGenre", methods=["POST"])
def addGenre():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO `Genre` (Genre, Movie_idMovie)"
        "VALUES (%s, %s)"
        )
    data = (request.form['Genre'], request.form['Movie_idMovie'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('addgenre.html', Movie_idMovie=request.form['Genre'], 
        MovieName=request.form['Movie_idMovie'])

# delete genre
@app.route("/deletegenre")
def deletegenrepage():
    return render_template('deletegenre.html')

@app.route("/deleteGenre", methods=["POST"])
def deleteGenre():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    delete_stmt = (
        "DELETE FROM `Genre` WHERE Movie_idMovie=%s and Genre=%s" 
        )
    data = (request.form['Movie_idMovie'], request.form['Genre']) 
    cursor.execute(delete_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('deletegenre.html', Movie_idMovie=request.form['Movie_idMovie'],
        Genre=request.form['Genre'])


# list genre
@app.route("/listgenre")
def listgenrepage():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("SELECT MovieName,Genre from `Movie` join `Genre` WHERE Movie.idMovie=Genre.Movie_idMovie ORDER BY Genre")
    cursor.execute(query)
    genres=cursor.fetchall()
    cnx.close()
    return render_template('listgenre.html', genres=genres)

# room
@app.route("/room")
def roompage():
    return render_template('room.html')

# add room
@app.route("/addroom")
def addroompage():
    return render_template('addroom.html')

@app.route("/addRoom", methods=["POST"])
def addRoom():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO `TheatreRoom` (RoomNumber,Capacity)"
        "VALUES (%s, %s)"
        )
    data = (request.form['RoomNumber'], request.form['Capacity'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('addroom.html', RoomNmber=request.form['RoomNumber'], 
        Capacity=request.form['Capacity'])

# delete room
@app.route("/deleteroom")
def deleteroompage():
    return render_template('deleteroom.html')

@app.route("/deleteRoom", methods=["POST"])
def deleteRoom():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    delete_stmt = (
        "DELETE FROM `TheatreRoom` WHERE RoomNumber=%s" #single value
        )
    data = (request.form['RoomNumber'],) # force string to become tuple
    cursor.execute(delete_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('deleteroom.html', RoomNumber=request.form['RoomNumber'])

# update room
@app.route("/updateroom")
def updateroompage():
    return render_template('updateroom.html')

@app.route("/updateRoom", methods=["POST"])
def updateRoom():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    update_stmt = (
        "UPDATE `TheatreRoom` SET Capacity=%s WHERE RoomNumber=%s"
        )
    data = (request.form['Capacity'], request.form['RoomNumber'])
    cursor.execute(update_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('updateroom.html', Capacity=request.form['Capacity'], 
        RoomNumber=request.form['RoomNumber'])

# list room
@app.route("/listroom")
def listroompage():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("SELECT * from `TheatreRoom` ORDER BY RoomNumber")
    cursor.execute(query)
    rooms=cursor.fetchall()
    cnx.close()
    return render_template('listroom.html', rooms=rooms)


# showing
@app.route("/showing")
def showingpage():
    return render_template('showing.html')

# add showing
@app.route("/addshowing")
def addshowingpage():
    return render_template('addshowing.html')

@app.route("/addShowing", methods=["POST"])
def addShowing():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO `Showing` (idShowing,ShowingDateTime,Movie_idMovie,TheatreRoom_RoomNumber,TicketPrice)"
        "VALUES (%s, %s, %s, %s, %s)"
        )
    data = (request.form['idShowing'], request.form['ShowingDateTime'], request.form['Movie_idMovie'],
        request.form['TheatreRoom_RoomNumber'], request.form['TicketPrice'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('addshowing.html', idShowing=request.form['idShowing'], ShowingDateTime=request.form['ShowingDateTime'],
        Movie_idMovie=request.form['Movie_idMovie'], TheatreRoom_RoomNumber=request.form['TheatreRoom_RoomNumber'],
        TicketPrice=request.form['TicketPrice'])

# delete showing
@app.route("/deleteshowing")
def deleteshowingpage():
    return render_template('deleteshowing.html')

@app.route("/deleteShowing", methods=["POST"])
def deleteShowing():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    delete_stmt = (
        "DELETE FROM `Showing` WHERE idShowing=%s" #single value
        )
    data = (request.form['idShowing'],) # force string to become tuple
    cursor.execute(delete_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('deleteshowing.html', idShowing=request.form['idShowing'])

# update showing
@app.route("/updateshowing")
def updateshowingpage():
    return render_template('updateshowing.html')

@app.route("/updateShowing", methods=["POST"])
def updateShowing():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    update_stmt = (
        "UPDATE `Showing` SET ShowingDateTime=%s, TicketPrice=%s WHERE idShowing=%s"
        )
    data = (request.form['ShowingDateTime'], request.form['TicketPrice'], request.form['idShowing'])
    cursor.execute(update_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('updateshowing.html', idShowing=request.form['idShowing'],
        ShowingDateTime=request.form['ShowingDateTime'],
        TicketPrice=request.form['TicketPrice'])

# list showing
@app.route("/listshowing")
def listshowingpage():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("SELECT * from `Showing` ORDER BY ShowingDateTime")
    cursor.execute(query)
    showings =cursor.fetchall()
    cnx.close()
    return render_template('listshowing.html', showings=showings)


# Customer
@app.route("/staff_customer")
def customerpage():
    return render_template('staff_customer.html')

# add room
@app.route("/addcustomer")
def addcustomerpage():
    return render_template('addcustomer.html')

@app.route("/addCustomer", methods=["POST"])
def addCustomer():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO `Customer` (idCustomer,FirstName,LastName,EmailAddress,Sex)"
        "VALUES (%s, %s, %s, %s, %s)"
        )
    data = (request.form['idCustomer'], request.form['FirstName'], request.form['LastName'],
        request.form['EmailAddress'], request.form['Sex'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('addcustomer.html', idCustomer=request.form['idCustomer'],
        FirstName=request.form['FirstName'], LastName=request.form['LastName'],
        EmailAddress=request.form['EmailAddress'], Sex=request.form['Sex'])

# delete customer
@app.route("/deletecustomer")
def deletcustomerpage():
    return render_template('deletecustomer.html')

@app.route("/deleteCustomer", methods=["POST"])
def deleteCustomer():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    delete_stmt = (
        "DELETE FROM `Customer` WHERE idCustomer=%s" #single value
        )
    data = (request.form['idCustomer'],) # force string to become tuple
    cursor.execute(delete_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('deletecustomer.html', idCustomer=request.form['idCustomer'])

# update customer
@app.route("/updatecustomer")
def updatecustomerpage():
    return render_template('updatecustomer.html')

@app.route("/updateCustomer", methods=["POST"])
def updateCustomer():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    update_stmt = (
        "UPDATE `Customer` SET EmailAddress=%s, Sex=%s WHERE idCustomer=%s"
        )
    data = (request.form['EmailAddress'], request.form['Sex'], request.form['idCustomer'])
    cursor.execute(update_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('updatecustomer.html', idCustomer=request.form['idCustomer'],
        EmailAddress=request.form['EmailAddress'], Sex=request.form['Sex'])

# list customer
@app.route("/listcustomer")
def listcustomerpage():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("SELECT idCustomer, FirstName, LastName, EmailAddress, CAST(Sex AS CHAR CHARACTER SET utf8) AS Sex from `Customer` ORDER BY LastName")
    cursor.execute(query)
    customers=cursor.fetchall()
    cnx.close()
    return render_template('listcustomer.html', customers=customers)


# addtend
@app.route("/attend")
def attendpage():
    return render_template('attend.html')

# list attend
@app.route("/attendCustomer", methods=["POST"])
def listattendCustomer():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("SELECT Customer_idCustomer,LastName,FirstName,Showing_idShowing,Rating from `Attend` join `Customer` where Attend.Customer_idCustomer=Customer.idCustomer ORDER BY Rating")
    cursor.execute(query)
    attends=cursor.fetchall()
    cnx.close()
    return render_template('listattendcustomer.html', attends=attends)

@app.route("/attendShowing", methods=["POST"])
def listattendShowing():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("SELECT Customer_idCustomer,Showing_idShowing,ShowingDateTime,Rating from `Attend` join `Showing` where Attend.Showing_idShowing=Showing.idShowing ORDER BY Rating")
    cursor.execute(query)
    attends=cursor.fetchall()
    cnx.close()
    return render_template('listattendshowing.html', attends=attends)

@app.route("/attendMovie", methods=["POST"])
def listattendMoive():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("SELECT Customer_idCustomer,Showing_idShowing,MovieName,Rating from (SELECT idShowing,MovieName from `Showing` join `Movie` where Showing.Movie_idMovie=Movie.idMovie) as temp join `Attend` where temp.idShowing=Attend.Showing_idShowing ORDER BY Rating")
    cursor.execute(query)
    attends=cursor.fetchall()
    cnx.close()
    return render_template('listattendmovie.html', attends=attends)


# injection Attack
@app.route('/injectionattack')
def injectionAttack():
    return render_template('injectionattack.html')
    
@app.route('/sqlinjectionattack', methods=["POST"])
def sqlInjectionAttack():

    LastName = request.form['LastName']

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("SELECT idCustomer, FirstName, LastName, EmailAddress, CAST(Sex AS CHAR CHARACTER SET utf8) AS Sex FROM Customer WHERE LastName = '" + LastName + "'")
    cursor.execute(query)
    customers = cursor.fetchall()
    cnx.commit()
    cnx.close()
    
    return render_template('sqlinjectionattack.html', customers=customers)






if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)