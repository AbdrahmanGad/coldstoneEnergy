import random
import time
import math
from collections import deque
import matplotlib.pyplot as plt

#Generate Random Floating numbers Stream
def floating_numbers_stream():
    counter = 0
    while True:
        normalNo = math.sin(counter / 20) * 50 #normal numbers
        seasonalNo = math.sin(counter / 10) * 100 # seasonal numbers
        noise = random.uniform(-30, 30) #noise numbers
        final = normalNo + seasonalNo + noise
        transaction_value = round(final, 3) #make 3 digits decimel values
        yield transaction_value
        counter += 1
        time.sleep(0.01)

#generate the Z score of the numbers usings (manually calulating mean, varience, standard deviation)
def z_score(latest_value, data, threshold=2.7):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    if std_dev == 0:
        return False
    z_score_value = (latest_value - mean) / std_dev
    return abs(z_score_value) > threshold

#check for anomalies values
def detect_anomalies(stream, window_size):
    window = deque(maxlen=window_size)
    for value in stream:
        window.append(value)
        if len(window) == window_size:
            is_anomaly = z_score(value, window)
            yield value, is_anomaly

#visualize the numbers
def plot_data_stream(stream, window_size, total_points):
    plt.ion()
    fig, ax = plt.subplots()
    allDataList = []
    anomalyDataList = []
    normal, = ax.plot([], [], label='Normal Data') #rename the noraml data
    anomaly, = ax.plot([], [], 'ro', label='Anomaly Data') #rename the anomaly data
    ax.set_ylim([-200, 200]) #set y axis range
    ax.set_xlim([0, total_points]) #set x axis range(without end for all data)
    ax.legend()

    for i, (data_point, is_anomaly) in enumerate(detect_anomalies(stream, window_size)):
        allDataList.append(data_point)
        normal.set_xdata(range(len(allDataList)))
        normal.set_ydata(allDataList)

        if is_anomaly:
            anomalyDataList.append(i)
            anomaly.set_xdata(anomalyDataList)
            anomaly.set_ydata([allDataList[j] for j in anomalyDataList])

        if i % window_size == 0:
            ax.set_xlim([max(0, i - total_points), i + total_points])

        plt.draw()
        plt.pause(0.001)

        if i >= total_points:
            break

    plt.ioff()
    plt.show()

# Start data stream and visualization
stream = floating_numbers_stream()
plot_data_stream(stream, window_size=50, total_points=1000)
