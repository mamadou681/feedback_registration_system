# feedback_registration_system
This project is a feedback registration system where the users can submit a form through the frontend side and  the data will pass a whole process to get to the database.

# To run this Project

1. you need to have Docker installed
2. And run **docker pull debian** 
3. clone this repo: git clone **https://github.com/mamadou681/feedback_registration_system.git**
4. run : **docker compose up**

# Description

The fontend side is on [http://localhost:80](http://localhost:80) with the nginx web server.
To implement the backend I use python(Tornado) where we get the data from the frontend side and send it to the queue service (rabbitmq).
The backend side is on [http://localhost:8888](http://localhost:8888) and the message broker is on [http://localhost:15672](http://localhost:15672).
In order to get the data from the queue service(rabbitmq) and send it to the database(postgresql) I use python(Fastapi). Fastapi is on  [http://localhost:5002](http://localhost:5002).
To send the data to the database you need just to go the url: [http://localhost:5002/fetchdata](http://localhost:5002/fetchdata) . 
**The database credentials are:**
* host: localhost
* port: 5432
* user: pgadmin
* password: admin
* database: pgdb.

In the terminal you can run: **psql -h localhost -p 5432 -U pgadmin -W pgdb** to get access to the database.

# Tools used
- Docker (debian image)
- Jquery
- Python(Tornado)
- Rabbitmq
- python(FastApi)
- SqlAlchemy
- Pydantic
- Postgresql











