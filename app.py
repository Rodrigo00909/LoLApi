from riotwatcher import LolWatcher

def Stats(summonerName, sv):
    summoner = watcher.summoner.by_name(sv, summonerName)
    print(summoner)
    stats = watcher.league.by_summoner(sv, summoner['id'])
    try:
        tier = stats[0]['tier']
        rank = stats[0]['rank']
        lp = stats[0]['leaguePoints']
        lv = summoner['summonerLevel']

        wins = int(stats[0]['wins'])
        losses = int(stats[0]['losses'])
        winrate = int((wins / (wins + losses)) * 100)

        print()
        print(summonerName,"{",
            "\n Rank:",tier, rank, "-" ,lp, "pl",
            "\n Level:", lv, 
            "\n Winrate:", str(winrate) + "%\n"
            "}")
        print()
    except IndexError:
        print('El invocador no tiene elo')
    except OSError as mensaje:
        print(mensaje)

summ = input('Nombre de invocador? ')
while summ == "":
    summ = input('Nombre de invocador? ')

sv = 'la2'
Apikey = 'tu api'
watcher = LolWatcher(Apikey)

Stats(summ, sv)