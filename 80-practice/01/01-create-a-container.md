# Work 1

## Create a docker image

- create html folder
- create index.html file into html folder
-create Dockerfile

- docker build -t sbm-nginx-app-1 .

- docker images

- docker run -d -p 8081:80 sbm-nginx-app-1

open the browser with: http://localhost:8081

## If the image is to be deleted

- docker images

- docker rmi sbm-nginx-app-1

## If you want to check running docker containers

- docker ps -a

- docker stop [container-id]

- docker rm [container-id]