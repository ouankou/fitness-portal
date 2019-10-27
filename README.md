# fitness-portal
Group project

Go to `docker/` located inside project root.
- To Simply run the project
```bash
sudo docker-compose build
sudo docker-compose up
```

- To migrate
```bash
sudo docker-compose run app python3 fitness-portal/manage.py makemigrations portal
sudo docker-compose run app python3 fitness-portal/manage.py migrate
```

- To access MySQL cmd
```bash
sudo docker-compose run db mysql -h service.mysql -uroot -p1234
```

- To access the application

Go to the link `localhost:8000` in the browser.
