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
results from these states, and the slow drip feed of additional ballots
being released left audiences constantly checking the news for updates.

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
%matplotlib inline
```

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
```

Note that at this point, the linear regression predicts a margin in
Pennsylvania and Arizona that are quite different from the final margin.
Georgia appears to be very close to the final margin. However, Arizona
seems to have outlier points that muddles this analysis (which was first
noted by Martin). Thus, while these models are useful starting points, they
do not appear to be particularly robust and are somewhat dependent on when
you choose to fit the data.

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

## Modelling Uncertainty in the Votes

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
the slope (for instance, simply using the fraction of mail ballots cast thus
far), and then used that estimate to project the votes remaining in order to
extrapolate and obtain our estimate of the final margin.

With this format in mind, we need to develop a way to account for the
uncertainty in both of these steps. Our Bayesian model will treat both
the probability that a vote goes for Biden as a probability distribution
(rather than a single number), and then the final projected margin will
also be a probability distribution. In practice, rather than determining
the analytical form of these probability distributions, we will instead
model the outcome by drawing samples from the distribution. This is a
standard method within Bayesian Inference, and illustrates the power
of this technique for quantifying uncertainty.

### Bayesian Model of the Vote Probability

Bayesian Inference tends to think of probability distributions as reflecting
statements about our beliefs. Formally, we need to state our initial beliefs
before we see any data, and then we can use that data to update our knowledge.
This previous belief is known as a *prior* in Bayesian inference, and the
updated beliefs once we look at our data is known as the *posterior*.

### Prior Specification

Before we look at our data, we thus need ask ourselves what we think
reasonable values might be for the fraction of votes for Biden, which we will
call $\theta$. We need to encode this in a probability distribution, so that
we can update this using the data.

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
```

### Updating the Posterior

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
can be tricky.

In practice, for most models we cannot compute the evidence very easily,
so instead of computing the posterior directly, we draw samples from it.
A common technique for this is Markov Chain Monte Carlo (MCMC) sampling.
A number of software libraries have been written in recent years to make
carrying out this sampling straightforward using what are known as
*probabilistic programming languages*. These languages formally treat
variables as probability distributions with priors and then draw samples
from the posterior to allow us to perform inference.

### Hierarchical Bayesian Model

In our linear regression model, we effectively treated the vote probability
as a single, unchanging value. This is the same as saying that every voter
in our model is identical. Given the political polarization in the US, this
is probably not a very good assumption. Although the data seems to strongly
suggest that the mail-in votes are consistently in favor of one candidate,
this is not the same as saying all voters are identical. In the following,
we build a model to relax this assumption, using what is known as a
*hierarchical* Bayesian model.

If the above model of assuming that every voter is identical is one extreme,
then the other extreme is to assume that every voter is different and we would
need to estimate hundreds of thousands to millions of parameters to fit our
model. This is not exactly practical, so a hierarchical model posits a middle
ground that the vote probability is itself drawn from a probability
distribution. Note that this goes a step further than simply making the
model Bayesian by treating the vote probability as a probability
distribution -- in the model, each incremental update of votes has a single
vote probability associated with it, but that probability is drawn from a
probability distribution and thus can vary.

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
same as above, except each individual vote update is modelled and
fit separately in order to estimate the *distribution* from which the
vote probability is drawn, rather than the vote probability itself.

Finally, we need to explicitly model the likelihood. When you flip a fair
coin a number of times, the distribution of outcomes follows a binomial
distribution. Thus, we can use a binomial likelihood to model the
range of vote probabilites that might be consistent with the votes that
were cast. This can be computed analytically, and most probabilistic
programming languages have built-in capacity for computing likelihoods
of this type. This is done by setting this particular variable to have a
known value, which indicates that this variable is used to compute the
likelihood. In our particular case, this likelihood will be a vector
of a series of trials, each with a different value of the vote probability.

Thus, we can now write down a model in a probabilistic programming language
in order to draw samples from the posterior. There are a number of popular
lanaguages for this -- here I use PyMC3 to implement my model. PyMC3
can easily handle all of the features we specified above (hierarchical
structure, and a vector representation of the binomial likelihood), which
is written out in the function below:

```
import pymc3

import logging
logger = logging.getLogger("pymc3")
logger.propagate = False
logger.setLevel(logging.ERROR)

