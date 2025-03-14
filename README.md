# spotify-to-youtube

<h1 align="center">
   <img alt="Flutter" src="https://raw.githubusercontent.com/TheAmanM/spotify_to_youtube/7330bc6414cfa922d028a67c07766927cef6538a/banner-dark.svg#gh-dark-mode-only">
   <img alt="Flutter" src="https://raw.githubusercontent.com/TheAmanM/spotify_to_youtube/b4a42bceb611edeb1eb25b962547d32c082ceab0/banner-light.svg#gh-light-mode-only">
</h1>

**spotify-to-youtube** is a Python 3 library that seamlessly clones Spotify playlists to YouTube playlists.

## Features

- Clone all Spotify playlists to YouTube
- Clone a specific Spotify playlist
- Clone your liked Spotify songs

## Requirements

- **Python 3.8 or higher** - [Download here](https://www.python.org/)
- **Firefox browser** - [Download here](https://www.mozilla.org/en-CA/firefox/new/)
- **Spotify API project**
- **GeckoDriver** for Firefox - [Download here](https://github.com/mozilla/geckodriver/releases)

## Usage

> **Note:** Currently, the library only supports **Firefox** as the browser.

To use this script, you must set up a **Spotify API project** and install **Firefox**.

### Setting Up a Spotify API Project

1. Navigate to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
2. Click **Create App** and provide the required details.
3. Use `http://localhost:8000` as the Redirect URI (or another localhost port of your choice).

### Installing and Configuring Firefox & GeckoDriver

#### Download Firefox

- [Download Firefox](https://www.mozilla.org/en-CA/firefox/new/)

#### Download and Set Up GeckoDriver

1. Visit the [GeckoDriver releases page](https://github.com/mozilla/geckodriver/releases).
2. Download the version compatible with your operating system.

#### Configure a Firefox Profile

1. Open Firefox and navigate to `about:profiles`.
2. Copy the **Root Directory** path from the default profile (or create a new profile using **Create Profile**).
3. This will be the **Firefox profile path** required during setup.

## Setting Up spotify-to-youtube

Run the following command to initialize the setup:

```sh
spotify-to-youtube --setup
```

You will be prompted to input the following parameters:

1. **Spotify API Client ID** (found in Spotify Developer Dashboard > App Settings)
2. **Spotify API Client Secret** (found in Spotify Developer Dashboard > App Settings > View Client Secret)
3. **Firefox Profile Path** (copy the root directory from `about:profiles` in Firefox)
   > **Recommendation:** Install an ad blocker (e.g., [uBlock Origin](https://ublockorigin.com/)) for the selected profile to improve performance.
4. **GeckoDriver Executable Path** (path to the downloaded GeckoDriver binary)

## Roadmap

- [ ] Support for additional browsers (Chrome, Edge, etc.)

## Contributing

We welcome contributions! If you'd like to contribute, please fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Need Help?

For issues or feature requests, please open a [GitHub Issue](https://github.com/your-repo/issues).
