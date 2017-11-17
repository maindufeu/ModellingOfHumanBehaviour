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
ASC_PT = Beta('ASC_PT',0,-10000,10000,1)
ASC_PM =  Beta('ASC_PM ',0,-10000,10000,0)
ASC_SM = Beta('ASC_SM',0,-10000,10000,0)
Time= Beta('Time',0,-10000,10000,0)
Distance= Beta('Distance',0,-10000,10000,0)
Cost = Beta('Cost',0,-10000,10000,0)

# Define here arithmetic expressions for name that are not directly available from the data

one  = DefineVariable('one',1)
#----time
car_time  = DefineVariable('car_time', TimeCar  )
pt_time = DefineVariable('pt_time', TimePT)
distance_trip=DefineVariable('distance_trip',distance_km)
#---cost
car_cost=DefineVariable('car_cost',CostCar)
PT_cost=DefineVariable('PT',CostPT)
reported_time=DefineVariable('reported_time',ReportedDuration)

# Utilities
## public transport
Opt1 = ASC_PT*one+Time*pt_time +Cost* PT_cost
## private mode
Opt2 = ASC_PM*one+Time*car_time+Cost*car_cost
## soft modes
Opt3 = ASC_SM*one






V = {0: Opt1,1: Opt2,2: Opt3}



## Availablility
pm_avail =  DefineVariable('Car_avail', ((CarAvail != 3)+(NbMoto>=1))>0 )
CAR_AV =  DefineVariable('CAR_AV',(NbCar > 1)) # the data that is not available (-1) is also omitted
WALK_AV =  DefineVariable('TRAIN_AV',((distance_km  < 8)+ (NbBicy >0) * (distance_km < 15) >0 ))

av = {0: one,1: pm_avail,2: WALK_AV}  

exclude = (Choice==1) * (CAR_AV ==0) + (Choice==2) * (WALK_AV == 0)


#Exclude_AV
BIOGEME_OBJECT.EXCLUDE = (Choice   ==  -1) + ((Choice==1)*(pm_avail != 1)>0) + ((Choice==2)*(WALK_AV!= 1)>0) 


# MNL (Multinomial Logit model), with availability conditions
logprob = bioLogLogit(V,av,Choice)

# Defines an iterator on the data
rowIterator('obsIter')

# Define the likelihood function for the estimation
BIOGEME_OBJECT.ESTIMATE = Sum(logprob,'obsIter')

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
