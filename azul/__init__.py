from bag import Bag
from tileSources import Factory, TableCenter
b = Bag()
print(b.state())
##print(b.take(5))
f = Factory(b, TableCenter())
f.startNewRound()
print(f.state())
print(f.take("B"))
print(f.state())