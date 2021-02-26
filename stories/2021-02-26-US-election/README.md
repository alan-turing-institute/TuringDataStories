# Modelling Mail-In Votes in the 2020 US Election

**Author:** Eric Daub

This story describes application of a Bayesian Hierarchical model to the
mail in ballots for Pennsylvania, Georgia, and Arizona in the 2020 US
Presendential Election. Included is a markdown file containing the
text/code, an executed Jupyter Notebook containing all the images
obtained by running the code, and a static HTML version of the notebook.

**Note:** The computations required to produce the animations take
several hours due to the large volume of MCMC samples that must be drawn
to estimate the posterior distributions (samples are re-drawn for each
ballot update over the course of 12 days after the election). If users
would like to run this notebook with any changes, they should be prepared
to wait a significant amount of time to re-create the animations. However,
all of the other plots where only a single set of MCMC samples are needed
will be much faster to update (around a minute or two).

## Installation

If running this notebook directly in Binder on the Turing Data Stories page,
all required dependencies should already be present in the environment.

Users wishing to run this notebook in a standalone fashion can install
all required dependencies using `pip install -r requirements.txt`.

## Converting File Formats

The original story was written in Markdown with code blocks due to the
large size of the resulting animation files (I wished to minimize the
amount of bloat in the repo that can occur if notebooks are committed
multiple times). This conversion was done using the `notedown` Python
package (which is pip installable, and will be installed if the included
`requirements.txt` file is used to install any packages). A Makefile for
doing this conversion is provided for convenience (simply enter `make`
or `make mail_vote_model.ipynb`). Similarly, a recipe is provided for
converting the notebook to HTML (`make html` or `make mail_vote_model.html`).
