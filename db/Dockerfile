FROM debian:11


# Update the debian and PostgreSQL repository indexes and install ``python-software-properties``,
# ``software-properties-common`` and PostgreSQL 12
WORKDIR /db
RUN apt-get update && apt-get -y -q install software-properties-common \
    && apt-get -y -q install postgresql postgresql-client postgresql-contrib

USER postgres

RUN /etc/init.d/postgresql start \
    && psql --command "CREATE USER pgadmin WITH SUPERUSER PASSWORD 'admin';" \
    && createdb -O pgadmin pgdb

USER root

# Adjust PostgreSQL configuration so that remote connections to the
# database are possible.
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/13/main/pg_hba.conf

# And add ``listen_addresses`` to ``/etc/postgresql/13/main/postgresql.conf``
RUN echo "listen_addresses='*'" >> /etc/postgresql/13/main/postgresql.conf

# Expose the PostgreSQL port
EXPOSE 5432

RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

USER postgres

# Set the default command to run when starting the container
CMD ["/usr/lib/postgresql/13/bin/postgres", "-D", "/var/lib/postgresql/13/main", "-c", "config_file=/etc/postgresql/13/main/postgresql.conf"]