# Eurovision story

To run the notebooks yourself, you will need a working installation of the `httpstan` package.
Installation instructions can be found [here](https://httpstan.readthedocs.io/en/latest/installation.html), but if you happen to be using an Apple Silicon Mac (which is true for most of us working on this project), a wheel for Python 3.10 has been included in this repository.
Thus, the following steps will get you set up:

```
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements-M1-python310.txt
```

If you don't have a `python3.10` executable, run `brew install python@3.10`.
