import pytest
import os

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate -c ./Report/tmp  -o ./Report/new_report')
