# Fitness Database Management System

## 📜 Project Overview

### Purpose

This project is a Python application for managing a fitness database. It includes functionalities for trainers and clients. The system allows users to:

- **Display future appointments** for clients
- **View exercises by Date** for clients  
- **View a trainer's upcoming appointment**   

---

## ⚠️ Prerequisites

### Required Software

- Python 3.8+  
- MySQL Server installed and running  

### Install MySQL Connector for Python

Install the `mysql-connector-python` package:

```bash
pip install mysql-connector-python
```

## 📥 Installation Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/xavierhampton/Rao-Database-Scripts.git
cd ./Rao-Database-Scripts
```

### 2. Modify Database Connection Information
 Update your database connection details in Interface.py:
 ```python
cnx = mysql.connector.connect(user='your-root-username', password='your-password',host='127.0.0.1')
```
### 3. Run the Application
Execute the main script to start the application:
```bash
python ./Interface.py
```
