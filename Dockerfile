FROM python:3.7-slim

COPY . /app
WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    python3-dev \
    python3-setuptools \
    gcc \
    make

# Create a virtual environment in /opt
RUN python3 -m venv /opt/venv

# RUN apt-get install libpq-dev 

# Install requirments to new virtual environment
RUN /opt/venv/bin/pip install -r requirements.txt


# purge unused
RUN apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# make entrypoint.sh executable

WORKDIR /app/src

RUN chmod +x entrypoint.sh


CMD [ "./entrypoint.sh" ]

