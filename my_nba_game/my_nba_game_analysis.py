import re

with open("nba_game_warriors_thunder_20181016.txt", encoding="utf-8") as f:
    data = f.readlines()

game_analysis = {
    "home_team": {"name": "GOLDEN_STATE_WARRIORS", "players_data": []}, 
    "away_team": {"name": "OKLAHOMA_CITY_THUNDER", "players_data": []}
}

def data_ply (name) :
        return {"player_name": name, "FG": 0, "FGA": 0, "FG%": 0,
              "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0,
                "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0,
                  "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}

def player_in (P,G) :
        players_list = game_analysis[G]["players_data"]
        player_already_exist = False
        for player in players_list:
            if P == player["player_name"]:
                player_already_exist = True
                break 
        if not player_already_exist:
            player = data_ply(P)
            game_analysis[G]["players_data"].append(player)            

def get_player_data(player_name, team):
    for p in game_analysis[team]["players_data"]:
        if p["player_name"] == player_name:
            return p
    return None

def my_nba_game_analysis(param_1) :
    
    for line in param_1 :
        cols = line.strip().split("|")
        Desc = cols[7]
        name_plays = re.findall(r"\w\.\s\w+", Desc)
        
        if cols[2] == cols[4]: 
            team = "home_team"
            oposite_team = "away_team"
        else:
            team = "away_team"
            oposite_team = "home_team"


        if len(name_plays) > 1 :  
            if "assist" in Desc or "enters the game" in Desc:
                player_in(name_plays[0],team)
                player_in(name_plays[1],team)
            elif "Shooting foul by" in Desc or "Personal foul by" in Desc or "Clear path foul by" in Desc:
                player_in(name_plays[0],oposite_team)
                player_in(name_plays[1],team)
            else:
                player_in(name_plays[0],team)
                player_in(name_plays[1],oposite_team)
        elif len(name_plays) == 1:
            if "foul" not in Desc:
                player_in(name_plays[0],team)

        if "makes 2-pt" in Desc:
            stats = get_player_data(name_plays[0],team)
            if stats :
                stats["FG"] += 1
                stats["FGA"] += 1
                stats["PTS"] += 2
        elif "misses 2-pt" in Desc:
            stats = get_player_data(name_plays[0],team)
            if stats :
                stats["FGA"] += 1
                
        if "makes 3-pt" in Desc:
            stats = get_player_data(name_plays[0],team)
            if stats :
                stats["FG"] += 1
                stats["FGA"] += 1
                stats["3P"] += 1
                stats["3PA"] += 1
                stats["PTS"] += 3
        elif "misses 3-pt" in Desc:
            stats = get_player_data(name_plays[0],team)
            if stats :
                stats["FGA"] += 1
                stats["3PA"] += 1

        if len(name_plays) > 0 :
            if "free throw" in Desc:
                stats = get_player_data(name_plays[0], team)

                if stats:
                    if "makes" in Desc:
                        stats["FT"] += 1
                        stats["PTS"] += 1
                    stats["FTA"] += 1
            elif "misses free throw" in Desc:
                stats = get_player_data(name_plays[0],team)
                if stats :
                    stats["FTA"] += 1

        if len(name_plays) > 0 :
            if "Offensive rebound" in Desc:
                stats = get_player_data(name_plays[0],team)
                if stats :
                    stats["ORB"] += 1

            if "Defensive rebound" in Desc:
                    stats = get_player_data(name_plays[0],team)
                    if stats :
                        stats["DRB"] += 1

        if len(name_plays) > 1 :
            if "assist by" in Desc:
                stats = get_player_data(name_plays[1],team)
                if stats :
                    stats["AST"] += 1

            if "steal by" in Desc:
                stats = get_player_data(name_plays[1],oposite_team)
                if stats :
                    stats["STL"] += 1

            if "block by" in Desc:
                stats = get_player_data(name_plays[1],oposite_team)
                if stats :
                    stats["BLK"] += 1

        if len(name_plays) > 0 :
            if "Turnover by" in Desc:
                stats = get_player_data(name_plays[0],team)
                if stats :
                    stats["TOV"] += 1

        if "foul by" in Desc :
            stats = get_player_data(name_plays[0],oposite_team)
            if stats :
                stats["PF"] += 1

        for team in ["home_team","away_team"] :
            for stats in game_analysis[team]["players_data"] :
                if stats["FGA"] > 0 :
                    stats["FG%"] = stats["FG"]/stats["FGA"]
                
                if stats["3PA"] > 0 :
                    stats["3P%"] = stats["3P"]/stats["3PA"]
                
                if stats["FTA"] > 0 :
                    stats["FT%"] = stats["FT"]/stats["FTA"]
                
                stats["TRB"] = stats["ORB"] + stats["DRB"]
    return game_analysis

def print_nba_game_stats(team_dict) :
    header = "Players\tFG\tFGA\tFG%\t3P\t3PA\t3P%\tFT\tFTA\tFT%\tORB\tDRB\tTRB\tAST\tSTL\tBLK\tTOV\tPF\tPTS"
    print(header)

    for team in ["home_team","away_team"] :
        FG = FGA = FG100 = T3P = T3PA = T3P100 = FT = FTA	= FT100 = ORB	= DRB	= TRB	= AST = STL	= BLK	= TOV	= PF = PTS = 0
        for stats in team_dict[team]["players_data"] :
            print(
                stats["player_name"],stats["FG"],stats["FGA"],round(stats["FG%"],3),stats["3P"],stats["3PA"],round(stats["3P%"],3),stats["FT"],stats["FTA"],
                round(stats["FT%"],3),stats["ORB"],stats["DRB"],stats["TRB"],stats["AST"],stats["STL"],stats["BLK"],stats["TOV"],stats["PF"],stats["PTS"],sep="\t"
            )

            FG += stats["FG"]
            FGA += stats["FGA"]
            T3P += stats["3P"]
            T3PA += stats["3PA"]
            FT += stats["FT"]
            FTA	+= stats["FTA"]
            ORB	+= stats["ORB"]
            DRB	+= stats["DRB"]
            TRB	+= stats["TRB"]
            AST += stats["AST"]
            STL	+= stats["STL"]
            BLK	+= stats["BLK"]
            TOV	+= stats["TOV"]
            PF += stats["PF"]
            PTS += stats["PTS"]

        FG100 = round((FG / FGA),3) if FGA > 0 else ""
        T3P100 = round((T3P / T3PA),3) if T3PA > 0 else ""
        FT100 = round((FT / FTA),3) if FTA > 0 else ""

        print("Team Totals",FG,FGA,FG100,T3P,T3PA,T3P100,FT,FTA,FT100,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS,sep="\t")

print_nba_game_stats(my_nba_game_analysis(data))