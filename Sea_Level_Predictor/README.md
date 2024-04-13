# Sea Level Predictor
This repository contains the projects completed as part of the FreeCodeCamp Data Analysis with Python Certification. The certification involves building five projects that demonstrate proficiency in data analysis using Python.

I analyzed a dataset of the global average sea level change since 1880 to predict the sea level change through the year 2050.

## Development
The code was written in sea_level_predictor.py.
For development, main.py was used to test the code.

## Testing
The unit tests for this project are in test_module.py.
We imported the tests from test_module.py to main.py for convenience.

## How to Use
Clone this repository to your local machine.
Open the project in an IDE or text editor.
Implement the necessary calculations in sea_level_predictor.py to analyze and predict sea level changes.
Run main.py to test your implementation.
Ensure all tests pass.

## Tasks
Import the data from epa-sea-level.csv using Pandas.
Create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit.
Plot the line of best fit over the top of the scatter plot, making it go through the year 2050 to predict the sea level rise in 2050.
Plot a new line of best fit using only the data from year 2000 through the most recent year in the dataset, also going through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.

## Dataset Source
Global Average Absolute Sea Level Change, 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.
