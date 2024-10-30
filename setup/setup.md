# Project Setup Instructions

This guide will help you set up the project on your local environment, using either **XAMPP** (which includes MySQL) or a **standalone MySQL** setup.

## Prerequisites

- **Python 3.x** installed on your system
- **Virtual Environment**: Recommended to keep dependencies isolated
- **XAMPP** (if using the XAMPP setup) installed and running
- **MySQL Connector** for Python installed via pip

## 1. Clone the Repository

Clone this project repository from GitHub:
```bash
git clone https://github.com/yourusername/SecureAuth.git
cd SecureAuth
```

## 2. Set Up a Virtual Environment

Create and activate a virtual environment to isolate dependencies:

```bash
# Create virtual environment
python -m venv SecureAuth

# Activate the environment
# On Windows
SecureAuth\Scripts\activate

# On macOS/Linux
source SecureAuth/bin/activate
```

## 3. Install Requirements

Install the necessary Python packages:
```bash
pip install -r requirements.txt
```

## Using XAMPP for MySQL Setup

### Start MySQL Server in XAMPP
1. Open the XAMPP Control Panel
2. Start the **Apache** and **MySQL** modules

### Create the Database and Tables
1. Go to http://localhost/phpmyadmin
2. Create a new database (e.g., `secure_auth`)
3. Run the following SQL commands in the **SQL** tab to set up the required tables:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password_hash BLOB NOT NULL,
    salt BLOB NOT NULL,
    symmetric_key_encrypted BLOB NOT NULL,
    hmac BLOB NOT NULL
);
```

### Update Database Configuration in `main.py`

Open the `main.py` file and set up the MySQL database credentials:
```python
database_host = "localhost"
database_user = "your_mysql_username"  # e.g., root
database_password = "your_mysql_password"
database_name = "secure_auth"  # The database name you created
```

### Run the Application
1. Ensure XAMPP's MySQL server is still running
2. Start the application:
```bash
python main.py
```

### Testing the Application
* You will be prompted to enter a username and password to register or log in
* The entered data should be stored securely in the database, following the encryption methods defined in your project

## Using MySQL (Standalone Setup)

### Step 1: Install MySQL (Skip if MySQL is already installed)
* Download and install MySQL from MySQL's official website
* During installation, note the **username**, **password**, and **port** (default is 3306)

### Step 2: Configure the Database

#### Start MySQL Server
* On **Windows**, start MySQL from the MySQL Workbench or Services
* On **macOS/Linux**, start MySQL with:
```bash
sudo service mysql start
```

#### Create the Database and Tables
1. Log in to MySQL via the command line:
```bash
mysql -u your_mysql_username -p
```

2. Create the database and tables:
```sql
CREATE DATABASE secure_auth;
USE secure_auth;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password_hash BLOB NOT NULL,
    salt BLOB NOT NULL,
    symmetric_key_encrypted BLOB NOT NULL,
    hmac BLOB NOT NULL
);
```

### Step 3: Update Database Configuration in `main.py`

Open `main.py` and enter the MySQL credentials for the standalone setup:
```python
database_host = "localhost"
database_user = "your_mysql_username"
database_password = "your_mysql_password"
database_name = "secure_auth"
```

### Step 4: Run the Application

Start the application with:
```bash
python main.py
```

### Step 5: Test the Application
* Follow the prompts in the command line to register or authenticate users
* All registered users and their encrypted data will be stored in the database, with proper security measures applied