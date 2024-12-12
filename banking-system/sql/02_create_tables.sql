DROP TABLE IF EXISTS transactions, accounts, customers, cards, atms, branches, employees, daily_transaction_summary CASCADE;
DROP TYPE IF EXISTS transaction_via CASCADE;


CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TYPE transaction_via AS ENUM ('atm', 'branch');

CREATE TABLE customers (
    customer_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE accounts (
    account_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID REFERENCES customers(customer_id),
    account_type VARCHAR(50) NOT NULL,
    balance NUMERIC(12,2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE cards (
    card_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID REFERENCES customers(customer_id),
    card_number VARCHAR(16) UNIQUE NOT NULL,
    pin VARCHAR(60) NOT NULL,
    expiration_date DATE,
    active BOOLEAN DEFAULT TRUE
);

CREATE TABLE atms (
    atm_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    location VARCHAR(100),
    status VARCHAR(50) DEFAULT 'operational'
);

CREATE TABLE branches (
    branch_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    address VARCHAR(200),
    city VARCHAR(100),
    state VARCHAR(100)
);

CREATE TABLE employees (
    employee_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    branch_id UUID REFERENCES branches(branch_id),
    full_name VARCHAR(100) NOT NULL,
    role VARCHAR(50)
);


CREATE TABLE transactions (
    transaction_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_id UUID REFERENCES accounts(account_id),
    amount NUMERIC(12,2) NOT NULL,
    transaction_type VARCHAR(50) NOT NULL CHECK (transaction_type IN ('deposit','withdrawal','transfer')),
    performed_at TIMESTAMP DEFAULT NOW(),
    performed_via transaction_via NOT NULL,
    atm_id UUID REFERENCES atms(atm_id),
    branch_id UUID REFERENCES branches(branch_id),
    destination_account_id UUID REFERENCES accounts(account_id)
);
