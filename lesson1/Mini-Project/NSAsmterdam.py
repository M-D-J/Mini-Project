import requests
import xmltodict

def reisinfo(station):

    auth_details = ('mike.m.dejong@student.hu.nl', 'H4cctzd6FrJVd55syghnqpr9B3yCgb-GzIiXhuqZHI6J5fNR5zCwKQ')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=amsterdam'


    response = requests.get(api_url, auth=auth_details)
    vertrekXML = xmltodict.parse(response.text)
    gegevens =''



    for vertrek in vertrekXML ['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']
        vertrektijd = vertrek['VertrekTijd']
        vertrektijd = vertrektijd[11:16]
        trein=vertrek['Treinsoort']
        spoor = str(vertrek['Vertrekspoor'])
        spoor1 = spoor.replace("OrderedDict([('@wijziging', 'false'), ('#text', '", "")
        spoor2 = spoor1.replace("')])", "")
        spoor3 = spoor2.replace("OrderedDict([('@wijziging', 'true'), ('#text', '", "")
        gegevens += str('Om '+vertrektijd+' vertrekt er een ' + trein + ' richting '+ eindbestemming + ' van spoor ' + spoor3 + '\n')
    return gegevens
