class Agent:
    def __init__(self, code, score):
        self.code = code
        self.score = score

agents = []
for _ in range(5):
    code, score = input().split()
    score = int(score)
    agents.append(Agent(code, score))

code = ''
score = 100
idx = 0
for i in range(len(agents)):
    if score > agents[i].score:
        score = agents[i].score
        idx = i

agent = agents[idx]
print(agent.code, agent.score)