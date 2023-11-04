# HeartRateToResonite

HeartRateToResonite is a Python application that allows you to transmit heart rate data from your Samsung Galaxy Watch or Pixel Watch to any application, such as Resonite, through the "HeartRateOnStream" application. It tricks the watch's connectivity into believing it's connecting to OBS, making it possible to pipe the heartbeat data.

## Installation

To install the necessary dependencies, follow these steps:

1. Ensure you have Python installed. If not, you can download it from the official [Python website](https://www.python.org/).

2. Open a terminal or command prompt.

3. Run the following command to install the required packages using `pip`:

   ```shell
   pip install websockets aioconsole
   ```

   The above command will install the `websockets` and `aioconsole` packages.

## Usage

To use HeartRateToResonite, follow these steps:

1. Clone or download the HeartRateToResonite repository from GitHub.

2. Open a terminal or command prompt.

3. Navigate to the main directory of the downloaded repository.

4. Connect your Samsung Galaxy Watch or Pixel Watch to your computer.

5. Run the main Python script using the following command:

   ```shell
   python main.py
   ```

   The script will hijack the HeartRateOnStream application's connectivity and make it believe it's connecting to OBS.

6. Open Resonite or any application you would like to pipe the heartbeat data to, and configure it to receive heart rate data from the specified source.

7. You should now be able to see and use your heart rate data in Resonite or your chosen application.

**Note**: Ensure that HeartRateOnStream is running on your watch before executing the script, as HeartRateToResonite relies on it.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute this code according to the terms of the license.