# Unity Study Group Website

The full backend and frontend of the Unity Study Group's website.

## Setup

### Prerequisites

You will need to install:
* Virtualbox
* Vagrant

Vagrant is used to ensure a consistent development environment regardless of host operating system.

### Project Setup

To set up your environment:

```sh
git clone https://github.com/TheodorosBalasis/unity-study-group-website.git
cd unity-study-group-website
vagrant up
vagrant ssh
cd app
make init
. venv/bin/activate
```

## Usage

To start the development server, run `make start`.

To run unit tests, run `make test`.

To deactivate the virtual environment, run `deactivate`.
