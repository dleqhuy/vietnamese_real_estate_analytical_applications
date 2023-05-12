#!/bin/bash

echo "Init database for Airflow metadata..."
docker-compose up airflow-init

echo "Starting up airflow in detached mode..."
docker-compose up -d

echo "Airflow started successfully!"