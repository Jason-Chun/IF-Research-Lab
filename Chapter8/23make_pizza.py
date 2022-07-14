import modpizza
modpizza.pizza(5, 'pepperoni')

from modpizza import pizzaa
pizzaa(9, 'cheese', 'lettuce')

from modpizza import pizzaa as p
p(10, 'cheese', 'lettuce', 'dog')

import modpizza as pz
pz.pizza(6, 'cat')

from modpizza import *
modpizza.pizza(14, 'turtle')
