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

#ASC for SocioEc
ASC_PM_1 =  Beta('ASC_PM_1',0,-10000,10000,0)
ASC_SM_1 = Beta('ASC_SM_1',0,-10000,10000,0)
ASC_PM_2 =  Beta('ASC_PM_2',0,-10000,10000,0)
ASC_SM_2 = Beta('ASC_SM_2',0,-10000,10000,0)
ASC_PM_3=  Beta('ASC_PM_3',0,-10000,10000,0)
ASC_SM_3 = Beta('ASC_SM_3',0,-10000,10000,0)
ASC_PM_4 =  Beta('ASC_PM_4',0,-10000,10000,0)
ASC_SM_4 = Beta('ASC_SM_4',0,-10000,10000,0)
ASC_PM_5 =  Beta('ASC_PM_5',0,-10000,10000,0)
ASC_SM_5 = Beta('ASC_SM_5',0,-10000,10000,0)
ASC_PM_6 =  Beta('ASC_PM_6',0,-10000,10000,0)
ASC_SM_6 = Beta('ASC_SM_6',0,-10000,10000,0)


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
#---SocioEc
Edu1=DefineVariable('Edu1',Education*Education==1)

#---segmentation
Edu_delta1=DefineVariable('Edu1',1*Education==1)
Edu_delta2=DefineVariable('Edu2',1*Education==2)
Edu_delta3=DefineVariable('Edu3',1*Education==3)
Edu_delta4=DefineVariable('Edu4',1*Education==4)
Edu_delta5=DefineVariable('Edu5',1*Education==5)
Edu_delta6=DefineVariable('Edu6',1*Education==5)



# Utilities
## public transport
Opt1 =  ASC_PT +Time*pt_time +Cost* PT_cost
## private mode
Opt2 = (Edu_delta1*ASC_PM_1+Edu_delta2*ASC_PM_2+Edu_delta3*ASC_PM_3+Edu_delta4*ASC_PM_4+Edu_delta5*ASC_PM_5+Edu_delta6*ASC_PM_6)*one\
            +Time*car_time+Cost*car_cost
## soft modes
Opt3 = (Edu_delta1*ASC_SM_1+Edu_delta2*ASC_SM_2+Edu_delta3*ASC_SM_3+Edu_delta4*ASC_SM_4+Edu_delta5*ASC_SM_5+Edu_delta6*ASC_SM_6)*one

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
