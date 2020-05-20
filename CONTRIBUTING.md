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

You can update your [fork][github-fork] of the Turing Data Stories [repository][turing-data-stories] and the pull request will automatically update with those changes.
You don't need to submit a new pull request when you make a change in response to a review.

You can also submit pull requests to other contributors' branches!
Do you see an [open pull request](https://github.com/alan-turing-institute/TuringDataStories/pulls) that you find interesting and want to contribute to?
Simply make your edits on their files and open a pull request to their branch!

GitHub has a [nice introduction][github-flow] to the pull request workflow, but please [get in touch](#get-in-touch) if you have any questions.

## The process of writing a data story

- Fork the repository from the alan turing version if you have not done so already.
- On the alan turing version create a branch with the same name as the data story to be written.
- On your fork create a branch with the same name and create a markdown file on it.
- Make a pull request to the Turing Data Stories version of the data story branch.
  The title of this request should have the form "[WIP] Write data_story_name data story".
  WIP indicates the data story is a Work In Progress and not yet ready for review.
- On your branch add material to the data story and commit.
  The goal of this project is to collate and build on the many good resources already available about good practise in data science.
  As such this material should primarily be drawn from outside sources.
  Note the link and (if available) license of the source.
- Once the first draft of the data story is complete change [WIP] in the pull request title to [Ready for review].
- Once the review is complete merge the pull request into the alan turing intitute's version of the data story branch.
- Merge the alan turing intitute's version of the data story branch into the alan turing master branch.
- DO not delete the branch as the data story may continue to undergo improvement and development in the future.



### Referencing and Citing

Make sure you data story has all the references included.

---

_These Contributing Guidelines have been adapted from the [Contributing Guidelines](https://github.com/alan-turing-institute/the-turing-way/blob/master/CONTRIBUTING.md) of [The Turing Way project](https://github.com/alan-turing-institute/the-turing-way)  (License: CC-BY)_

[turing-data-stories]: https://github.com/alan-turing-institute/TuringDataStories/issues
[turing-data-stories-repo]: https://github.com/alan-turing-institute/TuringDataStories/
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
[markdown]: https://daringfireball.net/projects/markdown
[rick-roll]: https://www.youtube.com/watch?v=dQw4w9WgXcQ
[jerry-maguire]: https://media.giphy.com/media/uRb2p09vY8lEs/giphy.gif
