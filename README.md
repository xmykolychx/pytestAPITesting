to run tests and be able generate report you need to install pytest, allure-pytest
cd tests
pytest --allure-dir=dir
allure serve -h localhost -p 8081 dir
