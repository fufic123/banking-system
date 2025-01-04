# Banking System API

This project is a **Banking System API** built with Python's FastAPI framework and plain SQL for database interactions. The system supports various operations for managing accounts, ATMs, branches, customers, employees, cards, and transactions.

## Features

The API includes the following functionality:

### Accounts
- **List all accounts**: `GET /accounts/`
- **Get account by ID**: `GET /accounts/{account_id}`
- **Create a new account**: `POST /accounts/`
- **Update an account**: `PUT /accounts/{account_id}`
- **Delete an account**: `DELETE /accounts/{account_id}`

### ATMs
- **List all ATMs**: `GET /atms/`
- **Get ATM by ID**: `GET /atms/{atm_id}`
- **Create a new ATM**: `POST /atms/`
- **Update an ATM**: `PUT /atms/{atm_id}`
- **Delete an ATM**: `DELETE /atms/{atm_id}`

### Branches
- **List all branches**: `GET /branches/`
- **Get branch by ID**: `GET /branches/{branch_id}`
- **Create a new branch**: `POST /branches/`
- **Update a branch**: `PUT /branches/{branch_id}`
- **Delete a branch**: `DELETE /branches/{branch_id}`

### Cards
- **List all cards**: `GET /cards/`
- **Get card by ID**: `GET /cards/{card_id}`
- **Create a new card**: `POST /cards/`
- **Update a card**: `PUT /cards/{card_id}`
- **Delete a card**: `DELETE /cards/{card_id}`

### Customers
- **List all customers**: `GET /customers/`
- **Get customer by ID**: `GET /customers/{customer_id}`
- **Create a new customer**: `POST /customers/`
- **Update a customer**: `PUT /customers/{customer_id}`
- **Delete a customer**: `DELETE /customers/{customer_id}`

### Employees
- **List all employees**: `GET /employees/`
- **Get employee by ID**: `GET /employees/{employee_id}`
- **Create a new employee**: `POST /employees/`
- **Update an employee**: `PUT /employees/{employee_id}`
- **Delete an employee**: `DELETE /employees/{employee_id}`

### Transactions
- **List all transactions**: `GET /transactions/`
- **Get transaction by ID**: `GET /transactions/{transaction_id}`
- **Create a new transaction**: `POST /transactions/`
- **Update a transaction**: `PUT /transactions/{transaction_id}`
- **Delete a transaction**: `DELETE /transactions/{transaction_id}`

