from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import pytest
from selenium.webdriver.support.ui import Select

from mexx.conftest import driver


class Chamados:
    def __init__(self, driver):
        self.driver = driver

    def botao_criar_chamados(self):
        # Espera até que o modal obscuring desapareça (substitua 'seletor_do_modal' pelo seletor apropriado)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.invisibility_of_element_located((By.XPATH, 'seletor_do_modal'))
            )
        except TimeoutException:
            pytest.fail("Modal ainda visível após o tempo limite estendido.")

        # Agora você pode clicar no botão de chamados
        elemento_chamados = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/main/div/div[1]/div[1]/a'))
        )
        self.driver.execute_script("arguments[0].click();", elemento_chamados)  # Use JavaScript para clicar no botão
        time.sleep(4)

    def preencher_organizacao(self):
        try:
            # Clique no campo combo-box
            combo_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/main/div/form/div/div[1]/div/div/div"))
            )
            combo_box.click()

            # Clique na opção esperada (combo-box-option-1)
            combo_box_option = self.driver.find_element(By.ID, "combo-box-option-0")
            combo_box_option.click()
        except:
            print("Não encontrado outra organização /ou usuario só possui uma organização")


    def preencher_categoria(self):
        # ================================= #
        # CAMPO CATEGORIA #
        time.sleep(3)
        try:
            # Clique no campo combo-box
            combo_boxD = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/main/div/form/div/div[3]/div/div/div")))
            combo_boxD.click()

            combo_box_option2 = self.driver.find_element(By.ID, "combo-box-option-1") ##selecione aqui o id da categoria (Recomendo utilizar o SELENIUM IDE)
            combo_box_option2.click()
        except:
            print("Organização não localizada ou o usuario possui apenas uma unica organização")
            pass

    def preencher_localizacao(self):
        time.sleep(3)
        try:
            combo_boxloc = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/main/div/form/div/div[2]/div/div/div")))
            combo_boxloc.click()

            combo_boxloc2 = self.driver.find_element(By.ID, "combo-box-option-1") ##selecione aqui o id da categoria (Recomendo utilizar o SELENIUM IDE)
            combo_boxloc2.click()

        except:
            print("Campo localização não encontrada")
            pass

    def preencher_tipo(self):
        time.sleep(3)
        try:
            combo_boxtipo = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/main/div/form/div/div[4]/div/div/div")))
            combo_boxtipo.click()

            combo_boxloc2 = self.driver.find_element(By.ID, "combo-box-option-1") ##selecione aqui o id da categoria (Recomendo utilizar o SELENIUM IDE)
            combo_boxloc2.click()
        except:
            print("Campo Tipo não localizado")
            pass

    def preencher_titulo(self):
        elemento_titulo = self.driver.find_element(By.ID, 'title')
        elemento_titulo.send_keys("Monitor não liga 3 - aut")
        self.driver.execute_script("arguments[0].scrollIntoView();", elemento_titulo)

    def preencher_descricao(self):
        self.driver.find_element(By.CLASS_NAME,'ql-editor').send_keys("monitor Não liga 3 - aut")

    def botao_enviar(self):

        # Esperar até que o botão de envio esteja visível e clicável
        elemento_enviar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.MuiButton-contained'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", elemento_enviar)
        elemento_enviar.click()



    def retornar_menu_chamadas(self):
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/header/div/button[1]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div/nav/a[1]/div[2]/span').click()



    def verificar_texto_chamado_criado(self):
        mensagem_elemento = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/main/div[2]/div/div[2]/span"))        )
        mensagem_texto = mensagem_elemento.text
        assert "Cadastrado com sucesso!" in mensagem_texto, "A mensagem esperada não foi encontrada"
        print("Mensagem exibida com sucesso!")


