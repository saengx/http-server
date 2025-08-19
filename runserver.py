import os, time, json




def banner():
        


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