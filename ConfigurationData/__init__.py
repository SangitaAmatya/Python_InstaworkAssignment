from selenium.webdriver import chrome

[basicinfo]
testsiteurl = "https://www.orbitz.com"
browser = chrome
[locator]
Flight_XPATH = "//span[contains(text(),'Flights')]"
roundTrip_XPATH = "//span[contains(text(),'Roundtrip')]"
LeavingFrom_XPATH = "//*[contains(@class,'Leaving from')]"
Goingto_XPATH = "//*[contains(@class,'Goingto')]"
Departing_XPATH = "//input[@id=\"d1\"]"
Nonstop_Flight_classname = "submit-button"
search_XPATH = "//button[@data-testid=\"submit-button\"]"
