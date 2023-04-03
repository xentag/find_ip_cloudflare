import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import re
from selenium.webdriver.common.alert import Alert
import itertools


def selen():  # функция скачивает рабочий прокси
    try:
        spisok_ip = []
        spisok_port = []
        spisok_ip_funtion = []
        spisok_ip_fun = []
        spisok_port_fun = []
        spisok_ping_fun = []
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # Строки для обхода cloudflare
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            'source': '''
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
        '''
        })
        driver.maximize_window()
        try:
            driver.get('https://hidemy.name/ru/proxy-list/?type=5#list')
            time.sleep(5)
            driver.implicitly_wait(10)
            ip = driver.find_elements(By.XPATH, '/html/body/div[1]/div[4]/div/div[4]/table/tbody/tr/td[1]')
            port = driver.find_elements(By.XPATH, '/html/body/div[1]/div[4]/div/div[4]/table/tbody/tr/td[2]')
            ping = driver.find_elements(By.XPATH, '/html/body/div[1]/div[4]/div/div[4]/table/tbody/tr/td[4]/div')
            [spisok_ip_fun.append(i.text.strip()) for i in ip]
            [spisok_port_fun.append(i.text.strip()) for i in port]
            [spisok_ping_fun.append(i.text.strip()) for i in ping]
        except Exception as e:
            print(f'Нету страниц hidemy.name {e}')

        try:
            driver.get('http://free-proxy.cz/en/proxylist/country/all/socks5/ping/all/1')
            driver.implicitly_wait(10)
            ip = driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/table/tbody/tr/td[1]')
            port = driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/table/tbody/tr/td[2]')
            [spisok_ip_funtion.append(i.text.strip()) for i in ip if str(i.text) != str('') and str(i.text) != str(' ')]
            [spisok_port.append(i.text.strip()) for i in port]
        except:
            print('Не нашло страницу free proxy')
        x = len(spisok_ip)
        for i in range(len(spisok_port) - len(spisok_ip)):
            spisok_ip.append(f'{spisok_ip_funtion[i + x]}:{spisok_port[i + x]}')
        print(len(spisok_ip), len(spisok_ip_funtion), len(spisok_port))
        try:
            driver.get('https://spys.one/socks/')
            try:
                time.sleep(10)
                driver.implicitly_wait(10)
                straniz_col = driver.find_element(By.XPATH,
                                                  '/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr[1]/td[2]/font/select[1]')
                straniz_col.click()
                [straniz_col.send_keys(Keys.DOWN) for _ in range(5)]
                time.sleep(1)
                straniz_col.send_keys(Keys.ENTER)
            except Exception as exes:
                print(f'{exes}')
            try:
                time.sleep(10)
                driver.implicitly_wait(10)
                straniz_col = driver.find_element(By.XPATH,
                                                  '/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr[1]/td[2]/font/select[1]')
                straniz_col.click()
                [straniz_col.send_keys(Keys.DOWN) for _ in range(5)]
                time.sleep(1)
                straniz_col.send_keys(Keys.ENTER)
            except Exception as exes:
                print(f'{exes}')
            time.sleep(15)
            driver.implicitly_wait(10)
            ip = driver.find_elements(By.XPATH, '/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr/td[1]')
            spisok_ip_fun = []
            [spisok_ip_fun.append(i.text.strip()) for i in ip]
            spisok_ip_fun = spisok_ip_fun[4:-3]
            for i in range(len(spisok_ip_fun)):
                spisok_ip_funtion.append(spisok_ip_fun[i].split(":")[0])
                spisok_port.append(spisok_ip_fun[i].split(":")[1])
                spisok_ip.append(f'{spisok_ip_fun[i].split(":")[0]}:{spisok_ip_fun[i].split(":")[1]}')
        except Exception as eh:
            print(f'Нету ip spys.one/socks/ {eh}')
        try:
            driver.get('https://www.freeproxy.world/?type=socks5')
            driver.implicitly_wait(10)
            ip = driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/table/tbody/tr/td[1]')
            port = driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/table/tbody/tr/td[2]/a')
            ping = driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/table/tbody/tr/td[5]/div/div/p/a')
            [spisok_ip_funtion.append(i.text.strip()) for i in ip if str(i.text) != str('') and str(i.text) != str(' ')]
            [spisok_port.append(i.text.strip()) for i in port if str(i.text) != str('') and str(i.text) != str(' ')]
            [spisok_ip.append(f'{spisok_ip_funtion[i]}:{spisok_port[i]}') for i in
             range(len(spisok_ip_funtion) - len(spisok_ip))]
        except Exception as e:
            print(f'Нету страниц freeproxy.world {e}')
        try:
            driver.get('https://advanced.name/ru/freeproxy')
            driver.implicitly_wait(10)
            type_proxy = driver.find_element(By.XPATH, '/html/body/section[2]/div[4]/table/thead/tr/th[4]/select')
            type_proxy.click()
            type_proxy.send_keys("socks5")
            time.sleep(1)
            type_proxy.send_keys(Keys.ENTER)
            time.sleep(5)
            ip = driver.find_elements(By.XPATH, '/html/body/section[2]/div[4]/table/tbody/tr/td[2]')
            port = driver.find_elements(By.XPATH, '/html/body/section[2]/div[4]/table/tbody/tr/td[3]')
            [spisok_ip_funtion.append(i.text.strip()) for i in ip if str(i.text) != str('') and str(i.text) != str(' ')]
            [spisok_port.append(i.text.strip()) for i in port if str(i.text) != str('') and str(i.text) != str(' ')]
            [spisok_ip.append(f'{spisok_ip_funtion[i]}:{spisok_port[i]}') for i in
             range(len(spisok_ip_funtion) - len(spisok_ip))]
            print(spisok_ip_funtion)
            print(spisok_port)
            print(spisok_ip)
            print(len(spisok_ip), len(spisok_ip_funtion), len(spisok_port))
        except Exception as e:
            print(f'Ошибка в advanced.name {e}')
        driver.close()
        print(len(spisok_ip), len(spisok_ip_funtion), len(spisok_port))
        return spisok_ip, spisok_ip_funtion, spisok_port
    except Exception as ex:
        print(f'Ошибка запуска хром антидект {ex}')
        time.sleep(3)
        return selen()


