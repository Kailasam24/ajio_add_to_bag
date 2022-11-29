import Data_ajio.reading_obj
from POM.Add_to_Bag import Ajio
import pytest
from Data_ajio.reading_obj import ReadExcel

data1 = Data_ajio.reading_obj.list_1
from Library.config import Config
class TestAjio:
    read_xl=ReadExcel()
    data=read_xl.read_testdata(Config.Data_sheet)


    @pytest.mark.parametrize("number,element,color,size",data)
    # @pytest.mark.parametrize("number,element,size",[(9966250321,'kurthi','L')])
    def test_ajio(self,number,element,color,size,_driver):
    # def test_ajio(self,_driver):r
        bag=Ajio(_driver)
        # bag.select_signin_button()
        # bag.enter_number(number)
        bag.search(element)
        bag.product()
        bag.size_select(size)
        bag.add_to_bag()
        bag.go_to_bag()
        bag.proceed_shopping()




