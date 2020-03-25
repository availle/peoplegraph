import networkx as nx
import matplotlib.pyplot as plt

#Funktion, die alle Knoten des Graphen druckt
def traverseNodes(g):
    for n in g.nodes:
        print(n)

#eine durchschnittliche Person
nichthaendewascher = {
    "infektionswahrscheinlichkeit": 0.8
}
# distanz: 1 = zuwinken, 2 = hand geben, 3 = umarmen, 4 = kuscheln, 5 = sex
berufsbeziehungOhneHandgeben = {
    "art" : "beruflich",
    "distanz": 1,
}

berufsbeziehungMitHandgeben = {
    "art" : "beruflich",
    "distanz": 2,
}

freundschaft = {
    "art" : "privat",
    "distanz": 3,
}

kuschelpartnerschaft = {
    "art" : "privat",
    "distanz": 4,
}

Leute = nx.Graph()
for i in range(1,10):
    Leute.add_node(i, typ=nichthaendewascher)

# traverseNodes(G)

print(Leute)
print ("hi")

plt.subplot(121)
nx.draw(Leute, with_labels=True, font_weight='bold')
plt.show()

