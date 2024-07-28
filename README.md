# Uptime Monitor

Uptime Monitor is a web application built using Dash that monitors the uptime of various services and displays the data in real-time.

## Features

- **Real-time Monitoring**: The application updates the uptime status every minute.
- **Interactive Graphs**: Visualize the uptime data with interactive graphs.
- **Loading Indicator**: Displays a loading indicator while fetching data.
- **Customizable Layout**: Easily modify the layout and style of the application.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Varp0s/uptime-monitor
    ```
2. Navigate to the project directory:
    ```sh
    cd uptime-monitor
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Docker Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Varp0s/uptime-monitor
    ```
2. Navigate to the project directory:
    ```sh
    cd uptime-monitor
    ```
3. Start docker:
    ```sh
    add domain in domain.txt
    docker-compose or docker compose up -d --build
    ```
4. Open browser:
    ```sh
    `http://127.0.0.1:1453`
    ```
## Usage

1. Run the application:
    ```sh
    pip install -r requirements.txt
    add domain in domain.txt
    python3 main.py
    ```
2. Open your web browser and go to `http://127.0.0.1:1453` to view the application.

## Project Structure

- `main.py`: The main application file.
- `assets/`: Directory containing static assets like the favicon.
- `requirements.txt`: List of dependencies required for the project.

## Customization

- **Title**: Modify the `title` function in `main.py` to change the application title.
- **Favicon**: Replace the favicon file in `assets/img/favicon.ico` with your own.
- **Layout**: Modify the `app.layout` section in `main.py` to customize the layout and style of the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## TO:DO

json api support
separate chart for each asset

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- [Dash](https://dash.plotly.com/) - A productive Python framework for building web applications.
- [Varp0s](https://github.com/Varp0s) - For powering the Uptime Monitor.

© 2024 - Uptime Monitor Powered by Varp0s