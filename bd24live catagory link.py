import bs4
import requests
import csv

def function1():

    base_url = "https://www.banglanews24.com/category"
    catagory = "বিনোদন/6"
    #next_page = "18"

    national_catagory = [""]

    all_url = []
    i=0
    for page_index in national_catagory:
        i=i+1
        if i==1:
            complete_url =  str(base_url) + '/' + str(catagory) #+ '/'#+ next_page + '/'
            #print(complete_url + '18')
            #print(complete_url + '36')
        else:
            complete_url = str(base_url) + '/' + str(catagory) + str(page_index)
            #print(complete_url + '18')
            #print(complete_url + '36')
        all_url.append([complete_url])
        #all_url.append([complete_url+'?page=2'])
        #all_url.append([complete_url + '?page=1'])
        all_url.append([complete_url + '?page=2'])
        all_url.append([complete_url + '?page=3'])
        all_url.append([complete_url + '?page=4'])
        all_url.append([complete_url + '?page=5'])
        all_url.append([complete_url + '?page=6'])
        all_url.append([complete_url + '?page=7'])
        all_url.append([complete_url + '?page=8'])
        all_url.append([complete_url + '?page=9'])
        all_url.append([complete_url + '?page=10'])
        all_url.append([complete_url + '?page=11'])
        all_url.append([complete_url + '?page=12'])
        all_url.append([complete_url + '?page=13'])
        all_url.append([complete_url + '?page=14'])
        all_url.append([complete_url + '?page=15'])
        all_url.append([complete_url + '?page=16'])
        all_url.append([complete_url + '?page=17'])
        all_url.append([complete_url + '?page=18'])
        all_url.append([complete_url + '?page=19'])
        all_url.append([complete_url + '?page=20'])
        all_url.append([complete_url + '?page=21'])
        all_url.append([complete_url + '?page=22'])
        all_url.append([complete_url + '?page=23'])
        all_url.append([complete_url + '?page=24'])
        all_url.append([complete_url + '?page=25'])
        all_url.append([complete_url + '?page=26'])
        all_url.append([complete_url + '?page=27'])
        all_url.append([complete_url + '?page=28'])
        all_url.append([complete_url + '?page=29'])
        all_url.append([complete_url + '?page=30'])
        all_url.append([complete_url + '?page=31'])
        all_url.append([complete_url + '?page=32'])
        all_url.append([complete_url + '?page=33'])
        all_url.append([complete_url + '?page=34'])
        all_url.append([complete_url + '?page=35'])
        all_url.append([complete_url + '?page=36'])
        all_url.append([complete_url + '?page=37'])
        all_url.append([complete_url + '?page=38'])
        all_url.append([complete_url + '?page=39'])
        all_url.append([complete_url + '?page=40'])
        all_url.append([complete_url + '?page=41'])
        all_url.append([complete_url + '?page=42'])
        all_url.append([complete_url + '?page=43'])
        all_url.append([complete_url + '?page=44'])
        all_url.append([complete_url + '?page=45'])
        all_url.append([complete_url + '?page=46'])
        all_url.append([complete_url + '?page=47'])
        all_url.append([complete_url + '?page=48'])
        all_url.append([complete_url + '?page=49'])
        all_url.append([complete_url + '?page=50'])
        all_url.append([complete_url + '?page=51'])
        all_url.append([complete_url + '?page=52'])
        all_url.append([complete_url + '?page=53'])
        all_url.append([complete_url + '?page=54'])
        all_url.append([complete_url + '?page=55'])
        all_url.append([complete_url + '?page=56'])
        all_url.append([complete_url + '?page=57'])
        all_url.append([complete_url + '?page=58'])
        all_url.append([complete_url + '?page=59'])
        all_url.append([complete_url + '?page=60'])
        all_url.append([complete_url + '?page=61'])
        all_url.append([complete_url + '?page=62'])
        all_url.append([complete_url + '?page=63'])
        all_url.append([complete_url + '?page=64'])
        all_url.append([complete_url + '?page=65'])
        all_url.append([complete_url + '?page=66'])
        all_url.append([complete_url + '?page=67'])
        all_url.append([complete_url + '?page=68'])
        all_url.append([complete_url + '?page=69'])
        all_url.append([complete_url + '?page=70'])
        all_url.append([complete_url + '?page=71'])
        all_url.append([complete_url + '?page=72'])
        all_url.append([complete_url + '?page=73'])
        all_url.append([complete_url + '?page=74'])
        all_url.append([complete_url + '?page=75'])
        all_url.append([complete_url + '?page=76'])
        all_url.append([complete_url + '?page=77'])
        all_url.append([complete_url + '?page=78'])
        all_url.append([complete_url + '?page=79'])
        all_url.append([complete_url + '?page=80'])
        all_url.append([complete_url + '?page=81'])
        all_url.append([complete_url + '?page=82'])
        all_url.append([complete_url + '?page=83'])
        all_url.append([complete_url + '?page=84'])
        all_url.append([complete_url + '?page=85'])
        all_url.append([complete_url + '?page=86'])
        all_url.append([complete_url + '?page=87'])
        all_url.append([complete_url + '?page=88'])
        all_url.append([complete_url + '?page=89'])
        all_url.append([complete_url + '?page=90'])
        all_url.append([complete_url + '?page=91'])
        all_url.append([complete_url + '?page=92'])
        all_url.append([complete_url + '?page=93'])
        all_url.append([complete_url + '?page=94'])
        all_url.append([complete_url + '?page=95'])
        all_url.append([complete_url + '?page=96'])
        all_url.append([complete_url + '?page=97'])
        all_url.append([complete_url + '?page=98'])
        all_url.append([complete_url + '?page=99'])
        all_url.append([complete_url + '?page=100'])
        all_url.append([complete_url + '?page=101'])
        all_url.append([complete_url + '?page=102'])
        all_url.append([complete_url + '?page=103'])
        all_url.append([complete_url + '?page=104'])
        all_url.append([complete_url + '?page=105'])
        all_url.append([complete_url + '?page=106'])
        all_url.append([complete_url + '?page=107'])
        all_url.append([complete_url + '?page=108'])
        all_url.append([complete_url + '?page=109'])
        all_url.append([complete_url + '?page=110'])
        all_url.append([complete_url + '?page=111'])
        all_url.append([complete_url + '?page=112'])
        all_url.append([complete_url + '?page=113'])
        all_url.append([complete_url + '?page=114'])
        all_url.append([complete_url + '?page=115'])
        all_url.append([complete_url + '?page=116'])
        all_url.append([complete_url + '?page=117'])
        all_url.append([complete_url + '?page=118'])
        all_url.append([complete_url + '?page=119'])
        all_url.append([complete_url + '?page=120'])
        all_url.append([complete_url + '?page=121'])
        all_url.append([complete_url + '?page=122'])
        all_url.append([complete_url + '?page=123'])
        all_url.append([complete_url + '?page=124'])
        all_url.append([complete_url + '?page=125'])
        all_url.append([complete_url + '?page=126'])
        all_url.append([complete_url + '?page=127'])
        all_url.append([complete_url + '?page=128'])
        all_url.append([complete_url + '?page=129'])
        all_url.append([complete_url + '?page=130'])
        all_url.append([complete_url + '?page=131'])
        all_url.append([complete_url + '?page=132'])
        all_url.append([complete_url + '?page=133'])
        all_url.append([complete_url + '?page=134'])
        all_url.append([complete_url + '?page=135'])
        all_url.append([complete_url + '?page=136'])
        all_url.append([complete_url + '?page=137'])
        all_url.append([complete_url + '?page=138'])
        all_url.append([complete_url + '?page=139'])
        all_url.append([complete_url + '?page=140'])
        all_url.append([complete_url + '?page=141'])
        all_url.append([complete_url + '?page=142'])
        all_url.append([complete_url + '?page=143'])
        all_url.append([complete_url + '?page=144'])
        all_url.append([complete_url + '?page=145'])
        all_url.append([complete_url + '?page=146'])
        all_url.append([complete_url + '?page=147'])
        all_url.append([complete_url + '?page=148'])
        all_url.append([complete_url + '?page=149'])
        all_url.append([complete_url + '?page=150'])
        all_url.append([complete_url + '?page=151'])
        all_url.append([complete_url + '?page=152'])
        all_url.append([complete_url + '?page=153'])
        all_url.append([complete_url + '?page=154'])
        all_url.append([complete_url + '?page=155'])
        all_url.append([complete_url + '?page=156'])
        all_url.append([complete_url + '?page=157'])
        all_url.append([complete_url + '?page=158'])
        all_url.append([complete_url + '?page=159'])
        all_url.append([complete_url + '?page=160'])
        all_url.append([complete_url + '?page=161'])
        all_url.append([complete_url + '?page=162'])
        all_url.append([complete_url + '?page=163'])
        all_url.append([complete_url + '?page=164'])
        all_url.append([complete_url + '?page=165'])
        all_url.append([complete_url + '?page=166'])
        all_url.append([complete_url + '?page=167'])
        all_url.append([complete_url + '?page=168'])
        all_url.append([complete_url + '?page=169'])
        all_url.append([complete_url + '?page=170'])
        all_url.append([complete_url + '?page=171'])
        all_url.append([complete_url + '?page=172'])
        all_url.append([complete_url + '?page=173'])
        all_url.append([complete_url + '?page=174'])
        all_url.append([complete_url + '?page=175'])
        all_url.append([complete_url + '?page=176'])
        all_url.append([complete_url + '?page=177'])
        all_url.append([complete_url + '?page=178'])
        all_url.append([complete_url + '?page=179'])
        all_url.append([complete_url + '?page=180'])
        all_url.append([complete_url + '?page=181'])
        all_url.append([complete_url + '?page=182'])
        all_url.append([complete_url + '?page=183'])
        all_url.append([complete_url + '?page=184'])
        all_url.append([complete_url + '?page=185'])
        all_url.append([complete_url + '?page=186'])
        all_url.append([complete_url + '?page=187'])
        all_url.append([complete_url + '?page=188'])
        all_url.append([complete_url + '?page=189'])
        all_url.append([complete_url + '?page=190'])
        all_url.append([complete_url + '?page=191'])
        all_url.append([complete_url + '?page=192'])
        all_url.append([complete_url + '?page=193'])
        all_url.append([complete_url + '?page=194'])
        all_url.append([complete_url + '?page=195'])
        all_url.append([complete_url + '?page=196'])
        all_url.append([complete_url + '?page=197'])
        all_url.append([complete_url + '?page=198'])
        all_url.append([complete_url + '?page=199'])
        all_url.append([complete_url + '?page=200'])
        all_url.append([complete_url + '?page=201'])
        all_url.append([complete_url + '?page=202'])
        all_url.append([complete_url + '?page=203'])
        all_url.append([complete_url + '?page=204'])
        all_url.append([complete_url + '?page=205'])
        all_url.append([complete_url + '?page=206'])
        all_url.append([complete_url + '?page=207'])
        all_url.append([complete_url + '?page=208'])
        all_url.append([complete_url + '?page=209'])
        all_url.append([complete_url + '?page=210'])
        all_url.append([complete_url + '?page=211'])
        all_url.append([complete_url + '?page=212'])
        all_url.append([complete_url + '?page=213'])
        all_url.append([complete_url + '?page=214'])
        all_url.append([complete_url + '?page=215'])
        all_url.append([complete_url + '?page=216'])
        all_url.append([complete_url + '?page=217'])
        all_url.append([complete_url + '?page=218'])
        all_url.append([complete_url + '?page=219'])
        all_url.append([complete_url + '?page=220'])
        all_url.append([complete_url + '?page=221'])
        all_url.append([complete_url + '?page=222'])
        all_url.append([complete_url + '?page=223'])
        all_url.append([complete_url + '?page=224'])
        all_url.append([complete_url + '?page=225'])
        all_url.append([complete_url + '?page=226'])
        all_url.append([complete_url + '?page=227'])
        all_url.append([complete_url + '?page=228'])
        all_url.append([complete_url + '?page=229'])
        all_url.append([complete_url + '?page=230'])
        all_url.append([complete_url + '?page=231'])
        all_url.append([complete_url + '?page=232'])
        all_url.append([complete_url + '?page=233'])
        all_url.append([complete_url + '?page=234'])
        all_url.append([complete_url + '?page=235'])
        all_url.append([complete_url + '?page=236'])
        all_url.append([complete_url + '?page=237'])
        all_url.append([complete_url + '?page=238'])
        all_url.append([complete_url + '?page=239'])
        all_url.append([complete_url + '?page=240'])
        all_url.append([complete_url + '?page=241'])
        all_url.append([complete_url + '?page=242'])
        all_url.append([complete_url + '?page=243'])
        all_url.append([complete_url + '?page=244'])
        all_url.append([complete_url + '?page=245'])
        all_url.append([complete_url + '?page=246'])
        all_url.append([complete_url + '?page=247'])
        all_url.append([complete_url + '?page=248'])
        all_url.append([complete_url + '?page=249'])
        all_url.append([complete_url + '?page=250'])
        all_url.append([complete_url + '?page=251'])
        all_url.append([complete_url + '?page=252'])
        all_url.append([complete_url + '?page=253'])
        all_url.append([complete_url + '?page=254'])
        all_url.append([complete_url + '?page=255'])
        all_url.append([complete_url + '?page=256'])
        all_url.append([complete_url + '?page=257'])
        all_url.append([complete_url + '?page=258'])
        all_url.append([complete_url + '?page=259'])
        all_url.append([complete_url + '?page=260'])
        all_url.append([complete_url + '?page=261'])
        all_url.append([complete_url + '?page=262'])
        all_url.append([complete_url + '?page=263'])
        all_url.append([complete_url + '?page=264'])
        all_url.append([complete_url + '?page=265'])
        all_url.append([complete_url + '?page=266'])
        all_url.append([complete_url + '?page=267'])
        all_url.append([complete_url + '?page=268'])
        all_url.append([complete_url + '?page=269'])
        all_url.append([complete_url + '?page=270'])
        all_url.append([complete_url + '?page=271'])
        all_url.append([complete_url + '?page=272'])
        all_url.append([complete_url + '?page=273'])
        all_url.append([complete_url + '?page=274'])
        all_url.append([complete_url + '?page=275'])
        all_url.append([complete_url + '?page=276'])
        all_url.append([complete_url + '?page=277'])
        all_url.append([complete_url + '?page=278'])
        all_url.append([complete_url + '?page=279'])
        all_url.append([complete_url + '?page=280'])
        all_url.append([complete_url + '?page=281'])
        all_url.append([complete_url + '?page=282'])
        all_url.append([complete_url + '?page=283'])
        all_url.append([complete_url + '?page=284'])
        all_url.append([complete_url + '?page=285'])
        all_url.append([complete_url + '?page=286'])
        all_url.append([complete_url + '?page=287'])
        all_url.append([complete_url + '?page=288'])
        all_url.append([complete_url + '?page=289'])
        all_url.append([complete_url + '?page=290'])
        all_url.append([complete_url + '?page=291'])
        all_url.append([complete_url + '?page=292'])
        all_url.append([complete_url + '?page=293'])
        all_url.append([complete_url + '?page=294'])
        all_url.append([complete_url + '?page=295'])
        all_url.append([complete_url + '?page=296'])
        all_url.append([complete_url + '?page=297'])
        all_url.append([complete_url + '?page=298'])
        all_url.append([complete_url + '?page=299'])
        all_url.append([complete_url + '?page=300'])
        all_url.append([complete_url + '?page=301'])
        all_url.append([complete_url + '?page=302'])
        all_url.append([complete_url + '?page=303'])
        all_url.append([complete_url + '?page=304'])
        all_url.append([complete_url + '?page=305'])
        all_url.append([complete_url + '?page=306'])
        all_url.append([complete_url + '?page=307'])
        all_url.append([complete_url + '?page=308'])
        all_url.append([complete_url + '?page=309'])
        all_url.append([complete_url + '?page=310'])
        all_url.append([complete_url + '?page=311'])
        all_url.append([complete_url + '?page=312'])
        all_url.append([complete_url + '?page=313'])
        all_url.append([complete_url + '?page=314'])
        all_url.append([complete_url + '?page=315'])
        all_url.append([complete_url + '?page=316'])
        all_url.append([complete_url + '?page=317'])
        all_url.append([complete_url + '?page=318'])
        all_url.append([complete_url + '?page=319'])
        all_url.append([complete_url + '?page=320'])
        all_url.append([complete_url + '?page=321'])
        all_url.append([complete_url + '?page=322'])
        all_url.append([complete_url + '?page=323'])
        all_url.append([complete_url + '?page=324'])
        all_url.append([complete_url + '?page=325'])
        all_url.append([complete_url + '?page=326'])
        all_url.append([complete_url + '?page=327'])
        all_url.append([complete_url + '?page=328'])
        all_url.append([complete_url + '?page=329'])
        all_url.append([complete_url + '?page=330'])
        all_url.append([complete_url + '?page=331'])
        all_url.append([complete_url + '?page=332'])
        all_url.append([complete_url + '?page=333'])
        all_url.append([complete_url + '?page=334'])
        all_url.append([complete_url + '?page=335'])
        all_url.append([complete_url + '?page=336'])
        all_url.append([complete_url + '?page=337'])
        all_url.append([complete_url + '?page=338'])
        all_url.append([complete_url + '?page=339'])
        all_url.append([complete_url + '?page=340'])
        all_url.append([complete_url + '?page=341'])
        all_url.append([complete_url + '?page=342'])
        all_url.append([complete_url + '?page=343'])
        all_url.append([complete_url + '?page=344'])
        all_url.append([complete_url + '?page=345'])
        all_url.append([complete_url + '?page=346'])
        all_url.append([complete_url + '?page=347'])
        all_url.append([complete_url + '?page=348'])
        all_url.append([complete_url + '?page=349'])
        all_url.append([complete_url + '?page=350'])
        all_url.append([complete_url + '?page=351'])
        all_url.append([complete_url + '?page=352'])
        all_url.append([complete_url + '?page=353'])
        all_url.append([complete_url + '?page=354'])
        all_url.append([complete_url + '?page=355'])
        all_url.append([complete_url + '?page=356'])
        all_url.append([complete_url + '?page=357'])
        all_url.append([complete_url + '?page=358'])
        all_url.append([complete_url + '?page=359'])
        all_url.append([complete_url + '?page=360'])
        all_url.append([complete_url + '?page=361'])
        all_url.append([complete_url + '?page=362'])
        all_url.append([complete_url + '?page=363'])
        all_url.append([complete_url + '?page=364'])
        all_url.append([complete_url + '?page=365'])
        all_url.append([complete_url + '?page=366'])
        all_url.append([complete_url + '?page=367'])
        all_url.append([complete_url + '?page=368'])
        all_url.append([complete_url + '?page=369'])
        all_url.append([complete_url + '?page=370'])
        all_url.append([complete_url + '?page=371'])
        all_url.append([complete_url + '?page=372'])
        all_url.append([complete_url + '?page=373'])
        all_url.append([complete_url + '?page=374'])
        all_url.append([complete_url + '?page=375'])
        all_url.append([complete_url + '?page=376'])
        all_url.append([complete_url + '?page=377'])
        all_url.append([complete_url + '?page=378'])
        all_url.append([complete_url + '?page=379'])
        all_url.append([complete_url + '?page=380'])
        all_url.append([complete_url + '?page=381'])
        all_url.append([complete_url + '?page=382'])
        all_url.append([complete_url + '?page=383'])
        all_url.append([complete_url + '?page=384'])
        all_url.append([complete_url + '?page=385'])
        all_url.append([complete_url + '?page=386'])
        all_url.append([complete_url + '?page=387'])
        all_url.append([complete_url + '?page=388'])
        all_url.append([complete_url + '?page=389'])
        all_url.append([complete_url + '?page=390'])
        all_url.append([complete_url + '?page=391'])
        all_url.append([complete_url + '?page=392'])
        all_url.append([complete_url + '?page=393'])
        all_url.append([complete_url + '?page=394'])
        all_url.append([complete_url + '?page=395'])
        all_url.append([complete_url + '?page=396'])
        all_url.append([complete_url + '?page=397'])
        all_url.append([complete_url + '?page=398'])
        all_url.append([complete_url + '?page=399'])
        all_url.append([complete_url + '?page=400'])
        all_url.append([complete_url + '?page=401'])
        all_url.append([complete_url + '?page=402'])
        all_url.append([complete_url + '?page=403'])
        all_url.append([complete_url + '?page=404'])
        all_url.append([complete_url + '?page=405'])
        all_url.append([complete_url + '?page=406'])
        all_url.append([complete_url + '?page=407'])
        all_url.append([complete_url + '?page=408'])
        all_url.append([complete_url + '?page=409'])
        all_url.append([complete_url + '?page=410'])
        all_url.append([complete_url + '?page=411'])
        all_url.append([complete_url + '?page=412'])
        all_url.append([complete_url + '?page=413'])
        all_url.append([complete_url + '?page=414'])
        all_url.append([complete_url + '?page=415'])
        all_url.append([complete_url + '?page=416'])
        all_url.append([complete_url + '?page=417'])
        all_url.append([complete_url + '?page=418'])
        all_url.append([complete_url + '?page=419'])
        all_url.append([complete_url + '?page=420'])
        all_url.append([complete_url + '?page=421'])
        all_url.append([complete_url + '?page=422'])
        all_url.append([complete_url + '?page=423'])
        all_url.append([complete_url + '?page=424'])
        all_url.append([complete_url + '?page=425'])
        all_url.append([complete_url + '?page=426'])
        all_url.append([complete_url + '?page=427'])
        all_url.append([complete_url + '?page=428'])
        all_url.append([complete_url + '?page=429'])
        all_url.append([complete_url + '?page=430'])
        all_url.append([complete_url + '?page=431'])
        all_url.append([complete_url + '?page=432'])
        all_url.append([complete_url + '?page=433'])
        all_url.append([complete_url + '?page=434'])
        all_url.append([complete_url + '?page=435'])
        all_url.append([complete_url + '?page=436'])
        all_url.append([complete_url + '?page=437'])
        all_url.append([complete_url + '?page=438'])
        all_url.append([complete_url + '?page=439'])
        all_url.append([complete_url + '?page=440'])
        all_url.append([complete_url + '?page=441'])
        all_url.append([complete_url + '?page=442'])
        all_url.append([complete_url + '?page=443'])
        all_url.append([complete_url + '?page=444'])
        all_url.append([complete_url + '?page=445'])
        all_url.append([complete_url + '?page=446'])
        all_url.append([complete_url + '?page=447'])
        all_url.append([complete_url + '?page=448'])
        all_url.append([complete_url + '?page=449'])
        all_url.append([complete_url + '?page=450'])
        all_url.append([complete_url + '?page=451'])
        all_url.append([complete_url + '?page=452'])
        all_url.append([complete_url + '?page=453'])
        all_url.append([complete_url + '?page=454'])
        all_url.append([complete_url + '?page=455'])
        all_url.append([complete_url + '?page=456'])
        all_url.append([complete_url + '?page=457'])
        all_url.append([complete_url + '?page=458'])
        all_url.append([complete_url + '?page=459'])
        all_url.append([complete_url + '?page=460'])
        all_url.append([complete_url + '?page=461'])
        all_url.append([complete_url + '?page=462'])
        all_url.append([complete_url + '?page=463'])
        all_url.append([complete_url + '?page=464'])
        all_url.append([complete_url + '?page=465'])
        all_url.append([complete_url + '?page=466'])
        all_url.append([complete_url + '?page=467'])
        all_url.append([complete_url + '?page=468'])
        all_url.append([complete_url + '?page=469'])
        all_url.append([complete_url + '?page=470'])
        all_url.append([complete_url + '?page=471'])
        all_url.append([complete_url + '?page=472'])
        all_url.append([complete_url + '?page=473'])
        all_url.append([complete_url + '?page=474'])
        all_url.append([complete_url + '?page=475'])
        all_url.append([complete_url + '?page=476'])
        all_url.append([complete_url + '?page=477'])
        all_url.append([complete_url + '?page=478'])
        all_url.append([complete_url + '?page=479'])
        all_url.append([complete_url + '?page=480'])
        all_url.append([complete_url + '?page=481'])
        all_url.append([complete_url + '?page=482'])
        all_url.append([complete_url + '?page=483'])
        all_url.append([complete_url + '?page=484'])
        all_url.append([complete_url + '?page=485'])
        all_url.append([complete_url + '?page=486'])
        all_url.append([complete_url + '?page=487'])
        all_url.append([complete_url + '?page=488'])
        all_url.append([complete_url + '?page=489'])
        all_url.append([complete_url + '?page=490'])
        all_url.append([complete_url + '?page=491'])
        all_url.append([complete_url + '?page=492'])
        all_url.append([complete_url + '?page=493'])
        all_url.append([complete_url + '?page=494'])
        all_url.append([complete_url + '?page=495'])
        all_url.append([complete_url + '?page=496'])
        all_url.append([complete_url + '?page=497'])
        all_url.append([complete_url + '?page=498'])
        all_url.append([complete_url + '?page=499'])









    with open('main_page_url.csv',mode = 'w', newline='',encoding='utf-8') as main_url_list:
        main_url_writer = csv.writer(main_url_list,delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in all_url:
            print(url)
            main_url_writer.writerow(url)

    main_url_list.close()
    return all_url
function1()
