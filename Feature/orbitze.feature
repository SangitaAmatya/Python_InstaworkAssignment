Feature: Visit the Orbitz side Logo

  Scenario Outline: Vallidating Orbitze the site
    Given  Select the Flights
    When   Click the roundTrip
    Then   Enter the Leaving fron <LeavingFrom> and going to<Going to> select d<Departing> and <Returing>
    And    Click the Search Button
    And    Select the Nonstop Flight
    And    Select Most expensive Flight from the list and click

      | LeavingFrom | Going to | Departing | Returing |
    Examples:
      | Sanfranscico | NewYork | july/15/2021 | july/25/2021 |