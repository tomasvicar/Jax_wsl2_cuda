# import jax

# from jax.lib import xla_bridge
# print(xla_bridge.get_backend().platform)


import jax
print(jax.devices())

import jax.numpy as jnp
from jax import jit

import numpy as np
import timeit


@jit
def add_one(img):
            
    return img + 1
            


img = jnp.array(np.random.rand(10, 10))

execution_time = timeit.timeit(lambda: add_one(img), number=10)
print(execution_time)



