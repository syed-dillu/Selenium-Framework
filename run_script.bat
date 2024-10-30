@echo off
REM Run pytest
pytest

REM Serve Allure report
start cmd /k "allure serve .\report\allure-results"

REM Open coverage report
start .\report\coverage_report\index.html

REM Open HTML report
start .\pytest_html_report.html
