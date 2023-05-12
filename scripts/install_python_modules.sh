#!/bin/bash

echo "Make sure Docker is running..."

echo "Build extended docker image.."
docker build . --tag extending_airflow:latest

echo "Update image name..."
sed -i 's/-apache\/airflow:2.6.0/-extending_airflow:latest/g' docker-compose.yaml

echo "Rebuild airflow webserver, airflow scheduler..."
docker-compose up -d --no-deps --build airflow-webserver airflow-scheduler