# GenAI
Project of the lecture 194.207 Generative AI (VU 4,0) 2025W


# Installation

Use your preferred terminal.

After downloading the sourcecode with `git clone`

Enter the created directory with `cd GenAI`

Make sure to have an adequate python version. To check this, run `pyenv versions`

If you don't have 3.13+, install it:

```
pyenv install 3.13.0
pyenv global 3.13.0
```

If you do not have uv installed, install it first with `pip install uv`

To download dependencies, run:

```
uv venv
uv build
uv pip install .
```


# Gemini API Key

In order to run the project, one needs a Gemini API Key. It is possible to get it for free.

1. Sign In to Google AI Studio
    - Navigate to the Google AI Studio API Keys page. <https://aistudio.google.com/app/apikey>
    - Sign in with your Google Account.

2. Create Your API Key
    - Once you are on the API Keys page, look for and click the "Create API Key" button.
    - A dialog will appear. Create a new project to associate with your key.

3. Generate and Copy the Key
    - Then the system will instantly generate your new API key.
    - The key is a long string of alphanumeric characters. Copy it immediately using the copy icon next to the key.

4. Create a file .env in the root folder of the project.
    - Include `GEMINI_API_KEY = <YOUR_KEY>`
-- OR --
4. add your Gemini API key to your environment by executing `export GEMINI_API_KEY=<YOUR_KEY>` in a terminal emulator


# MongoDB (Linux)

This project relies on a local mongodb database. Download mongodb and mongosh through your favorite package manager.

Ensure storage directories exists for the database and for its logs, and give mongodb control over them.
```
sudo mkdir -p /var/lib/mongodb
sudo chown -R mongodb:mongodb /var/lib/mongodb

sudo mkdir -p /var/log/mongodb
sudo chown -R mongodb:mongodb /var/log/mongodb
```

Next, create a configuration file at `/etc/mongodb.conf` and add the following:

```
# mongod.conf

# for documentation of all options, see:
#   http://docs.mongodb.org/manual/reference/configuration-options/

# Where and how to store data.
storage:
  dbPath: /var/lib/mongodb

# where to write logging data.
systemLog:
  destination: file
  logAppend: true
  path: /var/log/mongodb/mongod.log

# network interfaces
net:
  port: 27017
  bindIp: 127.0.0.1
```

Finally, enable the mongodb service with `sudo systemctl enable --now mongodb`

You can check that it is running without errors with `systemctl status mongodb`

or by running `mongosh`, if this command doesn't immediately return an error, mongodb is running. Use `exit` to exit the mongo shell.

# MongoDB (Windows)

**Option A: Use WSL (Recommended)**
Follow the Linux instructions above in your WSL terminal.

**Option B: Native Windows Installation**
1. Download MongoDB Community Server from https://www.mongodb.com/try/download/community
2. Run the installer and follow the setup wizard
3. Download mongosh from https://www.mongodb.com/try/download/shell
4. MongoDB will run as a Windows service by default
5. Add the paths of these two programmes to the system variable `Path`
   1. Press the Windows Key and search for "Edit the system environment variables".
   2. In the window that appears, click the Environment Variables button at the bottom right.
   3. Under the "System variables" section (the bottom list), find the variable named Path and click Edit.
   4. Click New and paste the path to your shell's bin folder. By default, it is usually: `C:\Users\user-name\Downloads\mongosh-2.6.0-win32-x64\bin`
   5. Click New and paste the path to your server's bin folder. By default, it is usually: `C:\Program Files\MongoDB\Server\8.x\bin`
   6. Click OK on all windows to confirm and save the changes.
6. Verify it's running: open PowerShell (or reopen it, if it was already opened) and run `mongosh`



# Running the Project
To start up the server locally, run `uv run streamlit run Home.py`

You can also run `uv run db_run.py` to initialize the database with a lecture and some test user notes for the comparison page.
