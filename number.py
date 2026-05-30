#!/usr/bin/python
# -*- coding: utf-8 -*-
# Shin_Code,, Number To Email

import requests
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, init
init(autoreset=True)

def process_number(number):
    try:
        access_key = "PUT YOUR API HERE"  # Your API key
        
        api = "http://apilayer.net/api/validate"

        params = {
            "access_key": access_key,
            "number": number
        }

        response = requests.get(api, params=params)

        if response.status_code == 200:
            data = response.json()
            if data.get("success") == False:
                error_info = data.get("error", {}).get("info", "Unknown error")
                print("{}Error: {}{}".format(Fore.RED, error_info, Fore.RESET))
                return

            carrier = data.get("carrier", "")
            carrier_domains = {
    "River Wireless": "sms.3rivers.net",
    "T-Mobile": "tmomail.net",
    "Verizon": "vtext.com",
    "ACS Wireless": "paging.acswireless.com",
    "Advantage Communications": "advantagepaging.com",
    "Airtouch Pagers": "myairmail.com",
    "Airtouch Pagers 2": "alphapage.airtouch.com",
    "Airtouch Pagers 3": "airtouch.net",
    "Airtouch Pagers 4": "airtouchpaging.com",
    "AlphNow": "alphanow.net",
    "Alltel": "alltelmessage.com",
    "Alltel PCS": "message.alltel.com",
    "Ameritech Paging": "paging.acswireless.com",
    "Ameritech Paging 2": "pageapi.com",
    "Ameritech Clearpath": "clearpath.acswireless.com",
    "Andhra Pradesh Airtel": "airtelap.com",
    "Arch Pagers (PageNet)": "archwireless.net",
    "Arch Pagers (PageNet) 2": "epage.arch.com",
    "AT&T Wireless": "txt.att.net",
    "AT&T Mobility LLC": "txt.att.net",
    "Consumer Cellular (AT&T)": "txt.att.net",
    "AT&T Pocketnet PCS": "dpcs.mobile.att.net",
    "Beepwear": "beepwear.net",
    "BeeLine GSM": "sms.beemail.ru",
    "Bell Atlantic": "message.bam.com",
    "Bell Canada": "txt.bellmobility.ca",
    "Bell Canada 2": "bellmobility.ca",
    "Bell Mobility": "txt.bellmobility.ca",
    "Bell South (Blackberry)": "bellsouthtips.com",
    "Bell South": "sms.bellsouth.com",
    "Bell South 2": "wireless.bellsouth.com",
    "Bell South 3": "blsdcs.net",
    "Bell South Mobility": "blsdcs.net",
    "Blue Sky Frog": "blueskyfrog.com",
    "Bluegrass Cellular": "sms.bluecell.com",
    "Boost": "myboostmobile.com",
    "BPL mobile": "bplmobile.com",
    "Cellular One East Coast": "phone.cellone.net",
    "Cellular One South West": "swmsg.com",
    "Cellular One PCS": "paging.cellone-sf.com",
    "Cellular One": "mobile.celloneusa.com",
    "Cellular One 2": "cellularone.txtmsg.com",
    "Cellular One 3": "cellularone.textmsg.com",
    "Cellular One 4": "cell1.textmsg.com",
    "Cellular One 5": "message.cellone-sf.com",
    "Cellular One 6": "sbcemail.com",
    "Cellular One West": "mycellone.com",
    "Cellular South": "csouth1.com",
    "Central Vermont Communications": "cvcpaging.com",
    "CenturyTel": "messaging.centurytel.net",
    "Chennai RPG Cellular": "rpgmail.net",
    "Chennai Skycell / Airtel": "airtelchennai.com",
    "Cincinnati Bell": "mobile.att.net",
    "Cingular Wireless": "mycingular.textmsg.com",
    "Cingular Wireless 2": "mobile.mycingular.com",
    "Cingular Wireless 3": "mobile.mycingular.net",
    "Claro Wireless": "vtexto",
    "Clearnet": "msg.clearnet.com",
    "Comcast": "comcastpcs.textmsg.com",
    "Communication Specialists": "pageme.comspeco.net",
    "Communication Specialist Companies": "pager.comspeco.com",
    "Comviq": "sms.comviq.se",
    "Cook Paging": "cookmail.com",
    "Corr Wireless Communications": "corrwireless.net",
    "Delhi Aritel": "airtelmail.com",
    "Delhi Hutch": "delhi.hutch.co.in",
    "Digi-Page / Page Kansas": "page.hit.net",
    "Dobson Cellular Systems": "mobile.dobson.net",
    "Dobson-Alex Wireless / Dobson-Cellular One": "mobile.cellularone.com",
    "DT T-Mobile": "t-mobile-sms.de",
    "Dutchtone / Orange-NL": "sms.orange.nl",
    "Edge Wireless": "sms.edgewireless.com",
    "EMT": "sms.emt.ee",
    "Emtel": "emtelworld.net",
    "Escotel": "escotelmobile.com",
    "Fido": "fido.ca",
    "Galaxy Corporation": "epage@sendabeep.net",
    "GCS Paging": "webpager.us",
    "Goa BPLMobil": "bplmobile.com",
    "Google Project Fi": "msg.fi.google.com",
    "Golden Telecom": "sms.goldentele.com",
    "GrayLink / Porta-Phone": "epage.porta-phone.com",
    "GTE": "airmessage.net",
    "GTE 2": "gte.pagegate.net",
    "GTE 3": "messagealert.com",
    "Gujarat Celforce": "celforce.com",
    "Houston Cellular": "text.houstoncellular.net",
    "Idea Cellular": "ideacellular.net",
    "Infopage Systems": "page.infopagesystems.com",
    "Inland Cellular Telephone": "inlandlink.com",
    "JSM Tele-Page": "jsmtel.com",
    "Kerala Escotel": "escotelmobile.com",
    "Kolkata Airtel": "airtelkol.com",
    "Kyivstar": "smsmail.lmt.lv",
    "Lauttamus Communication": "e-page.net",
    "LMT": "smsmail.lmt.lv",
    "Maharashtra BPL Mobile": "bplmobile.com",
    "Maharashtra Idea Cellular": "ideacellular.net",
    "Manitoba Telecom Systems": "text.mtsmobility.com",
    "MCI Phone": "mci.com",
    "MCI": "pagemci.com",
    "Meteor": "mymeteor.ie",
    "Metrocall": "page.metrocall.com",
    "Metrocall 2-way": "my2way.com",
    "Metro PCS": "mymetropcs.com",
    "Metro PCS 2": "metropcs.sms.us",
    "Microcell": "fido.ca",
    "Midwest Wireless": "clearlydigital.com",
    "MiWorld": "m1.com.sg",
    "Mobilecom PA": "page.mobilcom.net",
    "Mobilecomm": "mobilecomm.net",
    "Mobileone": "m1.com.sg",
    "Mobilfone": "page.mobilfone.com",
    "Mobility Bermuda": "ml.bm",
    "Mobistar Belgium": "mobistar.be",
    "Mobitel Tanzania": "sms.co.tz",
    "Mobtel Srbija": "mobtel.co.yu",
    "Morris Wireless": "beepone.net",
    "Motient": "isp.com",
    "Movistar": "correo.movistar.net",
    "Mumbai BPL Mobile": "bplmobile.com",
    "Mumbai Orange": "orangemail.co.in",
    "NBTel": "wirefree.informe.ca",
    "Netcom": "sms.netcom.no",
    "Nextel": "messaging.nextel.com",
    "Nextel 2": "page.nextel.com",
    "Nextel 3": "nextel.com.br",
    "NPI Wireless": "npiwireless.com",
    "Ntelos": "pcs.ntelos.com",
    "O2": "o2.co.uk",
    "O2 (M-mail)": "mmail.co.uk",
    "Omnipoint": "omnipoint.com",
    "Omnipoint 2": "omnipointpcs.com",
    "One Connect Austria": "onemail.at",
    "OnlineBeep": "onlinebeep.net",
    "Optus Mobile": "optusmobile.com.au",
    "Orange": "orange.net",
    "Orange Mumbai": "orangemail.co.in",
    "Orange – NL / Dutchtone": "sms.orange.nl",
    "Oskar": "mujoskar.cz",
    "P&T Luxembourg": "sms.luxgsm.lu",
    "Pacific Bell": "pacbellpcs.net",
    "PageMart": "pagemart.net",
    "PageMart Advanced /2way": "airmessage.net",
    "PageMart Canada": "pmcl.net",
    "PageNet Canada": "pagegate.pagenet.ca",
    "PageOne NorthWest": "page1nw.com",
    "PCS One": "pcsone.net",
    "Personal Communication": "sms@pcom.ru",
    "Pioneer / Enid Cellular": "msg.pioneerenidcellular.com",
    "PlusGSM": "text.plusgsm.pl",
    "Pondicherry BPL Mobile": "bplmobile.com",
    "Powertel": "voicestream.net",
    "Price Communications": "mobilecell1se.com",
    "Primco": "primeco@textmsg.com",
    "Primtel": "sms.primtel.ru",
    "ProPage": "page.propage.net",
    "Public Service Cellular": "sms.pscel.com",
    "Qualcomm": "pager.qualcomm.com",
    "Qwest": "txt.qwest.com",
    "Qwest 2": "qwest.net",
    "Rogers Wireless": "sms.rogers.com",
    "Rugby Communications": "rugbycomm.com",
    "SBC Paging": "sbcglobal.net",
    "SBC Wireless": "sbcwireless.com",
    "Singtel": "singtel.com.sg",
    "SkyCell": "skycell.com",
    "Skylink": "sms.skylink.net",
    "SMS USA": "sms.usa.net",
    "Southwestern Bell": "sms.sbcglobal.net",
    "T-Mobile": "tmomail.net",
    "TDC Mobil": "tdcmobil.dk",
    "Telcel Mexico": "sms.telcel.com",
    "Telenor": "sms.telenor.com",
    "Telecom New Zealand": "text.telecom.co.nz",
    "Telefónica": "movistar.net",
    "Telekom Austria": "sms.t-mobile.at",
    "Telstra": "telstra.com.au",
    "Texas PCS": "texaspaging.com",
    "Tiscali": "sms.tiscali.it",
    "T-Mobile UK": "t-mobile.co.uk",
    "U.S. Cellular": "uscc.net",
    "Ucom Armenia": "ucom.am",
    "Virgin Mobile": "vmobl.com",
    "Vodafone": "vodafone.com",
    "Vodafone IT": "sms.vodafone.it",
    "Vodafone NZ": "sms.vodafone.net.nz",
    "Vodafone UK": "vodafone.co.uk",
    "Wavemobile": "sms.wavemobile.com",
    "Wind Mobile": "sms.windmobile.ca",
    "Xplornet": "xplornet.com",
}


            domain = carrier_domains.get(carrier)
            if domain:
                print("{}OK: {}{}{} => {}{}".format(Fore.BLUE, Fore.RESET, Fore.GREEN, number, carrier, Fore.RESET))
                with open("{}.txt".format(carrier.replace(" ", "_")), 'a') as f:
                    f.write("{}@{}\n".format(number, domain))
            else:
                print("{}Carrier for {}{}{} not recognized or custom handling needed.{}".format(Fore.RED, Fore.RESET, number, Fore.RED, Fore.RESET))
                
        else:
            print("{}Error: {}{}{}".format(Fore.RED, response.status_code, response.text, Fore.RESET))
    
    except Exception as e:
        print("{}Exception occurred: {}{}".format(Fore.RED, e, Fore.RESET))

def main():
    print "\n{} Carrier Lookup + Number To Email  | {}Shin Code\n".format(Fore.YELLOW, Fore.CYAN)
    user_input = raw_input("Number List: ").strip()
    try:
        with open(user_input, 'r') as f:
            numbers = f.read().splitlines()

        if not numbers:
            print("{}Error: Empty file. Please enter a file with a valid list of numbers.{}".format(Fore.RED, Fore.RESET))
            return

    except IOError:
        print("{}Error: File not found or cannot be opened. Please check the file path.{}".format(Fore.RED, Fore.RESET))
        return

    pool = ThreadPool(4)
    pool.map(process_number, numbers)
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
