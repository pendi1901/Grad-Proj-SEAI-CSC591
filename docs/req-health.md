# Requirements: open-source health forecasting (`hpo/Health-ClosedIssues0000.csv`)

**Client.** The analytics lead at an open-source foundation. They
forecast how many issues each member project will close next
quarter, using a random-forest forecaster, and they want it tuned.
Each row is one forecaster setting that was tried (10,000 rows).
The knobs: number of trees, split criterion, minimum samples per
leaf, minimum impurity decrease, maximum depth. The outcomes:
`MRE-` (relative error, lower is better), `ACC+` (accuracy, higher
is better), `PRED40+` (share of forecasts within 40% of the truth,
higher is better).

| # | The client asks... | skill |
|--:|--------------------|-------|
| 1 | From the 10,000 forecaster settings we've tried, show the few that predict closed issues most accurately, and what they share. | remember |
| 2 | Before we spend compute on a run, guess how accurate this forecaster setting will be. | guess |
| 3 | Does the choice of split criterion really matter, or is the difference noise? | certify |
| 4 | As tuning runs finish one by one, tell me immediately which settings look like keepers. | flow |
| 5 | Why do some settings forecast so badly? Which knobs separate good from bad? | blame |
| 6 | Give our maintainers a few rules of thumb for configuring the forecaster that they can trust. | justify |
| 7 | Find a near-best forecaster setting while running only about 50 tuning jobs. | choose |
| 8 | Our current setting is one of the worst. What's the smallest change that makes it at least average? | fix |
| 9 | Flag tuning results that look like glitches: settings unlike anything else we've logged. | spot |
| 10 | Show your tuner beats running 50 random settings and keeping the best. | race |
| 11 | Group the settings into a few families so we can see the main styles of forecaster. | remember |
| 12 | When you guess a setting's accuracy, give a range, and say how often the real result falls inside it. | guess |
| 13 | Do deeper trees really get us within 40% of the true count more often, or is that luck? | certify |
| 14 | Warn me when new tuning results start drifting from what we've seen (as we try bigger and bigger forests). | flow |
| 15 | What's the single biggest driver of forecast error? | blame |
| 16 | Explain to a maintainer why you rated their particular setting the way you did. | justify |
| 17 | Our CI box is stuck with one split criterion and roughly one forest size. Find the best setting within that. | choose |
| 18 | What would this setting need to change to match our best family of settings? | fix |
| 19 | Which settings look ordinary but did far better or worse than similar ones? | spot |
| 20 | Are your accuracy guesses better than just quoting the average result? | race |

Each ask is one demo: `make askNN D=health`.
