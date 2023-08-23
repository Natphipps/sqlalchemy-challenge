# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(bind = engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start_end<br/>"
    )




@app.route("/api/v1.0/precipitation")
def precipitation():
    prcp_data = session.query(Measurement.prcp , Measurement.date).\
    filter(Measurement.date <= '2017-8-23').\
    order_by(Measurement.date).all()
    session.close()
    all_prcp = []
    for prcp, date in prcp_data:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        all_prcp.append(prcp_dict)
    return jsonify(all_prcp)


@app.route("/api/v1.0/stations")
def stations():
    station_list = session.query(Station.station).all()
    session.close()
    all_stations = list(np.ravel(station_list))
    return jsonify(all_stations) 


@app.route("/api/v1.0/tobs")
def tobs():
    temp_data = session.query(Measurement.tobs, Measurement.date).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date <= '2017-08-23'
          ).\
    order_by(Measurement.date).all()
    session.close()
    all_tobs = list(np.ravel(temp_data))
    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>")
def temp(start):
    start_temp = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date <= start).all()
    session.close()
    start_list = list(np.ravel(start_temp))
    return jsonify(start_list)

@app.route("/api/v1.0/<start>/<end>")
def temps(start,end):
    start_end_temp = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date <= start >= end).all()
    session.close()
    start_end_list = list(np.ravel(start_end_temp))
    return jsonify (start_end_list)


if __name__ == "__main__":
    app.run(debug=True)
