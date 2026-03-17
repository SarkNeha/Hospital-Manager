# Hospital Patient Management System

## Project Description

This project is a **Flask-based web application** that simulates a simple **Hospital Patient Management System**.
The system allows hospital staff to **add new patients, view current patients, and track recently admitted patients** through a web interface.

The goal of this project is to demonstrate the use of **Object-Oriented Programming (OOP), data structures, the Python datetime API, Flask routing, and HTML/CSS design** in building a functional web application.

---

## Features

* Add new patients through a web form
* View all admitted patients
* Display recently admitted patients
* Interactive webpage with CSS styling
* Uses Python classes for patient objects
* Tracks patient admission time using the datetime module
* Uses a **stack data structure** to store recently admitted patients

---

## Technologies Used

* Python
* Flask
* HTML
* CSS
* Git & GitHub
* Python datetime API

---

## Project Structure

```
hospital_manager/
│
├── apps.py
├── models.py
├── data.py
│
├── templates/
│   ├── index.html
│   └── add_patient.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## Object-Oriented Programming

The project uses a **Patient class** to represent each hospital patient.
Each patient has the following attributes:

* Name
* Age
* Diagnosis
* Admission Time
*Contact

This helps organize patient data in a structured way.

---

## Data Structures

A **stack data structure** is used to keep track of **recently admitted patients**.
This allows the system to quickly display the most recent admissions.

---

## Installation and Setup

### 1. Clone the repository

```
git clone <your-github-repository-link>
```

### 2. Navigate to the project folder

```
cd hospital_manager
```

### 3. Install Flask

```
pip install flask
```

### 4. Run the application

```
python apps.py
```

### 5. Open the browser

```
http://127.0.0.1:5000
```

---

## How the Application Works

1. The homepage displays all admitted patients.
2. Users can click **"Add Patient"** to open the admission form.
3. After submitting the form, the patient is added to the system.
4. The system updates the patient list and the recently admitted section.

---

## Author

Sneha Sarker – CSC202 Continuous Assessment

---

## License

This project is created for **educational purposes only**.
