[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<p align="center">

  <h3 align="center">YouTube & Twitter Script</h3>

  <p align="center">
    A Python script that tweets a link and message to a video whenever a specified channel uploads a new video
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Editing](#editing)
* [Usage](#usage)
* [License](#license)
* [Contact](#contact)


## About The Project

This is a simple Python script that tweets a link and message to a video whenever a specified channel uploads a new video.


### Built With

* [Python](https://www.python.org/)
* [Tweepy](https://www.tweepy.org/)


## Getting Started

Assuming you already have python installed you can follow the steps below.


### Prerequisites

Machines running this script will need Python and Tweepy installed. Users will also need access to the Twitter and YouTube APIs.


### Installation

1. Clone the repo
```sh
git clone https://github.com/AlisterRoe/Python-YouTube-Upload-Tweeter.git
```
2. Install Tweepy
```sh
pip install tweepy
```


### Editing

You will need to edit 7 lines of code in total.

First begin with the 5 lines in secrets.py and change them to their respective keys and auth codes.

Secondly go to main.py and update line 11 to the channel ID you want the script to query and check for new uploads.

Finally you should change line 28 in main.py and just change the 'Message: ' string to the message you want the script to tweet.


## Usage

People can use this as they please. Just a cool script that I wanted to share with people


## License

Distributed under the MIT License. See `LICENSE` for more information.


## Contact

Alister Roe - [@alisterroe](https://twitter.com/alisterroe)

Project Link: [https://github.com/AlisterRoe/Python-YouTube-Upload-Tweeter](https://github.com/AlisterRoe/Python-YouTube-Upload-Tweeter)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AlisterRoe/YouTube-Flutter-App.svg?style=flat-square
[contributors-url]: https://github.com/AlisterRoe/Python-YouTube-Upload-Tweeter/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AlisterRoe/YouTube-Flutter-App.svg?style=flat-square
[forks-url]: https://github.com/AlisterRoe/Python-YouTube-Upload-Tweeter/network/members
[stars-shield]: https://img.shields.io/github/stars/AlisterRoe/YouTube-Flutter-App.svg?style=flat-square
[stars-url]: https://github.com/AlisterRoe/Python-YouTube-Upload-Tweeter/stargazers
[issues-shield]: https://img.shields.io/github/issues/AlisterRoe/YouTube-Flutter-App.svg?style=flat-square
[issues-url]: https://github.com/AlisterRoe/Python-YouTube-Upload-Tweeter/issues
[license-shield]: https://img.shields.io/github/license/AlisterRoe/YouTube-Flutter-App.svg?style=flat-square
[license-url]: https://github.com/AlisterRoe/Python-YouTube-Upload-Tweeter/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/alisterroe/