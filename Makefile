MOOT ?= moot
D    ?= pom3a

pom3a       = $(MOOT)/optimize/process/pom3a.csv
pom3a_args  = --col="Team Size" --col2=Plan --goal=Idle- --goal2=Cost- \
              --drift=Dynamism --fixed=Culture,Criticality
health      = $(MOOT)/optimize/hpo/Health-ClosedIssues0000.csv
health_args = --col=criterion --col2=Max_depth --goal=PRED40+ --goal2=MRE- \
              --drift=N_estimators --fixed=criterion,N_estimators
hr          = $(MOOT)/optimize/behavior_data/WA_Fn-UseC_-HR-Employee-Attrition.csv
hr_args     = --drop=EmployeeNumber,EmployeeCount,StandardHours,over18 \
              --col=overTime --col2=WorkLifeBalance --goal=YearsWithCurrManager+ \
              --goal2=YearsAtCompany+ --drift=Age --fixed=department,jobRole

help: ## list the asks
	python3 -B -m ezl

ask%: $(MOOT) ## run one ask, e.g. make ask07 D=hr
	python3 -B -m ezl ask$* --file=$($(D)) $($(D)_args)

demo: $(MOOT) ## every ask on one domain
	python3 -B -m ezl all --file=$($(D)) $($(D)_args)

demos: ## every ask on all three domains
	$(MAKE) demo D=pom3a && $(MAKE) demo D=health && $(MAKE) demo D=hr

test: $(MOOT) ## unit tests
	python3 -B -m unittest discover -s tests -q

loc: ## new lines of code per step tag (the histogram)
	sh sh/loc.sh

$(MOOT):
	git clone --depth 1 https://github.com/timm/moot.git $(MOOT)
