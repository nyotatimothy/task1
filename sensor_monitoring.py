import time
import random  # Import the random module. Using this for simulations to mimic API calls
from create_objects import create_boreholes, create_sensors, initialize_statuses

def update_real_time_statuses(status_data):
    for sensor_id, status_info in status_data.items():
        # Simulate changes in sensor status. I modified this function to mimic API call that was receiving sensor statuses
        new_status = random.choice(['Off', 'Normal', 'Stretched', 'Critical'])
        status_info.status = new_status
        status_info.timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def sensor_monitoring(boreholes, sensors, status_data):
    borehole_hash = {borehole.borehole_id: borehole for borehole in boreholes}
    sensor_hash = {sensor.sensor_id: sensor for sensor in sensors}

    while True:
        # Simulate real-time status updates. I modified this function to mimic API calls that were updating the status
        update_real_time_statuses(status_data)

        # Update sensor_hash with the latest statuses
        for sensor_id, status_info in status_data.items():
            sensor_hash[sensor_id].current_status = status_info.status

        # Predictive algorithm. I modified this function to mimic API calls that were predicting sensor statuses
        for sensor_id, status_info in status_data.items():
            if status_info.status == 'Stretched':
                print(f"Predicting potential critical status for Sensor {sensor_id} in Borehole {sensor_hash[sensor_id].borehole_id}!")

        # Simulate a time delay between updates. I modified this function to mimic API calls that were calculating delay between updates
        time.sleep(60)

if __name__ == "__main__":
    excel_file_path = "sensor_statuses.csv"

    boreholes = create_boreholes(excel_file_path)
    sensors = create_sensors(excel_file_path)
    statuses = initialize_statuses(excel_file_path)

    status_data = {status.sensor_id: status for status in statuses}

    sensor_monitoring(boreholes, sensors, status_data)
