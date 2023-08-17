import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RealTime:

    def __init__(self, url, cookies):
        self.driver = uc.Chrome(use_subprocess=True,user_data_dir =f"c:\\temp\\{cookies}",headless=True)
        self.driver.get(url)

    def getElements(self, type, path):

        while (True):
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((type, path))).text
            if any(i.isdigit() for i in element):
                return element


class Scraping:

    def __init__(self, planet):

        self.planet = planet

    def getLRO(self):

        year = self.planet.getElements(By.XPATH, "//div[@class='countdown_time']/div[@class='time_years unit']")
        months = self.planet.getElements(By.XPATH, "//div[@class='time_months unit']")
        days =  self.planet.getElements(By.XPATH, "//div[@class='time_days unit']")
        hours = self.planet.getElements(By.XPATH, "//div[@class='time_hours unit']")
        minutes = self.planet.getElements(By.XPATH, "//div[@class='time_minutes unit']")
        seconds = self.planet.getElements(By.XPATH, "//div[@class='time_seconds unit']")

        time_data = [year, months, days, hours, minutes, seconds]
        l = [i.replace("\n", "") for i in time_data]
        return ' '.join(l)



    def getDistanceFromSun(self):

        distance = self.planet.getElements(By.CLASS_NAME, "value")
        return distance









