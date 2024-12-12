-- Insert initial data
-- Note: We do not need to insert accounts or cards manually for a new customer because
--       the trigger will handle that automatically upon customer insertion.

INSERT INTO customers (full_name, email, phone)
VALUES ('John Doe', 'john@example.com', '123456789'),
       ('Jane Smith', 'jane@example.com', '987654321');

-- Insert ATMs
INSERT INTO atms (location) VALUES ('Downtown'), ('Airport'), ('Mall');

-- Insert branches
INSERT INTO branches (address, city, state) VALUES
('123 Main St', 'Metropolis', 'NY'),
('456 High St', 'Gotham', 'NJ');

-- Insert employees
-- Link them to branches. For simplicity, use the first returned branch for each:
INSERT INTO employees (branch_id, full_name, role)
SELECT branch_id, 'Alice Manager', 'Manager' FROM branches LIMIT 1;

INSERT INTO employees (branch_id, full_name, role)
SELECT branch_id, 'Bob Teller', 'Teller' FROM branches LIMIT 1;

INSERT INTO employees (branch_id, full_name, role)
SELECT branch_id, 'Charlie Admin', 'Admin' FROM branches LIMIT 1 OFFSET 1;

-- After inserting customers, the trigger will create their accounts and card.
-- If needed, you can insert transactions here once you have actual account_ids retrieved.
