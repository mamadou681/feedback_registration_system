# For more information, please refer to https://aka.ms/vscode-docker-python
FROM debian:11

RUN apt-get update -y

RUN apt-get install -y python3

RUN apt-get install -y python3-pip

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

WORKDIR /servicedb
COPY . /servicedb

# Creates a non-root user with an explicit UID and adds permission to access the /servicedb folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /servicedb
USER appuser

EXPOSE 5002
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:5002", "servicedb.app:servicedb"]
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=5002"]
