# Work 2

## Create a docker image

- create html folder
- create index.html file into html folder
-create Dockerfile

- docker build -t sbm-nginx-app-2 .

- docker images

- docker run -d -p 8082:82 sbm-nginx-app-2

- docker ps -a

- docker cp nginx.conf 533d349e4c37:/etc/nginx/nginx.conf

- docker logs 533d349e4c37

- docker restart 533d349e4c37

- docker exec -it 533d349e4c37 /bin/bash


open the browser with: http://localhost:8082

## If the image is to be deleted

- docker images

- docker rmi sbm-nginx-app-2

## If you want to check running docker containers

- docker ps -a

- docker stop [container-id]

- docker rm [container-id]