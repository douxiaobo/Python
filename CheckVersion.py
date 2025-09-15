import sys
import platform
import requests     ## pip install requests
from bs4 import BeautifulSoup

def get_latest_python_version():
    url = "https://www.python.org/downloads/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    latest_version = soup.find('ul', class_='list-releases').find('a').text.strip()
    return latest_version

print("Python version:", sys.version)       ## python3 --version or python -V
print("Version info:", sys.version_info) 

print("Python version:", platform.python_version())

# douxiaobo@192 Python % python3 CheckVersion.py
# Python version: 3.12.7 (main, Oct  1 2024, 02:05:46) [Clang 16.0.0 (clang-1600.0.26.3)]
# Version info: sys.version_info(major=3, minor=12, micro=7, releaselevel='final', serial=0)
# Python version: 3.12.7


import requests     ## pip install requests beautifulsoup4
from bs4 import BeautifulSoup

def get_latest_python_version():
    url = "https://www.python.org/downloads/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    latest_version = soup.find('ul', class_='list-releases').find('a').text.strip()
    return latest_version

current_version, _ = get_python_version()
latest_version = get_latest_python_version()

print(f"当前Python版本: {current_version}")
print(f"最新Python版本: {latest_version}")