# Medical Data Visualizer
This repository contains the projects completed as part of the FreeCodeCamp Data Analysis with Python Certification. The certification involves building five projects that demonstrate proficiency in data analysis using Python.

I visualized and made calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations and included information such as age, gender, height, weight, blood pressure, cholesterol level, glucose level, smoking status, alcohol intake, physical activity, and the presence or absence of cardiovascular disease.

## Development
The code was written in medical_data_visualizer.py.
For development, main.py was used to test the code.

## Testing
The unit tests for this project are in test_module.py.
We imported the tests from test_module.py to main.py for convenience.

## How to Use
Clone this repository to your local machine.
Open the project in an IDE or text editor.
Implement the necessary calculations in medical_data_visualizer.py to answer the questions provided.
Run main.py to test your implementation.
Ensure all tests pass.

## Tasks
Add an overweight column to the data based on BMI calculations.
Normalize the data to have 0 for 'good' and 1 for 'bad' values.
Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot().
Clean the data by filtering out incorrect patient segments.
Create a correlation matrix and plot it using seaborn's heatmap().
