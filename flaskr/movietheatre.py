from flask import Flask, render_template, request, session
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

# specific customer history
@app.route("/choose1", methods=["POST"])
def cushistory():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    select_stmt = ("SELECT ShowingDateTime,MovieName,Rating from `Movie` join `Customer` join `Attend` join `Showing` WHERE idCustomer=%s AND Customer.idCustomer=Attend.Customer_idCustomer AND Movie.idMovie=Showing.Movie_idMovie AND Showing.idShowing=Attend.Showing_idShowing")
    data = (request.form['idCustomer'],)
    cursor.execute(select_stmt, data)
    historys=cursor.fetchall()
    cnx.close()
    return render_template('customerhistory.html',historys = historys)

# rate a showing result
@app.route("/ratingsubmit")
def rateresultpage():
    return render_template('ratingsubmit.html')

# rating page
@app.route("/rating")
def rating():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("SELECT * from `Customer`")
    customers=cursor.fetchall()
    cnx.close()
    return render_template('rating.html', customers = customers)

# give a movie list to rate for specific customer
@app.route("/choose2", methods=["POST"])
def ratingmovie():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    select_stmt = ("SELECT idCustomer,idShowing,ShowingDateTime,MovieName from `Movie` join `Customer` join `Attend` join `Showing` WHERE idCustomer=%s AND Customer.idCustomer=Attend.Customer_idCustomer AND Movie.idMovie=Showing.Movie_idMovie AND Showing.idShowing=Attend.Showing_idShowing")
    data = (request.form['idCustomer'],)
    cursor.execute(select_stmt, data)
    movies=cursor.fetchall()
    cnx.close()
    return render_template('ratingmovie.html',movies = movies)

# not complete
# submit the rating
@app.route("/updaterating", methods=["POST"])
def updateMovie():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    #how to update in join
    update_stmt = ("UPDATE `Attend` SET Attend.Rating=%s WHERE Attend.Customer_idCustomer=%s AND Attend.Showing_idShowing=%s")
    data = (request.form['star'], request.form['idCustomer'], request.form['idMovie'])
    try:
        cursor.execute(update_stmt, data)
        cnx.commit()
        cnx.close()
        msg="Your rating is submitted, you could go to your history page to check"
    except BaseException:
        msg="Error! Please try again"
    return render_template('ratingsubmit.html',msg=msg)


# but ticket result
@app.route("/buyresult")
def buyresultpage():
    return render_template('buyresult.html')

# buy a ticket
@app.route("/buyticket")
def buyticket():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query1 = ("SELECT * from `Customer`")
    cursor.execute(query1)
    customers=cursor.fetchall()
    query2 = ("SELECT Showing.idShowing,Showing.ShowingDateTime,Showing.TheatreRoom_RoomNumber,Showing.TicketPrice,Movie.MovieName from `Showing`,`Movie` WHERE Movie.idMovie=Showing.Movie_idMovie")
    cursor.execute(query2)
    showings=cursor.fetchall()
    cnx.close()
    return render_template('buyticket.html', customers = customers, showings=showings)

# submit the request to buy a ticket
# not complete
@app.route("/buyticketsubmit", methods=["POST"])
def buyticketsubmit():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    insert_stmt = ("INSERT INTO `Attend` (customer_idCustomer,showing_idShowing)"
                   "VALUES (%s, %s)"
                   )
    data = (request.form['idCustomer'], request.form['idShowing'])
    try:
        cursor.execute(insert_stmt, data)
        cnx.commit()
        cnx.close()
        msg="You purchase is finished"
    except BaseException:
        msg="Error! Please try again"
    return render_template('buyresult.html',msg=msg)

# search
@app.route("/searching")
def search():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query1 = ("SELECT * from `Genre`")
    cursor.execute(query1)
    genres=cursor.fetchall()
    query2 = ("SELECT Showing.idShowing,Showing.ShowingDateTime from `Showing` ORDER BY ShowingDateTime")
    cursor.execute(query2)
    starts=cursor.fetchall()
    query3 = ("SELECT Showing.idShowing,Showing.ShowingDateTime from `Showing` ORDER BY ShowingDateTime")
    cursor.execute(query3)
    ends=cursor.fetchall()
    cnx.close()
    return render_template('searching.html',genres=genres,starts=starts,ends=ends)

@app.route("/search", methods=["POST"])
def searchsubmit():
    seat=0
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    if(request.form.get('haveseat')):
        selectedShowings=[]
        query1=("SELECT idShowing,Genre,ShowingDateTime,MovieName,TheatreRoom_RoomNumber from `Showing`,`Movie`,`Genre` WHERE Showing.Movie_idMovie=Movie.idMovie AND Genre.movie_idMovie=Movie.idMovie AND Genre.Genre=%s AND Showing.ShowingDateTime>=%s AND Showing.ShowingDateTime<=%s AND Movie.MovieName=%s")
        data=(request.form['genre'], request.form['starttime'], request.form['endtime'], request.form['moviename'])
        cursor.execute(query1,data)
        selectedShowingTmp = cursor.fetchall()
        for tmp in selectedShowingTmp:
            idShowing=str(tmp[0])
            query2='SELECT Capacity from `TheatreRoom`, `Showing` WHERE TheatreRoom.RoomNumber=Showing.TheatreRoom_RoomNumber AND Showing.idShowing='+idShowing+') - (SELECT COUNT(*) from `Attend` WHERE Showing_idShowing='+idShowing+')'
            cursor.execute(query2)
            leftSeat=cursor.fetchall()
            if(leftSeat[0][0]>0):
                seat=1
                selectedShowings.append(tmp)

    else:
        seat=0
        selectedShowings=[]
        query1=("SELECT idShowing,Genre,ShowingDateTime,MovieName,TheatreRoom_RoomNumber from `Showing`,`Movie`,`Genre` WHERE Showing.Movie_idMovie=Movie.idMovie AND Genre.movie_idMovie=Movie.idMovie AND Genre.Genre=%s AND Showing.ShowingDateTime>=%s AND Showing.ShowingDateTime<=%s AND Movie.MovieName=%s")
        data=(request.form['genre'], request.form['starttime'], request.form['endtime'], request.form['moviename'])
        cursor.execute(query1,data)
        selectedShowings = cursor.fetchall()
        if(selectedShowings):
            seat=1

    cnx.close()
    return render_template('searchingresult.html',selectedShowings=selectedShowings,seat=seat)

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
    query1 = ("SELECT * from `Genre`")
    cursor.execute(query1)
    select_stmt = (
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