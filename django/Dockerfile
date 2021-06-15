FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED 1
RUN useradd --uid 1001 --create-home --shell /bin/sh -G sudo,root appuser && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    mkdir /code
USER appuser
ENV PATH $PATH:/home/appuser/.local/bin
WORKDIR /code
COPY ./django/code/requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY ./django/code .
