# covid-vax

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/alan-turing-institute/TuringDataStories/covid-vax-forecast?filepath=stories%2Fcovid-vax%2Fcovid_vax.ipynb)

Estimating when the UK will finish vaccinating the population. Use the link above
to run the notebook in Binder, or to run it locally:

- `cd` to the `covid-vax` directory.

- Create the `conda` virtual environment:
  ```
  conda env create
  ```

- Activate the environment:
  ```
  conda activate covid-vax
  ```

- Start the notebook:
  ```
  jupyter-notebook covid_vax.ipynb
  ```

If you get errors importing packages in the notebook it might be that the python virtual environment hasn't been correctly associated with the Jupyter kernel. In that case you can try explicitly adding the environment with the following command (after activating the environment):
```
python -m ipykernel install --user --name=covid-vax
```
then start the notebook as above and select the `covid-vax` kernel from the "Kernel" menu in the notebook. See [here](https://gdcoder.com/how-to-create-and-add-a-conda-environment-as-jupyter-kernel/) for more info.
