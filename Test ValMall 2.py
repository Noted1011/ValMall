from time import sleep
import os
from pystyle import *
import requests
from colored import bg, fg, attr
import AutoUpdate


AutoUpdate.set_url("https://raw.githubusercontent.com/Noted1011/ValMall/main/test.txt?token=GHSAT0AAAAAABZUTORFN74ZXUY2CKBWWSS6Y2BFLKQ")
AutoUpdate.set_current_version("0.0.1")
print(AutoUpdate.is_up_to_date())
