# Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from sqlalchemy import func
import warnings
from flask import Flask, jsonify
warnings.filterwarnings('ignore')
import datetime
today = datetime.datetime.now().strftime("%Y-%m-%d")

# Database setup
engine = create_engine('sqlite:///hawaii.sqlite', echo=False)
Base = automap_base()
Base.prepare(engine, reflect=True)

# References
stations = Base.classes.stations
measurements = Base.classes.measurements

# Session link
session = Session(engine)

# Flask setup
app = Flask(__name__)

# FRoutes
@app.route("/")
def welcome():
    """Hawaii Weather API Routes:"""
    return (
        f"<strong>Hawaii Weather API Routes</strong><br><br>"
        f"/api/v1.0/precipitation <br> Dates and temperature observations from the last year<br><br>"
        f"/api/v1.0/stations <br> Weather stations<br><br>"
        f"/api/v1.0/tobs <br> Temperature observations for the previous year<br><br>"
        f"/api/v1.0/&lt;start> <br> MAX, MIN, and MEAN temperatures for all dates greater than or equal to the start date<br><br>"
        f"/api/v1.0/&lt;start>/&lt;end> <br> MAX, MIN, and MEAN temperature for dates between the start and end date, inclusive"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Dates and temperature observations from the last year"""
    return jsonify(session.query(measurements.date, measurements.prcp).all()
    )

#@app.route("/api/v1.0/stations")
#def stations():
#    """Weather stations"""
#    return jsonify().all()
#    )

#@app.route("/api/v1.0/tobs")
#def tobs():
#    """Temperature observations for the previous year"""
#    return jsonify()
#    )

#@app.route("/api/v1.0/")
#def start():
#    """MAX, MIN, and MEAN temperatures for all dates greater than or equal to the start"""
#    return jsonify()
#    )

#@app.route("/api/v1.0/")
#def range():
#    """MAX, MIN, and MEAN temperature for dates between the start and end date, inclusive"""
#    return jsonify()
#    )

if __name__ == "__main__":
    app.run(debug=True)