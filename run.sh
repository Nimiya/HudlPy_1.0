behave -f allure_behave.formatter:AllureFormatter -o reports/json/ $1
allure generate reports/json --clean -o reports/allure-report