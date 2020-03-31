def switch(on_strike):
     players = {1,2}
     return list(players.difference(set([on_strike])))[0]
 
 
def get_player(previous_score, previous_player, previous_bowl_number):
    if previous_score%2 == 0 and (previous_bowl_number%6 !=0 or previous_bowl_number ==0):
         player = previous_player
    elif previous_score%2 != 0 and previous_bowl_number % 6 == 0:
         player = previous_player
    else:
         player = switch(previous_player)
    return player
 
 
 
a = [1, 2, 0, 0, 4, 1, 6, 2, 1, 3]
player_turns = []
player_score_chart = {1:0, 2:0}
total_score = 0
 
previous_score=0
previous_player=1
previous_bowl_number=0
 
for runs in a:
    player_turns.append(get_player(previous_score, previous_player, previous_bowl_number))
    previous_bowl_number+=1
    previous_score=runs
    previous_player=player_turns[-1]
    player_score_chart[previous_player] += previous_score
    total_score += previous_score
 
print 'Total Score : ', total_score
print 'Batsman 1 Score : ', player_score_chart[1]
print 'Batsman 2 Score : ', player_score_chart[2]
