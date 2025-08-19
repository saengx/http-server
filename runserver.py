import os, time, json
from editserver import banner


def runserver():
 try:       
     with open("online.json",encoding="utf-8") as set:
        load = set.read()
        loads = json.loads(load)
        pool = loads['pool']
        wallet = loads['wallet']
        password = loads['pass']

        print("\033[36m")
        print("การตั้งค่าที่บันทึก")
        print("POOL  =",pool)
        print("WALLET=",wallet)
        print("PASS  =",password)
        print("\033[0m\n")
 except:
        os.system("@cls||clear")
        print("เกิดข้อผิดพลาดโปรดตั้งค่าใหม่!")
        time.sleep(3)
        os.system("python3 editserver.py")

while True:
    banner()
    runserver()
    os.system("sh http-server.sh")
    break