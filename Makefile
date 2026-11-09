MOOT ?= moot
# extra domains read from a MOOT clone, made on first use
EXTRA = nasa readmit commits
D    ?= pom3a

pom3a       = data/raw/pom3a.csv
pom3a_args  = --col="Team Size" --col2=Plan --goal=Idle- --goal2=Cost- \
              --drift=Dynamism --fixed=Culture,Criticality
health      = data/raw/Health-ClosedIssues0000.csv
health_args = --col=criterion --col2=Max_depth --goal=PRED40+ --goal2=MRE- \
              --drift=N_estimators --fixed=criterion,N_estimators
hr          = data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv
hr_args     = --drop=EmployeeNumber,EmployeeCount,StandardHours,over18,TotalWorkingYears,YearsSinceLastPromotion \
              --change=businessTravel,overTime,MonthlyIncome,PercentSalaryHike,StockOptionLevel,TrainingTimesLastYear,JobLevel,jobRole,department,WorkLifeBalance \
              --col=overTime --col2=WorkLifeBalance --goal=YearsWithCurrManager+ \
              --goal2=YearsAtCompany+ --drift=Age --fixed=department,jobRole
nasa        = $(MOOT)/optimize/process/nasa93dem.csv
nasa_args   = --col=pmat --col2=acap --goal=Defects- --goal2=Effort- \
              --drift=cplx --fixed=rely,cplx
readmit      = $(MOOT)/optimize/health_data/Medical_Data_and_Hospital_Readmissions.csv
readmit_args = --col=Number_inpatient --col2=Num_medications --goal=Readmitted- \
               --goal2=Readmitted- --drift=Num_lab_procedures \
               --fixed=Number_inpatient,Number_emergency
commits      = $(MOOT)/optimize/hpo/Health-Commits0000.csv
commits_args = $(health_args)

help: ## list the asks
	python3 -B -m ezl

ask%: $(if $(filter $(D),$(EXTRA)),$(MOOT)) ## run one ask, e.g. make ask07 D=hr
	python3 -B -m ezl ask$* --file=$($(D)) $($(D)_args)

demo: $(if $(filter $(D),$(EXTRA)),$(MOOT)) ## every ask on one domain
	python3 -B -m ezl all --file=$($(D)) $($(D)_args)

demos: ## every ask on all six domains
	for d in pom3a health hr nasa readmit commits; do $(MAKE) demo D=$$d || exit 1; done

test: ## unit tests
	python3 -B -m unittest discover -s tests -q

loc: ## new lines of code per step tag
	sh experiments/loc.sh

$(MOOT):
	git clone --depth 1 https://github.com/timm/moot.git $(MOOT)
