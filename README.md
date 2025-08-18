# FlaskTube

**FlaskTube** is a sleek, modern, Youtube search and playback web app built with **Flask**, **TailwindCSS**, and **Alpine.js**. It even lets you search for youtube videos, view video details, play videos in a modal, see related videos, and even get search suggestions--all in a responsive, user-friendly interface.


<details>
    <summary>Table Of Contents</summary>
    <ol>
        <li>
            <a href="#features">Features</a>
        </li>
        <li>
            <a href="#tech-stack">Tech Stack</a>
        </li>
        <li>
            <a href="#usage">Usage</a>
        </li>
        <li>
            <a href="#notes">Notes</a>
        </li>
        <li>
            <a href="#known-issues">Known Issues</a>
        </li>
        <li>
            <a href="#contributing">Contributing</a>
        </li>
        <li>
            <a href="#license">LICENSE</a>
        </li>
        <li>
            <a href="#credits">Credits</a>
        </li>
    </ol>
</details>

## Features

- Dark-Mode UI: Beutiful, Readable dark theme by default.
- YouTube Search: Search for videos using the YouTube Data API.
- Instant Search Suggestions: Autocomplete suggestions while typing.
- Video Playback Modal: watch videos without leaving page.
- Video Details: View description, channel info, views, likes.
- Related Videos: Browse videos from the same channel directly in the modal.
- Responsive Grid Layout: Works on desktop, tablet, and mobile.

## Tech Stack

| Layer   | Technology/Library     |
| ------- | ---------------------- |
| Backend | Flask, Python          |
|Fontend  | TailwindCSS, Alpine.js |
| API     | YouTube Data API V3    |
| Hosting | Render                 |

## Usage

- Go to https://flasktube-trg7.onrender.com/

- Search your choice of video in the search bar

- Click and enjoy!

## Notes
- Maximum searc results are limited to 10
- Related Videos are fetched from same channel only
- If a video is missing thumbnails, a placeholder image is displayed

## Known Issues
- The YouTube API enofrces rate limits, frequent requests may return errors
- A lot of the videos have a missing likeCount and ViewCount this is becuase those aspects are still under construction
- Search suggestions depend on Google Suggest API, occasinal failures can occur
- Video Duration tags on video are still a work in progress

## Contributing

Feel free tu contribute towards this by either fixing an issue above or using your creativity to make this a million times better. Just sumbit a pull request for any contributions!

## LICENSE

IDK if I spelled that right but make check out the LICENSE page for more info

## Credits

Created by Kush Desay for [SoM](https://summer.hackclub.com/), View my project on [SoM Website](https://summer.hackclub.com/projects/11394) Today!
