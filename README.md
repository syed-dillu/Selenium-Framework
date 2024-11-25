### Automation Framework for Testing Applications

This automation framework is designed for end-to-end testing of web applications. It uses **Python**, **Selenium**, and **Pytest**, providing a structured, modular, and scalable approach to testing. It supports data-driven testing, logging, reporting, and CI/CD integration.

**Table of Contents**
---------------------

1.  [Framework Overview](#framework-overview)
    
2.  [Folder Structure](#folder-structure)
    
3.  [Prerequisites](#prerequisites)
    
4.  [Installation](#installation)
    
5.  [Usage](#usage)
    
6.  [Configuration](#configuration)
    
7.  [Reporting](#reporting)
    
8.  [Contributing](#contributing)
    
9.  [License](#license)
    

**Framework Overview**
----------------------

This framework:

*   Supports Page Object Model (POM) for maintainable test scripts.
    
*   Enables data-driven testing using Excel.
    
*   Includes **Allure Reports** for test result visualization.
    
*   Provides CI/CD integration with Jenkins.
    
*   Supports cross-browser testing and custom explicit waits.

**Prerequisites**
-----------------

*   **Python 3.8+**
    
*   **Google Chrome** and **Chromedriver**
    
*   **Allure Commandline** (for report generation)
    
*   **Jenkins** (optional for CI/CD)
    

**Installation**
----------------

1.  bashCopy codegit clone https://github.com/your-repo/automation-framework.gitcd automation-framework
    
2.  bashCopy codepip install -r requirements.txt
    
3.  **Set up Allure:**
    
    *   Download Allure
        
    *   Add it to your system's PATH.
        
4.  **Configure environment variables:**
    
    *   Update the .env file with the required base URL, credentials, etc.
        

**Usage**
---------

### Run Tests

1.  bashCopy codepytest --alluredir=reports/allure\_reports
    
2.  bashCopy codepytest tests/test\_login.py --alluredir=reports/allure\_reports
    
3.  bashCopy codeallure serve reports/allure\_reports
    
4.  bashCopy codepython run\_tests.py
    

**Configuration**
-----------------

### **config/config.py**

Contains global settings like:

*   Base URL
    
*   Browser type (Chrome, Firefox)
    
*   Default timeout values
    

### **.env**

Store sensitive data:

*   Base URL
    
*   Test credentials (username/password)
    

**Reporting**
-------------

*   **Allure Reports:** Generates interactive reports. Accessible via the allure serve command.
    
*   **Screenshots:** Automatically captures screenshots of failed test cases and stores them in reports/screenshots/.
    

**CI/CD Setup with Jenkins**
----------------------------

This repository is configured to use Jenkins for Continuous Integration (CI). The CI pipeline automatically runs tests on every push to the repository.

## **Jenkins Pipeline Configuration**

The Jenkins pipeline is defined in a Jenkinsfile at the root of the repository. The pipeline includes the following stages:

**1. Checkout**: Clones the repository to the Jenkins agent.

**2. Setup Environment**: Creates a virtual environment and installs the required dependencies.

**3. Run Test**: Executes the test.

**4. Publish Coverage Report**: Archives the coverage report for further analysis.

**5. Publish Allure Report**: Generates and publishes the Allure report.

## **Running the Pipeline**

**Set Up Jenkins**: Ensure you have Jenkins installed and configured. You can set up a Jenkins job to monitor your repository for changes.

**Create a New Pipeline Job**: In Jenkins, create a new pipeline job and link it to your GitHub repository.

**Configure Build Triggers**: Use POLL SCM to trigger builds on every push.

**View Results**: Once the pipeline is configured, you can view the test results and reports in the Jenkins dashboard after each build.
    
**License**
-----------

This is a private project. Unauthorized copying, distribution, or modification of this code is prohibited.

All rights reserved. This code is proprietary and confidential. No part of this project may be reproduced, distributed, or transmitted in any form without explicit permission from \[Your Company Name\].
