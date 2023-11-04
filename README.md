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

   (Windows complied Python executables are available [HERE](https://github.com/ItsAlphaNeon/HeartRateToResonite/releases) although using the Python script is reccomended)

7. Open Resonite or any application you would like to pipe the heartbeat data to, and configure it to receive heart rate data from the specified source.
An example for Resonite is available at `resrec:///U-AlphaNeon/R-803C300B18BF168A811A42301EF086600FC483A3FB9069CE592DC257E8D8DDC7`

8. You should now be able to see and use your heart rate data in Resonite or your chosen application.

**Note**: Ensure that HeartRateOnStream is running on your watch before executing the script, as HeartRateToResonite relies on it.

