from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument(
    '--disable-blink-features=AutomationControlled')  # выключаю webserver mode
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
options.add_argument("headless")
options.add_argument("start-maximized")
options.add_argument("window-size=1900,1080")

url = 'https://p2p.binance.com/ru/trade/all-payments/USDT?fiat=RUB'
s = Service('YOUR PATH')

driver = webdriver.Chrome(service=s, options=options)

# Для избавления от слипов
driver.implicitly_wait(10)

# Тэйк покупка
price_sb_usdt = price_tink_usdt = price_raif_usdt = price_qiwi_usdt = price_payer_usdt = price_yoomoney_usdt = 0
price_sb_btc = price_tink_btc = price_raif_btc = price_qiwi_btc = price_payer_btc = price_yoomoney_btc = 0
price_sb_eth = price_tink_eth = price_raif_eth = price_qiwi_eth = price_payer_eth = price_yoomoney_eth = 0

# Тэйк продажа
price_sb_usdt_s = price_tink_usdt_s = price_raif_usdt_s = price_qiwi_usdt_s = price_payer_usdt_s = price_yoomoney_usdt_s = 0
price_sb_btc_s = price_tink_btc_s = price_raif_btc_s = price_qiwi_btc_s = price_payer_btc_s = price_yoomoney_btc_s = 0
price_sb_eth_s = price_tink_eth_s = price_raif_eth_s = price_qiwi_eth_s = price_payer_eth_s = price_yoomoney_eth_s = 0

spread = 0.6

try:
    driver.get(url=url)

    cross_button = driver.find_element(By.CLASS_NAME,
                                       "css-1pcqseb").click()  # закрытие окна("как купить крипту/как продать...")

    amount_input = driver.find_element(By.CLASS_NAME, "css-16fg16t")
    amount_input.clear()
    amount_input.send_keys('6000')
    amount_button = driver.find_element(By.CLASS_NAME, "css-jk2s2w").click()

    # ТЭЙК ПОКУПКА  
    # цена usdt через сбер
    payment_method_button = driver.find_element(By.ID,
                                                "C2Cpaymentfilter_searchbox_payment")  # сделал по id так как по-другому не получалось
    payment_method_button.click()

    payment_method_sb_button = driver.find_element(By.ID, "Росбанк")
    payment_method_sb_button.click()

    price_sb_usdt = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip())

    # цена usdt через юмани
    payment_method_button.click()

    payment_method_yoomoney_button = driver.find_element(By.ID, "Юmoney")
    payment_method_yoomoney_button.click()

    price_yoomoney_usdt = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip())

    # цена usdt через тиньку
    payment_method_button.click()

    payment_method_tink_button = driver.find_element(By.ID, "Тинькофф")
    payment_method_tink_button.click()

    price_tink_usdt = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip())

    # цена usdt через райф
    payment_method_button.click()

    payment_method_raif_button = driver.find_element(By.ID, "Райффайзенбанк")
    payment_method_raif_button.click()

    price_raif_usdt = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip())

    # цена usdt через qiwi
    payment_method_button.click()

    payment_method_qiwi_button = driver.find_element(By.ID, "QIWI")
    payment_method_qiwi_button.click()

    price_qiwi_usdt = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip())

    # цена usdt через payer
    payment_method_button.click()

    payment_method_payer_button = driver.find_element(By.ID, "Payeer")
    payment_method_payer_button.click()

    price_payer_usdt = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip())

    # переход на вкладку с битком
    btc_button = driver.find_element(By.CLASS_NAME, "css-1gw94z4")
    btc_button.click()

    # цена btc через payer
    price_payer_btc = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))

    # цена btc через сбер
    payment_method_button.click()

    payment_method_sb_button.click()  # выбираю сбер

    price_sb_btc = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))

    # цена btc через юмани
    payment_method_button.click()

    payment_method_yoomoney_button.click()

    price_yoomoney_btc = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))

    # цена btc через тиньку
    payment_method_button.click()

    payment_method_tink_button.click()

    price_tink_btc = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))

    # цена btc через райф
    payment_method_button.click()

    payment_method_raif_button.click()

    price_raif_btc = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))

    # цена usdt через qiwi
    payment_method_button.click()

    payment_method_qiwi_button.click()

    price_qiwi_btc = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))

    # переход на вкладку с эфиром 

    eth_button = driver.find_element(By.XPATH,
                                     '//*[@id="__APP"]/div[2]/main/div[1]/div[3]/div[1]/div/div/div[2]/div/div[5]/h2')
    eth_button.click()

    # цена eth через qiwi
    price_qiwi_eth = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))

    # цена eth через сбер
    payment_method_button.click()

    payment_method_sb_button.click()  # выбираю сбер

    price_sb_eth = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))

    # цена eth через юмани
    payment_method_button.click()

    payment_method_yoomoney_button.click()

    price_yoomoney_eth = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))

    # цена eth через тиньку
    payment_method_button.click()

    payment_method_tink_button.click()

    price_tink_eth = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))

    # цена eth через райф
    payment_method_button.click()

    payment_method_raif_button.click()

    price_raif_eth = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))

    # цена eth через payer
    payment_method_button.click()

    payment_method_payer_button.click()

    price_payer_eth = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))

    # ТЭЙК ПРОДАЖА  
    # ВКЛАДКА С ЭФИРОМ 

    # Переход на вкладку ПРОДАЖА
    sell_button = driver.find_element(By.CLASS_NAME, "css-yxrkwa").click()
    
    # цена eth через payer
    price_payer_eth_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))
    
    # цена eth через сбер
    payment_method_button.click()
    payment_method_sb_button.click()
    
    price_sb_eth_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))
    
    # цена eth через юмани
    payment_method_button.click()
    
    payment_method_yoomoney_button.click()
    
    price_yoomoney_eth_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))
    
    # цена eth через тиньку
    payment_method_button.click()
    payment_method_tink_button.click()
    
    price_tink_eth_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))
    
    # цена eth через райф
    payment_method_button.click()
    payment_method_raif_button.click()
    
    price_raif_eth_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))
    
    # цена eth через qiwi
    payment_method_button.click()
    payment_method_qiwi_button.click()
    
    price_qiwi_eth_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))
    
    # ВКЛАДКА С BTC 
    
    # Переход на вкладку с BTC
    btc_button.click()
    
    # цена btc через qiwi
    price_qiwi_btc_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))
    
    # цена btc через сбер
    payment_method_button.click()
    payment_method_sb_button.click()  # выбираю сбер
    
    price_sb_btc_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))
    
    # цена btc через юмани
    payment_method_button.click()
    
    payment_method_yoomoney_button.click()
    
    price_yoomoney_btc_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))
    
    # цена btc через тиньку
    payment_method_button.click()
    payment_method_tink_button.click()
    
    price_tink_btc_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))
    
    # цена btc через райф
    payment_method_button.click()
    payment_method_raif_button.click()
    
    price_raif_btc_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))
    
    # цена btc через payer
    payment_method_button.click()
    payment_method_payer_button.click()
    
    price_payer_btc_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))
    
    # ВКЛАДКА С USDT 
    
    usdt_button = driver.find_element(By.CLASS_NAME, "css-1cvxz8n")
    usdt_button.click()
    
    # цена usdt через payer
    price_payer_usdt_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip())
    
    # цена usdt через сбер
    payment_method_button.click()
    payment_method_sb_button.click()
    
    price_sb_usdt_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip())
    
    # цена usdt через юмани
    payment_method_button.click()
    
    payment_method_yoomoney_button.click()
    
    price_yoomoney_usdt_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip().replace(',', ''))
    
    # цена usdt через тиньку
    payment_method_button.click()
    payment_method_tink_button.click()
    
    price_tink_usdt_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip())
    
    # цена usdt через райф
    payment_method_button.click()
    payment_method_raif_button.click()
    
    price_raif_usdt_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip())
    
    # цена usdt через qiwi
    payment_method_button.click()
    payment_method_qiwi_button.click()
    
    price_qiwi_usdt_s = float(driver.find_element(By.CLASS_NAME, "css-1m1f8hn").text.strip())

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

