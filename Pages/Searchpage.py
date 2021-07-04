class SearchPage ():

    def __init__ (self, driver):
        super ().__init__ (driver)

    def open (self, url):
     self.driver.get (url)

    def setLeavingFrom (self, LeavingFrom):
        self.type (" LeavingFrom_classname", LeavingFrom)

    def setGoingto (self, Goingto):
        self.type ("Goingto_classname", Goingto)

    def setDeparting (self, Departing):
        self.type ("Departing_classname", Departing)

    def setReturing (self, Returing):
        self.Returing ("Returing", Returing)

    def submitForm (self):
        self.click ("submit_XPATH")
