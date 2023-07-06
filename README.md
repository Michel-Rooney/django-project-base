# Django Project Base

## Create the virtual environment
```python
# Linux
python3 -m venv environment

# Windows
python -m venv environment
```

## Activate the virtual environment
```python
# Linux
source environment/bin/activate

# Windows
./venv/Scripts/activate
```

## Install dependencies
```python
(environment) pip install -r requirements.txt 
```

## Create your .env
In the ".env-example" file make a copy of the file with the name ".env" and generate a django secret key using the command:
```python
python -c "import string as s;from random import SystemRandom as sr;print(''.join(sr().choices(s.ascii_letters + s.punctuation, k=64)))"
```

## Run the Server
```python
(environment) python manage.py runserver
```