# DjangoRabbitMQ
A simpleproject where quotes created at the Quotes project are passed as messages using RabbitMQ and appropiate operations done on them at the receiving end, the Likes project.

The Home project is used to demonstarate how to use the two APIs in a single web page.

### Running the project...
1. ####The Quotes project
   Cd into Quotes
   
   Run python manage.py makemigrations
   
   Run python manage.py migrate
   
   Run python manage.py createsuperuser
   
   Run python consumer.py
   
  
2. ###The Likes project

    Cd into Likes
   
   Run python manage.py makemigrations
   
   Run python manage.py migrate
   
   Run python manage.py createsuperuser.Create a superuser similar to the one above. 
   
   Run python consumer.py
   
3.Communication
  Make sure you have RabbitMQ and pika installed.
  
  Start the server by running `sudo service rabbitmq-server start` if on linux
  
  There are also instructions for [Windows](https://www.rabbitmq.com/install-windows-manual.html) and [Mac](https://www.rabbitmq.com/install-homebrew.html) users.
  
  Create edit or delete quotes on Quotes project and similar opertaions happen at the Likes project.
  
  
   
 4. ###The Home project

     Run python manage.py makemigrations
   
     Run python manage.py migrate
     
     Run python manage.py runserver

