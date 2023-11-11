from create_objects import create_boreholes, create_sensors, initialize_statuses

if __name__ == "__main__":
    excel_file_path = "sensor_statuses.csv"

    boreholes = create_boreholes(excel_file_path)
    sensors = create_sensors(excel_file_path)
    statuses = initialize_statuses(excel_file_path)
