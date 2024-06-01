
   # Use the official Nginx image from the Docker Hub
   FROM nginx:alpine

   # Copy the static website files to the Nginx web root directory
   COPY . /usr/share/nginx/html

   # Expose port 80
   EXPOSE 80
