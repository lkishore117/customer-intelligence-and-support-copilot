# customer-intelligence-and-support-copilot
This repository is created and used for capstone project in Masai school's AI/ML Course

## 🔬 Reproduction Instructions

To reproduce the results or run this project locally, follow these steps in your terminal.

### 1. Prerequisites
Ensure you have the following installed on your system:
* **Python** 3.14.5
* **Numpy** 2.5.4
* **Pandas** 3.1.0

### 2. Clone the Repository
Clone the project and navigate into the project directory:
```zsh
git clone [https://github.com/lkishore117/customer-intelligence-and-support-copilot](https://github.com/lkishore117/customer-intelligence-and-support-copilot)
cd customer-intelligence-and-support-copilot
```

### 3. Setup the Environment
```zsh
python3 -m venv capstone
source capstone/bin/activate
pip install -r requirements.txt
```

### 4. Generate the Data ad Policy
```zsh
python3 generate_data.py
```

### 5. Part A - Data Foundation
```zsh
python3 data_foundation/shapes.py
python3 data_foundation/dataframe_details.py
python3 data_foundation/audit_figures.py
python3 data_foundation/clean_customers.py
python3 data_foundation/clean_orders.py
python3 data_foundation/store_and_validate.py
python3 data_foundation/sql_queries.py
python3 data_foundation/pandas_eda.py
```
