from Functions.Fixtures_template import *
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import webdriver
chrome_driver_path = '/Users/alexdezho/Documents/Personal/chromedriver'


# testing step before running scenarios - using fixtures
def test_somthing_before(fixture_func_hi, fixture_func_bye):
    assert fixture_func_hi == 'hi', 'Was expected to get hi'
    assert fixture_func_bye == 'bye', 'Was expected to get bye'

def test_simple():
    chrome_driver_path = '/Users/alexdezho/Documents/Personal/chromedriver'
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get('https://www.google.com')
    driver.quit()

# regular test scenarios
def test01_bmw_elements():
    # Start the Chrome browser
    driver = webdriver.Chrome(chrome_driver_path)
    # Navigate to the BMW website
    driver.get("https://www.bmw.com")
    # driver.maximize_window()
    time.sleep(3)

    # Verify that the logo is displayed
    logo = driver.find_element(By.CSS_SELECTOR, "body > header > div > div > div > div > a > img")
    assert logo.is_displayed(), 'Logo not found'

    # Close the browser
    driver.quit()
def test02_demoblaze_elements(chrome_location):
    # Start the Chrome browser
    driver = webdriver.Chrome(chrome_location)

    # Navigate to the Demoblaze website
    driver.get("https://www.demoblaze.com/")
    # driver.maximize_window()
    time.sleep(3)
    # Verify that the logo is displayed
    logo = driver.find_element(By.CSS_SELECTOR, "#navbarExample > ul")
    assert logo.is_displayed(), 'logo not found'

    # Verify that the search bar is displayed
    search_bar = driver.find_element(By.CSS_SELECTOR, "#itemc")
    assert search_bar.is_displayed(), 'search bar not found'

    # Verify that the footer is displayed
    footer = driver.find_element(By.CSS_SELECTOR, "#fotcont")
    assert footer.is_displayed(), ' footer not found'
def test03_google_search_bob(chrome_location):
    # Start the Chrome browser
    driver = webdriver.Chrome(chrome_location)

    # Navigate to Google
    driver.get("https://www.google.com")

    # Find the search box
    search_box = driver.find_element_by_name("q")

    # Enter the search term "BOB"
    search_box.send_keys("BOB")

    # Submit the search form
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load
    time.sleep(3)

    # Verify that the results page contains the text "BOB"
    assert "BOB" in driver.page_source, 'BOB not found'

    # Close the browser
    driver.quit()
def test04_google_search_alex(chrome_location):
    # Start the Chrome browser
    driver = webdriver.Chrome(chrome_location)

    # Navigate to Google
    driver.get("https://www.google.com")

    # Find the search box
    search_box = driver.find_element_by_name("q")

    # Enter the search term "Alex"
    search_box.send_keys("Alex")

    # Submit the search form
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load
    time.sleep(3)

    # Verify that the results page contains the text "Alex"
    assert "Alex" in driver.page_source, 'Alex not found'

    # Close the browser
    driver.quit()
def test05_google_maps_169(chrome_location):
    # Start the Chrome browser
    driver = webdriver.Chrome(chrome_location)

    # Navigate to Google Maps
    driver.get("https://www.google.com/maps")

    # Find the search box
    search_box = driver.find_element_by_name("q")

    # Enter the search term "169 fort york ontario"
    search_box.send_keys("169 fort york ontario")

    # Submit the search form
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)


    # Verify that the results page contains the text "169"
    assert "169" in driver.page_source, "address not located"

    # Close the browser
    driver.quit()












