# My First Django To-Do App

### Description
This is my first real go at a full-stack Django application.  I decided to go with something that seemed useful and relatively simple.  This application uses a vanilla javascript frontend with a Django and postgres backend.
___
### Prerequisites
This project requires the following:
* Python 3.10+
* Docker
___
### Instructions
Currently this project can only be run directly on the host.  
1. Modify create your own .env if you would like to replace environment variables in the *docker-compose.yml* file.
2. Deploy the postgres container using the *docker-compose.yml* file. 
   1. `docker-compose up -f docker-compose.yml`
3. The server will be listening on `localhost:1337`
___
### Future Plans
The goal for this project is to a completely containerized application that is deployed and managed with a single docker-compose command.  In terms of project features, I plan to add:
1. DONE ~~Add/Modify/Delete Action Items~~ 
2. ~~Daily, Weekly, and Monthly To-Do sections~~
3. ~~Multi-user support~~
4. AWS EC2 + Route53 deployment
