FROM debian:11

LABEL Name=callregistrationsystem Version=0.0.1

WORKDIR /rabbit_install

#Copy cloudsmith

COPY cloudsmith.sh cloudsmith.sh

# make cloudsmith.sh executable
RUN chmod u+r+x  cloudsmith.sh

# Install rabbitmq
RUN . ./cloudsmith.sh

RUN rabbitmq-plugins enable rabbitmq_management

ENV RABBITMQ_PID_FILE /var/lib/rabbitmq/mnesia/rabbitmq

COPY inituser.sh /inituser.sh

RUN chmod u+r+x /inituser.sh

# ENV RABBITMQ_USER user
# ENV RABBITMQ_PASSWORD user
# For RabbitMQ
EXPOSE 5672

# For RabbitMQ Admin
EXPOSE 15672

# COPY rabbitmq.conf /etc/rabbitmq/rabbitmq.conf
CMD ["/inituser.sh"]