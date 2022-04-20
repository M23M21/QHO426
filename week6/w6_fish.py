song = '''
Come on ladies, come on ladies
Come on ladies, come on ladies, 1 pound fish
Have, have a look, 1 pound fish
Have, have a look, 1 pound fish
Very very good, 1 pound fish
Very very cheap, 1 pound fish
6 for £5, or £1 each
6 for £5, or £1 each
Very very good and very very cheap,
One pound, one pound

Come on ladies, come on ladies
Come on ladies, come on ladies, 1 pound fish
Have, have a look, 1 pound fish
Have, have a look, 1 pound fish
Very very good, 1 pound fish
Very very cheap, 1 pound fish

Come on ladies, come on ladies
Come on ladies, come on ladies
Come on ladies, come on ladies, 1 pound fish
Come on ladies, come on ladies, 1 pound fish

Come on ladies, come on ladies, 1 pound fish

6 for £5, or £1 each
6 for £5, or £1 each
Very very good and very very cheap
One pound fish

Come on ladies, come on ladies, 1 pound fish
Come on ladies, come on ladies, 1 pound fish
'''

s1 = song.lower().replace(".", "").replace(",", "").split()
print(s1)
print("~"*30)
print(set(s1))
print("~"*30)
dicto = {}
for token in s1:
    dicto[token] = dicto.get(token, 0) + 1
print(dicto)
print("To write a viral song, you need {}".format(len(set(s1))))