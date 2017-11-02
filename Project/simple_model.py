# Translated to .py by Meritxell Pacheco
# 2017

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *

# Choice
chosenAlternative = Choice

#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed


Constant1	 = Beta('Constant1',0,-10000,10000,1)
Constant2	 = Beta('Constant2',0,-10000,10000,0)
Constant3	 = Beta('Constant3',0,-10000,10000,0)
BetaTT	 = Beta('BetaTT',0,-10000,10000,0)
BetaCost             = Beta('BetaCost',0,-10000,10000,0)

# Define here arithmetic expressions for name that are not directly available from the data


TTCar = DefineVariable('TTCar', TimeCar)
TTPt  = DefineVariable('TTPt', TimePT + WalkingTimePT + WaitingTimePT)
Carav = DefineVariable('Carav' , (((NbCar >= 1) + (NbMoto >= 1) )>=1) )
one   = DefineVariable('one',1)

# Utilities

Car = Constant1*one + BetaTT * TTCar + BetaCost* CostCar
Public = Constant2*one + BetaTT * TTPt + BetaCost* CostPT
Bike = 0*one

V = {0: Car, 1: Public,2: Bike}

av = {0: one, 1: one ,2: one}

#Exclude
BIOGEME_OBJECT.EXCLUDE =  Choice   ==  -1

# MNL (Multinomial Logit model), with availability conditions
logprob = bioLogLogit(V,av,chosenAlternative)

# Defines an iterator on the data
rowIterator('obsIter')


# Define the likelihood function for the estimation
BIOGEME_OBJECT.ESTIMATE = Sum(logprob,'obsIter')

# Optimization algorithm
BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "BIO"

# Print some statistics:

nullLoglikelihood(av,'obsIter')
choiceSet = [1,2,3]
cteLoglikelihood(choiceSet,chosenAlternative,'obsIter')
availabilityStatistics(av,'obsIter')
BIOGEME_OBJECT.FORMULAS['Car'] = Car
BIOGEME_OBJECT.FORMULAS['Public'] = Public
BIOGEME_OBJECT.FORMULAS['Bike'] = Bike
