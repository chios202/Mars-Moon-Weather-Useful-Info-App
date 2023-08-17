import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import sys


class Scraper:

    def __init__(self, url,cookies):
        self.driver = uc.Chrome(use_subprocess=True, user_data_dir=f"{sys.argv[1]}\\{cookies}",headless=True)
        self.driver.get(url)

    def getElements(self, type, xpath):

        element = WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((type,xpath)))
        return [i.text.replace('°','') for i in element]



class Elements:

    def __init__(self, planet):

        self.planet = planet


    def MarsTemperature(self):

        date = self.planet.getElements(By.XPATH, "//table[@id='weather_observation']/thead/tr/*[1]")[0]
        actual_date = self.planet.getElements(By.XPATH,"//div[@class='table_wrapper']//tbody/tr/*[1]")
        sol = self.planet.getElements(By.ID, "sol-header")
        actual_sol = self.planet.getElements(By.XPATH, "//div[@class='table_wrapper']//tbody/tr/*[2]")
        temperature_max = self.planet.getElements(By.XPATH,  "//table[@id='weather_observation']/thead/tr[2]/*[2]")
        temperature_min = self.planet.getElements(By.XPATH,  "//table[@id='weather_observation']/thead/tr[2]/*[3]")
        celsius_min = self.planet.getElements(By.XPATH, "//table[@id='weather_observation']//td[@class='temperature min']")
        celsius_max = self.planet.getElements(By.XPATH, "//table[@id='weather_observation']//td[@class='temperature max']")
        pressure = self.planet.getElements(By.ID, "pressure_lbl")
        actual_pressure = self.planet.getElements(By.XPATH, "//table[@id='weather_observation']//td[@class='pressure max']")
        sunrise = self.planet.getElements(By.ID, "sunrise_lbl")
        actual_sunrise = self.planet.getElements(By.XPATH, "//table[@id='weather_observation']//td[@class='sun rise']")
        sunset = self.planet.getElements(By.ID, "sunset_lbl")
        actual_sunset = self.planet.getElements(By.XPATH,"//table[@id='weather_observation']//td[@class='sun set']")

        rows = list(zip(actual_date, actual_sol, celsius_min, celsius_max, actual_pressure,actual_sunrise,actual_sunset))
        col = [date,sol,temperature_min,temperature_max,pressure,sunrise,sunset]
        df = pd.DataFrame(rows,columns=[''.join(i) for i in col])
        return df.to_csv(f"{sys.argv[1]}\\mars_weather.csv",index=None)



    def upComingMoonPhases(self):

        date1 = self.planet.getElements(By.ID, "moon1_date_text")
        date2 = self.planet.getElements(By.ID, "moon2_date_text")
        date3 = self.planet.getElements(By.ID, "moon3_date_text")
        date4 = self.planet.getElements(By.ID, "moon4_date_text")

        moon_phase1 = self.planet.getElements(By.ID, "moon1_phase_text")
        moon_phase2 = self.planet.getElements(By.ID, "moon2_phase_text")
        moon_phase3 = self.planet.getElements(By.ID, "moon3_phase_text")
        moon_phase4 = self.planet.getElements(By.ID, "moon4_phase_text")

        rows = list(zip(moon_phase1, moon_phase2, moon_phase3, moon_phase4))
        col = [date1, date2, date3, date4]
        df = pd.DataFrame(rows, columns = [''.join(i) for i in col])
        return df.to_csv(f"{sys.argv[1]}\\moon_phases.csv",index=None)


if __name__ == "__main__":
    Elements(Scraper("https://moonphases.co.uk/", "profile2")).upComingMoonPhases()
    Elements(Scraper("https://mars.nasa.gov/msl/weather/", "profile")).MarsTemperature()
    print("Succesfully extracted data to cvs file!")


