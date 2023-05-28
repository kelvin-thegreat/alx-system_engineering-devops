Infrastructure Design

Server 1
Web Server - Nginx
Firewall

Server 2
Application Server
Firewall

Server 3
Database - MySQL (Primary-Replica cluster)
Firewall
Load Balancer Cluster
HAproxy load balancer (configured as a cluster with another load balancer)

Additional Components
Firewalls - Added for enhanced security by controlling network traffic.
Load Balancer Cluster - Implemented for load distribution and high availability.
Split Components - Separated web server, application server, and database onto individual servers for better scalability, resource management, and isolation.

Specifics
Web Server (Nginx) - Handles incoming HTTP requests and serves static content efficiently.
Application Server - Executes application logic and processes dynamic requests.
Database (MySQL Primary-Replica cluster) - Ensures data integrity and availability with replication.

Reasoning for Additional Elements
Firewalls - Protect the infrastructure by filtering and blocking unauthorized network traffic.
Load Balancer Cluster - Distributes incoming traffic among multiple servers to improve performance and ensure high availability.
Split Components - Separating components onto dedicated servers allows for better resource allocation, scalability, and isolation. It also helps to optimize the performance of each component individually.
Thus, This design assumes that the cluster configuration of HAproxy load balancer is set up with at least one additional load balancer to provide redundancy and fault tolerance.

Issues with the Design

Single Point of Failure (SPOF) - Load Balancer Cluster
Failure of both load balancers can disrupt traffic distribution, impacting availability.

Network Bottlenecks and Complexity
Separating components onto different servers can introduce network bottlenecks and increase overall complexity, affecting performance and management.
