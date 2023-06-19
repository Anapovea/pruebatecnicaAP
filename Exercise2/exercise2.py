"""
## Ejercicio 2: Automatización de una web

En este ejercicio, se requiere realizar una automatización que cumpla con los siguientes pasos:
    1. Buscar en Google la palabra "automatización".
    2. Encontrar el enlace de Wikipedia resultante.
    3. Verificar en qué año se realizó el primer proceso automático.
    4. Realizar una captura de pantalla de la página de Wikipedia.

"""


import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup


class AutomatizationSearch:
    
    """
    Constructor inicializa el Selenium WebDriver
    """    
    def __init__(self):
        chrome_options = Options() #configurar el Chrome Driver
        chrome_options.add_argument("--no-sandbox") #security
        chrome_options.add_argument("--disable-dev-shm-usage") # disable memoria compartida /tmp/dev-shm en Chrome
        
        self.driver = webdriver.Chrome(options=chrome_options)
      
    """
    Aceptar COOKIES 
    """     
    def accept_cookies(self):
        time.sleep(3)
        accept_button = self.driver.find_element(By.ID, "L2AGLb")   
        accept_button.click()
        
        
    """
    Buscar en Google la palabra "automatizacion 
    """      
    def search_google(self):
        self.driver.get("https://www.google.com")
        self.accept_cookies()
        
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("automatizacion")
        time.sleep(3)
        
        search_box.send_keys(Keys.RETURN)        
        time.sleep(3)
    
    """
    Click en WIKIPEDIA Link 
    """     
    def click_wikipedia_link(self):
        wikipedia_link = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Wikipedia')]")
        wikipedia_link.click()
        time.sleep(3)
        
    """
    Obtener el año donde se realiza el primer proceso automatico 
    """         
    def obtain_first_auto_year(self):
        html_content = self.driver.page_source # devuelve el código fuente HTML 
        soupObject = BeautifulSoup(html_content, "html.parser")
        
        paragraphs = soupObject.find_all("p") #<p> 
        target_paragraph = None
        
        for paragraph in paragraphs:
            if "primer proceso" in paragraph.get_text().lower():
                target_paragraph = paragraph
                break
        
        if target_paragraph:
            first_auto_year = self.obtain_year(target_paragraph.get_text())
            if first_auto_year:
                print("El primer proceso automático se realizó en el año:", first_auto_year)
                assert first_auto_year == 1785, "El año obtenido NO es igual a 1785"
                return first_auto_year
            else:
                print("No se ha encontrado el año del primero proceso automatico.")
        else:
            print("No se ha encontrado el año del primero proceso automatico.")        
        
    
    """
    Uso de un Regex para buscar patrón 
    @Params: text es el texto del cual queremos buscar un patrón
    """       
    def obtain_year(self, text):
        patern = r'en (\d{4}), convirtiéndose en el primer proceso'
        coincidence = re.search(patern, text, re.IGNORECASE)
        if coincidence:
            return int(coincidence.group(1))
        else:
            return None
    
    """
    Hacer scroll al elemento seleccionado  
    @Params: element_to_scroll_to es el elemento a donde queremos hacer scroll
    """ 
    def scroll_to_element_with_number(self, element_to_scroll_to):
        p_elements = self.driver.find_elements(By.TAG_NAME, 'p')
        
        for element in p_elements:
            if element_to_scroll_to in element.text:
                actions = ActionChains(self.driver)
                actions.move_to_element(element)
                actions.perform()
                break
    
    """
    Tomar una captura de pantalla
    @Params: file_name es el nombre del output.png
    """ 
    def take_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)
    
    """
    Cerrar el ChromeDriver  
    """
    def close_driver(self):
        self.driver.quit()
    
    """
    Rutina  
    """
    def search_automatization(self):
        self.search_google()
        self.click_wikipedia_link()
        first_auto_year = self.obtain_first_auto_year()
        
        if first_auto_year:
            self.scroll_to_element_with_number(str(first_auto_year))
            time.sleep(5)
            self.take_screenshot("screenshot3.png")
        
        self.close_driver()


def main():
    automatization_search = AutomatizationSearch()  #instantiate
    automatization_search.search_automatization()  

if __name__ == "__main__":
    main()
