# AirBnB Clone Project
This project involves setting up a production environment for deploying the AirBnB Clone application using Python, Gunicorn, and Nginx. Below are the tasks completed as part of the project:

## Task 0: Set up Development with Python
In this task, I configured the Flask app in the web_flask/0-hello_route.py file to serve a simple "Hello HBNB!" message.

## Task 1: Set up Production with Gunicorn
For this task, I set up Gunicorn to serve the Flask app from Task 0 in a production environment. This involved installing and configuring Gunicorn to handle incoming requests.

## Task 2: Serve a Page with Nginx
In this task, I configured Nginx to act as a reverse proxy, forwarding requests from the /airbnb-onepage/ route to the Gunicorn app running on port 5000. The Nginx configuration file can be found in 2-app_server-nginx_config.

## Task 3: Add a Route with Query Parameters
For this task, I enhanced the Nginx configuration to handle requests on the route /airbnb-dynamic/number_odd_or_even/<int:num>, which are then proxied to the Gunicorn app running on port 5000. The Nginx configuration file can be found in 3-app_server-nginx_config.

## Task 4: Configure API to Run on Gunicorn
I configured the API from the AirBnB Clone version 3 to run on Gunicorn. The Nginx configuration file, 4-app_server-nginx_config, was adjusted to proxy requests on the AirBnB API to the corresponding Gunicorn app.

## Task 5: Serve AirBnB Clone Web App
In this task, I configured the complete AirBnB web app from AirBnB Clone version 4 to run on Gunicorn and be served through Nginx. The Nginx configuration file, 5-app_server-nginx_config, was updated to serve the static assets from web_dynamic/static/ on the Gunicorn AirBnB app.

## Task 6: Deploy with Upstart Script
For this task, I created a Gunicorn configuration file gunicorn.conf that includes an Upstart script. This script starts a Gunicorn process bound to port 5003, serving the content from Task 5. The Gunicorn process spawns three worker processes and logs errors to /tmp/airbnb-error.log while recording access to /tmp/airbnb-access.log.

## Task 7: No Service Interruption
To ensure smooth updates, I implemented a Bash script, 4-reload_gunicorn_no_downtime, that gracefully reloads Gunicorn, minimizing service interruption during updates.
