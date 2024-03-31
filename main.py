from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

prefs = {"profile.managed_default_content_settings.images":2}
chrome_options.headless = True


chrome_options.add_experimental_option("prefs", prefs)
wbe = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
