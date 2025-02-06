import jax  # noqa
import jax.numpy as jnp
import numpy as np  # noqa
import pyhf
import matplotlib.pyplot as plt  # noqa

pyhf.set_backend("jax")

model = pyhf.simplemodels.uncorrelated_background(
    signal=[5.0], bkg=[10.0], bkg_uncertainty=[3.5]
)
pars = jnp.array(model.config.suggested_init())
observations = [15.0]
data = jnp.array(observations + model.config.auxdata)

best_fit = pyhf.infer.mle.fit(data, model)


def plot_gradient_map(data, model, best_fit, **kwargs):
    pass


fig, ax = plot_gradient_map(data, model, best_fit)
