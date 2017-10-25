# Translated to .py by Meritxell Pacheco
# 2017

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *
  
# Choice
chosenAlternative = Choise

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


Costcar = DefineVariable('Costcar', Costcar)
CostPT  = DefineVariable('CostPT', CostPT)
TTCar = DefineVariable('TTCar', TimeCar)
TTPt  = DefineVariable('TTPt', TimePT + WalkingTimePT + WaintingTimePT)
Carav = DefineVariable('Carav' , ((NbCar >= 1) + (NbMoto >= 1) >=1) )


# Utilities

Car = Constant1 + BetaTT * TTCar + BetaCost* Costcar
Public = Constant2 + BetaTT * TTPt + BetaCost* CostPt
Bike = 0

V = {1: Car, 2: Public,3: Bike}

av = {1: Carav, 2: One ,3: One}

#Exclude
BIOGEME_OBJECT.EXCLUDE =  Choise   ==  -1

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
BIOGEME_OBJECT.FORMULAS['Opt1'] = Opt1
BIOGEME_OBJECT.FORMULAS['Opt2'] = Opt2
BIOGEME_OBJECT.FORMULAS['Opt3'] = Opt3
