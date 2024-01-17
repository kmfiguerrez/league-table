from collections import Counter
from collections import OrderedDict

class LeagueTable:

    # Constructor.
    def __init__(self, players) -> None:
        self.standings = OrderedDict([(player, Counter()) for player in players])

    
    def record_result(self, player, score):
        self.standings[player]["games_played"] += 1
        self.standings[player]["score"] += score

    
    def player_rank(self, rank):
        # Get the initial positions of the players.
        initialOrder = self.standings.keys()
        updatedOrder = []

        # Copy the Counter of each player.
        counters = [counter for counter in self.standings.values()]
        # Get the score of each player.
        scores = [counter["score"] for counter in counters]

        # Check if all scores equal.
        if all(score == scores[0] for score in scores):
            # print("Scores all tied!")

            # Check the number of games played of each player.
            games = [counter["games_played"] for counter in counters]
            # If each player played the same number of games.
            if all(game == games[0] for game in games):
                # Set the initial order of players.
                updatedOrder = initialOrder
            else:
                # Otherwise the number of games played are not the same.

                # Deduplicating or de-duping games in ascending order.
                sortedGames = sorted(set(games))

                # Get the new rank.
                for game in sortedGames:
                    for name, counter in self.standings.items():
                        if counter["games_played"] == game:
                            # Append the player's name.
                            updatedOrder.append(name)
        else:
            # Otherwise all scores are not equal.

            # Check first if there's two or more players with equal score.
            # Get the list of group of players that has the same score.
            playersOrderOnScore = []
            for score, occurence in Counter(sorted(scores, reverse=True)).items():
                if occurence == 1:
                    for name, counter in self.standings.items():
                        if counter["score"] == score:
                            playersOrderOnScore.append({"score": score, "name": name})
                            break
                else:
                    # Otherwise players are tied on a score.
                    playersOrderOnScore.append({
                        "score": score,
                        "initialPlayersOrder": [{"name": name, "games_played": counter["games_played"]} for name, counter in self.standings.items() if counter["score"] == score],
                        "updatedPlayersOrder": []
                    })

            # Check the number of games played of each player on the same score.
            for obj in playersOrderOnScore:
                if "initialPlayersOrder" in obj:
                    # Get the number of games for each player in a group.
                    games = []
                    for player in obj["initialPlayersOrder"]:
                        games.append(player["games_played"])
                    # Deduplicating or de-duping games and sorts it in ascending order.
                    sortedGames = sorted(set(games))
                    for game in sortedGames:
                        for player in obj["initialPlayersOrder"]:
                            if player["games_played"] == game:
                                obj["updatedPlayersOrder"].append(player)
            
            # Now ordering the players.
            for obj in playersOrderOnScore:
                if "updatedPlayersOrder" in obj:
                    for player in obj["updatedPlayersOrder"]:
                        updatedOrder.append(player["name"])
                else:
                    updatedOrder.append(obj["name"])
            
        print("New Rank: ", updatedOrder)

        # Finally, return data.
        try:
            # Make sure user's input data is type integer.
            playerRank = int(rank)

            if playerRank <= 0 or playerRank > len(updatedOrder):
                raise ValueError(f"Please enter number from 1-{len(updatedOrder)}")
                
            if playerRank:
                return updatedOrder[playerRank - 1]
        except (ValueError, TypeError) as e:
            print("Error: ", e)
            return

    
    def printTable(self):
        print("Name\tScore\tGames played")

        for name, counter in self.standings.items():
            print(f"{name}\t{counter["score"]}\t{counter["games_played"]}")
        
        print()