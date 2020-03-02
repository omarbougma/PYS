import requests
from bs4 import BeautifulSoup

class PlayerInfos:
    def Rank(self):
        Soup = BeautifulSoup(response.text, 'html.parser')
        Elo = Soup.find('div',{'class':'TierRank'})
        self.elo = Elo.text
        Wins = Soup.find('span',{'class':'wins'})
        Losses = Soup.find('span',{'class':'losses'}) 
        self.wins = Wins.text
        self.losses = Losses.text
        Winrate = Soup.find('span',{'class':'winratio'})
        self.winrate = Winrate.text
        Lp = Soup.find('span',{'class':'LeaguePoints'})
        self.lp = Lp.text.strip()
    def Prints(self):
        print('********************')
        print('*     '+ self.elo + '     *')
        print('*       '+ self.lp +'       *')
        print('*    '+self.wins+' && '+self.losses+'    *')
        print('*   '+self.winrate +'  *')
        print('********************')


while 1 == 1:
   print('PlayerName : ')
   PN = input()
   url = 'https://euw.op.gg/summoner/userName=' + PN
   response = requests.get(url)
   if response.status_code == 200:
      PI = PlayerInfos()
      PI.Rank()
      PI.Prints()

    
