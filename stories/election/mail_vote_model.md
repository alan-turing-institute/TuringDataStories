# Modelling Mail-In Votes In the 2020 US Election

## Author

* **Eric Daub**, Alan Turing Institute, Github: @edaub

## Other Contributors

* **Camila Rangel Smith**, Alan Turing Institute
* **Martin O'Reilly**, Alan Turing Institute

## Reviewers

## Introduction

The Covid-19 Pandemic led to record numbers of mail-in votes in the 2020
United States Presidential Election. Because of the high volume of mail
ballots, plus rules that prevented some states from counting these ballots
before election day, the result of the election remained uncertain for
a week, with periodic updates coming as ballots were tabulated and reported.

In particular, several states had very close races that had the potential
to tip the election in favor of either candidate. Because of the Electoral
College system, where states almost universally employ a "winner-take-all"
model for allocating their Electoral Votes, a few states can have a large
effect on the outcome of the election. For example, in 2000 the election
came down to around a 500 vote margin in Florida (out of 10 million
ballots cast), despite the fact that Al Gore easily won the popular vote.
In 2020, a few states with very close races dominated the headlines for the
week after the election, of which we will look at Pennsylvania, Arizona,
and Georgia in this post. The final outcome of the election hung on the
results from these states.

In this Turing Data Story, I examine a few ways to analyze the data updates
coming from each state to predict the final outcome. This originated from
some Slack discussions with Camila Rangel Smith and Martin O'Reilly, whom
I list above as contributors. In particular, our initial discussions centered
around uncertainties in the analysis done by Camila and Martin, which I have
carried out using Bayesian inference to quantify uncertainty and determine
when we might have reasonably called each state for the eventual winner
based on the updated data.

## Data

