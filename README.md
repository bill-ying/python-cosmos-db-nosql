# Cosmos DB (NoSQL) Management Scripts with Python
This is a proof of concept (POC) project.  The repository contains scripts to manage an Azure Cosmos DB (NoSQL) instance, including creating databases and containers, seeding data, and manipulating data using Python.

## Prerequisites
- Azure CLI installed
- Azure Cosmos DB Python SDK installed (pip install azure-cosmos)
- Azure subscription
- Azure resource group
- Azure Cosmos DB account

## Using CLI to Create Database and Container
- create_db_container.sh

This script uses Azure CLI to create a Cosmos DB database and container. Ensure you have an Azure subscription, resource group, and Cosmos DB account. 

## Seed Data and Update
- seed_data.py

This script loads initial data into the Cosmos DB container and updates existing data.

Usage:

Ensure you have the Azure Cosmos DB Python SDK installed:
- pip install azure-cosmos

Run the script:
- python seed_data.py

## Manipulate Data (Read and Delete)
- manipulate_data.py

This script reads and prints the names of students taking a specific course and deletes a specified student.

Usage:

Ensure you have the Azure Cosmos DB Python SDK installed:
- pip install azure-cosmos

Run the script:
- python manipulate_data.py