# Pull the minimal Ubuntu image
FROM debian:11

LABEL Name=callregistrationsystem Version=0.0.1

WORKDIR /frontend
# Install Nginx
RUN apt-get -y update && apt-get -y install nginx

# Copy the website files
COPY .  /usr/share/nginx/html
# Copy the Nginx config
COPY default /etc/nginx/sites-available/default

# Expose the port for access
EXPOSE 80/tcp

# Run the Nginx server
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]

