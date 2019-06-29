from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import sys
import driver_manager

# os.environ["PATH"] += os.pathsep + "/Users/egigundari/Downloads/chrome"

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome(chrome_options=options)

link = "http://journals.ums.ac.id/index.php/khif/issue/archive"

try:

  driver.get(link)

  element = driver.find_element_by_id("issues")
  links = element.find_elements_by_xpath("//h4/a")
  for l in links:
    issue_link = l.get_attribute("href") + "/showToc"
    # print(issue_link);
    d = driver_manager.create_driver();
    d.get(issue_link);
    vol = d.find_element_by_tag_name("h2").text;
    els = d.find_elements_by_css_selector(".tocTitle > a");
    for el in els:
      print(vol, "|", el.text, "|", el.get_attribute("href"))

except KeyError:
  print("ERROR")