To create the models in the post, I use the
[NYT Election Data Scraper](https://alex.github.io/nyt-2020-election-scraper)
to obtain the latest results which are updated every few minutes to ensure
that they have the latest data. To load this data into a Python session
for analysis, I can use Pandas to simply load from the CSV version of the
data directly from the URL, and extract the state that I wish to examine:

```
import pandas
import datetime

def load_data(state, timestamp=None):
    """
    Loads election data updates from CSV file as a pandas data frame

    Retrieves data from the live file on Github, which is loaded into a
    data frame before extracting the relevant state data.

    State must be a string, which will be searched in the "state" field
    of the data frame.

    Timestamp must be a datetime string. Optional, default is current
    date and time.

    Returns a data frame holding all updates from a particular state,
    prior to the given timestamp. The "vote_differential" field is turned
    into a signed margin that is positive for a Biden lead.
    """

    if timestamp is None:
       timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    data = pandas.read_csv("https://alex.github.io/nyt-2020-election-scraper/battleground-state-changes.csv")

    data.loc[data["leading_candidate_name"] == "Trump", "vote_differential"] \
        = -data.loc[data["leading_candidate_name"] == "Trump", "vote_differential"]

    data = data[data["timestamp"] < timestamp]

    return data[data["state"].str.contains(state)]
```

Note that rather than specifying the leading and trailing candidates, I instead
just convert the vote differential into a margin that is positive if Biden
is leading and negative if Trump is leading.

For instance, if I would like to see the data for Georgia:

```
df = load_data("Georgia")
df.head()
```

The data contains a timestamp, the number of votes for each candidate, the
margin, and an estimate of the number of votes remaining. This allows us to
see how the vote margin evolves over time as new ballots are counted. For
example, we can look at the data for all states up to midnight on 5 November
to see the evolution of the race:

```
import matplotlib.pyplot as plt

def plot_data(state, timestamp):
    "Plot the election data for a given state up through a given time"

    df = load_data(state, timestamp)

    plt.figure()
    plt.plot(df["votes_remaining"], df["vote_differential"], "o")
    plt.xlabel("Votes remaining")
    plt.ylabel("Biden margin")
    plt.title("{} Vote Updates through {}".format(state, timestamp))

plot_data("Georgia", "2020-11-05")
plot_data("Arizona", "2020-11-05")
plot_data("Pennsylvania", "2020-11-05")
plt.show()
```

Note that the trend shows that Biden is catching up as more votes are counted
in both Georgia and Pennsylvania, while Trump is catching up in Arizona.
The trend is fairly linear. Thus, one might first consider doing a simple
regression to estimate the final margin.

## Linear Regression Analysis

We can do a simple analysis based on this. A linear regression model will
have two parameters that are fit: the slope will be related to the fraction
of the outstanding votes that are for Biden, and the intercept, which
will indicate the final margin when there are no votes remaining. (This is
the initial analysis that was done by Camila for Pennsylvania and Martin for
Arizona.)

```
import numpy as np

def linear_regression(state, timestamp):
    """
    Fit a linear regression model to the election updates

    Fits a line to the data updates for a given state and a given
    timestamp. Plots the data and returns the fitting parameters
    (slope, intercept) as a numpy array.
    """

    plot_data(state, timestamp)

    df = load_data(state, timestamp)

    coeffs = np.polyfit(df["votes_remaining"], df["vote_differential"], 1)

    print("Predicted margin for {} as of {}: {}".format(state, timestamp, coeffs[1]))

    plotvals = np.linspace(0, df["votes_remaining"].iloc[-1])

    plt.plot(plotvals, coeffs[0]*plotvals + coeffs[1])

    return coeffs

coeffs = linear_regression("Pennsylvania", "2020-11-05")
coeffs = linear_regression("Georgia", "2020-11-05")
coeffs = linear_regression("Arizona", "2020-11-05")
plt.show()
```

Note that Pennsylvania and Georgia appear fairly well behaved, and the
margin that comes out of this is not too far off the eventual results,
while Arizona seems to have outlier points that muddles this analysis
(which was first noted by Martin):

```
for state in ["Pennsylvania", "Georgia", "Arizona"]:
    df = load_data(state)
    print("Current margin in {}: {}".format(state, df["vote_differential"].iloc[0]))
```

However, one thing to note about this is that even though the trends point
clearly in favor of Biden in this analysis, we do not have a good idea of
the uncertainties. Without this, one cannot comfortably call a state in
favor of one candidate, which is why the media waited a few more days beyond
this to call the states for Biden. How might we develop a model that
explicitly captures this uncertainty?

## Bayesian Inference

To address this shortcoming, we turn to Bayesian Inference. Bayesian
statisticians think of model parameters not as a single number, but rather
probability distributions -- in this way, we can get a sense of the range
of values that the model thinks are consistent with the data.

As noted above, the regression model has two different parameters: the slope
(related to the fraction of votes that are cast for Biden), and the intercept
(which is essentially the prediction of the final margin). Note that while
our linear regression fit these two things simultaneously, there is no reason
why we had to let the final margin be a "free" parameter that we adjusted
in the fitting: we could have instead just fit a single parameter for
the slope, and force the line to pass through the most recent margin and
votes remaining point. We can then "predict" the final margin by forecasting
the remaining votes using our fitted slope applied to the known number of
votes remaining. This is more akin to the way that the Bayesian analysis will
work: we will use the vote updates that we have to estimate the fraction of
votes for Biden, and then we will use that estimate to predict the outcome
of the remaining votes. However, instead of there being a single estimate
for the slope, we will treat the slope as a probability distribution to capture
its uncertainty.

Before we look at our data, we might ask ourselves what reasonable values we
would expect to see for the fraction of votes for Biden. This is known as
a *prior* in Bayesian inference, and since all fitting parameters in Bayesian
inference must be a probability distribution, we need to specify a distribution
for this.

* First, we know that this fraction must be between 0 and 1. A common family
  of probability distributions over this interval is what is known as the
  Beta distribution. This family of distributions has two shape parameters.
  Much like how normal distributions are specified by a mean and variance,
  the shape parameters for a Beta distribution determine the location
  and width of the highest probability regions.

* We know that very extreme values such as 0 or 1 are probably unlikely. Even
  in the most liberal or conservative regions of the US, there are a fair
  number of voters across the idealogical spectrum.

* Historically, mail in votes tend to skew heavily towards Democrats. This
  may be even more pronounced in this, election, because Trump spent the
  better part of the campaign casting doubt on mail ballots and encouraging
  his supporters to vote in person (no doubt because he intended to contest
  the mail in ballots as fradulent in order to win the election in court).

Based on this, a reasonable prior for the vote probability might be
the following:

```
from scipy.stats import beta

xvals = np.linspace(0, 1)

a = 8.
b = 4.

plt.plot(xvals, beta.pdf(xvals, a=a, b=b))
plt.title("PDF for the Beta distribution with a = {}, b = {}".format(a, b))
plt.show()
```

However, we will find that this choice of prior does not matter very much
given the amount of data that is available to estimate the vote probabilities.

Once we have specified a prior, we can update our beliefs about the value
for a parameter by computing the *posterior*. This involves applying Bayes'
rule:

$$ p(\theta|y) = \frac{p(y|\theta)p(\theta)}{p(y)} $$

Here, $p(\theta)$ is the prior distribution(described above), $p(y|\theta)$
is the *likelihood* (the probability that we would have gotten the data given
a particular choice of $\theta$), and $p(y)$ is known as the *evidence*
(the probability of getting that particular observation over all possible
outcomes of the experiment). For many problems, it is straightforward to
specify a prior and to compute the likelihood, while computing the evidence
can be tricky. Fortunately for the case described below, computing the posterior
can be done in closed form. This is because the Beta distribution is
*conjugate* for a Binomial likelihood, meaning that if we use a Beta prior
on the vote probability and a Binomial model to describe the outcome of
polling (i.e. voting can be treated as a series of weighted coin flips),
then the posterior for the vote probability is also a Beta
distribution.


