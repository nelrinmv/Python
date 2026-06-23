p1 = int(input("Enter score of Player 1:"))
p2 = int(input("Enter score of Player 2:"))
p3 = int(input("Enter score of Player 3:"))
p4 = int(input("Enter score of Player 4:"))
p5 = int(input("Enter score of Player 5:"))
p6 = int(input("Enter score of Player 6:"))

scorelist = [p1,p2,p3,p4,p5,p6]
print("The Score list is:", scorelist)

highscore = max(scorelist)
print("The highest Score is:",highscore)

lowscore = min(scorelist)
print("The lowest score is:", lowscore)

totalscore = sum(scorelist)
print("The total runs scored in the game:", totalscore)

avgscore = totalscore/6
print("The Average score of the team was:", avgscore)

scorelist.sort()

bestperformer = max(scorelist)
print("The best performer score is:", bestperformer)

worstperformer = min(scorelist)
print("The worst performer score is:", worstperformer)

newscore = scorelist.append(50)
print("Updated list:",scorelist)