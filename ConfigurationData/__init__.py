from selenium.webdriver import chrome

[basicinfo]
testsiteurl = "https://www.orbitz.com"
browser = chrome
[locator]
Flight_XPATH = "//span[contains(text(),'Flights')]"
roundTrip_XPATH = "//span[contains(text(),'Roundtrip')]"
LeavingFrom_XPATH = "//*[contains(@class,'Leaving from')]"
Goingto_classname = "//*[contains(@class,'Leaving from')]"
Departing_classname = "uitk-faux-input uitk-form-field-trigger"
Nonstop_Flight_classname = "submit-button"
search_XPATH = "//button[contains(text(),'Returning July 16, 2021']"
