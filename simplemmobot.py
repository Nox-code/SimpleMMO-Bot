import sys
import os
import time
from random import randrange
from selenium import webdriver

stepcount = 0
a = 100000


def end():
    global stepcount
    print("Stepped " + str(stepcount) + " times.")
    time.sleep(2)
    try:
        print("Closing Chrome...")
        driver.quit()
    except:
        pass
    print("Quitting...")
    try:
        sys.exit()
    except:
        os._exit(1)


def login():
    driver.get('https://web.simple-mmo.com/')
    time.sleep(12)  # Let the user actually see something!
    try:
        if driver.find_element_by_id("checkbox-label").is_displayed():
            print("CloudFlare Captcha is present. Please defeat this, log in, close browser and restart script.")
            input("Press ENTER once logged in successfully to kill script. Then you can restart.")
            end()
    except:
        pass

    driver.get("https://web.simple-mmo.com/travel")
    time.sleep(5)


def doquest(questpoints):
    if questpoints == 0:
        return
    else:
        driver.get("https://web.simple-mmo.com/quests/viewall")
        time.sleep(5)
        # view quest
        quests = driver.find_elements_by_class_name("btn-info")
        quests[0].click()
        time.sleep(3)
        # get quest name
        questname = str(driver.find_element_by_id("swal2-title").text)
        print("Doing quest: " + questname)
        # perform quest
        driver.find_element_by_class_name("swal2-confirm").click()
        for point in range(questpoints - 1):
            time.sleep(4)
            driver.find_element_by_class_name("swal2-confirm").click()
            time.sleep(4)
            print("Doing quest: " + questname)
            driver.find_element_by_class_name("swal2-confirm").click()
        time.sleep(2)
        driver.get("https://web.simple-mmo.com/travel")
        time.sleep(5)
        step(a)


def dobattle(energy):
    if energy == 0:
        return
    else:
        for point in range(energy):
            driver.get("https://web.simple-mmo.com/battlearena")
            time.sleep(5)
            driver.find_element_by_class_name("btn-custom").click()
            time.sleep(3)
            driver.find_element_by_class_name("swal2-confirm").click()
            time.sleep(5)
            print(
                "Battling " + str(driver.find_element_by_id("swal2-title").text) + " in the arena")
            driver.find_element_by_class_name("swal2-confirm").click()
            time.sleep(3)
            for i in range(8):
                try:
                    driver.find_element_by_id("attackButton").click()
                    time.sleep(1.2)
                except:
                    pass
                time.sleep(1)
            time.sleep(1)
        driver.get("https://web.simple-mmo.com/travel")
        time.sleep(5)
        step(a)


def getstate(stat):
    try:
        if stat == "questpoints":
            return int(driver.find_element_by_id("current_quest_points").text)
        elif stat == "energy":
            return int(driver.find_element_by_id("current_energy").text)
        else:
            pass
    except:
        pass


def stripchars(reward):
    reward = str(reward).lower()
    reward = ''.join(filter(str.isdigit, reward))
    return int(reward)


def attack():
    driver.find_element_by_link_text("Attack").click()
    print("Doing battle with a travelling enemy")
    time.sleep(3)
    for i in range(5):
        try:
            driver.find_element_by_id("attackButton").click()
        except:
            pass
        time.sleep(1)
    try:
        enemyname = driver.find_elements_by_xpath(
            "//*[@id='enemyBox']/div/div[2]/div/div[2]/div/h3").text
        enemylvl = driver.find_elements_by_xpath(
            "//*[@id='enemyBox']/div/div[2]/div/div[2]/div/span").text
        print("Defeated " + str(enemylvl) + " " + str(enemyname))
    except:
        pass
    time.sleep(1)
    driver.get("https://web.simple-mmo.com/travel")
    time.sleep(2)
    step(a)


def levelup():
    driver.get("https://web.simple-mmo.com/user/character")
    time.sleep(5)
    points = int(driver.find_element_by_id("available_points").text)
    if points == 0:
        pass
    else:
        dex_btn = driver.find_element_by_xpath(
            "//*[@id='kt_widget31_tab1_content']/div/div[3]/div[2]/a")
        strength_btn = driver.find_element_by_xpath(
            "//*[@id='kt_widget31_tab1_content']/div/div[1]/div[2]/a")
        strength_btn.click()
        time.sleep(1)
        point_box = driver.find_element_by_xpath(
            "/html/body/div[6]/div/div[2]/input[1]")
        point_box.send_keys(int(points / 5))
        print("Spent " + str(int(points / 5)) + " points on Strength")
        driver.find_element_by_xpath(
            "/html/body/div[6]/div/div[3]/button[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[6]/div/div[3]/button[1]").click()
        time.sleep(1)
        points = int(driver.find_element_by_id("available_points").text)
        dex_btn.click()
        time.sleep(1)
        point_box = driver.find_element_by_xpath(
            "/html/body/div[6]/div/div[2]/input[1]")
        point_box.send_keys(points)
        print("Spent " + str(points) + " points on Dexterity")
        driver.find_element_by_xpath(
            "/html/body/div[6]/div/div[3]/button[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[6]/div/div[3]/button[1]").click()
        time.sleep(1)

    driver.get("https://web.simple-mmo.com/travel")
    time.sleep(3)
    step(a)


def step(a):
    global stepcount
    while a > 0:
        # check if ready, click, delay
        try:
            if "step" in driver.find_element_by_class_name("stepbuttonnew").text:
                step_btn = driver.find_element_by_class_name("stepbuttonnew")
                step_btn.click()
                stepcount += 1
                a -= 1
                print("Step " + str(stepcount))
                if stepcount % 200 == 0:
                    levelup()
        except:
            pass
        time.sleep(2)
        # check if attack available
        try:
            if "Attack" in driver.find_element_by_link_text("Attack").text:
                attack()
                return
        except:
            pass
        # check if reward available
        try:
            if "nothing" in driver.find_element_by_class_name("reward-notice").text:
                pass
            elif "gold" in driver.find_element_by_class_name("reward-notice").text:
                reward = str(driver.find_element_by_class_name(
                    "reward-notice").text)
                print(reward)

            elif "experience" in driver.find_element_by_class_name("reward-notice").text:
                reward = str(driver.find_element_by_class_name(
                    "reward-notice").text)
                print(reward)

            elif "item" in driver.find_element_by_class_name("reward-notice").text:
                reward = str(driver.find_element_by_class_name(
                    "reward-notice").text)
                print(reward)

            else:
                pass
        except:
            pass
        # check if quest points available, do quests if so
        doquest(getstate("questpoints"))
        # check if energy available, do battle if so
        dobattle(getstate("energy"))
        # check if ready to step, if not wait
        try:
            delay = driver.find_element_by_class_name("stepbuttonnew").text
            if "step" in delay:
                pass
            else:
                time.sleep(int(delay) + 1)
        except:
            time.sleep(3)


print("Welcome to SimpleMMO Bot")
print("For first time use, please do not run headless mode, defeat the CloudFlare captcha and log in.")
print("Once finished, you can close out and restart in headless mode. This program will then launch using the cookies saved.")
print("Headless mode runs the browser in a non-visible state. This saves processing power.")
print("If you'd like to watch the bot work, don't use it.")
print("Would you like the bot to run in headless mode?")
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=SimpleMMObot")
choice = input("Y/N: ")
if choice.lower() == "y":
    options.add_argument('headless')
    print("Starting chromedriver in headless mode...")
options.add_argument("window-size=1280,720")
driver = webdriver.Chrome(options=options)
print("Loading page...")

login()
step(a)

end()
