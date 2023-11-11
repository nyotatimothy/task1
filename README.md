# Sensor Monitoring System

## Overview

-This project simulates real-time status updates for a network of sensors deployed in various boreholes. This system utilizes CSV files to store and manage sample data, providing a foundation for monitoring and predicting sensor statuses.
-I extracted this monitoring function from an existing application that I created for the Water Project at IBM. This was part of the entire application i.e. the sensor monitoring and prediction module.

## Overview

The Sensor Monitoring System is a Python project that simulates real-time status updates for a network of sensors deployed in various boreholes. This system utilizes CSV files to store and manage sample data, providing a foundation for monitoring and predicting sensor statuses.

## Project Structure

The project is structured as follows:

- `borehole.py`: Defines the Borehole class.
- `sensor.py`: Defines the Sensor class.
- `sensor_status.py`: Defines the SensorStatus class.
- `create_objects.py`: Handles the creation of boreholes, sensors, and initial statuses.
- `sensor_monitoring.py`: Simulates real-time updates and monitors the sensor statuses.

## Prerequisites

Before running the project, ensure that you have the following installed:

- Python 3.x
- Virtual environment (optional but recommended)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/sensor-monitoring-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd sensor-monitoring-system
    ```

3. (Optional) Set up a virtual environment:

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

1. Ensure your virtual environment is activated.

2. Run the main script:

    ```bash
    python main.py
    ```

This will initiate the Sensor Monitoring System, simulating real-time updates for the network of sensors.

## Sample Data

The project includes sample CSV files with data:

- `boreholes.csv`: Contains information about boreholes.
- `sensors.csv`: Contains information about sensors.
- `initial_statuses.csv`: Contains initial status information for sensors.

These files are used to initialize the system with sample data.

## Note

This project was originally developed to interact with external APIs for real-time data. For the purpose of this example, API calls were replaced with simulated data using CSV files. The CSV files (`boreholes.csv`, `sensors.csv`, and `initial_statuses.csv`) now provide sample data for the system.

Feel free to modify the CSV files with your own data or extend the project to interact with real APIs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Project Structure

The project is structured as follows:

- `borehole.py`: Defines the Borehole class.
- `sensor.py`: Defines the Sensor class.
- `sensor_status.py`: Defines the SensorStatus class.
- `create_objects.py`: Handles the creation of boreholes, sensors, and initial statuses.
- `sensor_monitoring.py`: Simulates real-time updates and monitors the sensor statuses.

## Prerequisites

Before running the project, ensure that you have the following installed:

- Python 3.x
- Virtual environment (optional but recommended)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/sensor-monitoring-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd sensor-monitoring-system
    ```

3. (Optional) Set up a virtual environment:

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

1. Ensure your virtual environment is activated.

2. Run the main script:

    ```bash
    python main.py
    ```

This will initiate the Sensor Monitoring System, simulating real-time updates for the network of sensors.

## Sample Data

The project includes sample CSV files with data:

- `boreholes.csv`: Contains information about boreholes.
- `sensors.csv`: Contains information about sensors.
- `initial_statuses.csv`: Contains initial status information for sensors.

These files are used to initialize the system with sample data.

## Note

This project was originally developed to interact with external APIs for real-time data. For the purpose of this example, API calls were replaced with simulated data using CSV files. The CSV files (`boreholes.csv`, `sensors.csv`, and `initial_statuses.csv`) now provide sample data for the system.

Feel free to modify the CSV files with your own data or extend the project to interact with real APIs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
