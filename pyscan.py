import requests
ENDPOINT = "http://192.168.1.201/bruktn/public/api/scan"


print("    ____             __   __ _")
print("   / __ )_______  __/ /__/ /( )____")
print("  / __  / ___/ / / / //_/ __/// __ \ ")
print(" / /_/ / /  / /_/ / ,< / /_  / / / /                                  ")
print("/_______/   \__,___/|_|\__/ /_/ /_/                           ______")
print("   / __ )____  / /________________ _____  ____  ___  _____   / _____\ ")
print("  / __  / __ \/ //_/ ___/ ___/ __ `/ __ \/ __ \/ _ \/ ___/  / / ___/ |")
print(" / /_/ / /_/ / ,< (__  ) /__/ /_/ / / / / / / /  __/ /     / / /__  /")
print("/_____/\____/_/|_/____/\___/\__,_/_/ /_/_/ /_/\___/_/     |  \___/ /")
print("                                                           \______/")

while True:
    word = input("SCAN KODE: ")
    DATA = {'metode': 'pyscan', 'code': word}
    r = requests.post(url=ENDPOINT, data=DATA)
    svar = r.text
    #if word.isalpha() == True:
    #    break
   # else:
    print("KODE: "+word+ " (Svar: "+svar+")")


