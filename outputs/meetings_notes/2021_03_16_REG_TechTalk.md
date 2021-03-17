# Turing Data Stories @ REG Tech Talk 2021-03-16

## Promo (to help adversite on Slack)
Tell the world something new, join the REG Tech Talk on Tuesday to build exciting new [Turing Data Stories](https://github.com/alan-turing-institute/TuringDataStories): a mix of open data, code, narrative 💬, visuals 📊📈 and knowledge 🧠 to help understand the world around us.

## Co-working
* Quick intro to Turing Data Stories (see below)
* Review stories https://github.com/alan-turing-institute/TuringDataStories/projects/3
* Quick intro from an advocate for each
* Any more stories, for a super quick intro
* Divide into breakout rooms, scope story and plan next steps
* Get back together and update on discussions

## Roll call
* David Beavan - Turing Research Engineering - t:@DavidBeavan g:@DavidBeavan
* Camila Rangel Smith (@camilarangels) - Turing Research Engineering
* 
* Arielle Bennett, PMU
* Eric Daub @edaub, REG
* Jack Roberts, Turing REG
* James Robinson - Turing Research Engineering
* Callum Mole - Turing, REG. 
* Kevin Xu - Civil Service
* Ed Chalstrey
* Glenn Abastillas ARC
* Radka Jersakova, REG
* Oscar Giles, REG
* Kasra Hosseini, REG
* Mishka Nemes, Academic Programmes
* Bill Finnegan, Engage@Turing

## Breakout rooms

### 1. Baseball Story
 - Eric
 - Jack


 
### 2. London Air Quality Story
 - Bill
 - James R
 - Callum

Comments:
- Progress seems contingent on the Clean Air project up and running. The Clean Air project is ongoing and there is pressure to get an API available for forecasting very soon. Oscar and James will mention to the Clean Air team in the next meeting.
- The cleanair forecasts might be on useful input to the story - we'll sync up the teams to discuss where there might be synergies.

### 3. Desert Island
 - Camila
 - Mishka
 - Ed
 - Arielle
 - Glenn

#### Notes:

 - Compare with national datasets of music taste (spotify)
 - How events change people choices in time
 - **Spotify has an API** that allow you to access metadata on the the music. ([API documentation link](https://developer.spotify.com/documentation/web-api/))
     - Do genres picked over time change
     - Python specific package: [spotipy](https://spotipy.readthedocs.io/en/2.9.0/)
 - Get in contact the BBC?
 - Do MPs have more embarassing music tastes than average guests?
    - Do they intentionally choose British artists?
 - How evolution of technology affects(?) people choices.
 - What are the most popular choices: books, songs, bands
 - Could we find a larger dataset from the BBC?
 - BBC ggplot2 style (they have a python equivalent?)
     - Yes, [`altair` <- link](https://altair-viz.github.io).
 - There is former TRF (Anna FitzMaurice) who now works for the data team at BBC and who could perhaps help us get hold of further data/ liaising us with other people

### 4. Scoping another story
- Radka
- Dave
- Kevin
- Kasra

Comments:
* RJ: Covid nowcasting model, as partial counts of covid come in, this is a model to estimate the full count when the full data will be in. This may be usful for other purposes. All public data, using the UK dashboard (inc/ historical CSVs). The general idea of anticipating results from partial data is pedagogically a good thing to teach. RJ will bring this to her colleagues at a forthcoming team meeting and will report back if this is a good fit for outputs.

* KH: work on computer vision with Living with Machines. Detection of railways and buildings on historical maps. Same method would be applied using modern open streetmaps (new work). How the morphalogical characteristics are shaped and controlled by the arrival of the railway. i.e. how the railway shapes our cities. Focus on London?


## Turing Data Stories

**How it began**:
[Turing Data Stories](https://github.com/alan-turing-institute/TuringDataStories) came out of a desire, back in spring 2020, from REG ppl to work on something Covid related. Leveraging the Internal Projects service area, making use of REG collaboration time. Initially Dave, Camila, Kevin fast streamer and Sam Van Stroud doctoral candidate. Now we can thank Louise, Nick and Eric for their time and contributions as we grow. Now with added Bill, who's joined the Turing as part of Engage@Turing.

**Our initial motivation was**:
* Government reporting of Covid-19 data is not always in the most accessible format. 
* During these times, many individuals may be interested in developing their technical skills in an impactful way, but not know where to start.
* We hope that by using the story telling medium, we can bring people along the data science journey by trying to answer both fascinating and very much relevant societal questions.

One story grew into a platform for at a stories, and that's where we have encouraged others to contribute. Such as Eric with a new story and Louise and Nick with reviews.

**Our mission is**:
> An open community creating “Data Stories”: A mix of open data, code, narrative 💬, visuals 📊📈 and knowledge 🧠 to help understand the world around us.

**What is a TDS?**
* A Turing Data Stories is a Jupyter notebook that documents an interesting insight using real world open data. 
* They should be:
* Told in a pedagogical way.
* Fully reproducible.
* Transparent  (data provenance, review process).
* Peer-reviewed by other contributors before being published.

We were awarded a project-wide [Open Life Science 2](https://openlifesci.org/ols-2) (fork of Mozilla Open Leaders) mentorship to build this and bring it to a wider community, and successfully graduated from that in December.

Our current outputs are on [fastpages](https://alan-turing-institute.github.io/TuringDataStories-fastpages/). We have published one story about Covid19 and deprivation, and have another story about the US election mail in votes from Eric.

Now we wish to present this as a method of publication for REG and the wider Turing community, fitting a need for a citable output which goes beyond a blog post, but short of an article. It fits public engagement, training and educational goals, as well as a chance to get an interesting method or piece of work out there, demonstrating what REG can do and connecting with others. There has been interest in partnering with a publisher for greater impact and reach.

**How can I get involved?**

- **Story ideas**: Have an idea for an interesting story that could be told if you had the data, or knew how to analyse it? We can help.
- **Data**: Stumbled across an interesting dataset, or perhaps mashed together several sources of data yourself? We want to hear about it.
- **Code**: Are you an expert in Bayesian analysis? Do you have sick matplotlib skills? Put that knowledge to work!
- **Peer Review**: Know a bit about data analysis? Good at communicating that knowledge? Interested in learning about it can be applied to understanding society? We need reviews to make sure our stories are the best they can be.
- **Communication**: Are you an amazing writer? Help us with the story telling side of our stories.
- **Community**: Don't fit in any of the above categories, but still want to hang out and be involved? We've got you, drop us a line.


Join us in our [slack channel](https://join.slack.com/t/turingdatastories/shared_invite/zt-nqpf47h1-lx1R85j2Gpf0TgouKmA4PA), or email us to turingdatastories@turing.ac.uk.

We virtually meet on Wednesday afternoons to work collaboratively. 
