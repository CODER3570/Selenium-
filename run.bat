behave -f allure_behave.formatter:AllureFormatter -o results\allure
allure generate results\allure -o results\allure_report --clean

