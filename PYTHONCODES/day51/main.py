from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time

options = Options()
options.add_experimental_option("detach", True)
options.binary_location = "/usr/bin/brave-browser"
options.add_argument(
    "--user-data-dir=/home/ronninx/.config/BraveSoftware/Brave-Browser"
)
options.add_argument("--profile-directory=Profile 1")

driver = webdriver.Chrome(options=options)
driver.get("https://www.speedtest.net/")

wait = WebDriverWait(driver, 10)

# Click the "Go" button
try:
    go_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]",
            )
        )
    )
    go_button.click()
except TimeoutException:
    print("Go button not found. Exiting.")
    driver.quit()
    exit()

# Wait until download speed is available
download_speed = None
upload_speed = None
max_wait = 200  # Maximum total wait time in seconds
poll_interval = 2  # Check every 2 seconds
elapsed = 0

while elapsed < max_wait:
    try:
        download_speed_element = driver.find_element(
            By.CSS_SELECTOR,
            ".result-data-large.number.result-data-value.download-speed",
        )

        upload_speed_element = driver.find_element(
            By.CSS_SELECTOR,
            ".result-data-large.number.result-data-value.upload-speed",
        )

        download_value = download_speed_element.text.strip()
        upload_value = upload_speed_element.text.strip()
        if (download_value and download_value.replace(".", "", 1).isdigit()) and (
            upload_value and upload_value.replace(".", "", 1).isdigit()
        ):  # check if numeric
            download_speed = download_value
            upload_speed = upload_value

            break
    except StaleElementReferenceException:
        pass
    time.sleep(poll_interval)
    elapsed += poll_interval

DOWNLOAD_EXPECTED = 200
UPLOAD_EXPECTED = 100
if download_speed and upload_value:
    print(
        f"Download Speed: {download_speed} Mbps . Upload Speed: {upload_speed} Mbps ."
    )
    download_speed = float(download_speed)
    upload_speed = float(upload_speed)
    if download_speed < DOWNLOAD_EXPECTED or upload_speed < UPLOAD_EXPECTED:
        print("Internet speed is below expected. Opening Twitter...")
        driver.get("https://x.com/")
else:
    print("Failed to retrieve download speed after waiting.")

# driver.quit()
