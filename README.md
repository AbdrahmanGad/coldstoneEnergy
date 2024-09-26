# Real-Time Anomaly Detection in Streaming Data

## Overview

This project implements a real-time anomaly detection system that analyzes a stream of floating-point numbers generated using a combination of normal, seasonal, and noise components. The system uses Z-score calculations to identify outliers in the data stream and visualizes the results using Matplotlib.

This code serves as a research project as part of the application process for a Graduate Software Engineer role.

## Technologies Used

- Python 3.x
- Matplotlib
- Collections (deque)
- Random
- Math

## How It Works

1. **Data Generation**:
   - The `floating_numbers_stream` function generates a continuous stream of floating-point numbers that simulate real-world data. The numbers are calculated using a combination of a sine function for normal and seasonal trends, and random noise.

2. **Anomaly Detection**:
   - The `z_score` function calculates the Z-score for each new data point against a sliding window of previous values to determine if it qualifies as an anomaly based on a configurable threshold.

3. **Visualization**:
   - The `plot_data_stream` function continuously visualizes the data points as they are generated, highlighting detected anomalies in real-time.
