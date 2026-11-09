# Requirements: staff retention office (`behavior_data/WA_Fn-UseC_-HR-Employee-Attrition.csv`)

**Client.** The head of a company's staff retention office. Each row is
one employee (1,470 rows): age, travel, department, distance from home,
education, satisfaction scores, job level and role, income, overtime,
stock options, training, work-life balance and more. The goals are
`YearsAtCompany+`, `YearsInCurrentRole+` and `YearsWithCurrManager+`
(higher is better: the person stays longer).

We ignore the ID column and three columns that have the same value for
everyone (`EmployeeNumber`, `EmployeeCount`, `StandardHours`,
`over18`). We also ignore `TotalWorkingYears` and
`YearsSinceLastPromotion`, because they mostly measure how long someone
has already been at the company, which is what we are trying to predict.

| # | The client asks... | skill |
|--:|--------------------|-------|
| 1 | Out of our staff, show me the groups who stay longest (with the company, in their role, with their manager) and what they share. | remember |
| 2 | For a new hire, guess how many years they'll stay with us, in their role and with their manager, using only what we know on day one. | guess |
| 3 | Does overtime really shorten how long people stay, or is that noise? | certify |
| 4 | As new employee records arrive one at a time, flag on the spot the ones who look like long-stayers. | flow |
| 5 | Why do some people leave early? What separates short-stayers from long-stayers? | blame |
| 6 | Give me a few rules of thumb about who stays that I can defend to leadership. | justify |
| 7 | Find the profile of a long-staying employee while reviewing only about 50 files in detail. | choose |
| 8 | This person looks like a flight risk. What's the smallest change we could make (pay, overtime, travel, level or role) that would make them at least typical? | fix |
| 9 | Flag employee records that look like nobody else (probably data-entry errors). | spot |
| 10 | Prove your shortlist beats reviewing 50 random files and keeping the best. | race |
| 11 | Group our staff into a few families so I can see the main kinds of employee we have. | remember |
| 12 | When you guess someone's tenure, give me a range, and say how often the truth lands inside it. | guess |
| 13 | Do people with better work-life balance really stay longer with their manager, or is it luck? | certify |
| 14 | Warn me when incoming records start looking different from our usual staff (say, as hires get older). | flow |
| 15 | What's the single biggest driver of how long people stay with the company? | blame |
| 16 | Explain, for this one employee, why you rated them the way you did. | justify |
| 17 | Within a given department and job role, what kind of employee stays longest? | choose |
| 18 | What would we need to change for this employee (pay, overtime, travel, level or role) to make them look like our longest-staying group? | fix |
| 19 | Who looked like a typical stayer on paper but left much sooner (or stayed much longer) than their look-alikes? | spot |
| 20 | Are your tenure guesses better than just quoting the company average? | race |

Each ask is one command: `make askNN D=hr`.

**Changed on Nov 8 (wording only; every skill is unchanged).** We
reworded asks 2, 8 and 18.
- Ask 2 now says "using only what we know on day one". To match this,
  we dropped the two columns that mostly measure time already spent at
  the company. Before, they decided almost every answer.
- Asks 8 and 18 now list what the office can actually change (pay,
  overtime, travel, level or role). Before, a suggested fix could
  include things nobody can change, such as age, gender or marital
  status.

The original wording is at tag `step0`.
