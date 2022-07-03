# ToDo App

## Requirements
```
python >= 3.8
```

## Getting started
```bash
git clone https://github.com/mikaelalvianrizky/todo-app-flask.git
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app
export FLASK_DEBUG=1 (if you in dev mod)
flask run
```

## Setting up MySQL
Create a `app.yaml` file in the root folder with the following content:
```yaml
runtime: python38 # or another supported version

instance_class: F1

env_variables:
  MYSQL_USER: <user_name> # please put in your credentials
  MYSQL_PASSWORD: <user_pw> # please put in your credentials
  MYSQL_DB: <database_name> # please put in your credentials
  MYSQL_HOST: <database_ip> # please put in your credentials
```
