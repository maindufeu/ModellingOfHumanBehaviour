# Tom Suter
# 19.10.2017

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *


#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_PT = Beta('ASC_PT',0.926131,-10000,10000,0,'ASC_PT' )

Time = Beta('Time',-0.0108355,-10000,10000,0,'Time' )

Cost = Beta('Cost',0.0337038,-10000,10000,0,'Cost' )

ASC_PM  = Beta('ASC_PM ',1.76034,-10000,10000,0,'ASC_PM ' )

## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_PT','Cost','Time']
values = [[0.0184354,0.0197142,0.000132191,-7.08996e-05],[0.0197142,0.0286246,0.000132408,-0.000136624],[0.000132191,0.000132408,2.56734e-05,-5.70885e-06],[-7.08996e-05,-0.000136624,-5.70885e-06,2.25818e-06]]
vc = bioMatrix(4,names,values)
BIOGEME_OBJECT.VARCOVAR = vc




# Define here arithmetic expressions for name that are not directly available from the data
pm_avail =  DefineVariable('pm_avail', ((CarAvail != 3)+(NbMoto>=1))>0 )
bike_walk_avail =  DefineVariable('bike_walk_avail', ((distance_km)<8 + (NbBicy>0)*(distance_km)<16)>0)

one  = DefineVariable('one',1)




# Utilities
## public transport
Opt1 = ASC_PT*one+Time*TimePT +Cost* CostPT
## private mode
Opt2 = ASC_PM*one+Time*TimeCar+Cost*CostCar
## soft modes
Opt3 = 0*one

V = {0: Opt1,1: Opt2,2: Opt3}
av = {0: one,1: pm_avail,2: bike_walk_avail}



#Exclude
BIOGEME_OBJECT.EXCLUDE = (Choice   ==  -1) + \
                         ((Choice == 1) * (pm_avail != 1) > 0)+ \
                          ((Choice == 2)* (bike_walk_avail!=1)>0)

BIOGEME_OBJECT.STATISTICS['SampleSize'] = Sum(one, 'obsIter')
x = Sum(one, 'obsIter')
BIOGEME_OBJECT.STATISTICS['UnAdjustedWeightSum']= Sum(Weight, 'obsIter')/x
y = Sum(Weight, 'obsIter')
BIOGEME_OBJECT.WEIGHT =  Weight*(x/y)
AdjWeight = Weight*(x/y)
BIOGEME_OBJECT.STATISTICS['AdjustedWeightSum'] = Sum(AdjWeight, 'obsIter')/x
AdjSum = Sum(AdjWeight, 'obsIter')


#### SIMULATION #####
prob_0 = bioLogit(V,av,0)
prob_1 = bioLogit(V,av,1)
prob_2 = bioLogit(V,av,2)
VOT_CAR = Derive(Opt2,'TimeCar')/Derive(Opt2,'CostCar')
VOT_PT = Derive(Opt1,'TimePT')/Derive(Opt1,'CostPT')
simulate = { 'probPT' : prob_0, 'probPM': prob_1, 'probSM' : prob_2,'VOT_CAR':VOT_CAR,'VOT_PT':VOT_PT }


# MNL (Multinomial Logit model), with availability conditions
logprob = bioLogLogit(V,av,Choice)

# Defines an iterator on the data
rowIterator('obsIter')

# Define the likelihood function for the estimation
BIOGEME_OBJECT.SIMULATE = Enumerate(simulate,'obsIter')

# Optimization algorithm
BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "BIO"
BIOGEME_OBJECT.PARAMETERS['stopFileName'] = "STOP"

# Print some statistics:
nullLoglikelihood(av,'obsIter')
choiceSet = [0,1,2]
cteLoglikelihood(choiceSet,Choice,'obsIter')
availabilityStatistics(av,'obsIter')
BIOGEME_OBJECT.FORMULAS['Opt1'] = Opt1
BIOGEME_OBJECT.FORMULAS['Opt2'] = Opt2
BIOGEME_OBJECT.FORMULAS['Opt3'] = Opt3

print('AdjSum',AdjSum)
print('y', y)
