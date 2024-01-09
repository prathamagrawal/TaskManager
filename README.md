<h1 align="center">Task Manager</h1>
<hr>
<div align="center">
<img width="1367" alt="image" src="https://github.com/prathamagrawal/TaskManager/assets/58286330/d6140c5a-5a10-47eb-8f67-5f5a458d520a">
</div>


<h3>Prerequisites:</h3>
<ol>
  <li>Python (>=3.9) and Npm should be installed. </li>
  <li>For database connectivity, MySQL server should be set up. </li>
  <li>Docker should be installed </li>
</ol>

<h2>Instructions to run the project: </h2>

<h3>To set up a local copy:</h3>

Clone the repository <br>    ```git clone https://www.github.com/prathamagrawal/taskmanager.git``` <br>
Move into the directory <br> ```cd taskmanager```<br>
<h4>Setup backend </h4>

```cd backend```

1. Python Environment setup
```
pip install virtualenv
virtualenv py39
source py39/bin/activate
```
2. Installing Requirements
```
pip install -r requirements.txt
```
in case of error while installing mysqlclient, run the following command
```
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

3. Changing the SQL Database configuration to your personal configuration <br>
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'demo',
        'USER':'demo',
        'HOST':'demo',
        'PASSWORD':'demo',
        'PORT':demo,
    }
}
```
Make sure to change the NAME, USER, HOST, PASSWORD and PORT for the Mysql Connection
4. Migrating and running the python server
```
python manage.py makemigration
python manage.py migrate
python manage.py runserver 8001
```

<h4>Setup Frontend </h4>

```cd frontend```
1. Install dependencies
   ```npm install```
2. starting the node server
   ```npm start```

<hr>

<h2>To Deploy following application using Docker: </h2>
Make sure you have docker installed using the following command: <br>

```docker```<br>
this will help you with all the valid arguements and valid configurations. <br>
```docker ps -a```<br>
The above command will give you a list of docker containers running, along with their status. <br>

<h3>To deploy the application using docker: </h3>

1. Change the host name in the ```settings.py``` in the django server to <b>db</b>
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'demo',
        'USER':'demo',
        'HOST':'db',
        'PASSWORD':'demo',
        'PORT':3306,
    }
}
```

2. Running the docker-compose command to build the docker and run the docker
```
docker-compose up -d
docker-compose up
```

3. To access the server go to ```localhost:3000```

<hr>
