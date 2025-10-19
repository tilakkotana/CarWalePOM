from pathlib import Path

import pytest
from Pages.HomePage import HomePageClass
from Utilities.read_excel import readExcel

file_path = Path.cwd().parent / f'Excel/SellCarDetails.xlsx'

@pytest.mark.usefixtures("setup")
class Test_Sell_Your_Car:

    @pytest.fixture(autouse=True)
    def start(self,setup):
        self.driver=setup
        self.sell_car=HomePageClass(self.driver)

    @pytest.mark.parametrize('City,Pincode,Year,Month,Brand,Model,Fuel,Version,Colour,Alternate_Fuel,Owner,Kilometers,selling_price',readExcel(file_path))
    def test_sell_your_car(self,City,Pincode,Year,Month,Brand,Model,Fuel,Version,Colour,Alternate_Fuel,Owner,Kilometers,selling_price):
        self.sell_car.go_to_sell_your_car().fill_details(City,Pincode,Year,Month,Brand,Model,Fuel,Version,Colour,Alternate_Fuel,Owner,Kilometers,selling_price)
