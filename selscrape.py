#selscrape.py - test selenium scraper on pdf/doc
from selenium import webdriver
import os, shutil, time

testurl = 'https://my.hrw.com/SocialStudies/ss_2010/online_tos/hs_modern_world_history_poi/data/unit01/student_ak.pdf'

#dlbasedir = "C:/Users/james/OneDrive/_Code/Python/basics/playground/selenium/hrw/test/" # for linux/*nix, download_dir="/usr/Public"

dlbasedir = 'C:/Users/james/Downloads/test/'

options = webdriver.ChromeOptions()

# profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
#                "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}

profile = {"plugins.always_open_pdf_externally": True, "download.default_directory": dlbasedir, "download.extensions_to_open": "applications/pdf"}
options.add_experimental_option("prefs", profile)


# start Chrome
driver = webdriver.Chrome(executable_path = 'C:/Users/james/OneDrive/_Code/Python/__Coursica/chromedriver/chromedriver.exe', chrome_options=options) # my laptop


driver.get(testurl)
time.sleep(2)


# filename = max([dlbasedir + "\\" + f for f in os.listdir(dlbasedir)],key=os.path.getctime)
# shutil.move(filename,os.path.join(Initial_path,r'test.pdf'))


print("Downloaded to " + dlbasedir)