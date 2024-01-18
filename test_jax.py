# import jax

# from jax.lib import xla_bridge
# print(xla_bridge.get_backend().platform)


import jax
print(jax.devices())

import jax.numpy as jnp
from jax import jit

import numpy as np
import timeit



def add_one0(img):
    for i in range(100):
        img2 = (img * img) / img
    return img2
            


img = np.random.rand(1000, 1000)
add_one = add_one0
add_one(img)
execution_time = timeit.timeit(lambda: add_one(img), number=10)
print(execution_time)


add_one(img)
add_one = jit(add_one0, device=jax.devices('cpu')[0])
img = jnp.array(np.random.rand(1000, 1000))


execution_time = timeit.timeit(lambda: add_one(img), number=10)
print(execution_time)




img = np.random.rand(1000, 1000)
add_one(img)
add_one = jit(add_one0, device=jax.devices('gpu')[0])
execution_time = timeit.timeit(lambda: add_one(img), number=10)
print(execution_time)












