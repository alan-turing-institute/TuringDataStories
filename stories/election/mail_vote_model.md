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
    into a signed margin that is positive for a Biden lead. Also adds
    columns for the number of votes for Biden and Trump.
    """

    if timestamp is None:
       timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    data = pandas.read_csv("https://alex.github.io/nyt-2020-election-scraper/battleground-state-changes.csv")

    data.loc[data["leading_candidate_name"] == "Trump", "vote_differential"] \
        = -data.loc[data["leading_candidate_name"] == "Trump", "vote_differential"]

    data["biden_votes"] = None
    data.loc[data["leading_candidate_name"] == "Biden", "biden_votes"] \
        = data.loc[data["leading_candidate_name"] == "Biden", "leading_candidate_votes"]
    data.loc[data["trailing_candidate_name"] == "Biden", "biden_votes"] \
        = data.loc[data["trailing_candidate_name"] == "Biden", "trailing_candidate_votes"]

    data["trump_votes"] = None
    data.loc[data["leading_candidate_name"] == "Trump", "trump_votes"] \
        = data.loc[data["leading_candidate_name"] == "Trump", "leading_candidate_votes"]
    data.loc[data["trailing_candidate_name"] == "Trump", "trump_votes"] \
        = data.loc[data["trailing_candidate_name"] == "Trump", "trailing_candidate_votes"] 			           

    data = data[data["timestamp"] < timestamp]

    return data[data["state"].str.contains(state)]
```

Note that rather than specifying the leading and trailing candidates, I instead
just convert the vote differential into a margin that is positive if Biden
is leading and negative if Trump is leading. I also add columns for the total
number of votes for Biden and Trump, which I will use later.

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

state_list = ["Pennsylvania", "Georgia", "Arizona"]
timestamp_list = ["2020-11-05"]*3
iter_vals = list(zip(state_list, timestamp_list))

def plot_data(state, timestamp=None):
    "Plot the election data for a given state up through a given time"

    df = load_data(state, timestamp)

    plt.figure()
    plt.plot(df["votes_remaining"], df["vote_differential"], "o")
    plt.xlabel("Votes remaining")
    plt.ylabel("Biden margin")
    plt.title("{} Vote Updates through {}".format(state, timestamp))

for (state, tstamp) in iter_vals:
    plot_data(state, tstamp)
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

def linear_regression(state, timestamp=None):
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

for (state, tstamp) in iter_vals:
    coeffs = linear_regression(state, tstamp)

plt.show()
```

Note that Pennsylvania and Georgia appear fairly well behaved, and the
margin that comes out of this is not too far off the eventual results,
while Arizona seems to have outlier points that muddles this analysis
(which was first noted by Martin):

```
for state in state_list:
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

### Model Structure

As noted above, the regression model has two different parameters: the slope
(related to the fraction of votes that are cast for Biden), and the intercept
(which is essentially the prediction of the final margin). Note that while
our linear regression fit these two things simultaneously, there is no reason
why we had to let the final margin be a "free" parameter that we adjusted
in the fitting: we could have instead just fit a single parameter for
the slope, and taken the votes remaining as a given from which we can
extrapolate in order to forecast the final margin.

Thus, in all of the models that follow, we will follow a procedure similar
to this. We will use the previous vote returns to estimate the vote
probability parameter, and then use the vote probability to predict the
outcome based on the remaining votes. We will consider several variants of
this structure to see how our modelling choices capture uncertainty.

### Point Estimates

We return to the regression model, but rather than fit it as was done
above, we will do our two step procedure to first estimate the vote
probability, and then forecast the remaining votes. To get an equivalent
single point estimate of the vote probability (akin to fitting the slope
above), we simply estimate the vote probability $\theta$ by taking the average
probability of a vote for Biden based on all observed mail-in votes.

```
def estimate_theta_point(state, timestamp=None):
    "computes the vote probability as a point estimate based on all returns"

    df = load_data(state, timestamp)

    return (df["biden_votes"].iloc[0] - df["biden_votes"].iloc[-1])/\
            ((df["biden_votes"].iloc[0] - df["biden_votes"].iloc[-1]) +
	     (df["trump_votes"].iloc[0] - df["trump_votes"].iloc[-1]))

for (state, tstamp) in iter_vals:
    print("Mean vote probability in {} as of {} is {}".format(
              state, tstamp, estimate_theta_point(state, tstamp))
	  )
```

Now based on these estimates, we can forecast the remaining votes. Note
that if the vote probability is $\theta$ and there are $v$ votes remaining,
then the final margin will change by $\theta v-(1-\theta)v = (2\theta-1)v$.

```
def predict_margin_point(theta, state, timestamp=None):
    "Predict remaining votes from a single estimate of the vote probability"

    assert theta >= 0.
    assert theta <= 1.

    df = load_data(state, timestamp)
    return df["vote_differential"].iloc[0] + df["votes_remaining"].iloc[0]*(2*theta - 1.)

for (state, tstamp) in iter_vals:
    theta = estimate_theta_point(state, tstamp)
    print("Predicted final margin in {} at {} is {}".format(state, tstamp,
           predict_margin_point(theta, state, tstamp)))
```

These margins are consistent with the regression models above.

### Uncertainty in the Predictions

When you flip a fair coin, you will not always get an equal number of heads
and tails. Similarly, even if we are very sure of the vote probability,
we do not expect that we will always get the exact same number of votes
that would be expected from the mean vote probability. As a first step
in determining the uncertainty in the final outcome, we would like to
capture this uncertainty.

If we do a fixed number of Bernoulli trials (i.e. a coin flip with a
known probability of producing heads or tails), we can quantify the expected
range of outcomes using a binomial distribution. While we can exactly compute
the probability mass function for a binomial distribution, in the following
we will find it easier to just sample randomly from the distribution, so
we will just draw samples here to help re-use some code, as we will eventually
need to make predictions by drawing many samples of $theta$.

```
from scipy.stats import binom

def predict_margin_samples(theta, state, timestamp=None):
    "Draws samples for the final margin given a set of samples for theta"

    theta = np.array(theta).flatten()
    assert np.all(theta >= 0.)
    assert np.all(theta <= 1.)

    n_samples = len(theta)
    n_samples_rvs = 100000 // n_samples

    df = load_data(state, tstamp)

    samples = []
    
    for tval in theta:
    	samples.append(binom.rvs(size=n_samples_rvs, p=tval, n=df["votes_remaining"].iloc[0]))

    samples = np.array(samples).flatten()

    return df["vote_differential"].iloc[0] + 2*samples - df["votes_remaining"].iloc[0]

for (state, tstamp) in iter_vals:

    theta = estimate_theta_point(state, tstamp)

    samples = predict_margin_samples(theta, state, tstamp)

    plt.figure()
    plt.hist(samples, bins=100)
    plt.xlabel("Biden Margin")
    plt.title("{} Predicted Margin (Point) as of {}".format(state, tstamp))

plt.show()
```

Now we can start to get an idea of the variability in our predictions. We
see that even if we use a regression-type model to make a single point estimate
of the vote probability, we still get a significant variation in the final
margin. This is because of the large number of remaining votes, something
that the base regression model cannot capture as easily.

### Uncertainty in the Vote Probability

To capture the uncertainty in the underlying vote probability and its effect
on the predictions, we now need to develop a Bayesian model. This means
that instead of the vote probability being a single value, it will instead
be described by a probability distribution. Bayesian inference gives us a
principled way to update this probability distribution as we see data.

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
  may be even more pronounced in this election, because Trump spent the
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
plt.xlabel("Biden vote probability")
plt.title("PDF for the Beta distribution with a = {}, b = {}".format(a, b))
plt.show()
```

However, we will find that this choice of prior does not matter very much
given the amount of data that is available to estimate the vote probabilities.
Also, given that the votes in Arizona are more favorable for Trump, the
third point above is probably not universally true. However, if you
try other values for $a$ and $b$ in what follows, you are unlikely to see
much difference given the large number of ballots that were cast.

Once we have specified a prior, we can update our beliefs about the value
for a parameter by computing the *posterior*. This involves applying Bayes'
rule:

$$ p(\theta|y) = \frac{p(y|\theta)p(\theta)}{p(y)} $$

Here, $p(\theta)$ is the prior distribution (described above), $p(y|\theta)$
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
distribution. The analytical solution for updating our prior with shape
parameters $a$ and $b$ to the posterior if we have $n$ trials and $k$
successes is

$$ p(\theta|n, k) = \beta(a + k, b + n - k) $$

Thus, we can draw samples from the posterior to see the variability of
the vote probability:

```
def estimate_theta_bayes(state, timestamp=None):
    "Draws samples from the posterior of the vote probability"

    df = load_data(state, timestamp)

    k = df["biden_votes"].iloc[0]-df["biden_votes"].iloc[-1]
    n = k + df["trump_votes"].iloc[0]-df["trump_votes"].iloc[-1]

    return beta.rvs(size=1000, a=a+k, b=b+n-k)

for (state, tstamp) in iter_vals:

    theta = estimate_theta_bayes(state, tstamp)

    plt.figure()
    plt.hist(theta, bins=100)
    plt.xlabel("Biden Vote Probability")
    plt.title("{} Vote Probability (Bayesian) as of {}".format(state, tstamp))

plt.show()
```

Clearly, the large number of votes means that the posterior distribution is
very tightly clustered around the point estimates we obtained above. We can
see that this doesn't influence the final predictions very much by making
predictions as above:

```
for (state, tstamp) in iter_vals:

    theta = estimate_theta_bayes(state, tstamp)

    samples = predict_margin_samples(theta, state, tstamp)

    plt.figure()
    plt.hist(samples, bins=100)
    plt.xlabel("Biden Margin")
    plt.title("{} Predicted Margin (Bayesian) as of {}".format(state, tstamp))

plt.show()
```

### Hierarchical Bayesian Model

In the above, the vote probability is treated as a single, unchanging value.
We may be uncertain about it, but the model assumes that every voter is
identical. Given the political polarization in the US, this is probably not
a very good assumption. Although the data seems to strongly suggest that the
mail-in votes are consistently in favor of one candidate, this is not the
same as saying all voters are identical. In the following, we adapt the
model to relax this assumption and build what is known as a *hierarchical*
Bayesian model.

If the above model of assuming that every voter is identical is one extreme,
then the other extreme is to assume that every voter is different and we would
need to estimate hundreds of thousands to millions of parameters to fit our
model. This is not exactly practical, so a hierarchical model posits a middle
ground that the vote probability is itself drawn from a probability
distribution. Note that this is different than saying that we specify a prior
distribution for a single value -- in the model, each incremental update of
votes has a single vote probability associated with it, but that probability is
drawn from a probability distribution and thus can vary.

In the following model, we specify the model by assuming that each vote
update has a single vote probability associated with it, and that vote
probability is drawn from a beta distribution. Since a beta distribution
depends on the $a$ and $b$ shape parameters, we will then need to set
prior distributions for those parameters, rather than for $\theta$ itself.
Having multiple levels like this are why these models are known as
*hierarchical* -- parameters are drawn from distributions whose parameters
are also distributions themselves.

Since $a$ and $b$ are positive, continuous variables, I will specify their
priors using lognormal distributions. Since I expect the distribution
from which $\theta$ is drawn to be roughly similar to the one I set for
the prior on $\theta$ above, I will use this for the mean of my lognormal
prior, and set unit variance for simplicity. The rest of the model is the
same as above, except each individual vote update is treated separately.

Adding this additional layer of complexity means that we unfortunately can
no longer compute our results analytically. Instead, we resort to Markov
Chain Monte Carlo sampling, which is a method of simultaneously drawing
samples from the posterior distribution of all of the parameters of the
model. MCMC sampling is frequently implemented in what is known as a
probabilistic programming language, where the language explicitly treats
all variables as probability distributions from which it must sample.
There are a number of popular lanaguages for this -- here I use PyMC3
to implement my model.

```
import pymc3

def estimate_theta_hierarchical(state, timestamp=None):
    "estimate theta for the vote probability distribution using a hierarchical model and MCMC sampling"

    df = load_data(state, timestamp)

    n = np.diff(-df["biden_votes"]) + np.diff(-df["trump_votes"])
    k = np.diff(-df["biden_votes"])

    keep = (n > 0)*(k >= 0)*(k <= n)
    n = n[keep]
    k = k[keep]

    with pymc3.Model() as model:
        a = pymc3.Lognormal("a", mu=np.log(8.), sd=1.)
        b = pymc3.Lognormal("b", mu=np.log(4.), sd=1.)
        theta = pymc3.Beta("theta", alpha=a, beta=b, shape=len(n)) 
        obs = pymc3.Binomial("obs", p=theta, n=n, observed=k, shape=len(n))
        trace = pymc3.sample(1000)

    theta = []

    for (aval, bval) in zip(trace["a"], trace["b"]):
    	theta.append(beta.rvs(size=10, a=aval, b=bval)

    return np.array(theta).flatten()

for (state, tstamp) in iter_vals:

    theta = estimate_theta_hierarchical(state, tstamp)

    plt.figure()
    plt.hist(theta, bins=100)
    plt.xlabel("Biden vote probability")
    plt.title("{} Vote Probability (Hierarchical) as of {}".format(state, tstamp))

plt.show()
```

Looking at these plots, we see that the model is now much more varied in
its estimates for the vote probability (note that this is the posterior for
the *distribution* expected for the vote probability, rather than the explicit
values of the vote probability itself). The mean is still where we expected
it from the previous analysis, but it is much more tolerant of outlying values.
This should considerably increase the spread of the predicted final margin,
which we do below:

```
for (state, tstamp) in iter_vals:

    theta = estimate_theta_hierarchical(state, tstamp)

    samples = predict_margin_samples(theta, state, tstamp)

    plt.figure()
    plt.hist(samples, bins=100)
    plt.xlabel("Biden Margin")
    plt.title("{} Predicted Margin (Hierarchical) as of {}".format(state, tstamp))

plt.show()
```

One limitation in this prediction method is that it overstates the variability
in the final margin, because it uses a single value for forecasting all
remaining votes. In reality, these votes will be divided up into smaller
chunks, each of which will have a different vote probability. This will
make extreme values less likely.