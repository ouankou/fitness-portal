# fitness-portal
Group project

Go to `docker/` located inside project root.
- To Simply run the project
`docker-compose build`
`docker-compose up`

- To migrate
`docker-compose run app python3 fitness-portal/manage.py makemigrations portal`
`docker-compose run app python3 fitness-portal/manage.py migrate`

- To access MySQL cmd
`docker-compose run db mysql -h service.mysql -uroot -p1234`