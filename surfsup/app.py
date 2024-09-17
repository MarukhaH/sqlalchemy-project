# Import the dependencies.
import datetime as dt 
import numbpy as np 

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import session
from sqlalchemy import create_engine, func

from flask import Flask, jsonfiy


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")



# reflect an existing database into a new model


# reflect the tables

Base = automap_base()
Base.prepare(engine)

# Save references to each table
Measurement = Base.classes.Measurement
Station = Base.classes.Station


# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return(
        f"Welcome to the Hawaii Climate Analysis API<br/>",
        f"Available Routes:<br/>",
        f"/api/v1.0/precipitation<br/>",
        f"/api/v1.0/station<br/>",
        f"/api/v1.0/tobs<br/>",
        f"/api/v1.0/temp/start<br/>",
        f"/api/v1.0/temp/start/end<br/>",
        f"<p>'start' and 'end' date should be in the format MMDDYYYY.</p>",
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8,23) - dt.timedelta(days=365)

    precip = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= prev_year).all()

        session.close()
        precip = {date: prcp for date, prcp in precipitation}

        return jsonify(precip)

    @app.route("/api/v1.0/")


    if __name__ == "__main__":
        app.run(debug=True)