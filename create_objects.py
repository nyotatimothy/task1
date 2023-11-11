import pandas as pd
import time
from borehole import Borehole
from sensor import Sensor
from sensor_status import SensorStatus

def read_data_from_excel(file_path):
    # Read data from an Excel file into a DataFrame. In the original implemetation, we would read this from an API
    df = pd.read_excel(file_path)

    # Excel columns are named 'BoreholeID', 'Location', 'SensorID', 'Parameter', 'InitialStatus'
    borehole_data = df[['BoreholeID', 'Location']].drop_duplicates()
    sensor_data = df[['SensorID', 'BoreholeID', 'Parameter']].drop_duplicates()
    initial_status_data = df[['SensorID', 'InitialStatus']].drop_duplicates()

    return borehole_data, sensor_data, initial_status_data

def create_boreholes(file_path):
    borehole_data, _, _ = read_data_from_excel(file_path)
    
    boreholes = [Borehole(row['BoreholeID'], row['Location']) for _, row in borehole_data.iterrows()]
    return boreholes

def create_sensors(file_path):
    _, sensor_data, _ = read_data_from_excel(file_path)

    sensors = [Sensor(row['SensorID'], row['BoreholeID'], row['Parameter']) for _, row in sensor_data.iterrows()]
    return sensors

def initialize_statuses(file_path):
    _, _, initial_status_data = read_data_from_excel(file_path)

    statuses = [SensorStatus(row['SensorID'], row['InitialStatus'], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) for _, row in initial_status_data.iterrows()]
    return statuses
