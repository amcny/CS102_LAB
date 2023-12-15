def get_info():
    team_name = input("Enter team name: ")
    wins = int(input("Enter wins: "))
    losses = int(input("Enter losses: "))
    return team_name, wins, losses

def create():
    team = {}
    while True:
        name, wins, losses = get_info()
        if name == "0":
            break
        team[name] = [wins, losses]
    return team

def win(t):
    n = input("Enter team name To find the Winning percentage: ")
    l = t[n]
    per = (l[0]*100) / (l[0] + l[1])
    print("Winning percentage =", per)

def main():
    team = create()
    win(team)

main()
