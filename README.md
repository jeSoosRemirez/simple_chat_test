###Before usage run migrations:
    $ python manage.py makemigrations threads
    $ python manage.py makemigrations users
    $ python manage.py migrate

###To load test data use:
    $ python manage.py loaddata users_test.json
    $ python manage.py loaddata threads_test.json
    $ python manage.py loaddata messages_test.json

###To run server:
    $ python manage.py runserver

##URLs and JSONs:
    /admin/
    django admin panel
###Users:
    POST
    /register/
    register a user
    {
      "first_name": "test",
      "last_name": "test",
      "email": "test2@mail.com",
      "password": "Pass1234"
    }
    

    POST
    /login/
    login a user
    Same JSON as for /register/
    !!!returns a JWT token to use application!!!

###Threads and Messages:
    FOR EVERY REQUEST TOKEN MUST BE PROVIDED!

    GET
    /threads/
    returns list of threads
    
    POST
    /threads/
    creates a thread
    {
        "header": "thread_name"
    }
    
    DELETE
    /threads/<thread_id>/
    deletes a thread


    GET
    /threads/<thread_id>/messages/
    returns a list of messages in thread

    POST
    /threads/<thread_id>/messages/
    creates a message in thread
    {
        "text": "text of message"
    }

    
    

##Usage:
To test project you can use "Postman".
In authorisation set BearerToken and provide a token from `/login/` url
