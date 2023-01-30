###########################
# Iiro Pitkänen 30.1.2023 #
###########################################################################################################################################################################################
# Tehtävänä oli pilkkoa URI:sta tarvittavat tiedot muotoon, josta ne saadaan helposti käyttöön. 
# Jokainen URI:n scheme ja path piti ensin varmistaa oikeaksi, jonka jälkeen sen sisältämä data piti pilkkoa ja muotoilla helposti luettavaan muotoon. 
# Haasteita minulle tuotti ymmärtää tehtävänanto, mutta lukemalla ja pilkkomalla se pieniin osiin tehtävä aukesi aika hyvin. Varsinkin kohdan 7 ymmärtäminen tuotti vaikeuksia. 
# Tein tehtävän haasteena ja oppimismielessä. Tehtävän annossa mainittii ajankäytöstä, mutta päätin käyttää tehtävää vähän enemmän aikaa, koska mielummin palautan toimivan
# kokonaisuuden kuin keskeneräistä työn. 
# Aloitin työn tekemällä ja testaamalla suurimman osan tarvittavista funktioista tehtävänannon järjestyksessä. Tämän jälkeen aloin miettimään fuktioiden ajamisjärjestystä ja logiikkaa. 
# Koodin kutsumista ulkopuolelta voidaan parantaa. Koodi sisältää kommentoituja print-kohtia, jotka helpottavat koodin jatkokehitystä. Datan
# ja arvojen määrää ja säilömistapaa voidaan parantaa.
###########################################################################################################################################################################################






#Esimerkki URI:t
URI1="visma-identity://login?source=severa"
URI2="visma-identity://confirm?source=netvisor&paymentnumber=102226"
URI3="visma-identity://sign?source=vismasign&documentid=105ab44"
URI=URI3


class Identity:
    #luokka johon tallennetaan saatuja arvoja URI:sta
    login =""
    confirm =""
    sign =""
    scheme = ""
    paymentnumber=""
    source=""
    documentid=""
Identity1 = Identity()

#Dictionary key-pareille
client= {   
    "paymentnumber" : "",
    "documentid" : "",
    "source" : ""
}



def visma_identity (URI):
    #Tarkistaa onko Shceme ok
    Shceme(URI)
    #Tarkistaa onko onko Path ok
    Path(URI)
    #print(Identity1.sign ,Identity1.scheme, Identity1.login, Identity1.confirm)
    for values in client.values():
        print(values)
    

def Shceme(URI):
    #Tarkistaa URI:sta löytyy visma-identity ja tallentaa sen olioon arvoksi.
    scheme = URI.startswith("visma-identity")
    #palauttaa True/False
    Identity1.scheme=scheme

def Path(URI):
    #Tarkastaa löytyykö URI:sta login, confirm tai sign
    Login(URI)
    Confirm(URI)
    Sign(URI)
    #siirtyy validation kohtaan jossa yhdistetään ylempien funktioiden tulokset
    validation(URI)


def Login(URI):
    #etsii URI:sta "login" ja tallentaa arvon True/False olioon
    login= URI.find("login")
    if int(login) == -1:
        login = False
        Identity1.login=login
    else :
        login = True
        Identity1.login=login 

def Confirm(URI):
    #etsii URI:sta "confirm" ja tallentaa arvon True/False olioon
    confirm= URI.find("confirm")
    if int(confirm) == -1:
        confirm = False
        Identity1.confirm=confirm 
    else :
        confirm = True
        Identity1.confirm=confirm
    return

def Sign(URI):
    #etsii URI:sta "sign" ja tallentaa arvon True/False olioon
    sign= URI.find("sign")
    if int(sign) == -1:
        sign = False
        Identity1.sign=sign
    else :
        sign = True
        Identity1.sign=sign
    return

def validation(URI):
    #tarkistaa että jokin (login, confirm tai sign) löytyy JA scheme on True
    if ((Identity1.login== True) or (Identity1.confirm== True) or (Identity1.sign== True) and (Identity1.scheme== True)):
        print("Validation OK")
        source(URI)
    #Vaatimukset täytetty ja ohjelma jatkaa sourceen sourceen

    else:
        print("Validation error")
    #vaatimukset ei täytetty ja ohjelma päättyy
        return

def source(URI):
    #etsii URI:sta sourcen ja & merkin jos sellainen on.
    source= URI.find("source")
    end= URI.find("&")

    #lisää olion source arvoon source=XXXX-osion
    if end== -1:
        
        source= URI[source+7:]
        Identity1.source=source
    else:
        source= URI[source+7:end]
        Identity1.source=source
    KeyValuePairs(URI)
    return

def Paymentnumber(URI):
    #Etsii URI:sta paymentnumberin ja tallentaa sen olion paymentnumber-kohtaan.
    paymentnumber= URI.find("paymentnumber")
    paymentnumber= URI[paymentnumber+14:]
    Identity1.paymentnumber=int(paymentnumber)
    #print(paymentnumber)
    return

def Documentid(URI):
    #Etsii URI:sta documentid kohdan ja sen arvon. Tallentaa saadun arvon olion documentid-arvoon.
    documentid= URI.find("documentid")
    documentid= URI[documentid+11:]
    Identity1.documentid=documentid
    #print(documentid)
    return

def KeyValuePairs(URI):
    #sourcen arvo määrittää mikä ehto toteutuu ja näin saadaan pari selvitettyä. (netvisor-paymentnumber tai vismasign-documentid). Tallentaa dictionaryyn saadut parit.
    if Identity1.source== "severa":
        print("source =", Identity1.source)
        
        return
    if Identity1.source == "netvisor":
        Paymentnumber(URI)
        #print("source =", Identity1.source)
        client.update({"source": Identity1.source})
        #print("paymentnumber=", Identity1.paymentnumber)
        client.update({"paymentnumber": Identity1.paymentnumber})
        

    if Identity1.source == "vismasign":
        Documentid(URI)
        #print("source =", Identity1.source)
        client.update({"source": Identity1.source})
        #print("vismasign = ",Identity1.documentid)
        client.update({"documentid": Identity1.documentid})
        return
        
    return
visma_identity(URI)
#Funktioita testausta varten
#Documentid(URI)
#Paymentnumber(URI)
#source(URI)
#Shceme(URI)
#Paymentnumber(URI)
