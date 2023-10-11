[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/alan-turing-institute/TuringDataStories/master?filepath=stories%2F)

<p align="center">
<img src="https://github.com/alan-turing-institute/TuringDataStories/blob/logos/logos/TDS-logo-thin.png" align="center" width="600" />
</p>

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-31-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Our stories are published online using Quarto and GitHub Pages: you can check them out [here](https://alan-turing-institute.github.io/TuringDataStories/).
Looking for how to get involved? [Click here.](https://github.com/alan-turing-institute/TuringDataStories#contributing)

### Our vision

Our aim is to help people understand the data driven world around us. We want to inspire an open community around a central platform. One that encourages us all to harness the potential of open data by creating 'data stories'. These 'data stories' will mix computer code, narrative, visuals and real world data to document an insightful result. They should relate to society in a way that people care about, and be educational. They must maintain a high standard of openness and reproducibility and be approved by the community in a peer review process. The stories will develop data literacy and critical thinking in the general readership.


### What is a Turing Data Story?

A Turing Data Story is an interactive mix of narrative, code, and visuals that derives insight from real world open data. They are written as pedagogic Jupyter notebooks that aim to spark curiosity and motivate more people to play with data.

We expect that the notebook of a data story takes the reader through each step of the analysis
done to create the data story results. Turing Data Stories should follow these principles:

* The story should be told in a pedagogical way, describing both the context of the story and the methods used in the analysis.
* The analysis must be fully reproducible (the notebooks should be able to be ran by others using a defined computer environment).
* The results should be transparent, all data sources are correctly referred to and included.
* In order to maintain the quality of the results, the Turing Data Story should be peer-reviewed by other contributors before published.


We don't expect sophisticated analyses, just interesting stories told with data. If you have an idea of a Turing Data Story you want to develop please follow our [contributing guidelines](CONTRIBUTING.md) to make sure your contributions can be easily integrated in the project. 

### Contributing

This repository is always a work in progress and **everyone** is encouraged to help us build something that will be useful to the many.

**How can I get involved?**
- **Story ideas:** Have an idea for an interesting story that could be told if you had the data, or knew how to analyse it? We can help.
- **Data:** Stumbled across an interesting dataset, or perhaps mashed together several sources of data yourself? We want to hear about it.
- **Code:** Are you an expert in Bayesian analysis? Do you have sick matplotlib skills? Put that knowledge to work!
- **Peer Review:** Know a bit about data analysis? Good at communicating that knowledge? Interested in learning about it can be applied to understanding society? We need reviews to make sure our stories are the best they can be.
- **Communication**: Are you an amazing writer? Help us with the story telling side of our stories.
- **Community:** Don't fit in any of the above categories, but still want to hang out and be involved? We've got you, drop us a line.


The process for proposing a story and reviewing a story can be found in our [submission and review guidelines](SUBMISSION_REVIEW_GUIDELINE.md).
All contributors are asked to follow our [code of conduct](CODE_OF_CONDUCT.md) and to checkout our [contributing guidelines](CONTRIBUTING.md) for more information on how to get started.

### How to Read Stories

Our stories are published online using Quarto and GitHub Pages. You can check them out [here](https://alan-turing-institute.github.io/TuringDataStories/).

Alternatively, click the binder badge at the top of this README to load an interactive version of our stories.

To build the website locally, install [Quarto](https://quarto.org/) and run from the top-level directory of this repository:
```bash
QUARTO_DENO_EXTRA_OPTIONS=--v8-flags=--stack-size=2048 quarto render
```
Note that Quarto uses precalculated outputs for each notebook cell.

Another option is to run the notebooks locally yourself.
Some of the notebooks have `requirements.txt` files inside their respective subdirectories; you can set up a virtual environment to run the notebooks using

```bash
python -m venv tds_venv
source tds_venv/bin/activate
python -m pip install -r requirements.txt
```

If this is not present, then you will need to instead use the `binder/environment.yml` file with [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/):
```bash
conda env create -f binder/environment.yml
```

Any problems, open an issue!


### Adding a new story

Under the `stories` directory, create a new folder with the name `YYYY-MM-DD-<Title>` and place your notebook inside there.
Make sure you have already run all the cells in your notebook. Add a `preview.png` with the figure you want to be previewed with Quarto. 
That's all!

If your notebook is not ready to be published to the web, you can prefix the folder with an underscore: Quarto will then ignore it.

### About the project

This project was initially formed by a desire to contribute and advance to the analysis of government COVID-19 data.

As part of this process we recognised that government reporting of COVID-19 data was not always in the most accessible format. We also recognised that especially during these times, many individuals may be interested in developing their technical skills in an impactful way, but not know where to start.

Our goal was therefore to help provide educational data science content that would guide the user through the process of making the data accessible, to using the data for analysis.

We hope that by using the story telling medium, we can bring people along the data science journey and showcase how these techniques can answer both fascinating and socially relevant questions. 


### The team

The team is currently composed of four members:

* David Beavan - GitHub:[@DavidBeavan](https://github.com/DavidBeavan) Twitter:[@DavidBeavan](https://twitter.com/davidbeavan) Web:[https://www.turing.ac.uk/people/researchers/david-beavan](https://www.turing.ac.uk/people/researchers/david-beavan)
* Camila Rangel Smith - GitHub:[@crangelsmith](https://github.com/crangelsmith). Twitter:[@CamilaRangelS](https://twitter.com/CamilaRangelS). Web:[https://www.turing.ac.uk/people/researchers/camila-rangel-smith](https://www.turing.ac.uk/people/researchers/camila-rangel-smith)

* Sam Van Stroud - Github: [@samvanstroud](https://github.com/samvanstroud). Web:[https://www.turing.ac.uk/people/enrichment-students/sam-van-stroud](https://www.turing.ac.uk/people/enrichment-students/sam-van-stroud)
* Kevin Xu - Github: [@kevinxufs](https://github.com/kevinxufs)

We currently meet every Wednesday afternoon



### Citing _TuringDataStories_

Beavan, D., C. Rangel Smith, S. Van Stroud, and K. Xu. Turing Data Stories, 2020. https://github.com/alan-turing-institute/TuringDataStories.

```
@misc{beavan_turing_2020,
	title = {Turing {Data} {Stories}},
	url = {https://github.com/alan-turing-institute/TuringDataStories},
	author = {Beavan, D. and Rangel Smith, C. and Van Stroud, S. and Xu, K.},
	year = {2020}
}
```

### Get in touch


You can join our community at Slack 🏡 (turingdatastories.slack.com) by opening an issue here along with your email id.
We virtually meet on Wednesday afternoons to work collaboratively.  


## Contributors ✨

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kevinxufs"><img src="https://avatars2.githubusercontent.com/u/48526846?v=4?s=100" width="100px;" alt="kevinxufs"/><br /><sub><b>kevinxufs</b></sub></a><br /><a href="#ideas-kevinxufs" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=kevinxufs" title="Tests">⚠️</a> <a href="#content-kevinxufs" title="Content">🖋</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=kevinxufs" title="Code">💻</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=kevinxufs" title="Documentation">📖</a> <a href="#projectManagement-kevinxufs" title="Project Management">📆</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/crangelsmith"><img src="https://avatars2.githubusercontent.com/u/11162074?v=4?s=100" width="100px;" alt="Camila Rangel Smith"/><br /><sub><b>Camila Rangel Smith</b></sub></a><br /><a href="#ideas-crangelsmith" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=crangelsmith" title="Tests">⚠️</a> <a href="#content-crangelsmith" title="Content">🖋</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=crangelsmith" title="Code">💻</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=crangelsmith" title="Documentation">📖</a> <a href="#projectManagement-crangelsmith" title="Project Management">📆</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/DavidBeavan"><img src="https://avatars3.githubusercontent.com/u/6524799?v=4?s=100" width="100px;" alt="David Beavan"/><br /><sub><b>David Beavan</b></sub></a><br /><a href="#ideas-DavidBeavan" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=DavidBeavan" title="Tests">⚠️</a> <a href="#content-DavidBeavan" title="Content">🖋</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=DavidBeavan" title="Code">💻</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=DavidBeavan" title="Documentation">📖</a> <a href="#projectManagement-DavidBeavan" title="Project Management">📆</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/samvanstroud"><img src="https://avatars0.githubusercontent.com/u/16232199?v=4?s=100" width="100px;" alt="Sam Vs"/><br /><sub><b>Sam Vs</b></sub></a><br /><a href="#ideas-samvanstroud" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=samvanstroud" title="Tests">⚠️</a> <a href="#content-samvanstroud" title="Content">🖋</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=samvanstroud" title="Code">💻</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=samvanstroud" title="Documentation">📖</a> <a href="#projectManagement-samvanstroud" title="Project Management">📆</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://yo-yehudi.com"><img src="https://avatars0.githubusercontent.com/u/9271438?v=4?s=100" width="100px;" alt="Yo Yehudi"/><br /><sub><b>Yo Yehudi</b></sub></a><br /><a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=yochannah" title="Documentation">📖</a> <a href="#ideas-yochannah" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/LouiseABowler"><img src="https://avatars1.githubusercontent.com/u/25640708?v=4?s=100" width="100px;" alt="Louise Bowler"/><br /><sub><b>Louise Bowler</b></sub></a><br /><a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3ALouiseABowler" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/nbarlowATI"><img src="https://avatars3.githubusercontent.com/u/33832774?v=4?s=100" width="100px;" alt="nbarlowATI"/><br /><sub><b>nbarlowATI</b></sub></a><br /><a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3AnbarlowATI" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/martintoreilly"><img src="https://avatars3.githubusercontent.com/u/21147592?v=4?s=100" width="100px;" alt="Martin O'Reilly"/><br /><sub><b>Martin O'Reilly</b></sub></a><br /><a href="#ideas-martintoreilly" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/edaub"><img src="https://avatars0.githubusercontent.com/u/45598892?v=4?s=100" width="100px;" alt="Eric Daub"/><br /><sub><b>Eric Daub</b></sub></a><br /><a href="#blog-edaub" title="Blogposts">📝</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=edaub" title="Code">💻</a> <a href="#ideas-edaub" title="Ideas, Planning, & Feedback">🤔</a> <a href="#content-edaub" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jack89roberts"><img src="https://avatars.githubusercontent.com/u/16308271?v=4?s=100" width="100px;" alt="Jack Roberts"/><br /><sub><b>Jack Roberts</b></sub></a><br /><a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3Ajack89roberts" title="Reviewed Pull Requests">👀</a> <a href="#blog-jack89roberts" title="Blogposts">📝</a> <a href="#ideas-jack89roberts" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/billfinnegan"><img src="https://avatars.githubusercontent.com/u/79983583?v=4?s=100" width="100px;" alt="billfinnegan"/><br /><sub><b>billfinnegan</b></sub></a><br /><a href="#ideas-billfinnegan" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3Abillfinnegan" title="Reviewed Pull Requests">👀</a> <a href="#content-billfinnegan" title="Content">🖋</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=billfinnegan" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/helendduncan"><img src="https://avatars.githubusercontent.com/u/46891265?v=4?s=100" width="100px;" alt="Helen Duncan"/><br /><sub><b>Helen Duncan</b></sub></a><br /><a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=helendduncan" title="Code">💻</a> <a href="#data-helendduncan" title="Data">🔣</a> <a href="#ideas-helendduncan" title="Ideas, Planning, & Feedback">🤔</a> <a href="#projectManagement-helendduncan" title="Project Management">📆</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3Ahelendduncan" title="Reviewed Pull Requests">👀</a> <a href="#content-helendduncan" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ChristinaLast"><img src="https://avatars.githubusercontent.com/u/36204574?v=4?s=100" width="100px;" alt="Christina Last"/><br /><sub><b>Christina Last</b></sub></a><br /><a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=ChristinaLast" title="Code">💻</a> <a href="#data-ChristinaLast" title="Data">🔣</a> <a href="#ideas-ChristinaLast" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3AChristinaLast" title="Reviewed Pull Requests">👀</a> <a href="#content-ChristinaLast" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lukehare"><img src="https://avatars.githubusercontent.com/u/44277986?v=4?s=100" width="100px;" alt="lukehare"/><br /><sub><b>lukehare</b></sub></a><br /><a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=lukehare" title="Code">💻</a> <a href="#data-lukehare" title="Data">🔣</a> <a href="#ideas-lukehare" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3Alukehare" title="Reviewed Pull Requests">👀</a> <a href="#content-lukehare" title="Content">🖋</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://mhauru.org"><img src="https://avatars.githubusercontent.com/u/5229876?v=4?s=100" width="100px;" alt="Markus Hauru"/><br /><sub><b>Markus Hauru</b></sub></a><br /><a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3Amhauru" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=mhauru" title="Code">💻</a> <a href="#projectManagement-mhauru" title="Project Management">📆</a> <a href="#content-mhauru" title="Content">🖋</a> <a href="#ideas-mhauru" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/radka-j"><img src="https://avatars.githubusercontent.com/u/29207091?v=4?s=100" width="100px;" alt="Radka Jersakova"/><br /><sub><b>Radka Jersakova</b></sub></a><br /><a href="#projectManagement-radka-j" title="Project Management">📆</a> <a href="#ideas-radka-j" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=radka-j" title="Documentation">📖</a> <a href="#infra-radka-j" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3Aradka-j" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://edchalstrey.com/"><img src="https://avatars.githubusercontent.com/u/5486164?v=4?s=100" width="100px;" alt="Ed Chalstrey"/><br /><sub><b>Ed Chalstrey</b></sub></a><br /><a href="#ideas-edwardchalstrey1" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3Aedwardchalstrey1" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/joecerniglia"><img src="https://avatars.githubusercontent.com/u/97735240?v=4?s=100" width="100px;" alt="joecerniglia"/><br /><sub><b>joecerniglia</b></sub></a><br /><a href="#ideas-joecerniglia" title="Ideas, Planning, & Feedback">🤔</a> <a href="#content-joecerniglia" title="Content">🖋</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=joecerniglia" title="Code">💻</a> <a href="#data-joecerniglia" title="Data">🔣</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/callummole"><img src="https://avatars.githubusercontent.com/u/22677759?v=4?s=100" width="100px;" alt="Callum Mole"/><br /><sub><b>Callum Mole</b></sub></a><br /><a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3Acallummole" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://aoifehughes.github.io"><img src="https://avatars.githubusercontent.com/u/10923695?v=4?s=100" width="100px;" alt="Aoife Hughes"/><br /><sub><b>Aoife Hughes</b></sub></a><br /><a href="#ideas-AoifeHughes" title="Ideas, Planning, & Feedback">🤔</a> <a href="#content-AoifeHughes" title="Content">🖋</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=AoifeHughes" title="Code">💻</a> <a href="#data-AoifeHughes" title="Data">🔣</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://phinate.github.io"><img src="https://avatars.githubusercontent.com/u/49782545?v=4?s=100" width="100px;" alt="Nathan Simpson"/><br /><sub><b>Nathan Simpson</b></sub></a><br /><a href="#infra-phinate" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#ideas-phinate" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/yongrenjie"><img src="https://avatars.githubusercontent.com/u/22414895?v=4?s=100" width="100px;" alt="Jonathan Yong"/><br /><sub><b>Jonathan Yong</b></sub></a><br /><a href="#infra-yongrenjie" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#ideas-yongrenjie" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=yongrenjie" title="Code">💻</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3Ayongrenjie" title="Reviewed Pull Requests">👀</a> <a href="#content-yongrenjie" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.flypig.co.uk"><img src="https://avatars.githubusercontent.com/u/1446122?v=4?s=100" width="100px;" alt="David Llewellyn-Jones"/><br /><sub><b>David Llewellyn-Jones</b></sub></a><br /><a href="#ideas-llewelld" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=llewelld" title="Code">💻</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3Allewelld" title="Reviewed Pull Requests">👀</a> <a href="#content-llewelld" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/IFenton"><img src="https://avatars.githubusercontent.com/u/5773962?v=4?s=100" width="100px;" alt="Isabel Fenton"/><br /><sub><b>Isabel Fenton</b></sub></a><br /><a href="#ideas-IFenton" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=IFenton" title="Code">💻</a> <a href="#content-IFenton" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://katrionagoldmann.github.io"><img src="https://avatars.githubusercontent.com/u/25952322?v=4?s=100" width="100px;" alt="Katriona Goldmann"/><br /><sub><b>Katriona Goldmann</b></sub></a><br /><a href="#ideas-KatrionaGoldmann" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=KatrionaGoldmann" title="Code">💻</a> <a href="#content-KatrionaGoldmann" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://rchan26.github.io/"><img src="https://avatars.githubusercontent.com/u/44200705?v=4?s=100" width="100px;" alt="Ryan Chan"/><br /><sub><b>Ryan Chan</b></sub></a><br /><a href="#ideas-rchan26" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=rchan26" title="Code">💻</a> <a href="#content-rchan26" title="Content">🖋</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3Archan26" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/eirini-zormpa"><img src="https://avatars.githubusercontent.com/u/30151074?v=4?s=100" width="100px;" alt="Eirini Zormpa"/><br /><sub><b>Eirini Zormpa</b></sub></a><br /><a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3Aeirini-zormpa" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://jending.com"><img src="https://avatars.githubusercontent.com/u/5104098?v=4?s=100" width="100px;" alt="Jennifer Ding"/><br /><sub><b>Jennifer Ding</b></sub></a><br /><a href="https://github.com/alan-turing-institute/TuringDataStories/pulls?q=is%3Apr+reviewed-by%3Adingaaling" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/edchapman88"><img src="https://avatars.githubusercontent.com/u/93717706?v=4?s=100" width="100px;" alt="Ed Chapman"/><br /><sub><b>Ed Chapman</b></sub></a><br /><a href="#ideas-edchapman88" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=edchapman88" title="Code">💻</a> <a href="#content-edchapman88" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mastoffel"><img src="https://avatars.githubusercontent.com/u/7348440?v=4?s=100" width="100px;" alt="martin"/><br /><sub><b>martin</b></sub></a><br /><a href="#ideas-mastoffel" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/alan-turing-institute/TuringDataStories/commits?author=mastoffel" title="Code">💻</a> <a href="#content-mastoffel" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/myyong"><img src="https://avatars.githubusercontent.com/u/5417696?v=4?s=100" width="100px;" alt="myyong"/><br /><sub><b>myyong</b></sub></a><br /><a href="#ideas-myyong" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
