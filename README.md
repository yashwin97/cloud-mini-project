# cloud-mini-project
Cloud Computing Mini-Project
 
 A movies database API which retrieves movie information from an external API [open movie database]. The app also has an internal API which links to a database of movies from Netflix where you have the ability to view, delete and add movies to the existing entries in the database using their title’s, through the app.

Built With :
Python – Flask
Cassandra
Docker
AWS-EC2 Instance
Encryption and Security – SSL

API:
GET – 
1)	Movie Description from the external API :
curl -k url/movies?title=""
2)	Movie from the Cassandra Database:
curl -k url/movies/<title>

DELETE –
Delete existing movie entry in the database :
curl -k -X  "DELETE url/movies?title=""

POST-
Add an entry to the Database-
curl -k -X POST url/new?title=""

INSTALLATION AND DEPLOYMENT :
Steps followed to create the project :
1)	Used AWS-t2.medium instance[ubuntu 16] 
2)	Created requirements.txt and Dockerfile
3)	Pulled and ran a Cassandra instance inside docker
4)	Copied the movies.csv file to the Cassandra instance
5)	Created a keyspace inside Cassandra to use named movies :
CREATE KEYSPACE movies WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1};
Created Table movies.list with Title Primary Key and 2 columns : duration and release_year
Copied the data from movies.csv into movies.list
6)	Created app.py containing our python code with Flask
7)	Added SSL HTTPS encryption using Self-Signed Certificates 
8)	Build and run through docker


Self-Signed Certificate command to obtain cert.pm and key.pm
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
