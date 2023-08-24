# sqlalchemy-challenge: Analyze and Explore the Climate Data
module 10 sqlalchemy challenge

# Main Goal

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. 

For this project you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database.

# Technologies

1.) SQLAlchemy ORM queries

2.) Pandas

3.) Matplotlib

4.) Flask

# Part 1: Precipitation Analysis

I used the provided starter files (climate_starter.ipynb) and (hawaii.sqlite).

 - I retrieved the most recent date in the hawaii_measurement.csv.
 - Using the most recent date I created a query to retrieve the previous 12 months of precipitation data.
 - I created a bar graph to plot the precipitation data.
 - I ran summary statistics for the data.

This analysis can be found in the precipitation analysis section in the climate_starter.ipynb file in this repository.

# Part 2: Station Analysis

- I designed a query to find the total number of stations in the dataset using the hawaii_station.csv.
- I designed a query to find the most active station in the dataset (the station with the most rows) using the hawaii_measurement.csv.
- I designed a query that calculated the lowest, highest, and average temperatures of the most-active station found in the previous query.
- I designed a query to get the previous 12 months of temperature observation (TOBS) data.
- I created a histogram to plot the station data.

This analysis can be found in the station analysis section in the climate_starter.ipynb file in this repository.

# Part 3: creating the climate app
After completing the initial analysis, I designed a Flask API based on the queries develped in the precipitation and station analysis. I created the flask routes in the app.py file.

- I imported all of the dependencies, created the database and flask setup.

- I created flask routes for the following:

  1.) A homepage with all of the routes.
  
  2.) A precipitation route that returns a JSON representation of the precipitation analysis data.
  
  3.) A station route that returns a JSON list of stations.
  
  4.) A tobs route that returns a JSON list of temperature observations for the previous year of data based on the most-active station.
  
  5.) A start  and end route that returns a JSON list of the min, max, and avg temperature based on the URLS's specified start date.

# Outside Resources

Most syntax help was retrieved from the class gitlab. 

Stack Overflow was used to help me understand how to create the start/end route queries.

Matplotlib website helped me with creating bar and histogram plots.













