# Development setup

1. Clone this repo. 

1. Install/update pyenv and Python 3.9.13 if needed, e.g.:

   ```
   brew update && brew upgrade pyenv
   pyenv install 3.9.13
   ```

   Follow pyenv's instructions for adding to the appropriate rc file, reload the 
   shell, and navigate to the project root. The project's `.python-version` file 
   specifies the appropriate Python version, which you can confirm using `which python`.

1. Create and activate a virtual environment using `venv`:

   ```commandline
   $ python -m venv mmenv
   ```

1. From within the virtual environment, install dependencies:
 
   ```commandline
   $ . mmenv/bin/activate
   (mmenv) $ pip install -r requirements.txt
   ```

1. Create a `.env` file in the project root with the contents:

   ```commandline
    SECRET_KEY=<secret key here>
   ```
   
   You can generate a key using `python -c 'import secrets; print(secrets.token_hex())'`

1. You should now be able to run the Flask application:

   ```commandline
   (mmenv) $ flask --app hello run
   ```
   
   * To make visible within the network, add `--host=0.0.0.0`
   * To use browser debugger and reload upon code changes, add `--debug`