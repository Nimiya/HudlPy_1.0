# HudlPy_1.0 (Hudly Python Behave BDD Cucumber Framework)

This repository contains automated test cases to validate login functionality of Hudl

## *Requirements*

1. Git or Command Prompt - Terminal
2. Python - 3.10.0 - https://www.python.org/downloads/
3. PyCharm Community Edition 2021.2.3 - IDE - https://www.jetbrains.com/pycharm/download/#section=windows
4. NodeJs - https://nodejs.org/en/download/

## *Set Environment Variables*

Path:
C:\Users\{user}\AppData\Roaming\npm

C:\Program Files\nodejs\node_modules\npm\bin


## *Set System Variables*

Path:
C:\Users\{user}\AppData\Local\Programs\Python\Python310

C:\Users\DELL\AppData\Local\Programs\Python\Python310\Scripts


## *Set up*

1. Open a terminal
2. Clone the repo 'git clone git@github.com:Nimiya/HudlPy_1.0.git'
3. Navigate to the reposiyory folder
4. Change the python interpreter to 'Python 3.10'
5. Install the dependencies './installDependencies.sh'

## *Running tests*

In terminal give

'./run.sh features/e2e/login.feature'

or 

'./run.sh features/e2e'

or

'./run.sh features'

or 

behave -f allure_behave.formatter:AllureFormatter -o reports/json/ features
allure generate reports/json --clean -o reports/allure-report

## *To see report*

Go to the location 'reports/allure-report/index.html'
And open index.html file in any browser of your choice

## *Framework Design*

Nimiya Joseph


