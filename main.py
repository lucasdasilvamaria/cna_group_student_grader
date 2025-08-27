from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import random

# --- Read login and password from file ---
credentials_file = "credentials.txt"
with open(credentials_file, "r") as f:
    lines = f.readlines()
    login = lines[1].strip()
    password = lines[3].strip()

# --- Launch Chrome ---
driver = webdriver.Chrome()
driver.maximize_window()

# --- Open login page ---
driver.get("https://www.cnabox.com.br/Account/Login")
time.sleep(5)

# --- First login step ---
for _ in range(5):
    pyautogui.press("tab")
pyautogui.typewrite(login)
pyautogui.press("tab")
pyautogui.typewrite(password)
pyautogui.press("tab", presses=2)
pyautogui.press("enter")

# --- Wait for second login step ---
time.sleep(10)
for _ in range(7):
    pyautogui.press("tab")
pyautogui.press("enter")

# --- Wait a random 5-10 seconds ---
time.sleep(random.randint(5, 10))

# --- Go straight to the Turma page ---
driver.get("https://www.cnabox.com.br/#/Turma")
time.sleep(5)  # wait for page to load

# --- Exact coordinates of the "Fechar" button ---
x, y = 920, 658

# --- First click on Fechar ---
pyautogui.moveTo(x, y, duration=0.5)
pyautogui.click()
print("Clicked 'Fechar' button first time at coordinates:", x, y)

# --- Press End to scroll to bottom ---
pyautogui.press("end")
time.sleep(1)

# --- Second click on Fechar coordinates ---
pyautogui.moveTo(x, y, duration=0.5)
pyautogui.click()
print("Clicked 'Fechar' button second time at coordinates:", x, y)

# --- Click the Filtrar button by ID ---
time.sleep(2)  # small pause to ensure scrolling/animation finished
try:
    filtrar_button = driver.find_element(By.ID, "btnFiltrarTurmas")
    filtrar_button.click()
    print("Clicked 'Filtrar' button successfully!")
except:
    print("'Filtrar' button not found.")

# --- Keep browser open ---
input("Press Enter to close the browser...")
driver.quit()