def extract_n_k_trials(state, timestamp=None):
    """
    Convert vote data into a series of bernoulli trials. If no
    data is valid, then return a list of a single zero for each.

    Returns two lists of positive integers for the total number
    of votes (n) and the votes for Biden (k)
    """

    df = load_data(state, timestamp)

    # convert raw vote counts into a series of trials (n, k),
    # where n is the total number of votes and k is the number
    # of votes for Biden

    n = np.diff(-df["biden_votes"]) + np.diff(-df["trump_votes"])
    k = np.diff(-df["biden_votes"])

    # throw out sets that don't make any sense; if none remain then use (0,0)

    keep = (n > 0)*(k >= 0)*(k <= n)
    n = n[keep]
    k = k[keep]

    if len(n) == 0:
       n = [0]
       k = [0]

    return n, k

def estimate_theta_hierarchical(state, timestamp=None):
    "estimate theta for the vote probability distribution using a hierarchical model and MCMC sampling"

    n, k = extract_n_k_trials(state, timestamp)

    # build model and draw MCMC samples

    with pymc3.Model() as model:
        a = pymc3.Lognormal("a", mu=np.log(8.), sd=1.)
        b = pymc3.Lognormal("b", mu=np.log(4.), sd=1.)
        theta = pymc3.Beta("theta", alpha=a, beta=b, shape=len(n)) 
        obs = pymc3.Binomial("obs", p=theta, n=n, observed=k, shape=len(n))
        trace = pymc3.sample(1000, progressbar=False)

    # convert posterior samples of a and b into samples from the
    # vote probability

    theta = []

    for (aval, bval) in zip(trace["a"], trace["b"]):
        theta.append(beta.rvs(size=10, a=aval, b=bval))

    return np.array(theta).flatten()

for (state, tstamp) in iter_vals:

    theta = estimate_theta_hierarchical(state, tstamp)

    plt.figure()
    plt.hist(theta, bins=100)
    plt.xlabel("Biden vote probability")
    plt.title("{} Vote Probability (Hierarchical) as of {}".format(state, tstamp))
```

Once I draw MCMC samples for $a$ and $b$, I convert those samples into samples
of $\theta$ as this is what is needed out of the model to make predictions.

Looking at these plots, we see that the model is now much more varied in
its estimates for the vote probability (note that this is the posterior for
the *distribution* expected for the vote probability, rather than the explicit
values of the vote probability itself). The mean is still where we expected
it from the linear regression analysis, but the distribution is much wider
due the fact that occasionally votes come in from places that are not as
heavily in favor of Biden. This should considerably increase the spread of
the predicted final margin and assure that it is not overconfident in the
final result.

### Predicting the Final Margin

Once we have samples from the vote probability, we need to simulate the
remaining votes to predict the final outcome. This is known as estimating the
*posterior predictive distribution* in Bayesian inference, as we use our
updated knowledge about one of our model parameters to predict some of the
data that it was fit on.

What is a reasonable way to simulate the remaining votes? As we see from the
data, the votes come in a steady drip feed as ballots are counted. Thus,
we can simulate this by sampling randomly, with replacement, from the data
for the number of ballots cast in each update until we get to the number of
votes remaining. We can then draw from the posterior of the vote probability
distribution for each set of ballots, and project those using a binomial
distribution. By repeating this many times using our posterior samples, we
will have a reasonable estimate of the range expected in the final outcome.

```
from scipy.stats import binom

def predict_final_margin(theta, state, timestamp):
    """
    Use posterior samples of the vote probability to predict the remaining
    votes.

    The remaining votes are split into batches by sampling from
    the previous votes until enough are accumulated. Then each batch is
    forecast by drawing from the posterior of the vote probability, and
    the total is summed.

    Returns a numpy array of samples of the final margin
    """

    assert np.all(theta >= 0.)
    assert np.all(theta <= 1.)

    df = load_data(state, timestamp)

    n_remain = df["votes_remaining"].iloc[0]

    n, k = extract_n_k_trials(state, timestamp)

    # simulate remaining votes

    predicted_margin = []

    for i in range(10000):

        trials_remain = []

        while np.sum(trials_remain) <= n_remain:
            trials_remain.append(np.random.choice(n))

        trials_remain[-1] = n_remain - np.sum(trials_remain[:-1])
        assert np.sum(trials_remain) == n_remain

        sim_votes = []

        for t in trials_remain:
            sim_votes.append(binom.rvs(size=1, n=t, p=np.random.choice(theta)))

        predicted_margin.append(df["vote_differential"].iloc[0] +
                                2*np.sum(sim_votes) - n_remain)

    return predicted_margin

