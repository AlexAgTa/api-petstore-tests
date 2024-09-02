# Python API Testing Project with pytest-html for Reporting

## Overview
This project demonstrates how to set up a Python project for API testing using `requests` and `pytest`, with `pytest-html` for generating detailed test reports.

## Prerequisites
- Python 3.x installed on your system
- pip package manager

## Installation Steps

### 1. Clone the Project
Clone the project repository from GitHub:
```bash
git clone https://github.com/AlexAgTa/api-petstore-tests.git
cd python-petstore-tests
```
### 2. Set Up Virtual Environment (Optional but Recommended)
Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows use `.\.venv\Scripts\activate`
```

### 3. Install Dependencies
Install required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Running Tests
Run tests with pytest and generate an HTML report:
```bash
pytest --html=report.html
```

### 5. Viewing Reports
Open the generated `report.html` in your default browser to view the test results.

## Project Structure
- **`test_petstore_api_pytest.py`**: Python script containing the API test cases.
- **`requirements.txt`**: File listing Python dependencies.