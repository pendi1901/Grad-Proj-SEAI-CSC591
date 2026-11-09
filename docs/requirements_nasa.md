# Requirements: NASA project estimation office (`process/nasa93dem.csv`)

**Client.** A cost-estimation manager at a NASA centre. Each row is one
past software project (93 rows), rated on the COCOMO scales (very low
to extra high): how new the work is, flexibility, risk resolution, team
cohesion, process maturity, required reliability, database size,
complexity, reuse, documentation, time and storage limits, platform
changes, analyst and programmer skill, staff turnover, application,
platform and language experience, tools, multi-site work and schedule
pressure. The goals are `Kloc+` (thousands of lines delivered, more is
better), `Effort-` (person-months, less is better) and `Defects-`
(fewer is better). We ignore the project id, centre, year and months.

| # | The client asks... | skill |
|--:|--------------------|-------|
| 1 | From our 93 past projects, show me the handful that delivered a lot of code for little effort and few defects, and what they share. | remember |
| 2 | Before a project starts, guess its size, effort and defects from its COCOMO ratings. | guess |
| 3 | Does process maturity really make projects better, or is the difference noise? | certify |
| 4 | As new project proposals come in one at a time, tell me on the spot which look like good bets. | flow |
| 5 | Why did our troubled projects blow their budgets? Which ratings separate them from the healthy ones? | blame |
| 6 | Give me a few rules of thumb about healthy projects that I can defend to the review board. | justify |
| 7 | Find the project profile that gives the most code for the least pain, while studying only a few projects in depth. | choose |
| 8 | This is our worst project. What's the smallest change in its ratings that would make it at least ordinary? | fix |
| 9 | Flag project records that look like nothing else in the database (typos, or numbers someone made up). | spot |
| 10 | Prove your profile-finder beats picking projects at random to study. | race |
| 11 | Sort our projects into a few families so I can see the kinds of work our centres do. | remember |
| 12 | When you guess a project's effort, give me a range, and tell me how often the real effort falls inside it. | guess |
| 13 | Do more capable analysts really mean fewer defects, or is that luck? | certify |
| 14 | Warn me when incoming projects start looking different from our history (say, as systems get more complex). | flow |
| 15 | What's the single biggest driver of effort? | blame |
| 16 | For this one project, explain why you rated it the way you did. | justify |
| 17 | Required reliability and complexity are set by the mission. Find the best project profile within those. | choose |
| 18 | What would this project need to change to look like our best family of projects? | fix |
| 19 | Which projects looked typical on paper but did much better or worse than their look-alikes? | spot |
| 20 | Are your effort and defect guesses actually better than quoting our historical average? | race |

Each ask is one command: `make askNN D=nasa`. With only 93 rows, the
asks with a budget of 50 measured rows (7, 10 and 17) get to see more
than half of the data, so they are weak tests here.
