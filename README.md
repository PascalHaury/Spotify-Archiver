# Spotify Archiver

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

## Description

"Spotify Archiver" is a Python program designed to help you archive specific Spotify playlists by creating new playlists that contain the same songs as the source playlist. It also allows you to customize the name and description of the archived playlists.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Cyclical Runs](#cyclical-runs)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```sh   
   git clone https://github.com/yourusername/Spotify-Archiver.git
   ```

2. Change to the project directory:

    ```sh
    cd Spotify-Archiver
    ```

3. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Update your Spotify credentials and playlist names in the script (main.py) to match your preferences. You can specify the playlists you want to archive and customize their names and descriptions.

2. Run the application:

    ```sh
    python Spotify-Archiver/src/main.py
    ```

3. The program will create archived playlists based on your settings.

## Configuration

You can configure the following settings in the script (main.py):

- Spotify credentials (client_id, client_secret, redirect_uri, username)
- List of playlist names to archive (playlist_names)
- Customizations for archived playlist names, descriptiosns, and privacy settings
- Spotify API scope (scope)

Please make sure to update the script with your Spotify credentials and preferences before running it.

## Obtaining a Spotify Client Secret

To obtain a Spotify client secret, follow these steps:

1. Visit the Spotify Developer Dashboard at https://developer.spotify.com/dashboard/.
2. Log in with your Spotify account or create one if you don't have an account.
3. Click on the "Create an App" button.
4. Fill in the required information for your app, including the name and description.
5. Once your app is created, you will find your client_id and client_secret on the app's dashboard.
6. Make sure to set the correct redirect URI in the Spotify Developer Dashboard. The redirect URI in your code (main.py) must match the one you specify in the developer portal.

## Cyclical Runs

To schedule the "Spotify Archiver" program for cyclical runs, you can use tools like cron on Unix-based systems or Task Scheduler on Windows. Below is an example of how to set up a daily run at midnight using cron:

1. Open your crontab configuration for editing:

    ```sh
    crontab -e
    ```

2. Add the following line to schedule the script for daily execution at midnight:

    ```sh
    0 0 * * * /usr/bin/python /path/to/Spotify-Archiver/main.py
    ```

    Replace /usr/bin/python with the path to your Python interpreter (you can find it by running which python).

    Replace /path/to/Spotify-Archiver with the actual path to your project directory.

3. Save and exit the crontab editor.

    This will run your script daily at midnight.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
This script is provided as-is, and the author is not responsible for any issues or data loss that may occur during its usage. It's recommended to back up your data before running this script.

Please use this script responsibly and ensure that you comply with Spotify's terms of service and API usage policies.