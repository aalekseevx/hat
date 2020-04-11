# Hat online

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
<!-- [![GitHub license](https://img.shields.io/github/license/aalekseevx/mipt-tp-game.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE) -->
<!-- [![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/badges/README.md)](https://GitHub.com/Naereen/badges/) -->
<!-- [![GitHub release](https://img.shields.io/github/release/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/releases/) -->

This is a web app, created to play word game "Hat" online, using browser.

Last release is hosted at [hat.alekseev.tk](https://hat.alekseev.tk).

Also, last master commit will be hosted at [staging.hat.alekseev.tk](https://staging.hat.alekseev.tk).

Information, connected to the MIPT Project description is located in [PROJECT.md](PROJECT.md) file.

## Status

![Online Hat CI Tests](https://github.com/aalekseevx/mipt-tp-game/workflows/Online%20Hat%20CI%20Tests/badge.svg?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4dfd3032ac3f42fb9633d42d3f0f6223)](https://www.codacy.com/manual/aalekseevx/mipt-tp-game?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=aalekseevx/mipt-tp-game&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/aalekseevx/mipt-tp-game/branch/master/graph/badge.svg)](https://codecov.io/gh/aalekseevx/mipt-tp-game)
[![Documentation Status](https://readthedocs.org/projects/hat-online/badge/?version=latest)](https://hat-online.readthedocs.io/en/latest/?badge=latest)
   

## Ultra-Fast deployment

## Part description

### Backend

Here game logic is described. It is divided on 4 main parts:

- words controller
- room settings
- game controller
- user statistics controller

Patterns:

- Singleton
- Decorator
- Adapter

Languages - Python 3.7

Status - Ready

Estimated implementation period -- 10.04.2020

### Frontend

Here Website design and its link with Backend are described. The setup of website based on this [repository](https://github.com/ANVoevodin/pixijs_v5_setup.git)

Patterns:
- Commang
- Chain of Responsibility
- Observer


Languages - HTML + CSS + JS

Status - Ready

Estimated implementation period -- 10.04.2020 

### Tests 

Unit tests for Backend.

Languages - Python 3.7

Status - Ready

Estimated implementation period -- 13.04.2020 - 15.04.2020

## Starting app outside container

Before running apps, satisfy following dependencies

- Poetry 1.0.5
- Python 3.7
- npm 6.14.4

Then, you can start everything:

### Backend

```bash
cd backend
poetry install
poetry run task flask
```


### Frontend

```bash
cd frontend
npm install
npm run start
```

## Running the tests

After installing dependencies, run
```bash
cd backend
poetry install
poetry run task test
```
## Built with

- [Flask](https://github.com/pallets/flask)
- [SocketIO](https://github.com/socketio/socket.io)
- [JQuery](https://github.com/jquery/jquery)
- [Bulma](https://github.com/jgthms/bulma)

## Authors


## Acknowledgments
