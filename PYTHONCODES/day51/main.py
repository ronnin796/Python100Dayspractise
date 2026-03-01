from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
from decouple import config

USERNAME = config("USERNAME")


class InternetSpeedBot:
    def __init__(
        self,
        download_expected=200,
        upload_expected=400,
        max_wait=200,
        poll_interval=2,
    ):
        self.DOWNLOAD_EXPECTED = download_expected
        self.UPLOAD_EXPECTED = upload_expected
        self.max_wait = max_wait
        self.poll_interval = poll_interval

        self.driver = self._setup_driver()
        self.wait = WebDriverWait(self.driver, 10)

    def _setup_driver(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.binary_location = "/usr/bin/brave-browser"
        options.add_argument(
            "--user-data-dir=/home/ronninx/.config/BraveSoftware/Brave-Browser"
        )
        options.add_argument("--profile-directory=Profile 1")

        return webdriver.Chrome(options=options)

    def open_speedtest(self):
        self.driver.get("https://www.speedtest.net/")

    def start_test(self):
        try:
            go_button = self.wait.until(
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
            self.driver.quit()
            exit()

    def get_speeds(self):
        download_speed = None
        upload_speed = None
        elapsed = 0

        while elapsed < self.max_wait:
            try:
                download_speed_element = self.driver.find_element(
                    By.CSS_SELECTOR,
                    ".result-data-large.number.result-data-value.download-speed",
                )

                upload_speed_element = self.driver.find_element(
                    By.CSS_SELECTOR,
                    ".result-data-large.number.result-data-value.upload-speed",
                )

                download_value = download_speed_element.text.strip()
                upload_value = upload_speed_element.text.strip()

                if (
                    download_value
                    and download_value.replace(".", "", 1).isdigit()
                    and upload_value
                    and upload_value.replace(".", "", 1).isdigit()
                ):
                    download_speed = float(download_value)
                    upload_speed = float(upload_value)
                    break

            except StaleElementReferenceException:
                pass

            time.sleep(self.poll_interval)
            elapsed += self.poll_interval

        return download_speed, upload_speed

    def check_speed(self):
        download_speed, upload_speed = self.get_speeds()

        if download_speed and upload_speed:
            print(
                f"Download Speed: {download_speed} Mbps | Upload Speed: {upload_speed} Mbps"
            )

            if (
                download_speed < self.DOWNLOAD_EXPECTED
                or upload_speed < self.UPLOAD_EXPECTED
            ):
                print("Internet speed is below expected. Opening Twitter...")

                self.login()

        else:
            print("Failed to retrieve download speed after waiting.")

    def run(self):
        self.open_speedtest()
        self.start_test()
        self.check_speed()

    def login(self):
        self.driver.get("https://x.com/")
        login_button = self.driver.find_element(By.XPATH, '//a[@href="/login"]')
        login_button.click()
        username = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//input[@autocapitalize="sentences" and @autocorrect="on"]')
            )
        )
        username.send_keys(USERNAME)


# RUN THE BOT

if __name__ == "__main__":
    bot = InternetSpeedBot()
    bot.login()