for (state, tstamp) in iter_vals:

    theta = estimate_theta_hierarchical(state, tstamp)
    predicted_margin = predict_final_margin(theta, state, tstamp)

    plt.figure()
    plt.hist(predicted_margin, bins=100)
    plt.xlabel("Biden Margin")
    plt.title("{} final predicted margin as of {}".format(state, tstamp))
```

As we can see from this, the model has fairly wide intervals surrounding the
predicted final margin based on the original linear regression model.
Interestingly, when we fit Georgia in this way, it looks much more likely that
Trump would win through this point than the linear regression model would
suggest, though the final margin is well within the error bounds suggested
from the predictions. Arizona looks likely to fall to Trump, but Pennsylvania
is much more firmly leaning towards Biden. We can look at the results again
a day later to see how the race evolved:

```
for (state, tstamp) in zip(state_list, ["2020-11-06"]*3):

    theta = estimate_theta_hierarchical(state, tstamp)
    predicted_margin = predict_final_margin(theta, state, tstamp)

    plt.figure()
    plt.hist(predicted_margin, bins=100)
    plt.xlabel("Biden Margin")
    plt.title("{} final predicted margin as of {}".format(state, tstamp))
```

Clearly, Georgia has swung in Biden's favor over the course of the day.
The mean final margin in Pennsylvania has not moved much, though the
uncertainty has tightened up and made the result more likely for Biden.
Arizona has moved slightly towards Biden, but is still more likely to go
for Trump. 

## Animating the Updates

Now that we have built a model, we can build an animation that shows the
evolution of the predicted results as a function of time. This will show
how the uncertainty shrinks over time as fewer votes remain.

**Note:** Because new MCMC samples need to be drawn for each new update,
creating this animation ends up being fairly expensive to run (this took
several hours on my laptop). I speed things up by saving the current
prediction each time the MCMC samples are drawn, so that if the previous
iteration is the same we do not need to re-run the model. However, this
is still fairly expensive, so don't try and run this unless you are willing
to wait!

```
import matplotlib.path as path
import matplotlib.patches as patches
import matplotlib.text as text
import matplotlib.animation as animation

from IPython.display import HTML

def fit_model(state, timestamp=None):
    """
    Fit a model to predict the final margin for the given date/time.
    Each iteration is saved as a numpy file, and the next step
    checks for a model that matches the existing vote count before
    doing the expensive MCMC fitting

    Returns the simulated final margin samples at the given time
    """

    try:
        model = np.load("model.npz")
        n_prev = model["n"]
        k_prev = model["k"]
        n_predict_prev = model["n_predict"]
        preds_prev = model["preds"]
        state_prev = model["state"]
    except (KeyError, IOError):
        n_prev = None
        k_prev = None
        n_predict_prev = None
        preds_prev = None

    n, k = extract_n_k_trials(state, timestamp)

    df = load_data(state, timestamp)
    n_predict = df["votes_remaining"].iloc[0]

    if (np.all(n_prev == n) and np.all(k_prev == k) and
        n_predict_prev == n_predict):
        return preds_prev
    else:
        theta = estimate_theta_hierarchical(state, timestamp)
        preds =  predict_final_margin(theta, state, timestamp)
        np.savez("model.npz", n=n, k=k, preds=preds, n_predict=n_predict)
        return preds

def initialize_bins(counts, bins):
    "initialize the patch corners for the animation"

    # get the corners of the rectangles for the histogram
    left = bins[:-1]
    right = bins[1:]
    bottom = np.zeros(len(left))
    top = bottom + counts
    nrects = len(left)

    nverts = nrects * (1 + 3 + 1)
    verts = np.zeros((nverts, 2))
    codes = np.full(nverts, path.Path.LINETO)
    codes[0::5] = path.Path.MOVETO
    codes[4::5] = path.Path.CLOSEPOLY
    verts[0::5, 0] = left
    verts[0::5, 1] = bottom
    verts[1::5, 0] = left
    verts[1::5, 1] = top
    verts[2::5, 0] = right
    verts[2::5, 1] = top
    verts[3::5, 0] = right
    verts[3::5, 1] = bottom

    return verts, codes, bottom

