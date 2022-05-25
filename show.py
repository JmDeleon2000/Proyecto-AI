from Conways import *


test = conways(size = 10, max_it=1000)
test.render = True
print(test.run())

x = np.array(
    [[False,  True,  True, False, False, False, False, False, False, False],
    [False, False,  True,  True, False, False,  True,  True,  True, False,],
    [ True, False,  True,  True, False, False, False, False, False, False,],
    [False, False, False, False, False, False,  True, False, False, False,],
    [False,  True, False,  True, False,  True,  True,  True, False, False,],
    [False, False, False,  True,  True, False,  True,  True,  True, False,],
    [ True, False, False, False, False, False, False, False, False,  True,],
    [ True, False,  True, False, False, False, False, False, False, False,],
    [False,  True, False,  True,  True, False, False,  True, False,  True,],
    [ True, False, False, False, False,  True,  True, False,  True, False,],], dtype=bool)
test.reset(x, offset=False)
print(test.run())


x = np.array(
    [[ True,  True,  True,  True,  True,  True,  True, True,  True,  True],
    [ True,  True,  True,  True,  True,  True,  True,  True,  True,  True,],
    [ True,  True,  True,  True,  True,  True,  True,  True,  True,  True,],
    [ True, False,  True,  True,  True,  True,  True,  True,  True,  True,],
    [False,  True, False, False, False, False,  True,  True,  True,  True,],
    [ True, False, False, False, False,  True,  True,  True,  True,  True,],
    [False, False,  True,  True,  True, False,  True,  True,  True,  True,],
    [ True,  True,  True,  True,  True,  True,  True,  True,  True,  True,],
    [ True,  True,  True,  True,  True,  True,  True,  True,  True,  True,],
    [ True,  True,  True,  True,  True,  True,  True,  True,  True,  True,],], dtype=bool)
test.reset(x, offset=False)
print(test.run())


x = np.array(
[[False,  True,  True, False, False, False, False, False, False, False],
[False, False,  True,  True, False, False,  True,  True,  True, False,],
[ True, False,  True,  True, False, False, False, False, False, False,],
[False, False, False, False, False, False,  True, False, False, False,],
[False,  True, False,  True, False,  True,  True,  True, False, False,],
[False, False, False,  True,  True, False,  True,  True,  True, False,],
[ True, False, False, False, False, False, False, False, False,  True,],
[ True, False,  True, False, False, False, False, False, False, False,],
[False,  True, False,  True,  True, False, False,  True, False,  True,],
[ True, False, False, False, False,  True,  True, False,  True, False,],], dtype=bool)
test.reset(x, offset=False)
print(test.run())