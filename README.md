[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/sTPm8XwT)
# ml-pipeline
# Tech Shop Database

This project contains scripts for managing a MongoDB database for a tech shop. The database includes collections for users, products, and transactions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3
- MongoDB
- pymongo library

### Installing

1. Clone the repository
2. Install the pymongo library using pip:

```bash
pip install pymongo
```
### Running the scripts
To run the scripts, navigate to the directory containing the script you want to run and execute the following command: 

``` bash
pyton script_name.py
```

Replace script_name.py with the name of the script you want to run

### Scripts

| Script | Description |
| --- | --- |
| [aggregate.py](https://github.com/ALU-BSE/databases-sql-GichuriNdungu/blob/main/aggregate.py) | This script uses mongodbs aggregation framework to count the number of products listed by each user |
| [create.py](https://github.com/ALU-BSE/databases-sql-GichuriNdungu/blob/main/create.py) | This script initites a connection to the Mongo db cluster, creates a database (tech_shop) and populates the db with the correct collections and subsequent documents|
| [popular_products.py](https://github.com/ALU-BSE/databases-sql-GichuriNdungu/blob/main/popular_products.py) | This script aggregates and sorts the transactions with respect to the products bought. Products are then listed from most popular down to the least popular|
| [products_update.py](https://github.com/ALU-BSE/databases-sql-GichuriNdungu/blob/main/products_update.py) | This script deletes the initial insertion into the products document, then updates the document with a set of new products |
| [spending.py](https://github.com/ALU-BSE/databases-sql-GichuriNdungu/blob/main/spending.py) | This script calculates how much each user spent in purchases |
| [transactions_update.py](https://github.com/ALU-BSE/databases-sql-GichuriNdungu/blob/main/transactions_update.py) | This script updates the transactions document by randomly generating assigning transactions to each of the users |

### Authors
- Martin Ndungu