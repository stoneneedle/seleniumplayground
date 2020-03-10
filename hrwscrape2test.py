#hrwscrape2test.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("prefs", {
  "download.default_directory": r"c:/users/james/downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  #"safebrowsing.enabled": True,
  "plugins.always_open_pdf_externally": True
})
#options.add_argument("user-data-dir=C:/Users/james/AppData/Local/Google/Chrome/User Data/Profile 2") #Path to your chrome profile

plan_url = 'https://my.hrw.com/SocialStudies/ss_2010/online_tos/hs_modern_world_history_poi/osp/resource_index/g_3_1/index.html'
#pdf_directurl = 'https://my.hrw.com/SocialStudies/ss_2010/online_tos/hs_modern_world_history_poi/data/unit01/chap1pr/planning_ak.pdf'

# start Chrome
#driver = webdriver.Chrome(executable_path = 'C:/Users/james/OneDrive/_Code/Python/__Coursica/chromedriver/chromedriver.exe', chrome_options=options) # my laptop
driver = webdriver.Chrome(executable_path = 'E:/OneDrive/_Code/cpp/cdctest/chromedriver.exe', chrome_options=options) # my laptop

driver.get(plan_url)

driver.find_element_by_xpath('//*[@id="content-menu"]/div/ul/li[1]/div/a').click()

# pdfstr = driver.page_source

# with open('derp.pdf', 'wb') as pdf_file:
# 	pdf_file.write(pdfstr)

