Welcome to the first Turing Data Story.

Our goal at _TuringDataStories_ is to produce educational data science content through the story telling medium.

Our stories begin with a question about a societal issue that is close to our hearts, and covers our entire analysis process in trying to answer it. From gathering and cleaning the data, to using it for data analysis.

Our hope that our stories will not only provide the reader with interesting insight into these key issues, but also to showcase the explanatory power of data science techniques and hopefully enable the reader to try out some of these techniques themselves.

Each of our stories will take the form of a Jupyter notebook, which will contain all the code required to follow along with the analysis but also an explanation of our thought process and what the code is doing.

## Covid19 Deprivation

Everyone in the UK will have been impacted by the Covid19 pandemic, from London to Manchester, Cardiff to Edinburgh. The virus has affected and taken many lives of people across society.

Back on the 23rd of March 2020, the UK Government announced various lockdown measures with the intention to limit the spread of the virus and reduce the number of Covid19 related deaths. These lockdown measures meant the temporary closure of many commercial shops and businesses, as well as the limiting of work based travel to only those jobs that could not be done at home.

We worry that the impact of Covid19 and the lockdown measures have disproportionally affected certain groups of people, in particular those in the most deprived areas whose livelihoods may have required them to leave the house more frequently.

Earlier in June, the Office of National Statistics published a report exploring this exact question: to assess whether those living in the most deprived areas of the UK were disproportionally affected by Covid19. The report seems to confirm our fear - between the months of  March to May 2020 those in the most deprived areas of the UK were more than twice as likely to die as a result of Covid19 than those in the least deprived areas.

There are two caveats that we have with the Government analysis. The first is **trust** - whether we can trust that the analysis has been performed correctly. There have been a number of concerns with Government Covid19 reporting, in particular with testing statistics. Whilst the ONS report comes attached with datasets, we would like to be able to independently confirm this analysis. The second caveat is the **time frame** of the ONS report. Between March and May represents the time when the lockdown was most severe, with measures relaxing from June onwards. We wonder whether the ONS analysis will continue to be relevant as lockdown eases. For this purpose, we wish to extend the ONS analysis for when new data comes in.

Thus for our first story we ask:

**Have the Covid19 lockdown measures disproportionally affected those that live in social-economically deprived areas of the country?"**

We have two main objectives

1) We want to confirm that the ONS analysis is correct, by attempting to replicate their analysis using the provided data.

2) We want to extend the ONS analysis to consider different time periods - representing the severity of lockdown measures - to see how this affects people from different social-economic groups.
