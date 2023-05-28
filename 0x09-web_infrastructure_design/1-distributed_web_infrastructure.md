The three-server web infrastructure that hosts the website www.foobar.com. 

 components and their roles:
Server 1
Web Server - Nginx
Application Server
Application Files (Code Base)

Server 2:
Application Server
Application Files (Code Base)

Server 3:
Load Balancer - HAproxy
Database - MySQL (Primary-Replica cluster)

The specifics of the infrastructure

Additional Servers
Two additional servers are added to distribute the load and improve performance and redundancy.

Load Balancer (HAproxy)
The load balancer acts as an intermediary between the clients and the servers. It distributes incoming traffic across multiple servers to achieve better resource utilization and high availability. 

Distribution Algorithm
The load balancer is configured with a distribution algorithm, such as round-robin, which cyclically distributes requests to each server in a sequential manner. In case of the three servers, the load balancer will route the first request to Server 1, the second request to Server 2, and the third request to Server 3, and then repeat the cycle.

Active-Active vs. Active-Passive Setup
In this infrastructure, the load balancer enables an Active-Passive setup. In an Active-Active setup, all servers actively handle requests simultaneously. In an Active-Passive setup, only one server actively handles requests while the others remain passive. The load balancer directs traffic to the active server, and if the active server fails, the load balancer switches to the passive server. This setup ensures high availability by quickly recovering from server failures.

Database Primary-Replica Cluster
The database is configured as a Primary-Replica (Master-Slave) cluster. The Primary node is the main database server that handles read and write operations. The Replica nodes are synchronized copies of the Primary node, used for read-only operations and backup purposes.

Primary-Replica Cluster Working
When a write operation occurs, it is performed on the Primary node. The Primary node then replicates the changes to the Replica nodes, ensuring data consistency. 

Difference between Primary and Replica Nodes
The Primary node handles write operations and is responsible for maintaining the authoritative copy of the data. The Replica nodes handle read-only operations and serve as backup servers. The application typically interacts with the Primary node for write operations and can interact with any Replica node for read operations, distributing the load across the Replica nodes.

 Issues with this infrastructure

Single Points of Failure (SPOFs)
While this infrastructure has improved redundancy, certain components can still be SPOFs. For example, if the load balancer or the database's Primary node fails, it can disrupt the availability of the website.

Security Issues
The infrastructure lacks certain security measures, such as a firewall and HTTPS (SSL/TLS encryption). Without a firewall, the servers may be vulnerable to unauthorized access or attacks. The absence of HTTPS exposes user data to interception or tampering. Implementing a firewall and enabling HTTPS are important for securing the infrastructure.

Monitoring
The infrastructure lacks monitoring capabilities, making it difficult to identify performance issues, server failures, or anomalies. Monitoring tools and practices should be implemented to proactively detect and address issues, ensuring the reliability and availability of the website.
