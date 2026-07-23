# Comprehensive Guide to MySQL Constraints

This document outlines the core constraints and related attributes used in MySQL to enforce data integrity and business rules.

---
## 🛡️ The 6 Core MySQL Constraints
**MySQL uses six primary constraints** to enforce data integrity and specify rules for the data allowed in your tables.

* **PRIMARY KEY**
    * **Definition:** Uniquely identifies each record in a table. It is a strict combination of `NOT NULL` and `UNIQUE` properties. A table can only have one primary key.
    * **Syntax:** `PRIMARY KEY (column_name)`
    * **Example:**
``` sql
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50)
);
```

* **FOREIGN KEY**
    * **Definition:** Links two tables together. It matches a primary key in another table to maintain referential integrity and prevent orphaned records.
    * **Syntax:** `FOREIGN KEY (column_name) REFERENCES other_table(column_name)`
    * **Example:**
``` sql
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
```

* **UNIQUE**
    * **Definition:** Guarantees that all values in a column or a group of columns are distinct from one another. Unlike PRIMARY KEY, it does allow `NULL` values.
    * **Syntax:** `UNIQUE (column_name)`
    * **Example:**
``` sql
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);
```

* **NOT NULL**
    * **Definition:** Restricts a column from accepting `NULL` values, forcing the column to always contain a valid value during inserts and updates.
    * **Syntax:** `column_name data_type NOT NULL`
    * **Example:**
``` sql
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL
);
```

* **CHECK**
    * **Definition:** Evaluates a specific boolean condition before inserting or updating data. (Enforced natively in MySQL 8.0.16 and later).
    * **Syntax:** `CHECK (condition)`
    * **Example:**
``` sql
CREATE TABLE Persons (
    person_id INT PRIMARY KEY,
    age INT,
    CHECK (age >= 18)
);
```

* **DEFAULT**
    * **Definition:** Provides a fallback value for a column when no value is explicitly provided in an `INSERT` statement.
    * **Syntax:** `DEFAULT default_value`
    * **Example:**
``` sql
CREATE TABLE Accounts (
    account_id INT PRIMARY KEY,
    status VARCHAR(20) DEFAULT 'Active'
);
```

---

## ⚙️ Related Attributes (Often Grouped with Constraints)

While not strictly categorized as standard relational database constraints under the SQL standard, the following mechanisms also restrict or rule column behavior in MySQL:

* **AUTO_INCREMENT**
    * **Definition:** Automatically generates a unique, sequential integer for new rows. Typically used alongside the PRIMARY KEY constraint.
    * **Syntax:** `AUTO_INCREMENT`
    * **Example:**
``` sql
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50)
);
```

* **ENUM / SET**
    * **Definition:** Limits the allowable data inputs to an explicit list of predefined string values. ENUM allows one choice, while SET allows zero or more choices.
    * **Syntax:** `ENUM('val1', 'val2')` or `SET('val1', 'val2')`
    * **Example:**
``` sql
CREATE TABLE Tasks (
    task_id INT PRIMARY KEY,
    priority ENUM('Low', 'Medium', 'High')
);
```

---

#### Comparison of Levels

| Constraint      | Column-Level Support | Table-Level Support | Multi-Column Support |
| --------------- | -------------------- | ------------------- | -------------------- |
| **PRIMARY KEY** | Yes                  | Yes                 | Yes (Composite Key)  |
| **FOREIGN KEY** | Yes                  | Yes                 | Yes                  |
| **UNIQUE**      | Yes                  | Yes                 | Yes                  |
| **NOT NULL**    | Yes                  | No                  | No                   |
| **CHECK**       | Yes                  | Yes                 | Yes                  |
| **DEFAULT**     | Yes                  | No                  | No                   |

---

#### How to Check Existing Constraints

You can see all active constraints on a specific table using this command in your client:
```sql
SHOW CREATE TABLE your_table_name;
```

Alternatively, you can query the system tables directly through the [MySQL Data Dictionary](https://www.google.com/url?sa=i&source=web&rct=j&url=https://dev.mysql.com/doc/refman/8.4/en/information-schema-table-constraints-table.html&ved=2ahUKEwjizeqrvfGUAxVQTWwGHcDOK74Qy_kOegoIAggACAEIIxAC&opi=89978449&cd&psig=AOvVaw0GAWbDNahNfp-OfYPLtsVQ&ust=1780796307408000): 
```sql
SELECT constraint_name, constraint_type 
FROM information_schema.table_constraints 
WHERE table_name = 'your_table_name';
```

