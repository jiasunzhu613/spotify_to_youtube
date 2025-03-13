# spotify-to-youtube

spotify-to-youtube is a Python3 library that clones spotify playlist to youtube playlist

## Features:

- add all spotify playlists
- add specific spotify playlist
- add liked spotify playlist

## Requirements:

- Python 3.8 or higher - https://www.python.org/

## Usage:

> **Note** that currently the library only supports **Firefox** as the browser.

In order to use the script, you will need a **Spotify API project** and **Firefox** installed.

#### Creating a Spotify API project

Navigate to https://developer.spotify.com/dashboard and click _Create project_ and fill in the required information.

- the _"App name"_ and _"App description"_ can be anything, use `http://localhost:8000` as the Redirect URI (note that this could be any localhost port)

#### Downloading Firefox (and Gecko Driver) and Setting up Firefox profile

Firefox:
You can download Firefox from https://www.mozilla.org/en-CA/firefox/new/

Firefox Gecko Driver:
Navigate to https://github.com/mozilla/geckodriver/releases and choose the download for your corresponding operating system.

Set-up Firefox Profile:

1. Open Firefox and navigate to `about:profiles`.
2. Copy the root directory from the default profile (or another profile created using `Create Profile`)
   - this will be the Firefox profile filepath you input in the setup for spotify-to-youtube

### Setup spotify-to-youtube

Run `spotify-to-youtube --setup` and then you will be prompted to input 4 parameters:

1. Spotify API client id (which you can find by navigating to your Spotify API project > Settings)
2. Spotify API client secret (which you can find by navigating to your Spotify API project > Settings > view client secret)
3. Firefox profile path (navigate to `about:profiles` in Firefox and copy the root directory of a profile)
   > NOTE: it is **highly recommended** to download an adblocker (e.g. uBlock Origin) for the profile you are using
4. Firefox Gecko Driver executable path (filepath to downloaded gecko driver)

## TODO:

- [ ] Support for other browsers
