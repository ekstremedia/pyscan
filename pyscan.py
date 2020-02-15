import requests
ENDPOINT = "http://192.168.1.201/bruktn/public/api/scan"

while True:
    word = input("SCAN KODE: ")
    DATA = {'metode':'pyscan','code':word}
    r = requests.post(url = ENDPOINT, data = DATA)
    svar = r.text
    #if word.isalpha() == True:
    #    break
   # else:
    print("KODE: "+word+ " (Svar: "+svar+")")


