from league_table import LeagueTable

if __name__ == "__main__":
    
    table = LeagueTable([
        "Mike",
        "Chris",
        "Arnold",
    ])

    table.record_result("Mike", 2)
    table.record_result("Mike", 3)
    table.record_result("Arnold", 5)
    table.record_result("Chris", 5)

    table.printTable()

    print(table.player_rank(1))


