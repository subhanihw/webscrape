# TO get images of the userID

import wget
import os
import shutil

path = os.path.dirname(os.path.abspath(__file__))
newp = path+"\\n17SmsPhotos"
if os.path.exists(newp):
    shutil.rmtree(newp)
os.makedirs(newp)

for i in range(1, 1300):
    try:
        idNum = "N17"+str(i).zfill(4)
        url = "https://intranet.rguktn.ac.in/SMS/usrphotos/user/"+idNum+".jpg"
        file = wget.download(url, out=newp)
    except Exception:
        continue
print("Completed")
