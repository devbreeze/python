## website

## Run Locally
1. Install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
See the README file for directions. You'll need python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html) installed too.
1. Install dependencies in the project's lib directory.
   Note: App Engine can only import libraries from inside your project directory.
   ```
   cd appengine-python-flask-skeleton
   pip install -r requirements.txt -t lib
   ```
1. Run this project locally from the command line:
   ```
   dev_appserver.py .
   ```

Visit the application [http://localhost:8080](http://localhost:8080)

## Deploy
To deploy the application:

1. [Deploy the
   application](https://developers.google.com/appengine/docs/python/tools/uploadinganapp) with
   ```
   appcfg.py -A <your-project-id> --oauth2 update .
   ```

## Licensing
See [LICENSE](LICENSE)
