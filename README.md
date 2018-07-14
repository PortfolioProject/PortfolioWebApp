# PorfolioDisplay
This app displays your portfolio of stocks.

### How to run
- Clone the repository
- ```cd ./portfolio```
- Run the database migration using ```python manage.py migrate```. We use a sqlite3 database for development.
- Create a superuser using ```python manage.py createsuperuser```
- There are a couple of _fixtures_ in place for the database migrations. Run them using ```python manage.py loaddata 
<fixture_names>```
- Start the webserver using ```python manage.py runserver```


**Note:** The provided docker-compose is a work in progress, and will be made available once the code moves to using 
Postgresql.