def create_animation(state):
    "Create an animation of the vote updates for the given state"

    start_time = "2020-11-04T00:00:00"
    
    preds = fit_model(state, start_time)

    xlim = 100000
    ylim = 20000
    nbins = 200

    bins_b = np.linspace(0, xlim, xlim//nbins, dtype=np.int64)
    counts_b, bins_b = np.histogram(preds[preds > 0], bins_b)

    bins_t = np.linspace(-xlim, 0, xlim//nbins, dtype=np.int64)
    counts_t, bins_t = np.histogram(preds[preds < 0], bins_t)
    
    verts_t, codes_t, bottom_t = initialize_bins(counts_t, bins_t)
    verts_b, codes_b, bottom_b = initialize_bins(counts_b, bins_b)

    patch_t = None
    patch_b = None

    def animate(i, state, bins_t, bins_b, bottom_t, bottom_b, start_time):
        # simulate new data coming in

        timestamp = ((datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S") +
                      datetime.timedelta(hours=i)).strftime("%Y-%m-%dT%H:%M:%S"))

        print(timestamp)

        df = load_data(state, timestamp)
        votes = df["votes_remaining"].iloc[0]

        preds = fit_model(state, timestamp)

        n_t, bins_t = np.histogram(preds, bins_t)
        top_t = bottom_t + n_t
        verts_t[1::5, 1] = top_t
        verts_t[2::5, 1] = top_t

        n_b, bins_b = np.histogram(preds, bins_b)
        top_b = bottom_b + n_b
        verts_b[1::5, 1] = top_b
        verts_b[2::5, 1] = top_b

        date_text.set_text(timestamp)
        vote_text.set_text("{} Votes Remaining".format(str(votes)))

        mean_text.set_text("Margin = {:>8} $\pm$ {:>7}".format(int(np.mean(preds)),
                                                        int(2.*np.std(preds))))
        prob_text.set_text("Biden win prob = {:.2f}".format(np.sum(preds > 0)/len(preds)))
        
        return [patch_t, patch_b, date_text, vote_text, mean_text, prob_text]

    fig, ax = plt.subplots()
    barpath_t = path.Path(verts_t, codes_t)
    patch_t = patches.PathPatch(barpath_t, facecolor='C3',
                              edgecolor='C3', alpha=0.5)
    ax.add_patch(patch_t)
    barpath_b = path.Path(verts_b, codes_b)
    patch_b = patches.PathPatch(barpath_b, facecolor='C0',
                              edgecolor='C0', alpha=0.5)
    ax.add_patch(patch_b)

    date_text = text.Text(-9xlim//10, 9*ylim//10, start_time)
    ax.add_artist(date_text)

    df = load_data(state, start_time)
    votes = df["votes_remaining"].iloc[0]

    vote_text = text.Text(-9*xlim//10, 8*ylim//10,
                          "{} Votes Remaining".format(str(votes)))
    ax.add_artist(vote_text)

    prob_text = text.Text(9*xlim//10, 9*ylim//10,
                          "Biden win prob = {:.2f}".format(np.sum(preds > 0)/len(preds)),
                          align=right)
    ax.add_artist(prob_text)

    mean_text = text.Text(9*xlim//10, 8*ylim//10,
                          "Margin = {:>8} $\pm$ {:>7}".format(int(np.mean(preds)),
                                                        int(2.*np.std(preds))),
                          align=right)
    ax.add_artist(mean_text)

    ax.set_xlim(-xlim, xlim)
    ax.set_ylim(0, ylim)
    ax.set_xlabel("Biden margin")
    ax.set_title("{} Final Margin Prediction".format(state))

    ani = animation.FuncAnimation(fig, animate, frames=3,
                                  fargs=(state, bins_t, bins_b, bottom_t, bottom_b, start_time),
                                  repeat=False, blit=True)

    HTML(ani.to_jshtml())

for state in ["Georgia"]:
    create_animation(state)
```

## Summary

In this Data Story, we examined a hierarchical Bayesian model for the mail
votes from the 2020 election. This is a method to forecast the remaining
votes while capturing the uncertainty inherent in predicting the final
result. The final model showed...

One limitation of the predictions is that it does not account for the
uncertainty in the estimates of the remaining vote. This can be added
by explicitly adding some fixed uncertainty to the remaining vote, though
it is difficult to estimate this in a rigorous empirical fashion and
instead can only really be added as a fudge factor in the model.