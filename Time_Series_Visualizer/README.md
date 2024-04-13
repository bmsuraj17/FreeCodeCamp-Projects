# Page View Time Series Visualizer
This repository contains the projects completed as part of the FreeCodeCamp Data Analysis with Python Certification. The certification involves building five projects that demonstrate proficiency in data analysis using Python.

I visualized time series data using a line chart, bar chart, and box plots. The dataset contained the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03.

## Development
The code was written in time_series_visualizer.py.
For development, main.py was used to test the code.

## Testing
The unit tests for this project are in test_module.py.
We imported the tests from test_module.py to main.py for convenience.

## How to Use
Clone this repository to your local machine.
Open the project in an IDE or text editor.
Implement the necessary calculations in time_series_visualizer.py to answer the questions provided.
Run main.py to test your implementation.
Ensure all tests pass.

## Tasks
Import the data from "fcc-forum-pageviews.csv" using Pandas and set the index to the date column.
Clean the data by filtering out days when the page views were in the top 2.5% or bottom 2.5% of the dataset.
Create a draw_line_plot function that uses Matplotlib to draw a line chart showing daily page views.
Create a draw_bar_plot function that draws a bar chart showing average daily page views for each month grouped by year.
Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots showing the distribution of page views within a given year or month.

## Dataset Source
Data obtained from the freeCodeCamp.org forum.