def open_ip(count_ip):
    ip_rabochie, spisok_ip_fun, spisok_port_fun = selen()
    with open(r"C:\Users\BERS\Desktop\ip_test_now.txt", 'r') as i:
        provekra = i.read().split()  # тут уникальные ip до порта полный номер
    proverka_unikum = []
    proverka_unikum_ip_rabochie = []
    for r in range(len(provekra)):
        ip_prov = provekra[r].strip().split('.')[0:3]
        ip_prov = ('.').join(ip_prov)
        proverka_unikum.append(ip_prov)
    for t in range(len(ip_rabochie)):
        ip_prov = ip_rabochie[t].strip().split('.')[0:3]
        ip_prov = ('.').join(ip_prov)
        proverka_unikum_ip_rabochie.append(ip_prov)

    try:
        unikalinie_ip1 = set(proverka_unikum_ip_rabochie).difference(set(proverka_unikum))
        unikalinie_ip1 = list(unikalinie_ip1)
        unikalinie_ip = []
        for i in range(len(list(unikalinie_ip1))):
            for k in range(len(ip_rabochie)):
                if re.search(str(unikalinie_ip1[i]), list(ip_rabochie)[k]):
                    print(list(ip_rabochie)[k])
                    unikalinie_ip.append(ip_rabochie[k].strip())
                    break
        print(unikalinie_ip)

        # with open(r"C:\Users\BERS\Desktop\ip_test_now.txt", 'r') as i:
        #     provekra = i.read().split()
        # try:

        #     unikalinie_ip1 = set(ip_rabochie).difference(set(provekra))  # вычитает ip уникальные не повторяющийся
        #     unikalinie_ip1 = list(unikalinie_ip1)
        #     ip_list = []
        #     for i in range(len(unikalinie_ip1)):
        #         ip = unikalinie_ip1[i].strip().split('.')[0:3]
        #         ip = ('.').join(ip)
        #         ip_list.append(ip)
        #     unikalinie_ip_proverka = list(set(ip_list))  # Уникальные ip
        #     unikalinie_ip = []
        #     for i in range(len(list(unikalinie_ip_proverka))):
        #         for k in range(len(unikalinie_ip1)):
        #             if re.search(str(unikalinie_ip_proverka[i]), list(unikalinie_ip1)[k]):
        #                 print(list(unikalinie_ip1)[k])
        #                 unikalinie_ip.append(unikalinie_ip1[k])
        #                 break
        #     print(unikalinie_ip)
        def sbor_ip_accountov(nomer_fermi):
            account_ip = []
            for j in range(35):  # ищет цикл внизу все ip в аккаунтах потом надо их расскидать по фермам
                try:
                    with open(f'C:\\Users\\BERS\\Desktop\\bot_telegram_prosmotr_reklam{nomer_fermi}\\ip{j}.txt',
                              'r') as file:
                        ip_account = file.read().splitlines()
                        account_ip.append(ip_account)
                except:
                    continue
            return account_ip

        account_ip1 = sbor_ip_accountov(nomer_fermi=1)
        account_ip2 = sbor_ip_accountov(nomer_fermi=2)
        account_ip3 = sbor_ip_accountov(nomer_fermi=3)
        account_ip1 = list(itertools.chain(*account_ip1))
        account_ip2 = list(itertools.chain(*account_ip2))
        account_ip3 = list(itertools.chain(*account_ip3))
        spisok_ip_fun, spisok_port_fun = [], []
        for j in range(len(unikalinie_ip)):
            spisok_ip_fun.append((unikalinie_ip[j].split(':')[0]))
            spisok_port_fun.append((unikalinie_ip[j].split(':')[1]))
        for k in range(len(unikalinie_ip)):  # Идет проверка ip ниже
            print(f'Количество найденных уникальных ip {count_ip} \nИз номер ip {k} из количества {len(unikalinie_ip)}')
            options = Options()
            # options.add_argument('--headless')
            options.set_preference("permissions.default.image", 2)
            # options.page_load_strategy = 'eager'
            options.set_preference('network.proxy.type', 1)
            options.set_preference('network.proxy.socks', f'{spisok_ip_fun[k]}')
            options.set_preference('network.proxy.socks_port', int(spisok_port_fun[k]))
            print(f'{spisok_ip_fun[k]}:{spisok_port_fun[k]}')
            if str(spisok_port_fun[k]) == '30000':
                continue
            else:
                options.set_preference("network.proxy.socks_version", 5)
                service = Service(
                    r'C:\Users\BERS\Desktop\poisk_ip_cloudflare\firefoxdriver\geckodriver.exe')
                driver = Firefox(service=service, options=options)
                try:
                    driver.get('https://handyclicker.botdev.me')
                    try:
                        driver.implicitly_wait(10)
                        clouflare = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/a').text
                        print(f'Защита {clouflare}')
                        driver.close()
                    except:
                        driver.close()

                        def write_ip_ferm(nomer_ferm, count_ip_new, povtor):
                            with open(f"C:\\Users\\BERS\\Desktop\\ip_test_now{nomer_ferm}.txt", 'a') as i:
                                print(
                                    f'Прошли Сlouflare \nЗаписываем в базу общиее запись уникальный ip {unikalinie_ip[k]}')
                                ip = unikalinie_ip[k]
                                i.write(f'{ip}\n')
                            if povtor == True:
                                return
                            elif nomer_ferm != '':
                                count_ip_new += 1
                                return count_ip_new
                            else:
                                return count_ip_new

                        def perebor_ip_povtor():
                            flag = False
                            for l in range(len(account_ip1)):
                                if str(account_ip1[l]) != '':
                                    if re.search(str(account_ip1[l].strip()), str(unikalinie_ip[k].strip())):
                                        write_ip_ferm(nomer_ferm=0, count_ip_new=count_ip, povtor=True)
                                        write_ip_ferm(nomer_ferm='', count_ip_new=count_ip, povtor=True)
                                        print('Занес ip в первую ферму')
                                        return flag
                            for o in range(len(account_ip2)):
                                if str(account_ip2[o]) != '':
                                    if re.search(str(account_ip2[o].strip()), str(unikalinie_ip[k].strip())):
                                        write_ip_ferm(nomer_ferm=1, count_ip_new=count_ip, povtor=True)
                                        write_ip_ferm(nomer_ferm='', count_ip_new=count_ip, povtor=True)
                                        print('Занес ip в вторую ферму')
                                        return flag
                            for p in range(len(account_ip3)):
                                if str(account_ip3[p]) != '':
                                    if re.search(str(account_ip3[p].strip()), str(unikalinie_ip[k].strip())):
                                        write_ip_ferm(nomer_ferm=2, count_ip_new=count_ip, povtor=True)
                                        write_ip_ferm(nomer_ferm='', count_ip_new=count_ip, povtor=True)
                                        print('Занес ip в третью ферму')
                                        return flag
                            flag = True
                            return flag

                        flag = perebor_ip_povtor()
                        if flag == True:
                            if count_ip % 3 == 0:
                                print(count_ip)
                                count_ip = write_ip_ferm(nomer_ferm=0, count_ip_new=count_ip, povtor=False)
                                print(count_ip)
                                write_ip_ferm(nomer_ferm='', count_ip_new=count_ip, povtor=False)
                                print(count_ip)
                            elif count_ip % 3 == 1:
                                count_ip = write_ip_ferm(nomer_ferm=1, count_ip_new=count_ip, povtor=False)
                                write_ip_ferm(nomer_ferm='', count_ip_new=count_ip, povtor=False)
                            elif count_ip % 3 == 2:
                                count_ip = write_ip_ferm(nomer_ferm=2, count_ip_new=count_ip, povtor=False)
                                write_ip_ferm(nomer_ferm='', count_ip_new=count_ip, povtor=False)
                except:
                    driver.close()
                    print('Не рабочий прокси')
    except Exception as exa:
        print(exa)


