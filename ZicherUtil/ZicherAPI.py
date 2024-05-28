from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

DRIVER_PATH = "C:\___Programing___\Python Projects\Selenium\ZicherUtil\chromedriver.exe"
EXEL_PATH = "C:\___Programing___\Python Projects\Selenium\ZicherUtil\Add_To_Zicher.xlsx"
LOGIN = "Some Login"
PASSWORD = "Some Password"

DICT_COLUM = {
    0 :"Data",
    1 :"Numer",
    2 :"Opis",
    ###
    3 :"Sz",
    4 :"Sp",
    5: "Dar",
    6 : "Az",
    7 : "Poz",
    8 : "Proc",
    ###
    9 : "Wyp",
    10 : "Mat",
    11 : "Wyzy",
    12 : "Uslu",
    13 : "Tran",
    14 : "Czynsz",
    15 : "Ubezp",
    16 : "Inne",
    17 : "Wynagr",
    18 : "Sklad",
    19 : "Wydatek",

}

##########################

class FinancialPosition:
    def __init__(self, date, doc_number, description):
        self.date = date
        self.doc_number = doc_number
        self.description = description
        #NOT expense
        self.sk_z = None
        self.sk_p = None
        self.dar = None
        self.ak_z = None
        self.pozst = None
        self.proc = None
        #expense
        self.wyp = None
        self.mat = None
        self.wyrz = None
        self.usl = None
        self.tran = None
        self.cznsz = None
        self.ubez = None
        self.inne = None
        self.wyngr = None
        self.skldk = None
        #expense %
        self.wyp_proc = None
        self.mat_proc = None
        self.wyrz_proc = None
        self.usl_proc = None
        self.tran_proc = None
        self.cznsz_proc = None
        self.ubez_proc = None
        self.inne_proc = None
        self.wyngr_proc = None
        self.skldk_proc = None

        self.wydatk = None

##########################

class AutoZicher:
    def __init__(self, _login, _password, _driver_path):
        self._login = _login
        self._password = _password
        self._driver_path = _driver_path
        self.DRIVER = webdriver.Chrome(_driver_path)

    def begin(self):
        self.DRIVER.get("https://ziher.zhr.pl/polnocny-zachod/")    # and opens Chrome on Zicher

    def login(self):
        login_element = self.DRIVER.find_element_by_id("user_email")
        login_element.send_keys(self._login)
        password_element = self.DRIVER.find_element_by_id("user_password")
        password_element.send_keys(self._password)
        password_element.send_keys(Keys.ENTER)


    def open_page(self, url):
        self.DRIVER.get(url)

    def click_by_name(driver, name):
        elem = driver.find_element_by_name(name)
        elem.click()

    def ban_add_NOT_expense(self, position:FinancialPosition, year:int):
        
        # should probably be outside of this func but am not gona move it yet
        dict_year = {       #May be a bug deppending on how exactly those numbers are generated 
            2019 : "1446",
            2020 : "1600",
            2021 : "1683",
            2022 : "1753",
        }

        str_num_year = dict_year[year]

        self.open_page("https://ziher.zhr.pl/polnocny-zachod/entries/new?is_expense=false&journal_id=" + str_num_year)

        if position.sk_z != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_0_amount").send_keys(position.sk_z)
            print(position.sk_z)
        if position.sk_p != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_1_amount").send_keys(position.sk_p)
        if position.dar != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_2_amount").send_keys(position.dar)
        if position.ak_z != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_3_amount").send_keys(position.ak_z)
        if position.pozst != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_4_amount").send_keys(position.pozst)
        if position.proc != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_5_amount").send_keys(position.proc)
        ###
        if position.date != None:
            self.DRIVER.find_element_by_id("entry_date").send_keys(position.date)
        if position.doc_number != None:
            self.DRIVER.find_element_by_id("entry_document_number").send_keys(position.doc_number)
        if position.description != None:
            self.DRIVER.find_element_by_id("entry_name").send_keys(position.description + u'\ue007')


        #self.DRIVER.find_element_by_name("commit").click()

    def ban_add_EXPENSE(self, position:FinancialPosition, year:int):
                # should probably be outside of this func but am not gona move it yet
        dict_year = {       #May be a bug deppending on how exactly those numbers are generated 
            2019 : "1446",
            2020 : "1600",
            2021 : "1683",
            2022 : "1753",
        }

        str_num_year = dict_year[year]

        self.open_page("https://ziher.zhr.pl/polnocny-zachod/entries/new?is_expense=true&journal_id=" + str_num_year)


        if position.wyp != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_0_amount").send_keys(position.wyp)
        if position.mat != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_1_amount").send_keys(position.mat)
        if position.wyrz != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_2_amount").send_keys(position.wyrz)
        if position.usl != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_3_amount").send_keys(position.usl)
        if position.tran != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_4_amount").send_keys(position.tran)
        if position.cznsz != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_5_amount").send_keys(position.cznsz)
        if position.ubez != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_6_amount").send_keys(position.ubez)
        if position.inne != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_7_amount").send_keys(position.inne)
        if position.wyngr != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_8_amount").send_keys(position.wyngr)
        if position.skldk != None:
            self.DRIVER.find_element_by_id("entry_items_attributes_9_amount").send_keys(position.skldk)
        ###
        if position.date != None:
            self.DRIVER.find_element_by_id("entry_date").send_keys(position.date)
        if position.doc_number != None:
            self.DRIVER.find_element_by_id("entry_document_number").send_keys(position.doc_number)
        if position.description != None:
            self.DRIVER.find_element_by_id("entry_name").send_keys(position.description + u'\ue007')



