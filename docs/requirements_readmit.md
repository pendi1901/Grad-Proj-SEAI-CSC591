# Requirements: hospital readmissions team (`health_data/Medical_Data_and_Hospital_Readmissions.csv`)

**Client.** The discharge-planning lead at a hospital's diabetes unit.
Each row is one patient stay (25,000 rows): days in hospital, lab
tests, procedures, medications, earlier outpatient, emergency and
inpatient visits, number of diagnoses, and yes/no columns for
demographics, payer, specialty, common diagnoses and each diabetes
drug. There is one goal, `Readmitted-` (1 = the patient came back,
0 = they did not; lower is better).

| # | The client asks... | skill |
|--:|--------------------|-------|
| 1 | Out of 25,000 stays, show me the groups of patients who almost never come back, and what they have in common. | remember |
| 2 | At discharge, guess whether this patient will be readmitted. | guess |
| 3 | Are patients with earlier inpatient stays really readmitted more, or is that noise? | certify |
| 4 | As patients are discharged one at a time, flag on the spot the ones at low risk of coming back. | flow |
| 5 | Why do some patients keep coming back? What separates them from those who don't? | blame |
| 6 | Give my nurses a few rules of thumb about readmission risk that they can trust. | justify |
| 7 | Find the lowest-risk patient profile while chart-reviewing only about 50 patients. | choose |
| 8 | This patient looks very likely to come back. What's the smallest change in their care that would make them at least typical? | fix |
| 9 | Flag patient records that look like nobody else's (probably coding errors). | spot |
| 10 | Prove your shortlist beats chart-reviewing 50 random patients. | race |
| 11 | Group our patients into a few families so I can see the main kinds of stay we handle. | remember |
| 12 | When you guess a patient's risk, give me a range, and say how often the outcome lands inside it. | guess |
| 13 | Does the number of medications at discharge really change readmission, or is that luck? | certify |
| 14 | Warn me when incoming patients start looking different from our usual case mix (say, as lab workloads rise). | flow |
| 15 | What's the single biggest driver of readmission? | blame |
| 16 | For this one patient, explain why you rated their risk the way you did. | justify |
| 17 | We can't change a patient's history of inpatient and emergency visits. Within that, what care profile has the lowest risk? | choose |
| 18 | What would this patient's stay need to change to look like our lowest-risk group? | fix |
| 19 | Which patients looked low-risk on paper but came back anyway (or the reverse)? | spot |
| 20 | Are your risk guesses better than just quoting our overall readmission rate? | race |

Each ask is one command: `make askNN D=readmit`. Because the only goal
is yes/no, the "score" in this domain is just the readmission rate.
