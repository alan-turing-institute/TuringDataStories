# Desert Island Discs

As the iconic BBC radio programme turns 80, we explore notable people and the music that tells the stories of their lives.

Turing Data Stories are published via fastpages and can be checked out [here](https://alan-turing-institute.github.io/TuringDataStories-fastpages/).
Alternatively users can run the stories run locally:

- `cd` to the `TuringDataStories/stories/2021-09-08-Desert-Island-Disks` directory.

- Create the `conda` virtual environment:
  ```
  conda env create
  ```

- Activate the environment:
  ```
  conda activate tds-did
  ```

- Start the notebook:
  ```
  jupyter-notebook Desert-Island-Disks.ipynb
  ```

If you get errors importing packages in the notebook it might be that the python virtual environment hasn't been correctly associated with the Jupyter kernel. In that case you can try explicitly adding the environment with the following command (after activating the environment):
```
python -m ipykernel install --user --name=tds-did
```
then start the notebook as above and select the `tds-did` kernel from the "Kernel" menu in the notebook. See [here](https://gdcoder.com/how-to-create-and-add-a-conda-environment-as-jupyter-kernel/) for more info.
