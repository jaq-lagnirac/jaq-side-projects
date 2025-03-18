# Justin Caringal
#
# A program to automate the download and backup of all default (i.e. main)
# branches of a given user's repository list.

# imports necessary libraries and packages
import os
import sys
import requests
from datetime import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# initializes webdriver, attempts to navigate to user's repository list
driver = Chrome()
account_name = 'jaq-lagnirac'
url = f'https://github.com/{account_name}?tab=repositories'
driver.get(url)

# ensures existence of user account
try:
    XPATH_404 = '//img[@alt="404 “This is not the web page you are looking for”"]'
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, XPATH_404)))
    find_404 = driver.find_element(By.XPATH, XPATH_404)
    print(f'{account_name} does not exist.')
    driver.quit()
    sys.exit()
except TimeoutException as e:
    print(f'{account_name} found, processing repositories.')

# finds repository names
REPO_XPATH = '//a[@itemprop="name codeRepository"]'
WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, REPO_XPATH)))
extracted_repos = driver.find_elements(By.XPATH, REPO_XPATH)

# extracts repository name and link
repo_list = []
for repo in extracted_repos:
    repo_name = repo.text
    repo_url = repo.get_attribute('href')
    print(f'{repo_name:<30}{repo_url}')
    repos_info = {
        'name' : repo_name,
        'url' : repo_url,
    }
    repo_list.append(repos_info)

# gets name of default branch for repository
BRANCH_ID = 'branch-picker-repos-header-ref-selector'
for repo in repo_list:
    driver.get(repo['url'])
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, BRANCH_ID)))
    branch_name = driver.find_element(By.ID, BRANCH_ID)
    branch_name.click()
    repo['branch'] = branch_name.text.strip()
    print(f'Found default branch for {repo['name']:<30}{repo['branch']}')

print('Done extracting information, closing window.')
driver.quit()
print('Downloading ZIP files.')

# downloads zip files into sub-directory
time_now = datetime.now().strftime('%Y%m%d_%H%M%S')
save_path = os.path.join(os.curdir, f'{time_now}_repo_downloads')
os.makedirs(save_path, exist_ok=True)
for repo in repo_list:
    
    print(f'{repo['name']:<30}', end='')
    repo_zip = f'{repo['url']}/archive/refs/heads/{repo['branch']}.zip'

    # downloads zip
    repo_path = os.path.join(save_path, f'{repo['name']}.zip')
    response = requests.get(repo_zip, stream=True)
    with open(repo_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    print('Repository downloaded successfully.')

print('All public repositories downloaded.')