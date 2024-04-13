### Making the CRUD app work via the Docker PWD
---
1. Upload zip file
2. Unzip zip file
3. Run `docker-compose up --build -d` to build image, create and start container in detached mode. 
4. Check if 2 containers have started, using `docker ps -a`.
5. Interact with the containers using exec command and open up a shell in interactive, terminal mode. `docker exec -it dj-web-app-container bash`
6. Need to migrate the db in order to make it work. Run the `python manage.py migrate` cmd in bash shell CLI. 
7. Exit out of container.
