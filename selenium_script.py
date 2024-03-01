from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from datetime import datetime

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# bel-india website is used as sample
driver.get("https://bel-india.in/")

# We go to the career section
element = driver.find_element(By.XPATH, "//span[text()='Careers']")
element.click()

# we go to recruitment advertisements
rec_element = driver.find_element(By.XPATH, "//a[text() = 'Recruitment - Advertisements']")
rec_element.click()
time.sleep(2)

# we accept terms and conditions
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
time.sleep(1)
driver.find_element(By.XPATH,
                    "//span[text()='Please tick the checkbox for proceedings further']"
                    "/ancestor::div[1]/following-sibling::div//input[@type='submit']").click()
time.sleep(2)

# we find links provided in recruitment notices table
links = driver.find_elements(By.XPATH, "//table//a")

latest_link = ""
latest_date = None

# we iterate through the links got from above and save the latest link in the latest link

for link in links:
    link_str = link.get_attribute("href")

    if link_str[-4:] == '.pdf':
        try:
            date_str = datetime.strptime(link_str[-14:-4], '%d-%m-%Y')
        except:
            pass
        try:
            date_str = datetime.strptime(link_str[-12:-4], '%d-%m-%y')
        except:
            pass

        if latest_link == "" or latest_date < date_str:
            latest_link = link_str
            latest_date = date_str

# we save the pdf if we have found at least 1 valid link
if latest_link != "":
    driver.get(latest_link)
    time.sleep(1)

    pdf_object = driver.find_element(By.XPATH, "//object")

    response = requests.get(pdf_object.get_attribute("data"), verify=False)

    # Specify the file name to save the PDF as
    file_name = "latest_pdf.pdf"

    # Save the PDF content to a file
    with open(file_name, 'wb') as f:
        f.write(response.content)

# Close the webdriver
driver.quit()
