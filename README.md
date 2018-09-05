# Unity Study Group Website

The full backend and frontend of the Unity Study Group's website.

## Setup

### Bash

If you're using Git Bash on Windows you will need to manually install `make` such as detailed [here](https://gist.github.com/evanwill/0207876c3243bbb6863e65ec5dc3f058).

To set up your environment:

```bash
git clone https://github.com/TheodorosBalasis/UnityStudyGroupWebsite.git
cd UnityStudyGroupWebsite/usgw
```

If you're on Windows:

```bash
make wdev
```

or on Linux:

```bash
make ldev
```

then

```bash
python setup.py install
```

## Usage

### Bash

To start the server run `make wserver` or `make lserver` for Windows and Linux respectively.

To run unit tests, run `make wunit` or `make lunit` for Windows and Linux respectively.
