# Contributing to `enigmatoolbox`

**Welcome to the `enigmatoolbox` repository!**

*We're so excited you're here and want to contribute.*

The point of this guide is to welcome new users and contributors to `enigmatoolbox`.
We hope that these guidelines are designed to make it as easy as possible to get involved.
We welcome all contributions and would love it if you could follow these guidelines to make sure your contributions can be easily integrated!
That said, please don't let [the perfect be the enemy of the good](https://en.wiktionary.org/wiki/perfect_is_the_enemy_of_good)&mdash;any contributions are worth making, even if you don't follow the process detailed below to a T.

If you have any questions that aren't discussed below, please let us know by opening an [issue][link_enigmatoolbox_issues]!

## Table of Contents

Been here before?
Already know what you're looking for in this guide?
Jump to the following sections:

-[Joining the community](#joining-the-community)
-[Contributing through Github](#contributing-through-github)
-[Where to start: GitHub Issues](#where-to-start-github-issues)
  -[Issue labels](#issue-labels)
-[Making a change with a pull request](#making-a-change-with-a-pull-request)
  -[1. Comment on or open an issue](#1-comment-on-an-existing-issue-or-open-a-new-issue-referencing-your-addition)
  -[2. Fork the `enigmatoolbox` repository](#2-forklink_fork-the-enigmatoolbox-repositorylink_enigmatoolbox-to-your-profile)
  -[3. Install `enigmatoolbox` locally](#3-install-enigmatoolbox-in-developer-mode)
  -[4. Make the discussed changes](#4-make-the-changes-youve-discussed)
  -[5. Test your changes](#5-test-your-changes)
  -[6. Submit a pull request](#6-submit-a-pull-requestlink_pullrequest)
-[Style guide](#style-guide)
  -[Writing Python code](#writing-python-code)
  -[Writing in reStructuredText](#writing-in-restructuredtext)
  -[Pull requests](#pull-requests)
-[Recognizing contributions](#recognizing-contributions)

## Joining the community

We requires that all interactions that take place on the `enigmatoolbox` repository **adhere to our [Code of Conduct](CODE_OF_CONDUCT.md)**.

## Contributing through GitHub

[Git][link_git] is a really useful tool for version control. 
[GitHub][link_github] sits on top of Git and supports collaborative and distributed working.

We know that it can be daunting to start using Git and GitHub if you haven't worked with them in the past, but `enigmatoolbox` maintainers are here to help you figure out any of the jargon or confusing instructions you encounter! :heart:

In order to contribute to `enigmatoolbox` you'll need to set up a free [GitHub][link_github] account and sign in.
You can follow these [instructions][link_signupinstructions] to help you get going, but please ask us any questions you might need along the way.

Once you have an account you'll have to use [Markdown][link_markdown] to chat in issues and pull requests on GitHub.
You can think of Markdown as a few little symbols around your text that will allow GitHub to render the text with a little bit of formatting.
For example you could write words as bold (`**bold**`), or in italics (`*italics*`), or as a [link](https://google.com) (`[link](https://google.com)`) to another webpage.

GitHub has a helpful page on [getting started with writing and formatting Markdown on GitHub][link_formatting_md].

## Where to start: GitHub Issues

Communication on `enigmatoolbox` primarily happens through discussion on our [issues][link_enigmatoolbox_issues] and [pull request][link_enigmatoolbox_prs].
Before you open a new issue, please check if any of our [open issues][link_enigmatoolbox_issues] cover your idea already!

### Issue labels

The current list of labels can be found [here][link_enigmatoolbox_labels] and includes:

-[![Good first issue](https://img.shields.io/badge/-good%20first%20issue-%237057ff)][labels_goodfirst] *These issues are great ways to get started contributing.*

  If you are interested in getting involved in `enigmatoolbox` then these are good places to start!
  The maintainers will be happy to walk you through the contribution process step-by-step.
  Please note: if you're a seasoned contributor we would appreciate if you could select a different issue to work from to keep these available for newer and potentially more anxious team members!

-[![Help Wanted](https://img.shields.io/badge/-help%20wanted-%23008672)][labels_helpwanted] *These issues contain a task that a member of the team has determined we need additional help with.*

  If you feel that you can contribute to one of these issues, we especially encourage you to do so.

-[![Bug](https://img.shields.io/badge/-bug-%23d73a4a)][labels_bugs] *These issues point to problems in the project.*

  If you find new a bug, please give as much detail as possible in your issue, including steps to recreate the error.
  If you experience the same bug as one already listed please add any additional information that you have as a comment on the issue.

-[![Documentation](https://img.shields.io/badge/-documentation-%2376e853)][labels_documentation] *These issues relate to updating documentation.*

  This is used to highlight when something is missing from or unclear in the current documentation.

-[![Question](https://img.shields.io/badge/-question-%23d876e3)][labels_question] *These issues are open-ended and don't necessarily have a definite solution.*

  If you're unclear about something in repository or the related documentation and simply need to ask a clarifying *question*, this is the label for you!
  This can also be paired with other labels (e.g., *enhancement*, *refactor*) on issues when the means by which to resolve the issue is unclear and warrants discussion.

-[![Enhancement](https://img.shields.io/badge/-enhancement-%23a2eeef)][labels_enhancement] *These issues suggest new features that can be added to the project.*

  If you want to ask for something new please try to make sure that your request is distinct from any others that are already in the queue.
  If you find another issue requesting an enhancement that is similar to your suggestion but still distinct please reference the related enhancement in your issue.

-[![Maintenance](https://img.shields.io/badge/-maintenance-%23ffe359)][labels_maintenance] *These issues relate to general package management*

  Does a dependency need to be pinned?
  Is a link not resolving anymore?
  These issues address when there's a change, update, or modification that needs to be made to the package that doesn't necessarily impact anything other besides managing `enigmatoolbox`.

-[![Refactor](https://img.shields.io/badge/-refactor-%23ffdbc6)][labels_refactor] *These issues address changes that need to be made*

  If you're suggesting a modification that isn't a bug or enhancement, but rather a change to the existing code designed to make it more accessible/understandable, this label may be appropriate.
  While refactoring often **does** significantly enhance the code, we reserve the *enhacement* label for **new** features.

-[![High priority](https://img.shields.io/badge/-high%20priority-%233387f4)][labels_highpriority] *These issues are pressing and need to be addressed urgently*
  
  This label will likely be added by an `enigmatoolbox` team member to highlight critical bugs or updates that need to be made.

-[![Testing](https://img.shields.io/badge/-testing-%23c5def5)][labels_testing] *These issues relate to code testing*

## Making a change with a pull request

We appreciate all contributions to `enigmatoolbox`!
Thank you so much for helping us build this exciting tool.

The following steps serve as a guide to help you contribute in a way that will make it easy for you and the `enigmatoolbox` team members to get your changes merged quickly and efficiently!

### 1. Comment on an existing issue or open a new issue referencing your addition

This allows other members of the `enigmatoolbox` development team to confirm that you aren't overlapping with work that's currently underway and that everyone is on the same page with the goal of the work you're going to carry out.

[This blog][link_pushpullblog] is a nice explanation of why putting this work in up front is so useful to everyone involved.

### 2. [Fork][link_fork] the [enigmatoolbox repository][link_enigmatoolbox] to your profile

This is now your own unique copy of `enigmatoolbox`.
Changes here won't effect anyone else's work, so it's a safe space to make edits to the code.

If you will be making changes on your local machine, remember to [clone your fork][link_clonerepo] of `enigmatoolbox`.

Make sure to [keep your fork up to date][link_updateupstreamwiki] with the master repository, otherwise you can end up with lots of dreaded [merge conflicts][link_mergeconflict]! :grimacing:

### 3. Install `enigmatoolbox` in "developer" mode

To test a change you may need to install the copy of `enigmatoolbox` that you [cloned][link_clonerepo] to your local machine.
To do so, change into the `enigmatoolbox` directory and run:

```bash
pip install -e .[all]
```

This should ensure that when you open Python and type `import enigmatoolbox` you are using the version of the code that you're editing!
(But note that if you make changes to the code after you've run `import enigmatoolbox` you may need to close Python and re-open a new instance for the changes to take effect.)

### 4. Make the changes you've discussed

_Before you being making changes please make sure you review the `enigmatoolbox` [style conventions](#style-guide)!_

Try to keep your changes focused.
If you submit a large amount of work all in one go it will be much more work for whomever is reviewing your pull request!

We've found that working on a [new branch][link_branches] for each Issue makes it easier to keep your changes targeted.
Using a new branch allows you to follow the ["standard" GitHub workflow](link_gitworkflow) when making changes.
[This blog](https://www.igvita.com/2011/12/19/dont-push-your-pull-requests/) details different Git branching models.

While making your changes, commit often and write good, detailed commit messages.
[This blog](https://chris.beams.io/posts/git-commit/) explains how to write a good Git commit message and why it matters.
It is also perfectly fine to have a lot of commits&mdash;including ones that break code!
If you **are** temporarily breaking things locally a good rule is to only push your changes to GitHub once your [tests](#5-test-your-changes) are passing!

### 5. Test your changes

Although `enigmatoolbox` is set up with [continuous integration (CI) testing](link_travisdocs), it's always good to test your changes locally, too!

#### Testing changes to code

If you're making modifications to the Python code in `enigmatoolbox` you can test your changes with the following command:

```bash
pytest --doctest-modules enigmatoolbox
```

This may take a while to run, but it should give you a detailed output of what tests are being run and what errors, if any, were generated.
This command is run by the CI tests when you [open a PR](#6-submit-a-pull-requestlink_pullrequest), so if you're stumped by an error message feel free to push your changes to GitHub and make a PR to ask the `enigmatoolbox` team for help!

#### Testing changes to documentation

If you're making changes to documentation we suggest rendering the HTML files locally in order to review your edits.
You can do this with the following command:

```bash
make clean html
```

which should be run from the `docs/` directory in your local `enigmatoolbox` repository.
Once this finishes you can fire up a web browser and open the `enigmatoolbox/docs/_build/html/index.html` file to investigate how the documentation looks with your modifications.

### 6. Submit a [pull request][link_pullrequest]

*Before submitting your pull request please make sure you review the `enigmatoolbox` [pull request style guide](#pull-requests)!*

We encourage you to open a pull request as early in your contributing process as possible.
This allows everyone to see what is currently being worked on.
It also provides you, the contributor, feedback in real time from both the community and the continuous integration tests as you make commits (which will help prevent stuff from breaking!).

If you have opened the pull request early and know that its contents are not ready for review or to be merged, please mark it as  ["draft" pull request][link_draftprs].
When you are happy with it and are ready for it to be merged into the main repository please mark it as ["Ready for review"][link_readyprs].
When you mark a pull request ready for review please make sure that you also check the box to [allow edits from maintainers][link_predits].

A member of the `enigmatoolbox` team will then review your changes to confirm that they can be merged into the main repository.
A review will probably consist of a few questions to help clarify the work you've done.
Keep an eye on your GitHub notifications and be prepared to join in that conversation.

If a team member requests modifications to your changes you can continue editing your local copy of the repository and push the new changes back up to your fork.
The pull request you created from your fork will be automatically updated&mdash;no need to create a new pull request when you make a change in response to reviews!

Sometimes team members will "suggest" changes to the code using GitHub's built-in suggestion feature.
In that case you can [automatically incorporate the suggested changes][link_suggestedchanges] directly from Github!

After successful merging of the pull request, remember to [keep your fork up to date][link_syncfork] with the master `enigmatoolbox` repository.

#### Continuous integration tests

What happens if the continuous integration (CI) tests fails (that is, if the pull request notifies you that "Some checks were not successful")?
The CI can fail for any number of reasons.
At the bottom of the pull request where it says whether your build passed or failed you can click “Details” next to the test.
This will automatically open the TravisCI website which details all the builds that were run for your pull request.
You can view the log for the CI test builds which will often provide the exact error that caused the failure.
Sometimes failures are stochastic and simply need to be re-run; if you think this is the case please notify someone on the `enigmatoolbox` team and they will trigger a "rebuild!"

Generally, team members won't conduct reviews of pull requests (even if they are marked as "ready for review") until the CI tests are all passing.
However, if you have any questions about your pull request before the tests are passing or if you are confused about why your tests are failing, please reach out and ask us about it!

## Style guide

### Writing Python code

To ensure some consistency in the `enigmatoolbox` Python codebase we have a few style conventions.

All code should follow the [PEP8][link_pep8] conventions, whenever possible.
Importantly, we abide by a strict 79-character line length maximum.
You can check that your code follows these conventions by running `flake8 enigmatoolbox` from inside the local copy of your `enigmatoolbox` repository.
The CI tests will error and your pull request will not be merged if your code fails to follow these conventions.

When writing new functions or classes please make sure you include doc-strings (even if they are internal functions/classes!).
Doc-strings should follow the [numpydoc][link_numpydoc] conventions.
In general we encourage extensive documentation and code comments for all contributions to `enigmatoolbox`!

### Writing in reStructuredText

Besides this document and the [Code of Conduct](CODE_OF_CONDUCT.md), all documentation for `enigmatoolbox` is written using [reStructuredText][link_rst] (RST).
You can tell whether a file is written in reStructuredText by checking for the the ".rst" suffix.
Writing our documentation in RST allows us to use the [Sphinx] documentation generator and host our documentation on [ReadTheDocs][link_readthedocs], allowing an easily accessible way to access [`enigmatoolbox` documentation][link_enigmatoolbox_docs].

While using RST can be a bit confusing at first, there are lots of fantastic resources for learning how to use it.
We especially like [this walkthrough][link_sphinxrst], but other good guides include this [primer][link_rstprimer] and this [quick reference][link_rstref].
If you have any questions as you make edits to the documentation please don't hesitate to ask!

### Pull requests

To improve understanding of pull requests "at a glance", we encourage the use of several standardized tags. 
When opening a pull request, please use at least one of the following prefixes in the title of the pull request:

-**[BRK]** for changes which break existing builds or tests
-**[DOC]** for new or updated documentation
-**[ENH]** for enhancements
-**[FIX]** for bug fixes
-**[REF]** for refactoring existing code
-**[STY]** for stylistic changes
-**[TST]** for new or updated tests, and

You can also combine the tags!
If you are updating both a test and some related documentation, you could use **[TST, DOC]**.
Feel free to look at our [closed pull requests][link_enigmatoolbox_closedprs] for examples of good titles!

The body of the pull request should first describe what issue(s) the pull request addresses using GitHub's [pull request keywords][link_prkeywords] (for example, "Closes #12" or "Fixes #13").
The remainder of the pull request body should explain what changes are being made and if there are any things you would like an `enigmatoolbox` team member to concentrate on with their feedback during their review.

## Recognizing contributions

We welcome and recognize all contributions to `enigmatoolbox` from documentation to testing to code development to participating in discussion on Issues and PRs!
You can see a list of our current contributors in the [contributors tab][link_enigmatoolbox_contributors].

---

_These Contributing Guidelines have been adapted from the contributing guidelines of [The Turing Way](https://github.com/alan-turing-institute/the-turing-way/blob/master/CONTRIBUTING.md#contributing-through-github) and [tedana](https://github.com/ME-ICA/tedana/blob/master/CONTRIBUTING.md). (License: CC-BY)_

[link_enigmatoolbox]: https://github.com/MICA-MNI/ENIGMA
[link_enigmatoolbox_contributors]: https://github.com/MICA-MNI/ENIGMA/graphs/contributors
[link_enigmatoolbox_docs]: https://enigma-toolbox.readthedocs.io/
[link_enigmatoolbox_issues]: https://github.com/MICA-MNI/ENIGMA/issues
[link_enigmatoolbox_labels]: https://github.com/MICA-MNI/ENIGMA/labels
[link_enigmatoolbox_prs]: https://github.com/MICA-MNI/ENIGMA/pulls
[link_enigmatoolbox_closedprs]: https://github.com/MICA-MNI/ENIGMA/pulls?q=is%3Apr+is%3Aclosed

[labels_bugs]: https://github.com/MICA-MNI/ENIGMA/labels/bug
[labels_documentation]: https://github.com/MICA-MNI/ENIGMA/labels/documentation
[labels_enhancement]: https://github.com/MICA-MNI/ENIGMA/labels/enhancement
[labels_goodfirst]: htttps://github.com/MICA-MNI/ENIGMA/labels/good%20first%20issue
[labels_helpwanted]: https://github.com/MICA-MNI/ENIGMA/labels/help%20wanted
[labels_highpriority]: https://github.com/MICA-MNI/ENIGMA/labels/high%20priority
[labels_lowpriority]: https://github.com/MICA-MNI/ENIGMA/labels/low%20priority
[labels_maintenance]: https://github.com/MICA-MNI/ENIGMA/labels/maintenance
[labels_question]: https://github.com/MICA-MNI/ENIGMA/labels/question
[labels_refactor]: https://github.com/MICA-MNI/ENIGMA/labels/refactor
[labels_testing]: https://github.com/MICA-MNI/ENIGMA/labels/testing

[link_branches]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository
[link_clonerepo]: https://help.github.com/articles/cloning-a-repository
[link_discussingissues]: https://help.github.com/articles/discussing-projects-in-issues-and-pull-requests
[link_draftrpr]: https://github.blog/2019-02-14-introducing-draft-pull-requests
[link_fork]: https://help.github.com/articles/fork-a-repo
[link_formatting_md]: https://help.github.com/articles/getting-started-with-writing-and-formatting-on-github
[link_git]: https://git-scm.com
[link_github]: https://github.com
[link_gitworkflow]: https://guides.github.com/introduction/flow
[link_markdown]: https://en.wikipedia.org/wiki/Markdown
[link_mergeconflict]: https://help.github.com/articles/about-merge-conflicts
[link_numpydoc]: https://numpydoc.readthedocs.io/en/latest/format.html
[link_pep8]: https://www.python.org/dev/peps/pep-0008
[link_pullrequest]: https://help.github.com/articles/creating-a-pull-request
[link_predits]: https://help.github.com/en/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork
[link_prkeywords]: https://help.github.com/en/articles/closing-issues-using-keywords
[link_pushpullblog]: https://www.igvita.com/2011/12/19/dont-push-your-pull-requests
[link_react]: https://github.com/blog/2119-add-reactions-to-pull-requests-issues-and-comments
[link_readthedocs]: https://readthedocs.org
[link_readyprs]: https://help.github.com/en/articles/changing-the-stage-of-a-pull-request
[link_rst]: http://docutils.sourceforge.net/rst.html
[link_rstprimer]: http://docutils.sourceforge.net/docs/user/rst/quickstart.html
[link_rstref]: http://docutils.sourceforge.net/docs/user/rst/quickref.html
[link_signupinstructions]: https://help.github.com/articles/signing-up-for-a-new-github-account
[link_sphinx]: https://www.sphinx-doc.org/en/master
[link_sphinxrst]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
[link_suggestedchanges]: https://help.github.com/en/articles/incorporating-feedback-in-your-pull-request
[link_syncfork]: https://help.github.com/articles/syncing-a-fork
[link_travisdocs]: https://docs.travis-ci.com/user/for-beginners
[link_updateupstreamwiki]: https://help.github.com/articles/syncing-a-fork
