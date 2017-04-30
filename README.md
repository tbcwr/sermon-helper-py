[![Build Status](https://travis-ci.org/hbcwr/sermon-helper-py.svg?branch=master)](https://travis-ci.org/hbcwr/sermon-helper-py)

# sermon-helper-py

Helper files for managing sermon files

### Prerequisites

Run `pip install -r requirements.txt` before beginning.

## tagmp3.py

This script has to run via command prompt. For Mac OS, you can hit the magnifying glass at the top right to search for and open `Terminal`. Make sure you are in the same directory as `tagmp3.py` when running.

```sh
python tagmp3.py                            # defaults to looking for a file named "sermon.ini"
python tagmp3.py --config selah-series.ini  # Looks for configs in "selah-series.ini"
```

### Configs

* See [tagmp3.py](tagmp3/tagmp3.py)'s variable `REQUIRED_CONFIGS` for list of required configs.
* See [sermon-example.ini](tagmp3/sermon-example.ini) for an example config.
  * The `artwork` config expects an image file in the same folder with that name.
  * The `source` config expects an MP3 file in the same folder with that name.
