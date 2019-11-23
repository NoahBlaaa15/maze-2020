import Tile
import Wall

s = Tile.Tile(None, None, None, None)
t = Tile.Tile(None, None, None, None)
a = Tile.Tile(None, None, None, None)
b = Tile.Tile(None, None, None, None)

s.set_top(a)
s.set_rgt(t)
t.set_top(b)

s.set_lft(Wall.Wall())
s.set_bot(Wall.Wall())

a.set_top(Wall.Wall())
a.set_lft(Wall.Wall())
a.set_rgt(Wall.Wall())
# a.rgt.set_victim('True')

b.set_lft(Wall.Wall())
b.set_top(Wall.Wall())
b.set_rgt(Wall.Wall())

t.set_rgt(Wall.Wall())
t.set_bot(Wall.Wall())

print("s", s.get_neighbours(), s.id)
print("t", t.get_neighbours(), t.id)
print("a", a.get_neighbours(), a.id)
print("b", b.get_neighbours(), b.id)

print(a.rgt.get_victim())
