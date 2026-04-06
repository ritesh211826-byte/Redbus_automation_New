from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.seat_page import SeatPage
from pages.boarding_page import BoardingPage
from pages.passenger_page import PassengerPage

def test_complete_booking(setup):

    driver = setup

    home = HomePage(driver)
    search = SearchPage(driver)
    seat = SeatPage(driver)
    boarding = BoardingPage(driver)
    passenger = PassengerPage(driver)

    # Step 1: Search
    home.enter_from("Delhi")
    home.enter_to("Lucknow")
    home.select_date()
    home.click_search()

    # Step 2: View seats
    search.click_first_bus()

    # Step 3: Seat selection
    #seat.close_popup_if_any()
    seat.select_seat()

    # 🔥 Step 4: Boarding (NEW)
    boarding.select_boarding_and_dropping()

    # 🔥 Step 5: Passenger
    passenger.open_passenger_section()
    passenger.fill_details()
    passenger.click_continue()