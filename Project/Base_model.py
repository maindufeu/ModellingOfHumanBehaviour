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
# Define here arithmetic expressions for name that are not directly available from the data

one  = DefineVariable('one',1)
car_time  = DefineVariable('car_time', TimeCar  )
pt_time = DefineVariable('pt_time', TimePT)
distance_trip=DefineVariable('distance_trip',distance_km)

# Utilities
## public transport
Opt1 = ASC_PT*one+Time*pt_time
## private mode
Opt2 = ASC_PM*one+Time*car_time
## soft modes
Opt3 = ASC_SM*one+Distance*distance_trip

V = {0: Opt1,1: Opt2,2: Opt3}
av = {0: one,1: one,2: one}  #what is that???



#Exclude
BIOGEME_OBJECT.EXCLUDE = Choice   ==  -1


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
