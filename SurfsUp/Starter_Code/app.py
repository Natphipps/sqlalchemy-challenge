# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

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
from flask import Flask

app = Flask(__name__)

date = {"prcp"}

@app.route("/api/v1.0/precipitation")
def home():
    return date

list_ = {"stations"}

@app.route("/api/v1.0/stations")
def home():
    return list_

temperature = {"tobs"}

@app.route("/api/v1.0/tobs")
def home():
    return temperature


if __name__ == "__main__":
    app.run(debug=True)


#################################################
# Flask Routes
#################################################
