Infrastructure Design:

Server 1:

Web Server - Nginx
Application Server
Application Files
Firewall

Server 2:

Application Server
Application Files
Firewall

Server 3:

Load Balancer - HAproxy
Database - MySQL (Primary-Replica cluster)
Firewall

Additional Components

SSL Certificate - Added for secure HTTPS communication.
Firewalls - Enhance security by controlling network traffic.
Monitoring Clients - Collect data for monitoring services.

Specifics

Firewalls
Provide security by filtering network traffic.

HTTPS
Ensures secure communication with encryption.

Monitoring
Tracks infrastructure performance and health.

Data Collection
Monitoring clients collect data for analysis.
Web Server QPS: Monitor request rates and response times.

Issues

Terminating SSL at load balancer
Increases load and reduces end-to-end encryption.

Single MySQL server accepting writes
Single point of failure and potential downtime.

Identical component servers
Limited scalability and resource utilization.
