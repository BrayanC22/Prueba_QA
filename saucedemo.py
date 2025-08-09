from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from config import URL, USERNAME, PASSWORD
from time import sleep

class Saucedemo:
    
    def __init__(self):
        """ Inicializar WebDriver """
        options = Options()
        options.add_argument("--start-maximized")  # Maximizar la ventana de Chrome
        options.add_argument("--disable-extensions")  # Desactivar extensiones si no las necesitas
        options.add_argument("--incognito")  # Usar Modo Incógnito para evitar alertas
        options.add_argument("--disable-notifications")  # Desactiva las notificaciones
        
        # Inicializar el WebDriver con la configuración de Service y las opciones
        service = Service(ChromeDriverManager().install())  # Inicializa el servicio de ChromeDriver
        self.driver = webdriver.Chrome(service=service, options=options)  # Usamos el servicio con opciones

    def login(self):
        """ Iniciar sesión en Saucedemo """
        self.driver.get(URL)
        self.driver.find_element(By.ID, "user-name").send_keys(USERNAME)
        self.driver.find_element(By.ID, "password").send_keys(PASSWORD)
        self.driver.find_element(By.ID, "login-button").click()

    def anadir_carrito(self):
        """ Agregar productos al carrito"""

        # Espera explícita para asegurar que los botones de agregar al carrito estén disponibles
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light")))
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    def confirmar_pago(self):
        """ Proceder al checkout """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("Brayan")
        self.driver.find_element(By.ID, "last-name").send_keys("Calvopiña")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")
        self.driver.find_element(By.ID, "continue").click()
        self.driver.find_element(By.ID, "finish").click()

    def verificar_orden(self):
        """ Verificar que la compra fue exitosa """
        confirmation_message = self.driver.find_element(By.CLASS_NAME, "complete-header").text
        if confirmation_message == "Thank you for your order!":
            print("Compra completada exitosamente.")
        else:
            print("Error en la compra.")
    
    def principal(self):
        """ Ejecutar todo el flujo de la automatización """
        self.login()
        self.anadir_carrito()
        self.confirmar_pago()
        self.verificar_orden()
        sleep(3)  # Esperar 3 segundos antes de cerrar
        self.driver.quit()  # Cerrar el navegador