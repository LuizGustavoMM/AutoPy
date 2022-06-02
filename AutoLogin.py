from gettext import install
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#navegando pelo google
navegador = webdriver.Chrome(ChromeDriverManager().install()) 

#especificando o site a ser navegado
navegador.get("https://www.instagram.com")

sleep(3)
#insere o user no insta
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('user')
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('passwd')

#clica no login
sleep(1)
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()

#abre o direct já logado
sleep(3)
navegador.get("https://www.instagram.com/direct/inbox")

#negar notificações
sleep(3)
navegador.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()

#selecionar conversa
sleep(3)
navegador.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[7]').click()

#escrever mensagem
sleep(1)
navegador.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys('Mensagem enviada automaticamente a partir de um bot de python desenvolvido pelo teu pai')

#enviar
sleep(1)
navegador.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

sleep(10)
navegador.quit()