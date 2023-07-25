from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

base_url = 'https://ge.globo.com/'
element_menu = 'burger'
element_link_brasileirao = 'menu-item-title'
get_primeiro = '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[1]/tbody/tr[1]/td[2]/strong'

@given(u'acesso a pagina inicial do globo esporte')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(base_url)

@when(u'Clico no menu brasileirao')
def step_impl(context):
    context.element_menu = context.driver.find_element(By.CLASS_NAME, element_menu)
    context.element_menu.click()
    sleep(20)
    context.element_link_brasileirao = context.driver.find_element(By.CLASS_NAME, element_link_brasileirao)
    context.element_link_brasileirao.click()

@when(u'classificação e exibida')
def step_impl(context):
    context.get_primeiro = context.driver.find_element(By.XPATH, get_primeiro)

@then(u'devo saber os times da tabela')
def step_impl(context):
    primeiro = context.get_primeiro.text
    print(primeiro)

    with open("features/results/results.txt", "r") as arquivo:
        conteudo = arquivo.read().strip()

    if conteudo:
        with open("features/results/results.txt", "a") as arquivo:
            arquivo.write("\n" + primeiro)
    else:
        with open("features/results/results.txt", "w") as arquivo:
            arquivo.write(primeiro)

    context.driver.quit()


#resultado no arquivo results.txt