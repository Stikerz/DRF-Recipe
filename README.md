# Recipe DRF


## Setup:

- Create virtualenv(Optional) using python 3.6
- Run pip install -r requirements.txt
- Run python manage.py makemigrations
- Run python manage.py migrate
- Run python manage.py createsuperuser
- Run python manage.py runserver # Now go to localhost:8000

## Endpoints
- Create : /api/recipes/create/ 
- Update : /api/recipes/<ID>/update 
- List : /api/recipes/ 
- Delete : /api/recipes/<ID>/delete 

## Testing
- Run python manage.py test api.tests # Run test

