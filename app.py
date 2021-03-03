from riotwatcher import LolWatcher

summ = 'Messenzani'
Apikey = 'tu api'
watcher = LolWatcher(Apikey)

def Stats(summonerName):
    summoner = watcher.summoner.by_name('la2', summonerName)
    stats = watcher.league.by_summoner('la2', summoner['id'])

    tier = stats[0]['tier']
    rank = stats[0]['rank']
    lp = stats[0]['leaguePoints']

    wins = int(stats[0]['wins'])
    losses = int(stats[0]['losses'])
    winrate = int((wins / (wins + losses)) * 100)

    print(summonerName,"{",
        "\n Rank:",tier, rank, "-" ,lp, "pl"
        "\n Winrate:", str(winrate) + "%\n"
        "}")
    print()

Stats(summ)