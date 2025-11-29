
# Coffee Shop Domain Modeling

## Project Overview

This project models a simple **Coffee Shop domain** using **object-oriented programming** in Python.
It consists of three main entities:

* `Customer` — represents a coffee shop customer
* `Coffee` — represents a coffee item
* `Order` — represents a purchase made by a customer for a specific coffee

The relationships are as follows:

* A **Customer** can place many **Orders**.
* A **Coffee** can be part of many **Orders**.
* An **Order** belongs to exactly one **Customer** and one **Coffee**.
* Customers and Coffees have a **many-to-many relationship** through Orders.

---

## Features Implemented

### Customer Class

* Initialize with a `name` (string, 1–15 characters)
* Properties with validation:

  * `name`
* Methods:

  * `orders()` → list of all orders placed by this customer
  * `coffees()` → list of unique coffees ordered
  * `create_order(coffee, price)` → create a new order
* Class method:

  * `most_aficionado(coffee)` → returns the customer who spent the most on a given coffee

### Coffee Class

* Initialize with a `name` (string, at least 3 characters)
* Properties with validation:

  * `name`
* Methods:

  * `orders()` → list of all orders for this coffee
  * `customers()` → unique list of customers who ordered this coffee
  * `num_orders()` → total number of orders
  * `average_price()` → average price across all orders

### Order Class

* Initialize with `customer` (Customer), `coffee` (Coffee), and `price` (1.0–10.0)
* Properties with validation:

  * `customer`
  * `coffee`
  * `price`
* Tracks all orders using `Order.all_orders` for querying relationships

---

## Project Setup

1. Create a project directory, e.g., `coffee_shop`
2. Navigate to the project directory in your terminal
3. Set up a Python virtual environment using pipenv:

```bash
pipenv install
pipenv shell
```

4. Install `pytest` for testing:

```bash
pipenv install --dev pytest
```

5. Save the class files (`customer.py`, `coffee.py`, `order.py`) in the project directory

---

## Running a Demo

A `debug.py` file is provided for testing and demonstration:

```bash
python debug.py
```

The demo will:

* Create customers and coffees
* Place orders
* Show coffee order statistics
* Show the top customer for a given coffee

---

## Running Tests

Unit tests are provided in the `tests/` directory:

```bash
pytest
```

Tests cover:

* Property validation (name, price, types)
* Order creation
* Relationship methods (`orders()`, `coffees()`, `customers()`)
* Aggregate methods (`num_orders()`, `average_price()`)
* Class method `most_aficionado()`

---

## Exception Handling & Validation

The project validates all inputs and raises exceptions:

* `TypeError` for incorrect types
* `ValueError` for invalid value ranges
* Ensures names and prices follow the assignment requirements

---

## Project Structure

```
coffee_shop/
│
├── customer.py       # Customer class
├── coffee.py         # Coffee class
├── order.py          # Order class
├── debug.py          # Demo script
├── tests/
│   ├── test_customer.py
│   ├── test_coffee.py
│   └── test_order.py
└── README.md         # Project documentation
```

---

## Notes

* All orders, customers, and coffees are tracked in-memory for this project
* The design follows **object-oriented principles**:

  * Encapsulation
  * Relationships through properties and class-level storage
  * Aggregate methods for computations
* The project is ready for extension to persistent storage if required

---

## Author

Peter Emu
