list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
colvo_players = len(list_players)
colvo_players_in_one_team = colvo_players // 2
first_team = list_players[:colvo_players_in_one_team]
second_team = list_players[colvo_players_in_one_team:]
print(first_team)
print(second_team)
# TODO Разделите участников на две команды
