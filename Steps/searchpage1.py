from behave import *
from selenium.webdriver.support.select import Select

from Utilities import configReader


@given ('I navigate to the Home page')
def step_impl (context):
    context.reg = (context.driver)
    context.reg.open (configReader.readConfig ("basic info", "testsiteurl"))


@when ('I click on Flight page')
def step_imp (context, setLeavingFrom):
    @then ('I enter the  Leaving from  And going to')
    def step_imp1 (context):


# context.reg.LeavingFrom (LeavingFrom)
# context.reg.Goingto (Goingto)
# context.reg.Departing (Departing)
# context.reg.Returing (Returing)
@then ('I Enter Departing and Returndate')
def step_imp2 (context):
    context.driver.find_element_by_Xpath ("submit-button").click ()


@then ('I click the search button')
def step_imp3 (context):
    context.driver.find_element_by_Xpath ("is-visually-hidden")
    sel = Select (context.driver.find_element_by_Xpath ("is-visually-hidden"))
    sel.select_by_visible_text ("Highest")


@then (' I should see the search resultsls')
def step_imp4 (context):
    context.driver.find_element_by_Xpath ("//button[contains(text(),'Returning July 16, 2021']").click ()