def pereprovekra_ip(nomer_fermi):
    with open(f"C:\\Users\\BERS\\Desktop\\ip_test_now{nomer_fermi}.txt", 'r') as i:
        provekra = i.readlines()  # provekra = i.read().splitlines()
        copy_list_proverka = []
        copy_list_proverka.extend(provekra)
    for x in range(len(copy_list_proverka)):
        try:
            ip = copy_list_proverka[x].strip()
            ip = ip.split(':')
            spisok_ip_fun = ip[0]
            spisok_port_fun = ip[1]
        except:
            print('Битый ip')
            continue
        print(f'Перепроверка ip {spisok_ip_fun} номер {x} из {len(copy_list_proverka)}')
        options = Options()
        # options.add_argument('--headless')
        options.set_preference("permissions.default.image", 2)
        options.set_preference('network.proxy.type', 1)
        options.set_preference('network.proxy.socks', f'{spisok_ip_fun}')
        options.set_preference('network.proxy.socks_port', int(spisok_port_fun))
        options.set_preference("network.proxy.socks_version", 5)
        service = Service(
            r'C:\Users\BERS\Desktop\poisk_ip_cloudflare\firefoxdriver\geckodriver.exe')
        driver = Firefox(service=service, options=options)
        try:
            driver.get('https://handyclicker.botdev.me')
        except:
            driver.close()
            print('Не рабочий прокси')
            for i in range(len(provekra)):
                if re.search(f'{copy_list_proverka[x]}', provekra[i]):
                    del provekra[i]
                    break
            continue
        try:
            driver.implicitly_wait(10)
            clouflare = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/a').text
            print(f'Защита {clouflare}')
            driver.close()
            for i in range(len(provekra)):
                if re.search(f'{copy_list_proverka[x]}', provekra[i]):
                    print(provekra[i])
                    del provekra[i]
                    break
            continue
        except:
            # print('Прошли Сlouflare')
            driver.close()
    with open(r"C:\Users\BERS\Desktop\proveka_ferm.txt", 'w') as p:
        p.write(f'lock')
    with open(f"C:\\Users\\BERS\\Desktop\\ip_test_now{nomer_fermi}.txt", 'w') as file:
        file.writelines(provekra)
    with open(r"C:\Users\BERS\Desktop\proveka_ferm.txt", 'w') as p:
        p.write(f'open')
    if nomer_fermi == 0:
        with open(f"C:\\Users\\BERS\\Desktop\\ip_test_now.txt", 'w') as file:
            file.writelines('')
    with open(f"C:\\Users\\BERS\\Desktop\\ip_test_now.txt", 'a') as file:
        file.writelines(provekra)


def main():
    open_ip(count_ip=0)
    pereprovekra_ip(nomer_fermi=0)
    pereprovekra_ip(nomer_fermi=1)
    pereprovekra_ip(nomer_fermi=2)
    print('Новый поиск IP')


while True:
    try:
        main()
    except:
        print('Ошибка в программе')
        time.sleep(60)
        main()