# print(price_sb_btc, price_tink_btc, price_raif_btc, price_qiwi_btc, price_payer_btc)
# print(price_sb_usdt, price_tink_usdt, price_raif_usdt, price_qiwi_usdt, price_payer_usdt)
# print(price_sb_eth, price_tink_eth, price_raif_eth, price_qiwi_eth, price_payer_eth)

#print(price_sb_btc_s, price_tink_btc_s, price_raif_btc_s, price_qiwi_btc_s, price_payer_btc_s)
#print(price_sb_usdt_s, price_tink_usdt_s, price_raif_usdt_s, price_qiwi_usdt_s, price_payer_usdt_s)
#print(price_sb_eth_s, price_tink_eth_s, price_raif_eth_s, price_qiwi_eth_s, price_payer_eth_s)

good_spred = []

#Покупка по тэйку -> продажа по мэйку
def take_make():
    # проверяю для usdt(сделал для сбера)
    if price_sb_usdt < price_tink_usdt and (round((price_tink_usdt - price_sb_usdt) / price_sb_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_tink_usdt - price_sb_usdt) / price_sb_usdt * 100, 2)) + "! Покупка usdt через Сбербанк за " + str(
            price_sb_usdt) + "! Продажа через Тинькофф за " + str(price_tink_usdt) + "!")
    if price_sb_usdt < price_raif_usdt and (round((price_raif_usdt - price_sb_usdt) / price_sb_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_raif_usdt - price_sb_usdt) / price_sb_usdt * 100, 2)) + "! Покупка usdt через Сбербанк за " + str(
            price_sb_usdt) + "! Продажа через Райфайзен за " + str(price_raif_usdt) + "!")
    if price_sb_usdt < price_qiwi_usdt and (round((price_qiwi_usdt - price_sb_usdt) / price_sb_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_qiwi_usdt - price_sb_usdt) / price_sb_usdt * 100, 2)) + "! Покупка usdt через Сбербанк за " + str(
            price_sb_usdt) + "! Продажа через Qiwi за " + str(price_qiwi_usdt) + "!")
    if price_sb_usdt < price_payer_usdt and (round((price_payer_usdt - price_sb_usdt) / price_sb_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_payer_usdt - price_sb_usdt) / price_sb_usdt * 100, 2)) + "! Покупка usdt через Сбербанк за " + str(
            price_sb_usdt) + "! Продажа через Payer за " + str(price_payer_usdt) + "!")
    if price_sb_usdt < price_yoomoney_usdt and (round((price_yoomoney_usdt - price_sb_usdt) / price_sb_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_yoomoney_usdt - price_sb_usdt) / price_sb_usdt * 100, 2)) + "! Покупка usdt через Сбербанк за " + str(
            price_sb_usdt) + "! Продажа через YooMoney за " + str(price_yoomoney_usdt) + "!")

    # проверяю для usdt(сделал для тиньки)
    if price_sb_usdt > price_tink_usdt and (round((price_sb_usdt - price_tink_usdt) / price_tink_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_sb_usdt - price_tink_usdt) / price_tink_usdt * 100,
                                                2)) + "! Покупка usdt через Тинькофф за " + str(
            price_tink_usdt) + "! Продажа через Сбербанк за " + str(price_sb_usdt) + "!")
    if price_raif_usdt > price_tink_usdt and (
    round((price_raif_usdt - price_tink_usdt) / price_tink_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_raif_usdt - price_tink_usdt) / price_tink_usdt * 100,
                                                2)) + "! Покупка usdt через Тинькофф за " + str(
            price_tink_usdt) + "! Продажа через Райфайзен за " + str(price_raif_usdt) + "!")
    if price_qiwi_usdt > price_tink_usdt and (
    round((price_qiwi_usdt - price_tink_usdt) / price_tink_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_qiwi_usdt - price_tink_usdt) / price_tink_usdt * 100,
                                                2)) + "! Покупка usdt через Тинькофф за " + str(
            price_tink_usdt) + "! Продажа через Qiwi за " + str(price_qiwi_usdt) + "!")
    if price_payer_usdt > price_tink_usdt and (
    round((price_payer_usdt - price_tink_usdt) / price_tink_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_payer_usdt - price_tink_usdt) / price_tink_usdt * 100,
                                                2)) + "! Покупка usdt через Тинькофф за " + str(
            price_tink_usdt) + "! Продажа через Payer за " + str(price_payer_usdt) + "!")
    if price_yoomoney_usdt > price_tink_usdt and (
    round((price_yoomoney_usdt - price_tink_usdt) / price_tink_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_yoomoney_usdt - price_tink_usdt) / price_tink_usdt * 100,
                                                2)) + "! Покупка usdt через Тинькофф за " + str(
            price_tink_usdt) + "! Продажа через YooMoney за " + str(price_yoomoney_usdt) + "!")

    # проверяю для usdt(сделал для райфа)
    if price_sb_usdt > price_raif_usdt and (round((price_sb_usdt - price_raif_usdt) / price_raif_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_sb_usdt - price_raif_usdt) / price_raif_usdt * 100,
                                                2)) + "! Покупка usdt через Райфайзен за " + str(
            price_raif_usdt) + "! Продажа через Сбербанк за " + str(price_sb_usdt) + "!")
    if price_tink_usdt > price_raif_usdt and (
    round((price_tink_usdt - price_raif_usdt) / price_raif_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_tink_usdt - price_raif_usdt) / price_raif_usdt * 100,
                                                2)) + "! Покупка usdt через Райфайзен за " + str(
            price_raif_usdt) + "! Продажа через Тинькофф за " + str(price_tink_usdt) + "!")
    if price_qiwi_usdt > price_raif_usdt and (
    round((price_qiwi_usdt - price_raif_usdt) / price_raif_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_qiwi_usdt - price_raif_usdt) / price_raif_usdt * 100,
                                                2)) + "! Покупка usdt через Райфайзен за " + str(
            price_raif_usdt) + "! Продажа через Qiwi за " + str(price_qiwi_usdt) + "!")
    if price_payer_usdt > price_raif_usdt and (
    round((price_payer_usdt - price_raif_usdt) / price_raif_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_payer_usdt - price_raif_usdt) / price_raif_usdt * 100,
                                                2)) + "! Покупка usdt через Райфайзен за " + str(
            price_raif_usdt) + "! Продажа через Payer за " + str(price_payer_usdt) + "!")
    if price_yoomoney_usdt > price_raif_usdt and (
    round((price_yoomoney_usdt - price_raif_usdt) / price_raif_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_yoomoney_usdt - price_raif_usdt) / price_raif_usdt * 100,
                                                2)) + "! Покупка usdt через Райфайзен за " + str(
            price_raif_usdt) + "! Продажа через YooMoney за " + str(price_yoomoney_usdt) + "!")

    # проверяю для usdt(сделал для киви)
    if price_sb_usdt > price_qiwi_usdt and (round((price_sb_usdt - price_qiwi_usdt) / price_qiwi_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_sb_usdt - price_qiwi_usdt) / price_qiwi_usdt * 100, 2)) + "! Покупка usdt через Qiwi за " + str(
            price_qiwi_usdt) + "! Продажа через Сбербанк за " + str(price_sb_usdt) + "!")
    if price_tink_usdt > price_qiwi_usdt and (
    round((price_tink_usdt - price_qiwi_usdt) / price_qiwi_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_tink_usdt - price_qiwi_usdt) / price_qiwi_usdt * 100, 2)) + "! Покупка usdt через Qiwi за " + str(
            price_qiwi_usdt) + "! Продажа через Тинькофф за " + str(price_tink_usdt) + "!")
    if price_raif_usdt > price_qiwi_usdt and (
    round((price_raif_usdt - price_qiwi_usdt) / price_qiwi_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_raif_usdt - price_qiwi_usdt) / price_qiwi_usdt * 100, 2)) + "! Покупка usdt через Qiwi за " + str(
            price_qiwi_usdt) + "! Продажа через Райфайзен за " + str(price_raif_usdt) + "!")
    if price_payer_usdt > price_qiwi_usdt and (
    round((price_payer_usdt - price_qiwi_usdt) / price_qiwi_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_payer_usdt - price_qiwi_usdt) / price_qiwi_usdt * 100, 2)) + "! Покупка usdt через Qiwi за " + str(
            price_qiwi_usdt) + "! Продажа через Payer за " + str(price_payer_usdt) + "!")
    if price_yoomoney_usdt > price_qiwi_usdt and (
    round((price_yoomoney_usdt - price_qiwi_usdt) / price_qiwi_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_yoomoney_usdt - price_qiwi_usdt) / price_qiwi_usdt * 100, 2)) + "! Покупка usdt через Qiwi за " + str(
            price_qiwi_usdt) + "! Продажа через YooMoney за " + str(price_yoomoney_usdt) + "!")

    # проверяю для usdt(сделал для Payer)
    if price_sb_usdt > price_payer_usdt and (
    round((price_sb_usdt - price_payer_usdt) / price_payer_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_sb_usdt - price_payer_usdt) / price_payer_usdt * 100, 2)) + "! Покупка usdt через Payer за " + str(
            price_payer_usdt) + "! Продажа через Сбербанк за " + str(price_sb_usdt) + "!")
    if price_tink_usdt > price_payer_usdt and (
    round((price_tink_usdt - price_payer_usdt) / price_payer_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_tink_usdt - price_payer_usdt) / price_payer_usdt * 100,
                                                2)) + "! Покупка usdt через Payer за " + str(
            price_payer_usdt) + "! Продажа через Тинькофф за " + str(price_tink_usdt) + "!")
    if price_raif_usdt > price_payer_usdt and (
    round((price_raif_usdt - price_payer_usdt) / price_payer_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_raif_usdt - price_payer_usdt) / price_payer_usdt * 100,
                                                2)) + "! Покупка usdt через Payer за " + str(
            price_payer_usdt) + "! Продажа через Райфайзен за " + str(price_raif_usdt) + "!")
    if price_qiwi_usdt > price_payer_usdt and (
    round((price_qiwi_usdt - price_payer_usdt) / price_payer_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_qiwi_usdt - price_payer_usdt) / price_payer_usdt * 100,
                                                2)) + "! Покупка usdt через Payer за " + str(
            price_payer_usdt) + "! Продажа через Qiwi за " + str(price_qiwi_usdt) + "!")
    if price_yoomoney_usdt > price_payer_usdt and (
    round((price_yoomoney_usdt - price_payer_usdt) / price_payer_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_yoomoney_usdt - price_payer_usdt) / price_payer_usdt * 100,
                                                2)) + "! Покупка usdt через Payer за " + str(
            price_payer_usdt) + "! Продажа через YooMoney за " + str(price_yoomoney_usdt) + "!")

    # проверяю для usdt(сделал для юмани)
    if price_sb_usdt > price_yoomoney_usdt and (
    round((price_sb_usdt - price_yoomoney_usdt) / price_yoomoney_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_sb_usdt - price_yoomoney_usdt) / price_yoomoney_usdt * 100,
                  2)) + "! Покупка usdt через YooMoney за " + str(
            price_yoomoney_usdt) + "! Продажа через Сбербанк за " + str(price_sb_usdt) + "!")
    if price_tink_usdt > price_yoomoney_usdt and (
            round((price_tink_usdt - price_yoomoney_usdt) / price_yoomoney_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_tink_usdt - price_yoomoney_usdt) / price_yoomoney_usdt * 100,
                  2)) + "! Покупка usdt через YooMoney за " + str(
            price_yoomoney_usdt) + "! Продажа через Тинькофф за " + str(price_tink_usdt) + "!")
    if price_raif_usdt > price_yoomoney_usdt and (
            round((price_raif_usdt - price_yoomoney_usdt) / price_yoomoney_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_raif_usdt - price_yoomoney_usdt) / price_yoomoney_usdt * 100,
                  2)) + "! Покупка usdt через YooMoney за " + str(
            price_yoomoney_usdt) + "! Продажа через Райфайзен за " + str(price_raif_usdt) + "!")
    if price_payer_usdt > price_yoomoney_usdt and (
            round((price_payer_usdt - price_yoomoney_usdt) / price_yoomoney_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_payer_usdt - price_yoomoney_usdt) / price_yoomoney_usdt * 100,
                  2)) + "! Покупка usdt через YooMoney за " + str(
            price_yoomoney_usdt) + "! Продажа через Payer за " + str(price_payer_usdt) + "!")
    if price_qiwi_usdt > price_yoomoney_usdt and (
            round((price_qiwi_usdt - price_yoomoney_usdt) / price_yoomoney_usdt * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_qiwi_usdt - price_yoomoney_usdt) / price_yoomoney_usdt * 100,
                  2)) + "! Покупка usdt через YooMoney за " + str(
            price_yoomoney_usdt) + "! Продажа через Qiwi за " + str(price_qiwi_usdt) + "!")

    # проверяю для btc(сделал для сбера)
    if price_sb_btc < price_tink_btc and (round((price_tink_btc - price_sb_btc) / price_sb_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_tink_btc - price_sb_btc) / price_sb_btc * 100, 2)) + "! Покупка btc через Сбербанк за " + str(
            price_sb_btc) + "! Продажа через Тинькофф за " + str(price_tink_btc) + "!")
    if price_sb_btc < price_raif_btc and (round((price_raif_btc - price_sb_btc) / price_sb_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_raif_btc - price_sb_btc) / price_sb_btc * 100, 2)) + "! Покупка btc через Сбербанк за " + str(
            price_sb_btc) + "! Продажа через Райфайзен за " + str(price_raif_btc) + "!")
    if price_sb_btc < price_qiwi_btc and (round((price_qiwi_btc - price_sb_btc) / price_sb_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_qiwi_btc - price_sb_btc) / price_sb_btc * 100, 2)) + "! Покупка btc через Сбербанк за " + str(
            price_sb_btc) + "! Продажа через Qiwi за " + str(price_qiwi_btc) + "!")
    if price_sb_btc < price_payer_btc and (round((price_payer_btc - price_sb_btc) / price_sb_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_payer_btc - price_sb_btc) / price_sb_btc * 100, 2)) + "! Покупка btc через Сбербанк за " + str(
            price_sb_btc) + "! Продажа через Payer за " + str(price_payer_btc) + "!")
    if price_sb_btc < price_yoomoney_btc and (round((price_yoomoney_btc - price_sb_btc) / price_sb_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_yoomoney_btc - price_sb_btc) / price_sb_btc * 100, 2)) + "! Покупка btc через Сбербанк за " + str(
            price_sb_btc) + "! Продажа через YooMoney за " + str(price_yoomoney_btc) + "!")

    # проверяю для btc(сделал для тиньки)
    if price_sb_btc > price_tink_btc and (round((price_sb_btc - price_tink_btc) / price_tink_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_sb_btc - price_tink_btc) / price_tink_btc * 100, 2)) + "! Покупка btc через Тинькофф за " + str(
            price_tink_btc) + "! Продажа через Сбербанк за " + str(price_sb_btc) + "!")
    if price_raif_btc > price_tink_btc and (round((price_raif_btc - price_tink_btc) / price_tink_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_raif_btc - price_tink_btc) / price_tink_btc * 100, 2)) + "! Покупка btc через Тинькофф за " + str(
            price_tink_btc) + "! Продажа через Райфайзен за " + str(price_raif_btc) + "!")
    if price_qiwi_btc > price_tink_btc and (round((price_qiwi_btc - price_tink_btc) / price_tink_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_qiwi_btc - price_tink_btc) / price_tink_btc * 100, 2)) + "! Покупка btc через Тинькофф за " + str(
            price_tink_btc) + "! Продажа через Qiwi за " + str(price_qiwi_btc) + "!")
    if price_payer_btc > price_tink_btc and (round((price_payer_btc - price_tink_btc) / price_tink_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_payer_btc - price_tink_btc) / price_tink_btc * 100, 2)) + "! Покупка btc через Тинькофф за " + str(
            price_tink_btc) + "! Продажа через Payer за " + str(price_payer_btc) + "!")
    if price_yoomoney_btc > price_tink_btc and (
    round((price_yoomoney_btc - price_tink_btc) / price_tink_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_yoomoney_btc - price_tink_btc) / price_tink_btc * 100,
                                                2)) + "! Покупка btc через Тинькофф за " + str(
            price_tink_btc) + "! Продажа через YooMoney за " + str(price_yoomoney_btc) + "!")

    # проверяю для btc(сделал для райфа)
    if price_sb_btc > price_raif_btc and (round((price_sb_btc - price_raif_btc) / price_raif_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_sb_btc - price_raif_btc) / price_raif_btc * 100, 2)) + "! Покупка btc через Райфайзен за " + str(
            price_raif_btc) + "! Продажа через Сбербанк за " + str(price_sb_btc) + "!")
    if price_tink_btc > price_raif_btc and (round((price_tink_btc - price_raif_btc) / price_raif_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_tink_btc - price_raif_btc) / price_raif_btc * 100, 2)) + "! Покупка btc через Райфайзен за " + str(
            price_raif_btc) + "! Продажа через Тинькофф за " + str(price_tink_btc) + "!")
    if price_qiwi_btc > price_raif_btc and (round((price_qiwi_btc - price_raif_btc) / price_raif_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_qiwi_btc - price_raif_btc) / price_raif_btc * 100, 2)) + "! Покупка btc через Райфайзен за " + str(
            price_raif_btc) + "! Продажа через Qiwi за " + str(price_qiwi_btc) + "!")
    if price_payer_btc > price_raif_btc and (round((price_payer_btc - price_raif_btc) / price_raif_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_payer_btc - price_raif_btc) / price_raif_btc * 100,
                                                2)) + "! Покупка btc через Райфайзен за " + str(
            price_raif_btc) + "! Продажа через Payer за " + str(price_payer_btc) + "!")
    if price_yoomoney_btc > price_raif_btc and (
    round((price_yoomoney_btc - price_raif_btc) / price_raif_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_yoomoney_btc - price_raif_btc) / price_raif_btc * 100,
                                                2)) + "! Покупка btc через Райфайзен за " + str(
            price_raif_btc) + "! Продажа через YooMoney за " + str(price_yoomoney_btc) + "!")

    # проверяю для btc(сделал для киви)
    if price_sb_btc > price_qiwi_btc and (round((price_sb_btc - price_qiwi_btc) / price_qiwi_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_sb_btc - price_qiwi_btc) / price_qiwi_btc * 100, 2)) + "! Покупка btc через Qiwi за " + str(
            price_qiwi_btc) + "! Продажа через Сбербанк за " + str(price_sb_btc) + "!")
    if price_tink_btc > price_qiwi_btc and (round((price_tink_btc - price_qiwi_btc) / price_qiwi_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_tink_btc - price_qiwi_btc) / price_qiwi_btc * 100, 2)) + "! Покупка btc через Qiwi за " + str(
            price_qiwi_btc) + "! Продажа через Тинькофф за " + str(price_tink_btc) + "!")
    if price_raif_btc > price_qiwi_btc and (round((price_raif_btc - price_qiwi_btc) / price_qiwi_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_raif_btc - price_qiwi_btc) / price_qiwi_btc * 100, 2)) + "! Покупка btc через Qiwi за " + str(
            price_qiwi_btc) + "! Продажа через Райфайзен за " + str(price_raif_btc) + "!")
    if price_payer_btc > price_qiwi_btc and (round((price_payer_btc - price_qiwi_btc) / price_qiwi_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_payer_btc - price_qiwi_btc) / price_qiwi_btc * 100, 2)) + "! Покупка btc через Qiwi за " + str(
            price_qiwi_btc) + "! Продажа через Payer за " + str(price_payer_btc) + "!")
    if price_yoomoney_btc > price_qiwi_btc and (
    round((price_yoomoney_btc - price_qiwi_btc) / price_qiwi_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_yoomoney_btc - price_qiwi_btc) / price_qiwi_btc * 100, 2)) + "! Покупка btc через Qiwi за " + str(
            price_qiwi_btc) + "! Продажа через YooMoney за " + str(price_yoomoney_btc) + "!")

    # проверяю для btc(сделал для Payer)
    if price_sb_btc > price_payer_btc and (round((price_sb_btc - price_payer_btc) / price_payer_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_sb_btc - price_payer_btc) / price_payer_btc * 100, 2)) + "! Покупка btc через Payer за " + str(
            price_payer_btc) + "! Продажа через Сбербанк за " + str(price_sb_btc) + "!")
    if price_tink_btc > price_payer_btc and (
    round((price_tink_btc - price_payer_btc) / price_payer_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_tink_btc - price_payer_btc) / price_payer_btc * 100, 2)) + "! Покупка btc через Payer за " + str(
            price_payer_btc) + "! Продажа через Тинькофф за " + str(price_tink_btc) + "!")
    if price_raif_btc > price_payer_btc and (
    round((price_raif_btc - price_payer_btc) / price_payer_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_raif_btc - price_payer_btc) / price_payer_btc * 100, 2)) + "! Покупка btc через Payer за " + str(
            price_payer_btc) + "! Продажа через Райфайзен за " + str(price_raif_btc) + "!")
    if price_qiwi_btc > price_payer_btc and (
    round((price_qiwi_btc - price_payer_btc) / price_payer_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_qiwi_btc - price_payer_btc) / price_payer_btc * 100, 2)) + "! Покупка btc через Payer за " + str(
            price_payer_btc) + "! Продажа через Qiwi за " + str(price_qiwi_btc) + "!")
    if price_yoomoney_btc > price_payer_btc and (
    round((price_yoomoney_btc - price_payer_btc) / price_payer_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_yoomoney_btc - price_payer_btc) / price_payer_btc * 100,
                                                2)) + "! Покупка btc через Payer за " + str(
            price_payer_btc) + "! Продажа через YooMoney за " + str(price_yoomoney_btc) + "!")

    # проверяю для usdt(сделал для юмани)
    if price_sb_btc > price_yoomoney_btc and (
    round((price_sb_btc - price_yoomoney_btc) / price_yoomoney_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_sb_btc - price_yoomoney_btc) / price_yoomoney_btc * 100,
                  2)) + "! Покупка btc через YooMoney за " + str(
            price_yoomoney_btc) + "! Продажа через Сбербанк за " + str(price_sb_btc) + "!")
    if price_tink_btc > price_yoomoney_btc and (
            round((price_tink_btc - price_yoomoney_btc) / price_yoomoney_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_tink_btc - price_yoomoney_btc) / price_yoomoney_btc * 100,
                  2)) + "! Покупка btc через YooMoney за " + str(
            price_yoomoney_btc) + "! Продажа через Тинькофф за " + str(price_tink_btc) + "!")
    if price_raif_btc > price_yoomoney_btc and (
            round((price_raif_btc - price_yoomoney_btc) / price_yoomoney_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_raif_btc - price_yoomoney_btc) / price_yoomoney_btc * 100,
                  2)) + "! Покупка btc через YooMoney за " + str(
            price_yoomoney_btc) + "! Продажа через Райфайзен за " + str(price_raif_btc) + "!")
    if price_payer_btc > price_yoomoney_btc and (
            round((price_payer_btc - price_yoomoney_btc) / price_yoomoney_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_payer_btc - price_yoomoney_btc) / price_yoomoney_btc * 100,
                  2)) + "! Покупка btc через YooMoney за " + str(
            price_yoomoney_btc) + "! Продажа через Payer за " + str(price_payer_btc) + "!")
    if price_qiwi_btc > price_yoomoney_btc and (
            round((price_qiwi_btc - price_yoomoney_btc) / price_yoomoney_btc * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_qiwi_btc - price_yoomoney_btc) / price_yoomoney_btc * 100,
                  2)) + "! Покупка btc через YooMoney за " + str(
            price_yoomoney_btc) + "! Продажа через Qiwi за " + str(price_qiwi_btc) + "!")

    # проверяю для eth(сделал для сбера)
    if price_sb_eth < price_tink_eth and (round((price_tink_eth - price_sb_eth) / price_sb_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_tink_eth - price_sb_eth) / price_sb_eth * 100, 2)) + "! Покупка eth через Сбербанк за " + str(
            price_sb_eth) + "! Продажа через Тинькофф за " + str(price_tink_eth) + "!")
    if price_sb_eth < price_raif_eth and (round((price_raif_eth - price_sb_eth) / price_sb_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_raif_eth - price_sb_eth) / price_sb_eth * 100, 2)) + "! Покупка eth через Сбербанк за " + str(
            price_sb_eth) + "! Продажа через Райфайзен за " + str(price_raif_eth) + "!")
    if price_sb_eth < price_qiwi_eth and (round((price_qiwi_eth - price_sb_eth) / price_sb_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_qiwi_eth - price_sb_eth) / price_sb_eth * 100, 2)) + "! Покупка eth через Сбербанк за " + str(
            price_sb_eth) + "! Продажа через Qiwi за " + str(price_qiwi_eth) + "!")
    if price_sb_eth < price_payer_eth and (round((price_payer_eth - price_sb_eth) / price_sb_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_payer_eth - price_sb_eth) / price_sb_eth * 100, 2)) + "! Покупка eth через Сбербанк за " + str(
            price_sb_eth) + "! Продажа через Payer за " + str(price_payer_eth) + "!")

    # проверяю для eth(сделал для тиньки)
    if price_sb_eth > price_tink_eth and (round((price_sb_eth - price_tink_eth) / price_tink_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_sb_eth - price_tink_eth) / price_tink_eth * 100, 2)) + "! Покупка eth через Тинькофф за " + str(
            price_tink_eth) + "! Продажа через Сбербанк за " + str(price_sb_eth) + "!")
    if price_raif_eth > price_tink_eth and (round((price_raif_eth - price_tink_eth) / price_tink_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_raif_eth - price_tink_eth) / price_tink_eth * 100, 2)) + "! Покупка eth через Тинькофф за " + str(
            price_tink_eth) + "! Продажа через Райфайзен за " + str(price_raif_eth) + "!")
    if price_qiwi_eth > price_tink_eth and (round((price_qiwi_eth - price_tink_eth) / price_tink_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_qiwi_eth - price_tink_eth) / price_tink_eth * 100, 2)) + "! Покупка eth через Тинькофф за " + str(
            price_tink_eth) + "! Продажа через Qiwi за " + str(price_qiwi_eth) + "!")
    if price_payer_eth > price_tink_eth and (round((price_payer_eth - price_tink_eth) / price_tink_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_payer_eth - price_tink_eth) / price_tink_eth * 100, 2)) + "! Покупка eth через Тинькофф за " + str(
            price_tink_eth) + "! Продажа через Payer за " + str(price_payer_eth) + "!")

    # проверяю для eth(сделал для райфа)
    if price_sb_eth > price_raif_eth and (round((price_sb_eth - price_raif_eth) / price_raif_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_sb_eth - price_raif_eth) / price_raif_eth * 100, 2)) + "! Покупка eth через Райфайзен за " + str(
            price_raif_eth) + "! Продажа через Сбербанк за " + str(price_sb_eth) + "!")
    if price_tink_eth > price_raif_eth and (round((price_tink_eth - price_raif_eth) / price_raif_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_tink_eth - price_raif_eth) / price_raif_eth * 100, 2)) + "! Покупка eth через Райфайзен за " + str(
            price_raif_eth) + "! Продажа через Тинькофф за " + str(price_tink_eth) + "!")
    if price_qiwi_eth > price_raif_eth and (round((price_qiwi_eth - price_raif_eth) / price_raif_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_qiwi_eth - price_raif_eth) / price_raif_eth * 100, 2)) + "! Покупка eth через Райфайзен за " + str(
            price_raif_eth) + "! Продажа через Qiwi за " + str(price_qiwi_eth) + "!")
    if price_payer_eth > price_raif_eth and (round((price_payer_eth - price_raif_eth) / price_raif_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(round((price_payer_eth - price_raif_eth) / price_raif_eth * 100,
                                                2)) + "! Покупка eth через Райфайзен за " + str(
            price_raif_eth) + "! Продажа через Payer за " + str(price_payer_eth) + "!")

    # проверяю для eth(сделал для киви)
    if price_sb_eth > price_qiwi_eth and (round((price_sb_eth - price_qiwi_eth) / price_qiwi_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_sb_eth - price_qiwi_eth) / price_qiwi_eth * 100, 2)) + "! Покупка eth через Qiwi за " + str(
            price_qiwi_eth) + "! Продажа через Сбербанк за " + str(price_sb_eth) + "!")
    if price_tink_eth > price_qiwi_eth and (round((price_tink_eth - price_qiwi_eth) / price_qiwi_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_tink_eth - price_qiwi_eth) / price_qiwi_eth * 100, 2)) + "! Покупка eth через Qiwi за " + str(
            price_qiwi_eth) + "! Продажа через Тинькофф за " + str(price_tink_eth) + "!")
    if price_raif_eth > price_qiwi_eth and (round((price_raif_eth - price_qiwi_eth) / price_qiwi_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_raif_eth - price_qiwi_eth) / price_qiwi_eth * 100, 2)) + "! Покупка eth через Qiwi за " + str(
            price_qiwi_eth) + "! Продажа через Райфайзен за " + str(price_raif_eth) + "!")
    if price_payer_eth > price_qiwi_eth and (round((price_payer_eth - price_qiwi_eth) / price_qiwi_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_payer_eth - price_qiwi_eth) / price_qiwi_eth * 100, 2)) + "! Покупка eth через Qiwi за " + str(
            price_qiwi_eth) + "! Продажа через Payer за " + str(price_payer_eth) + "!")

    # проверяю для eth(сделал для Payer)
    if price_sb_eth > price_payer_eth and (round((price_sb_eth - price_payer_eth) / price_payer_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_sb_eth - price_payer_eth) / price_payer_eth * 100, 2)) + "! Покупка eth через Payer за " + str(
            price_payer_eth) + "! Продажа через Сбербанк за " + str(price_sb_eth) + "!")
    if price_tink_eth > price_payer_eth and (
    round((price_tink_eth - price_payer_eth) / price_payer_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_tink_eth - price_payer_eth) / price_payer_eth * 100, 2)) + "! Покупка eth через Payer за " + str(
            price_payer_eth) + "! Продажа через Тинькофф за " + str(price_tink_eth) + "!")
    if price_raif_eth > price_payer_eth and (
    round((price_raif_eth - price_payer_eth) / price_payer_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_raif_eth - price_payer_eth) / price_payer_eth * 100, 2)) + "! Покупка eth через Payer за " + str(
            price_payer_eth) + "! Продажа через Райфайзен за " + str(price_raif_eth) + "!")
    if price_qiwi_eth > price_payer_eth and (
    round((price_qiwi_eth - price_payer_eth) / price_payer_eth * 100, 2)) >= spread:
        good_spred.append("Спред: " + str(
            round((price_qiwi_eth - price_payer_eth) / price_payer_eth * 100, 2)) + "! Покупка eth через Payer за " + str(
            price_payer_eth) + "! Продажа через Qiwi за " + str(price_qiwi_eth) + "!")

#Связки с покупкой по тэйку, далее с 1 промежуточной операцией на споте и последующей продажей по мэйку
def take_1op_make():
    pass

if __name__ == '__main__':
    print(price_yoomoney_usdt_s,price_yoomoney_btc_s,price_yoomoney_eth_s)
