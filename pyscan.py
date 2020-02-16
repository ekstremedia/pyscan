import requests
from subprocess import call

ENDPOINT = "http://192.168.1.201/bruktn/public/api/scan"
V = "0.02"
green = "\033[1;32;38m"
endcolor = "\033[0m"

def greenText(text):
    return green+text+endcolor



print("    ")
print("   ,-----.                 ,--.     ,--.  ,--.  ")
print("   |  |) /_ ,--.--.,--.,--.|  |,-.,-'  '-.|  |,--,--, ")
print("   |  .-.  \|  .--'|  ||  ||     /'-.  .-'`-' |      \   ")
print("   |  '--' /|  |   '  ''  '|  \  \  |  |      |  ||  |      ")
print("   `------' `--'    `----' `--'`--' `--'      `--''--'         ")
print("   ,-----.         ,--.                                           ")
print("   |  |) /_  ,---. |  |,-.  ,---.  ,---. ,--,--.,--,--, ,--,--,  ,---. ,--.--. ")
print("   |  .-.  \| .-. ||     / (  .-' | .--'' ,-.  ||      \|      \| .-. :|  .--'    ")
print("   |  '--' /' '-' '|  \  \ .-'  `)\ `--.\ '-'  ||  ||  ||  ||  |\   --.|  |        ")
print("   `------'  `---' `--'`--'`----'  `---' `--`--'`--''--'`--''--' `----'`--'        ")
print("    ")
print("  v"+V+"  (C) Terje Nesthus 2020 ")
print("    ")



call(["espeak", "-vno", "Scanning er klar!"])
while True:
    word = input("SCAN KODE: ")

    DATA = {'metode': 'pyscan', 'code': word}
    r = requests.post(url=ENDPOINT, data=DATA)
    svar = r.text
    print("   KODE: "+word+ ": "+svar)


