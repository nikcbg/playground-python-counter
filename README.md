# playground-python-counter

### Purpose of the repository
- The repository is for web counter writen in Python3.7 that prints a number from Redis database each time when you visit/refresh the page.

---------------------------------------------------------------------------------------------------------------------------

### List of files in the repository
File name |	File description
----------|--------------------
Vagrantfile |  the file describes the VM machine required for this project, and how to configure and provision it. 
conf/redis.conf | redis database configuration file.
scripts/provision.sh | provision script for redis database.
redis_db/db.py | python code that establishes conection to redis database and stores counter values. 
web.py | imports `db.py` file as module and diplays counter values on a web page.

--------------------------------------------------------------------------------------------------------------------------

### How to use this repository 
- Install `vagrant` by following this [instructions](https://www.vagrantup.com/downloads.html).
- Clone the repository to your local computer: `git clone git@github.com:nikcbg/playground-python-counter.git`.
- Go to the cloned repo on your computer: `cd playground-python-counter`.
- Next execute `vagrant up` command to start the VM that is hosting the redis database. 
- Next execute `python3.7 web.py` command to.
- Next open a web browser and type `192.168.101.45:8082` which is the redis VM IP address and port.
- Next refresh the web page couple of times to see if the web page displays a diferent number after every refresh.
