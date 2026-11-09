# Requirements: open-source commit forecasting (`hpo/Health-Commits0000.csv`)

**Client.** A program manager at an open-source fund who decides which
projects get maintainer grants. They use a random-forest model to
forecast each project's commits next quarter, and want to know which
model settings to trust. Each row is one setting that was tried
(10,000 rows): the number of trees, the split criterion, the minimum
samples per leaf, the minimum impurity decrease and the maximum depth.
The goals are `MRE-` (relative error), `ACC+` (accuracy) and `PRED40+`
(the share of forecasts within 40% of the true commit count).

Note: these are the same settings as the health domain, with a
different thing being forecast. This domain checks whether results
carry over between two forecasting jobs. It is not a new kind of data.

| # | The client asks... | skill |
|--:|--------------------|-------|
| 1 | From the 10,000 forecaster settings tried, show the few that forecast commit activity best, and what they share. | remember |
| 2 | Before we spend compute, guess how well this setting will forecast commits. | guess |
| 3 | Does the split criterion really matter for commit forecasts, or is that noise? | certify |
| 4 | As tuning jobs finish, tell me right away which settings are worth keeping. | flow |
| 5 | Why do some settings forecast commits so badly? Which knobs are to blame? | blame |
| 6 | Give our grant reviewers a few plain rules for configuring the forecaster. | justify |
| 7 | Find a near-best setting while running only about 50 tuning jobs. | choose |
| 8 | Our current setting is among the worst. What's the smallest change that makes it at least average? | fix |
| 9 | Flag tuning results that look like glitches. | spot |
| 10 | Show your tuner beats 50 random settings. | race |
| 11 | Group the settings into a few families. | remember |
| 12 | Give each accuracy guess a range, and say how often the truth falls inside it. | guess |
| 13 | Do deeper trees really get more forecasts within 40%, or is it luck? | certify |
| 14 | Warn me when tuning results drift as we try bigger forests. | flow |
| 15 | What's the single biggest driver of forecast error? | blame |
| 16 | Explain why you rated this particular setting the way you did. | justify |
| 17 | Our CI box allows one criterion and roughly one forest size. Find the best setting within that. | choose |
| 18 | What would this setting need to change to match our best family? | fix |
| 19 | Which settings did far better or worse than similar ones? | spot |
| 20 | Are your accuracy guesses better than quoting the average result? | race |

Each ask is one command: `make askNN D=commits`.
