import time
from Pages.BasePage import BasePageClass
from Pages.NewCarsPage import NewCarsClass
from Pages.NewsPage import NewsPageClass
from Pages.SellYourCarPage import SellYourCar
from Utilities.generate_logs import get_logs
log=get_logs()

class HomePageClass(BasePageClass):

    def __init__(self,driver):
        super().__init__(driver)

    def go_to_find_new_cars(self):
        log.info('hovering on new cars')
        self.hover_on('new_cars_XPATH')
        log.info('hovered on new cars')
        log.info('clicking on find new cars')
        self.click('find_new_cars_XPATH')
        log.info('clicked on find new cars')
        time.sleep(1)
        return NewCarsClass(self.driver)


    def go_to_sell_your_car(self):
        self.hover_on('used_cars_XPATH')
        self.click('sell_your_car_XPATH')
        return SellYourCar(self.driver)


    def go_to_reviews_and_news(self):
        self.hover_on('reviews_and_news_XPATH')
        self.click('news_XPATH')
        return NewsPageClass(self.driver)