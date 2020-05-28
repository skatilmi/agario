# auf einer party sind n gäste und jeder gast stoßt mit jedem anderen gast an, wie oft klingen gläser?


class guest:
    def __init__(self, name):
        self.name = name


guests = [guest(i) for i in range(1, 5)]
n = len(guests)

for i in range(n):
    for j in range(i, n):
        if i != j:
            print(guests[i].name, guests[j].name)
