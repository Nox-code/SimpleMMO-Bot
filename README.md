# SimpleMMO-Bot
Python &amp; Selenium bot for the web based MMO SimpleMMO

Simple MMO Bot v1
-----------------

This bot will control a Chrome browser and essentially play SimpleMMO for you! Simply log in and watch it work. It will take steps, attack travelling enemies, spend quest points on quests and energy in the battle arena. It'll also spend skill points every so often on DEX to ensure you're able to complete quests with 100% ability.

Whilst developing this, it has run successfully with no errors for 12-18 hours at a time on elementaryOS, Ubuntu, Windows 10 & a Raspberry Pi 3. If it does hang however, it will just close. Proper error catching and reporting coming in the future.

--IMPORTANT--

My test account has had no attention from admins/mods either. Because there's no script changes to the site, it's (for now) reasonably undetectable. We'd advise against leaving it running 24/7 however. It's a good idea to stop the bot, log in and check your progress periodically. Equip your new gear and ensure you're outfitted to easily kill enemies you may encounter on your travels.

Please note, there is currently no graceful way of stopping and cleaning up after the bot. This will be a future update. For now, when you wish to stop the bot, simply close the command line / terminal window and kill any Chromedriver/ Google Chrome / Chromium browser processes that are still running.
This can be done easily on linux by running this command in a terminal:
Code:
pkill chrom
On Windows it's not as graceful. Open task manager and kill all Chrome processes. This will give you back that precious RAM. 
-----------------


You will need to ensure you have the following installed/set up:

-Python 3 (Program was written & debugged with Python 3.8.3 so I'd recommend updating.
-Selenium which is easily installed by running:
Code:
pip3 install selenium
-Google Chrome/Chromium web browser
-Chromedriver (Needs to be the specific version compatiable with your version of Google Chrome/Chromium browser. You can find this and details of installation at https://chromedriver.chromium.org/do...sion-selection)
Installation instructions can be found at the same link above.

My linux machine is using Chromium v 83. You can find the version you're running by navigating to chrome://settings/help within Chrome.

Download the python script

Feel free to make changes or ask questions, would be great to work on this together. Still quite new to Python and very new to bots/exploits.
Happy stepping!
