from behave import *
from selenium.webdriver.support.select import Select

from Utilities import configReader


@given ('Select the Flights')


def step_impl (context):
    context.reg = (context.driver)
    context.reg.open (configReader.readConfig ("basic info", "testsiteurl"))


@when ('Click the roundTrip')


def step_imp (context, setLeavingFrom):


@then ('Enter the Leaving fron"{LeavingFrom}" and going to"{Going to}" select d"{Departing}" and "{Returing}"')


def step_imp1 (context, LeavingFrom, Goingto, Departing, Returing):


    context.reg.LeavingFrom (LeavingFrom)
context.reg.Goingto (Goingto)
context.reg.Departing (Departing)
context.reg.Returing (Returing)


@then ('Select the Nonstop Flight')
def step_imp2 (context):
    context.driver.find_element_by_Xpath ("submit-button").click ()


@then ('Select Most expensive Flight from the list')
def step_imp3 (context):
    context.driver.find_element_by_Xpath ("is-visually-hidden")
    sel = Select (context.driver.find_element_by_Xpath ("is-visually-hidden"))
    sel.select_by_visible_text ("Highest")


@then ('Select Most expensive Flight from the list and click')
def step_imp4 (context):
    context.driver.find_element_by_Xpath ("//button[contains(text(),'Returning July 16, 2021']").click ()
