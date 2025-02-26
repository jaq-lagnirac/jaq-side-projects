# Justin Caringal

import os
import requests
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# based off of
# https://medium.com/@nithishreddy0627/a-beginners-guide-to-image-scraping-with-python-and-selenium-38ec419be5ff

driver = Chrome()
url = 'https://www.star-registration.com/blogs/constellations-and-zodiac-signs/an-overview-of-all-88-constellations'
driver.get(url)

IMG_CLASS = 'constellation-list-img'
TITLE_CLASS = 'constellation-card-title'
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, IMG_CLASS)))
img_elements = driver.find_elements(By.CLASS_NAME, IMG_CLASS)
name_elements = driver.find_elements(By.CLASS_NAME, TITLE_CLASS)

save_path = os.path.join(os.curdir, 'constellations_numbered')
os.makedirs(save_path, exist_ok=True)

for index, (image, name) in enumerate(zip(img_elements, name_elements)):
    try:
        # finds image url
        img_url = image.get_attribute("src")
        # start_str = 'files/'
        # start_index = img_url.index(start_str) + len(start_str) + 3
        # end_str = '?'
        # end_index = img_url.index(end_str)
        # img_name = img_url[start_index : end_index]
        img_name = name.text
        number = str(index + 1).zfill(2)

        # downloads image
        img_path = os.path.join(save_path, f'{number}_{img_name}.jpg')
        response = requests.get(img_url, stream=True)
        with open(img_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"Image {index + 1} downloaded successfully")
    
    except Exception as e:
            print(f"Failed to download image {index + 1}: {e}") 

driver.quit()
print('Completed scraping constellations')