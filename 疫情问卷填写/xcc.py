from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select


def auto_qiandao(username, pwds, ids):
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = "http://xgxlsg.cqbvc.edu.cn:17535/SPCP/Web/"
    driver.get(url)
    identity = driver.find_element_by_name("txtUid")
    identity.send_keys(username)
    pwd = driver.find_element_by_name("txtPwd")
    pwd.send_keys(pwds)
    code = driver.find_element_by_id("code-box").text
    driver.find_element_by_name("codeInput").send_keys(code)
    print(code)
    sleep(2)
    driver.find_element_by_id("Submit").click()
    driver.refresh()
    sleep(1)
    driver.find_element_by_xpath("//a[@href='/SPCP/Web/Report/Index']").click()
    Select(driver.find_element_by_name("City")).select_by_value("500200")
    Select(driver.find_element_by_name("County")).select_by_value(ids)
    driver.find_element_by_id("ckCLS").click()
    driver.find_element_by_xpath("//button[@class='save_form']").click()


auto_qiandao("自己的账号", "自己的密码", "乡镇代码")
# 垫江代码："500231"
