import requests
import sys
import time
import numpy as np
import random

class Crawler:
    def __init__(self, CITY_CODE = 13000, AREA_CODE = 13096):
        self.CITY_CODE = CITY_CODE
        self.AREA_CODE = AREA_CODE
        self.DEFAULT = DEFAULT = 'https://gateway.chotot.com/v1/public/ad-listing?'
        self.user_agents = [ 
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
            'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
            'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36' 
        ] 

    def run(self):
        data = []    
        page = 0
        o = -20
        sys.stdout.write('Scanning area: %d\n' % (self.AREA_CODE))
        
        while (True):
            try:
                page = page + 1
                o = o + 20
                url = self.DEFAULT + 'region_v2' + str(self.CITY_CODE) + '&area_v2=' + str(self.AREA_CODE) + '&cg=1000&o=' + str(o) + '&page=' + str(page) + '&st=s,k&limit=20&key_param_included=false'
                headers = {'User-Agent': random.choice(self.user_agents)}
                r = requests.get(headers = headers, url = url)
                json = r.json()['ads']
                if 0 == len(json):
                    break
                data.extend(json)

                sys.stdout.write('Number of items: %d \r' % (len(data)))
                sys.stdout.flush()

            except:
                pass
            
            time.sleep(np.random.choice([x/10 for x in range(3,12)]))
        
        sys.stdout.write('\n')
        sys.stdout.write('\nFinish %d items' % (len(data)))
        sys.stdout.flush()
        return data