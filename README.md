<!--
Hey, thanks for using the awesome-readme-template template.
If you have any enhancements, then fork this project and create a pull request
or just open an issue with the label "enhancement".

Don't forget to give this project a star for additional support ;)
Maybe you can mention me or this repo in the acknowledgements too
-->
<div align="center">

  <img src="app/static/img/logo.png" alt="logo" width="150" height="auto" />
  <h1>E-letter</h1>
  
  <p>
    Web-based correspondence archiving application, built using the Flask.
  </p>
  
  
<!-- Badges -->
<p>
  <a href="https://github.com/superiorkid/content-aggregator/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/superiorkid/content-aggregator" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/superiorkid/content-aggregator" alt="last update" />
  </a>
  <a href="https://github.com/superiorkid/content-aggregator/network/members">
    <img src="https://img.shields.io/github/forks/superiorkid/content-aggregator" alt="forks" />
  </a>
  <a href="https://github.com/superiorkid/content-aggregator/stargazers">
    <img src="https://img.shields.io/github/stars/superiorkid/content-aggregator" alt="stars" />
  </a>
  <a href="https://github.com/superiorkid/content-aggregator/issues/">
    <img src="https://img.shields.io/github/issues/superiorkid/content-aggregator" alt="open issues" />
  </a>
  <a href="https://github.com/superiorkid/content-aggregator/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/superiorkid/content-aggregator.svg" alt="license" />
  </a>
</p>
   
<h4>
    <a href="https://demogregator.herokuapp.com/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/superiorkid/content-aggregator/issues/">Report Bug</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->

# :notebook_with_decorative_cover: Table Of Content

- [About the Project](#star2-about-the-project)
  - [Screenshots](#camera-screenshots)
  - [Tech Stack](#space_invader-tech-stack)
  - [Features](#dart-features)
  - [Environment Variables](#key-environment-variables)
  - [Getting Started](#toolbox-getting-started)
  - [Prerequisites](#bangbang-prerequisites)
  - [Installation](#gear-installation)
  - [Run Locally](#running-run-locally)
  <!-- About the Project -->

## :star2: About the Project

<!-- Screenshots -->

### :camera: Screenshots

<div align="center"> 
  <img src="prtscr/dashboard.png" alt="screenshot" />
</div>

<!-- TechStack -->

### :space_invader: Tech Stack

  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://flask.palletsprojects.com/">Flask</a></li>
    <li><a href="https://getbootstrap.com/">Bootstrap</a></li>
    <li><a href="https://www.postgresql.org/">Postgresql</a></li>
  </ul>

<!-- Features -->

### :dart: Features

- Dashboard
- Surat Masuk & Surat Keluar
- Surat Balasan
- Aktifitas Harian
- Agenda Harian
- Disposisi
- Admin

<!-- Env Variables -->

### :key: Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`IS_ADMIN` <br>
`FLASK_APP` <br>
`FLASK_DEBUG`

<!-- Getting Started -->

## :toolbox: Getting Started

<!-- Run Locally -->

### :running: Run Locally

Clone the project

```bash
  git clone https://github.com/magang-brida-2022/surat-menyurat.git
```

Go to the project directory

```bash
  cd surat-menyurat
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  flask run
```
