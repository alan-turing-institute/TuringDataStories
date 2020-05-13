# Contributing to the Turing Data Stories project

 **Welcome to the Turing Data Stories project** 

_We're so excited you're here and want to contribute._ 

We hope that this guideline document will make it as easy as possible for you to get involved.

We welcome all contributions to this project via GitHub issues and pull requests. 
Please follow these guidelines to make sure your contributions can be easily integrated in the projects. 

# Contributing through GitHub

[Git][git] is a really useful tool for version control. [GitHub][github] sits on top of Git and supports collaborative and distributed working.

In order to contribute via GitHub you'll need to set up a free account and sign in.
Here are some [instructions](https://help.github.com/articles/signing-up-for-a-new-github-account/) to help you get going.
Remember that you can ask us any questions you need to along the way.

## Where to start: issues

If you have a new idea about a data story or implementation that can be done in this project you can let use know via an issue.
Before you open a new issue, please check if any of our [open issues](https://github.com/alan-turing-institute/TuringDataStories/issues) covers your idea already.

### Issue labels

The list of labels for current issues can be found [here][turing-way-labels] and includes:

- [![approval-request](https://img.shields.io/badge/-approval%20request-8bd82d.svg)][labels-approval-request] _When a bug or minor changes have been made, contributors can label their PR along with "bug fixed"._

- [![book-build](https://img.shields.io/badge/-book--build-8d7aef.svg)][data-story-idea] _These issues are related to the a new data story idea.


- [![Bug](https://img.shields.io/badge/-bug-d73a4a.svg)][labels-bug] _These issues are reporting a problem or a mistake in the project._

  The more details you can provide the better!
  If you know how to fix the bug, please open an issue first and then submit a pull request :sparkles:

- [![bug-fixed](https://img.shields.io/badge/-bug%20fixed-cef298.svg)][labels-bug-fixed] _These are bugs that have been fixed and only need approval._

- [![collaboration-book](https://img.shields.io/badge/-collaboration--book-c877ff.svg)][labels-collaboration-book] _These issues relate to the content of the collaboration book._

- [![Comms](https://img.shields.io/badge/-comms-15c4b2.svg)][labels-comms] _These issues discuss how we as a project interact with other initiatives._

- [![Community](https://img.shields.io/badge/-community-8605c1.svg)][labels-community] _These issues relate to building and supporting the Turing Data Stories community._

- [![Enhancement](https://img.shields.io/badge/-enhancement-84b6eb.svg)][labels-enhancement] _These issues are suggesting new features that can be added to the project._

  If you want to ask for something new, please try to make sure that your request is distinct from any others that are already in the queue (or part of the Turing Data Stories).
  If you find one that's similar but there are subtle differences please reference the other enhancement in your issue.

- [![good-first-issue](https://img.shields.io/badge/-good%20first%20issue-1b3487.svg)][labels-firstissue] _These issues are particularly appropriate if it is your first contribution to the Turing Data Stories, or to GitHub overall._

  If you're not sure about how to go about contributing, these are good places to start. You'll be mentored through the process by the maintainers team.
  If you're a seasoned contributor, please select a different issue to work from and keep these available for the newer and potentially more anxious team members.

- [![help-wanted](https://img.shields.io/badge/-help%20wanted-159818.svg)][labels-helpwanted] _These issues contain a task that a member of the team has determined we need additional help with._

  If you feel that you can contribute to one of these issues, we especially encourage you to do so!

- [![project-management](https://img.shields.io/badge/-project%20management-bfd86c.svg)][labels-project-management] _We like to model best practice, so the Turing Data Stories itself is managed through these issues.
  These issues help us to coordinate some logistics._

- [![question](https://img.shields.io/badge/-question-cc317c.svg)][labels-question] _These issues contain a question that you'd like to have answered._

  There are [lots of ways to ask questions](#get-in-touch) but opening an issue is a great way to start a conversation and get your answer.

  - [![work-in-progress](https://img.shields.io/badge/-work--in--progress-e08f72.svg)][labels-work-in-progress] _These issues are work in progress._

## Making a change with a pull request


The following steps are a guide to help you contribute in a way that will be easy for everyone to review and accept with ease :sunglasses:.

### 1. Comment on an [existing issue](https://github.com/alan-turing-institute/TuringDataStories/issues) or open a new issue referencing your addition

This allows other members of the Turing Data Stories team to confirm that you aren't overlapping with work that's currently underway and that everyone is on the same page with the goal of the work you're going to carry out.

[This blog](https://www.igvita.com/2011/12/19/dont-push-your-pull-requests/) is a nice explanation of why putting this work in up front is so useful to everyone involved.

### 2. [Fork][github-fork] the [Turing Data Stories repository][turing-data-stories] to your profile

This is now your own unique copy of the Turing Data Stories repo.
Changes here won't affect anyone else's work, so it's a safe space to explore edits to the code!

Make sure to [keep your fork up to date][github-syncfork] with the master repository, otherwise you can end up with lots of dreaded [merge conflicts][github-mergeconflicts].
If you prefer working in the browser, [these instructions](https://github.com/KirstieJane/STEMMRoleModels/wiki/Syncing-your-fork-to-the-original-repository-via-the-browser) describe how to sync your fork to the original repository via GitHub.

### 3. Make the changes you've discussed

Try to keep the changes focused.
If you submit a large amount of work all in one go it will be much more work for whomever is reviewing your pull request.
[Help them help you.][jerry-maguire] :wink:

While making your changes, commit often and write good, detailed commit messages.
[This blog](https://chris.beams.io/posts/git-commit/) explains how to write a good Git commit message and why it matters.
It is also perfectly fine to have a lot of commits - including ones that break code.
A good rule of thumb is to push up to GitHub when you _do_ have passing tests then the continuous integration (CI) has a good chance of passing everything. 😸

If you feel tempted to "branch out" then please make a [new branch][github-branches] and a [new issue][turing-way-issues] to go with it. [This blog](https://nvie.com/posts/a-successful-git-branching-model/) details the different Git branching models.

Please do not re-write history!
That is, please do not use the [rebase](https://help.github.com/en/articles/about-git-rebase) command to edit previous commit messages, combine multiple commits into one, or delete or revert commits that are no longer necessary.

Are you new to Git and GitHub or just want a detailed guide on getting started with version control? Check out our [Version Control chapter](https://the-turing-way.netlify.com/version_control/version_control.html) in the Turing Data StoriesBook!

### 4. Submit a [pull request][github-pullrequest]

We encourage you to open a pull request as early in your contributing process as possible.
This allows everyone to see what is currently being worked on.
It also provides you, the contributor, feedback in real time from both the community and the continuous integration as you make commits (which will help prevent stuff from breaking).

When you are ready to submit a pull request, you will automatically see the [Pull Request Template](https://github.com/alan-turing-institute/the-turing-way/blob/master/.github/PULL_REQUEST_TEMPLATE.md) contents in the pull request body.
It asks you to:

- Describe the problem you're trying to fix in the pull request, reference any related issue and use fixes/close to automatically close them, if pertinent.
- List of changes proposed in the pull request.
- Describe what the reviewer should concentrate their feedback on.

By filling out the "_Lorem ipsum_" sections of the pull request template with as much detail as possible, you will make it really easy for someone to review your contribution!

If you have opened the pull request early and know that its contents are not ready for review or to be merged, add "[WIP]" at the start of the pull request title, which stands for "Work in Progress".
When you are happy with it and are happy for it to be merged into the main repository, change the "[WIP]" in the title of the pull request to "[Ready for review]".

A member of the Turing Data Storiesteam will then review your changes to confirm that they can be merged into the main repository.
A [review][github-review] will probably consist of a few questions to help clarify the work you've done.
Keep an eye on your GitHub notifications and be prepared to join in that conversation.

You can update your [fork][github-fork] of the Turing Data Stories[repository][turing-data-stories] and the pull request will automatically update with those changes.
You don't need to submit a new pull request when you make a change in response to a review.

You can also submit pull requests to other contributors' branches!
Do you see an [open pull request](https://github.com/alan-turing-institute/the-turing-way/pulls) that you find interesting and want to contribute to?
Simply make your edits on their files and open a pull request to their branch!

What happens if the continuous integration (CI) fails (for example, if the pull request notifies you that "Some checks were not successful")?
The CI could fail for a number of reasons.
At the bottom of the pull request, where it says whether your build passed or failed, you can click “Details” next to the test, which takes you to the Travis page.
You can view the log or rerun the checks if you have write access to the repo by clicking the “Restart build” button in the top right (you must be logged in to Travis CI with your GitHub account see the “Restart build” button).
You can learn more about Travis in the [Continuous Integration chapter](https://the-turing-way.netlify.com/continuous_integration/continuous_integration.html) of the book!

GitHub has a [nice introduction][github-flow] to the pull request workflow, but please [get in touch](#get-in-touch) if you have any questions :balloon:.

## The process of writing a data story

- Fork the repository from the alan turing version if you have not done so already.
- On the alan turing version create a branch with the same name as the data story to be written.
- On your fork create a branch with the same name and create a markdown file on it.
- Make a pull request to the Turing Data Stories version of the story branch.
  The title of this request should have the form "[WIP] Write Chapter_name chapter".
  WIP indicates the chapter is a Work In Progress and not yet ready for review.
- On your branch add material to the story and commit.
  The goal of this project is to collate and build on the many good resources already available about good practise in data science.
  As such this material should primarily be drawn from outside sources.
  Note the link and (if available) license of the source.
- Once the first draft of the data story is complete change [WIP] in the pull request title to [Ready for review].
- Once the review is complete merge the pull request into the alan turing intitute's version of the chapter branch.
- Merge the alan turing intitute's version of the story branch into the alan turing master branch.
- DO not delete the branch as the chapter may continue to undergo improvement and development in the future.

## Style Guide


### Writing style

To ensure all text can be read easily by all (including screen readers and non-native english speakers), follow Gov.uk guidance on e.g., i.e., and etc. (1)
That is, do not use them:

eg can sometimes be read aloud as ‘egg’ by screen reading software. Instead use ‘for example’ or ‘such as’ or ‘like’ or ‘including’ - whichever works best in the specific context.

etc can usually be avoided.
Try using ‘for example’ or ‘such as’ or ‘like’ or ‘including’.
Never use etc at the end of a list starting with these words.

ie - used to clarify a sentence - is not always well understood.
Try (re)writing sentences to avoid the need to use it. If that is not possible, use an alternative such as ‘meaning’ or ‘that is’.

1. https://www.gov.uk/guidance/style-guide/a-to-z-of-gov-uk-style#eg-etc-and-ie

### Sentences

When writing all sentences should go on a new line.
This will make no difference to how the text is displayed, there will still be paragraphs, but it will mean that any pull requests will be easier to check; the changes will be on a single line instead of somewhere in a paragraph. Consider the example below.

 ```
Today you are you, that is truer than true. There is no one alive who is youer than you. - Dr Seuss
```

 A pull request on this correcting it to have a ‘.’ after Dr would show as a change to the whole paragraph.
Contrast this with the next example which will be displayed online in the exact same way, but would see a change to a single line.

 ```
Today you are you, that is truer than true.
There is no one alive who is youer than you.
- Dr Seuss
```


### Figures

To make things look cleaner, it is advised that all figures be encapsulated in a table with a caption.
This can be done simply as:

```
| ![A dish with Green Eggs and Ham](/figures/green_eggs_ham.jpg)         |
| ------------------------------------------------------------------------------------ |
| Try them, try them, and you may! Try them and you may, I say.  |
```

Figures should be added to the `book/content/figures` directory.

### Referencing and Citing

Make sure you story has all the references included.

## Recognising Contributions

The Turing Data Stories follows the [all-contributors][all-contributors] specification, so we welcome and recognise all contributions from documentation to testing to writing chapters.
You can see a list of current contributors [here](https://github.com/alan-turing-institute/the-turing-way/blob/master/contributors.md). 😍

The all-contributors bot usage is described [here](https://allcontributors.org/docs/en/bot/usage).
To add yourself or someone else as a contributor, comment on the relevant Issue or Pull Request with the following:

```
@all-contributors please add <username> for <contributions>
```

You can see the [Emoji Key (Contribution Types Reference)](https://allcontributors.org/docs/en/emoji-key) for a list of valid `<contribution>` types and examples of how we've run this command in [this issue](https://github.com/alan-turing-institute/the-turing-way/issues/274).
The bot will then create a Pull Request to add the contributor and reply with the pull request details.

**PLEASE NOTE: Only one contributor can be added with the bot at a time!**
Add each contributor in turn, merge the pull request and delete the branch (`all-contributors/add-<username>`) before adding another one.
Otherwise, you can end up with dreaded [merge conflicts][github-mergeconflicts].
Therefore, please check the [open pull requests](https://github.com/alan-turing-institute/the-turing-way/pulls) first to make sure there aren't any open requests from the bot before adding another.

What happens if you accidentally run the bot before the previous run was merged and you got those pesky merge conflicts?
(Don't feel bad, we have all done it! 🙈)
Simply close the pull request and delete the branch (`all-contributors/add-<username>`).
If you are unable to do this for any reason, please let us know in the [Gitter channel](https://gitter.im/alan-turing-institute/the-turing-way) or by opening an issue, and a Turing Data Stories team member will be very happy to help!

Finally, don't forget to add yourself to the list of contributors [here](https://github.com/alan-turing-institute/the-turing-way/blob/master/contributors.md)!

---

_These Contributing Guidelines have been adapted from the [Contributing Guidelines](https://github.com/alan-turing-institute/the-turing-way/blob/master/CONTRIBUTING.md) of [The Turing Way project](https://github.com/alan-turing-institute/the-turing-way)  (License: CC-BY)_

[turing-data-stories]: https://github.com/alan-turing-institute/TuringDataStories/issues
[turing-data-stories-repo]: https://github.com/alan-turing-institute/TuringDataStories/
[turing-way-issues]: https://github.com/alan-turing-institute/the-turing-way/issues
[turing-way-labels]: https://github.com/alan-turing-institute/the-turing-way/labels
[git]: https://git-scm.com
[github]: https://github.com
[github-branches]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository
[github-fork]: https://help.github.com/articles/fork-a-repo
[github-flow]: https://guides.github.com/introduction/flow
[github-mergeconflicts]: https://help.github.com/articles/about-merge-conflicts
[github-pullrequest]: https://help.github.com/articles/creating-a-pull-request
[github-review]: https://help.github.com/articles/about-pull-request-reviews
[github-syncfork]: https://help.github.com/articles/syncing-a-fork
[issue-template]: https://github.com/alan-turing-institute/the-turing-way/blob/master/ISSUE_TEMPLATE.md
[labels-link]: https://github.com/alan-turing-institute/the-turing-way/labels
[labels-book]: https://github.com/alan-turing-institute/the-turing-way/labels/book
[labels-bug]: https://github.com/alan-turing-institute/the-turing-way/labels/bug
[labels-bug-fixed]: https://github.com/alan-turing-institute/the-turing-way/labels/bug%20fixed
[labels-collaboration-book]: https://github.com/alan-turing-institute/the-turing-way/labels/collaboration%2Dbook
[labels-communication-book]: https://github.com/alan-turing-institute/the-turing-way/labels/communication%2Dbook
[labels-community]: https://github.com/alan-turing-institute/the-turing-way/labels/community
[labels-comms]: https://github.com/alan-turing-institute/the-turing-way/labels/comms
[labels-conflicting-file-error]: https://github.com/alan-turing-institute/the-turing-way/labels/conflicting%2Dfile%2Derror
[labels-dependencies]: https://github.com/alan-turing-institute/the-turing-way/labels/dependencies
[labels-enhancement]: https://github.com/alan-turing-institute/the-turing-way/labels/enhancement
[labels-ethics-book]: https://github.com/alan-turing-institute/the-turing-way/labels/ethics%2Dbook
[labels-events]: https://github.com/alan-turing-institute/the-turing-way/labels/events
[labels-firstissue]: https://github.com/alan-turing-institute/the-turing-way/labels/good%20first%20issue
[labels-helpwanted]: https://github.com/alan-turing-institute/the-turing-way/labels/help%20wanted
[labels-idea-for-discussion]: https://github.com/alan-turing-institute/the-turing-way/labels/idea%2Dfor%2Ddiscussion
[labels-jupyter]: https://github.com/alan-turing-institute/the-turing-way/labels/jupyter
[labels-project-management]: https://github.com/alan-turing-institute/the-turing-way/labels/project%20management
[labels-newsletter]: https://github.com/alan-turing-institute/the-turing-way/labels/newsletter
[labels-outreach]: https://github.com/alan-turing-institute/the-turing-way/labels/Outreach
[labels-pr-draft]: https://github.com/alan-turing-institute/the-turing-way/labels/PR%3A%20draft
[labels-pr-merged]: https://github.com/alan-turing-institute/the-turing-way/labels/PR%3A%20merged
[labels-pr-partially-approved]: https://github.com/alan-turing-institute/the-turing-way/labels/PR%3A%20partially%2Dapproved
[labels-pr-reviewed-approved]: https://github.com/alan-turing-institute/the-turing-way/labels/PR%3A%20reviewed%2Dapproved
[labels-pr-reviewed-changes-requested]: https://github.com/alan-turing-institute/the-turing-way/labels/PR%3A%20reviewed%2Dchanges%2Drequested
[labels-pr-unreviewed]: https://github.com/alan-turing-institute/the-turing-way/labels/PR%3A%20unreviewed
[labels-project-design-book]: https://github.com/alan-turing-institute/the-turing-way/labels/project%2Ddesign%2Dbook
[labels-question]: https://github.com/alan-turing-institute/the-turing-way/labels/question
[labels-ready-for-merge]: https://github.com/alan-turing-institute/the-turing-way/labels/ready%20for%20merge
[labels-reproducibility-book]: https://github.com/alan-turing-institute/the-turing-way/labels/reproducibility%2Dbook
[labels-research-related-theory]: https://github.com/alan-turing-institute/the-turing-way/labels/research%2Drelated%2Dtheory
[labels-review-request]: https://github.com/alan-turing-institute/the-turing-way/labels/review%20request
[labels-software-skills]: https://github.com/alan-turing-institute/the-turing-way/labels/software%2Dskills
[labels-tools]: https://github.com/alan-turing-institute/the-turing-way/labels/tools
[labels-translation]: https://github.com/alan-turing-institute/the-turing-way/labels/translation
[labels-travel]: https://github.com/alan-turing-institute/the-turing-way/labels/travel
[labels-typo-fix]: https://github.com/alan-turing-institute/the-turing-way/labels/typo%2Dfix
[labels-work-in-progress]: https://github.com/alan-turing-institute/the-turing-way/labels/work%2Din%2Dprogress
[labels-workshops]: https://github.com/alan-turing-institute/the-turing-way/labels/workshops
[markdown]: https://daringfireball.net/projects/markdown
[rick-roll]: https://www.youtube.com/watch?v=dQw4w9WgXcQ
[jerry-maguire]: https://media.giphy.com/media/uRb2p09vY8lEs/giphy.gif
[all-contributors]: https://github.com/kentcdodds/all-contributors#emoji-key
