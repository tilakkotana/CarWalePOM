# Carwale Automation Framework

**Selenium-based automation framework for the Carwale website.**  

This project is designed to automate several key functionalities on the Carwale website, including:

- **Fetching new car details:**  
  Retrieves all brand new cars’ information, including **name and price**, and stores it in an **Excel sheet**.

- **Fetching latest car news:**  
  Collects the latest car news and automatically includes **news images in the Allure report** for better visualization.

- **Posting ads for selling a car:**  
  Automates posting an ad on Carwale using **data from an Excel sheet**, including details such as:
  - Car brand and model  
  - Year and version  
  - Fuel type  
  - Kilometers driven  
  - Selling price  
  - Owner details  

---

## **Project Features**
- Implements **Page Object Model (POM)** for maintainable and reusable test scripts.  
- Uses **Selenium WebDriver** for browser automation.
- Uses Pytest for test execution and test management.
- Handles **Excel data input/output** using `openpyxl`.  
- Generates **Allure reports** including news images.  
- Easy to extend for additional automation tasks.

---

Setup & Running the Project

Step 1: First, clone the repository to your local machine using 
git clone https://github.com/tilakkotana/CarWalePOM.git
and navigate into the project folder with 
cd CarwalePOM

Step 2: It is recommended to create a Python virtual environment by running 
python -m venv .venv 
and activate it using 
.venv\Scripts\activate 
on Windows or 
source .venv/bin/activate 
on Mac/Linux.

Step 3: Once the virtual environment is active, install all required dependencies with 
pip install -r requirements.txt
This will install Selenium, OpenPyXL, pytest, and other necessary packages.

Step 4: Make sure the configuration settings in ConfigurationData/config.ini are correct, and ensure that the Excel sheets in the Excel/ folder contain the necessary data for posting car ads.

Step 5: Now you can run all test cases using 
cd TestCases
pytest --alluredir ../Reports
allure serve ../Reports
or run a specific test case like 
cd TestCases
pytest TestCases/test_example.py

Step 6: After execution, you can view the detailed results and news images in the Allure reports, and check the Logs/ folder if you need execution logs.
Always ensure your browser version matches the WebDriver version used in the framework and that the virtual environment is activated before running tests.