##########################

def trans_exel_into_financial_poz(arkusz, row):

    fin_poz = FinancialPosition(arkusz.loc[row,DICT_COLUM[0]],arkusz.loc[row,DICT_COLUM[1]],arkusz.loc[row,DICT_COLUM[2]])

    cont = list()

    print("WYDATEK: " + str(arkusz.loc[row,DICT_COLUM[19]]))
    if(int(arkusz.loc[row,DICT_COLUM[19]]) == 0):
        for i in range(6):
            j = i + 3
            print(str(i) + " : " + str(j) + " : " + str(arkusz.loc[row,DICT_COLUM[j]]))
            cont.append(str(arkusz.loc[row,DICT_COLUM[j]]))

        if cont [0] != "nan":
            fin_poz.sk_z = cont[0]
        if cont [1] != "nan":
            fin_poz.sk_p = cont[1]
        if cont [2] != "nan":
            fin_poz.dar = cont[2]
        if cont [3] != "nan":
            fin_poz.ak_z = cont[3]
        if cont [4] != "nan":
            fin_poz.pozst = cont[4]
        if cont [5] != "nan":
            fin_poz.proc = cont[5]

        fin_poz.wydatk = 0

    else:
        for i in range(10):
            j = i + 9
            print(arkusz.loc[row,DICT_COLUM[j]])
            cont.append(str(arkusz.loc[row,DICT_COLUM[j]]))

        if cont [0] != "nan":
            fin_poz.wyp = cont[0]
        if cont [1] != "nan":
            fin_poz.mat = cont[1]
        if cont [2] != "nan":
            fin_poz.wyrz = cont[2]
        if cont [3] != "nan":
            fin_poz.usl = cont[3]
        if cont [4] != "nan":
            fin_poz.tran = cont[4]
        if cont [5] != "nan":
            fin_poz.cznsz = cont[5]
        if cont [6] != "nan":
            fin_poz.ubez = cont[6]
        if cont [7] != "nan":
            fin_poz.inne = cont[7]
        if cont [8] != "nan":
            fin_poz.wyngr = cont[8]
        if cont [9] != "nan":
            fin_poz.skldk = cont[9]

        fin_poz.wydatk = 1


    return fin_poz

##########################
xls = pd.ExcelFile(EXEL_PATH)
arkusz_1 = pd.read_excel(xls, 'Arkusz1')



fin_poz_list = list()

for i in range(len(arkusz_1.loc[:,DICT_COLUM[0]])):
    fin_poz_list.append(trans_exel_into_financial_poz(arkusz_1, i))



ZicherInstance = AutoZicher(LOGIN, PASSWORD, DRIVER_PATH)
ZicherInstance.begin()
ZicherInstance.login()

for i in range(len(fin_poz_list)):
    auto_year = int(fin_poz_list[i].date[:4])
    if(fin_poz_list[i].wydatk == 0):
        ZicherInstance.ban_add_NOT_expense(fin_poz_list[i], auto_year)
    else:
        ZicherInstance.ban_add_EXPENSE(fin_poz_list[i], auto_year)


#time.sleep(1000)
print("The automaton has completed the task succesfully")

