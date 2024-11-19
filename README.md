# backend

Link to database design: https://drive.google.com/file/d/1BxUF6cSr11s3BiKVhRrI3o_O1tWd-P0E/view?usp=sharing
Note that you can comment there so feel free to do it.

Paginagion was not implemented, in an ideal world we would like to have pagination (both on FE and BE) 
but becasue of lack of time I didn't implement it.

To init the DB:
1. Start the docker (you have a docker file). DB is MySQL 8.
2. Run manually the migrations (Create tables and inserts) which are located in migrations folder. (In a perfect world it can be handle by a CI/CD.
