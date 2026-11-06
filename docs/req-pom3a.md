# Requirements: agile delivery office (`process/pom3a.csv`)

**Client.** The head of delivery at an agile consultancy. Each row is
one simulated project (POM3 requirements-prioritisation model,
20,000 rows). The knobs: team culture, system criticality,
criticality modifier, how many requirements are known up front,
inter-dependency, requirements dynamism, size, planning effort,
team size. The outcomes: `Cost-`, `Score-`, `Idle-` (lower is better
for all three, as the data marks them).

| # | The client asks... | skill |
|--:|--------------------|-------|
| 1 | Out of 20,000 past project setups, show me the few that came in cheap, on target and with nobody sitting idle, and what they have in common. | remember |
| 2 | Before we kick off, guess this project's cost, score and idle time from its setup. | guess |
| 3 | Do small teams really do better than big teams, or is that just noise? | certify |
| 4 | As new project proposals land on my desk one at a time, tell me on the spot which look like winners. | flow |
| 5 | Why do the bad projects go bad? Show me which setup choices separate them from the good ones. | blame |
| 6 | Give me two or three rules of thumb I can defend to the board: what our best and worst projects look like. | justify |
| 7 | Find us a near-best project setup while only piloting about 50 of them. | choose |
| 8 | This is our worst project. What's the smallest change to its setup that makes it at least ordinary? | fix |
| 9 | Flag project records that look like nothing else we've run (probably typos or broken logging). | spot |
| 10 | Prove your setup-finder beats piloting 50 random setups and keeping the best. | race |
| 11 | Sort our projects into a handful of families so I can see the kinds of work we actually do. | remember |
| 12 | When you guess a project's numbers, give me a range, and tell me how often the truth lands inside it. | guess |
| 13 | Did more up-front planning actually cut idle time, or did we just get lucky? | certify |
| 14 | Warn me as soon as incoming projects start behaving differently from the ones we're used to (say, as requirements get more volatile). | flow |
| 15 | What's the single biggest driver of cost? | blame |
| 16 | For this one project, explain in plain terms why you rated it the way you did. | justify |
| 17 | We can't change our team culture or how safety-critical the system is. Find the best setup within those limits. | choose |
| 18 | What would this project need to change to look like our best family of projects? | fix |
| 19 | Which projects looked perfectly normal on paper but turned out much better or worse than their look-alikes? | spot |
| 20 | Are your cost and idle guesses actually better than just quoting our average? | race |

Each ask is one demo: `make askNN D=pom3a` (for example `make ask07 D=pom3a`).
