# Meritxell Pacheco
# 19.10.2017

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *
  
# Choice
chosenAlternative = ( (  BestAlternative_1   *  1  ) + (  BestAlternative_2   *  2  ) ) + (  BestAlternative_3   *  3  )

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
Fare	 = Beta('Fare',0,-10000,10000,0)
Legroom	 = Beta('Legroom',0,-10000,10000,0)
SchedDE	 = Beta('SchedDE',0,-10000,10000,0)
SchedDL	 = Beta('SchedDL',0,-10000,10000,0)
Total_TT1	 = Beta('Total_TT1',0,-10000,10000,0)
Total_TT2	 = Beta('Total_TT2',0,-10000,10000,0)
Total_TT3	 = Beta('Total_TT3',0,-10000,10000,0)

# Define here arithmetic expressions for name that are not directly available from the data

one  = DefineVariable('one',1)
DepartureTimeSensitive  = DefineVariable('DepartureTimeSensitive', q11_DepartureOrArrivalIsImportant   ==  1 )
ArrivalTimeSensitive  = DefineVariable('ArrivalTimeSensitive', q11_DepartureOrArrivalIsImportant   ==  2 )
Missing  = DefineVariable('Missing',(  q11_DepartureOrArrivalIsImportant   !=  1  ) * (  q11_DepartureOrArrivalIsImportant   !=  2  ))
DesiredDepartureTime  = DefineVariable('DesiredDepartureTime',q12_IdealDepTime )
DesiredArrivalTime  = DefineVariable('DesiredArrivalTime',q13_IdealArrTime )
ScheduledDelay_1  = DefineVariable('ScheduledDelay_1',(  DepartureTimeSensitive   * (  DepartureTimeMins_1   -  DesiredDepartureTime   ) ) + (  ArrivalTimeSensitive   * (  ArrivalTimeMins_1   -  DesiredArrivalTime   ) ))
ScheduledDelay_2  = DefineVariable('ScheduledDelay_2',(  DepartureTimeSensitive   * (  DepartureTimeMins_2   -  DesiredDepartureTime   ) ) + (  ArrivalTimeSensitive   * (  ArrivalTimeMins_2   -  DesiredArrivalTime   ) ))
ScheduledDelay_3  = DefineVariable('ScheduledDelay_3',(  DepartureTimeSensitive   * (  DepartureTimeMins_3   -  DesiredDepartureTime   ) ) + (  ArrivalTimeSensitive   * (  ArrivalTimeMins_3   -  DesiredArrivalTime   ) ))
Opt1_SchedDelayEarly  = DefineVariable('Opt1_SchedDelayEarly',(  -(ScheduledDelay_1 )  * (  ScheduledDelay_1   <  0  ) ) /  60 )
Opt2_SchedDelayEarly  = DefineVariable('Opt2_SchedDelayEarly',(  -(ScheduledDelay_2 )  * (  ScheduledDelay_2   <  0  ) ) /  60 )
Opt3_SchedDelayEarly  = DefineVariable('Opt3_SchedDelayEarly',(  -(ScheduledDelay_3 )  * (  ScheduledDelay_3   <  0  ) ) /  60 )
Opt1_SchedDelayLate  = DefineVariable('Opt1_SchedDelayLate',(  ScheduledDelay_1   * (  ScheduledDelay_1   >  0  ) ) /  60 )
Opt2_SchedDelayLate  = DefineVariable('Opt2_SchedDelayLate',(  ScheduledDelay_2   * (  ScheduledDelay_2   >  0  ) ) /  60 )
Opt3_SchedDelayLate  = DefineVariable('Opt3_SchedDelayLate',(  ScheduledDelay_3   * (  ScheduledDelay_3   >  0  ) ) /  60 )

# Utilities
Opt1 = Constant1 * one + Fare * Fare_1 + Legroom * Legroom_1 + SchedDE * Opt1_SchedDelayEarly + SchedDL * Opt1_SchedDelayLate + Total_TT1 * TripTimeHours_1
Opt2 = Constant2 * one + Fare * Fare_2 + Legroom * Legroom_2 + SchedDE * Opt2_SchedDelayEarly + SchedDL * Opt2_SchedDelayLate + Total_TT2 * TripTimeHours_2
Opt3 = Constant3 * one + Fare * Fare_3 + Legroom * Legroom_3 + SchedDE * Opt3_SchedDelayEarly + SchedDL * Opt3_SchedDelayLate + Total_TT3 * TripTimeHours_3
V = {1: Opt1,2: Opt2,3: Opt3}
av = {1: one,2: one,3: one}

#Exclude the male and female observations
BIOGEME_OBJECT.EXCLUDE = ( (  q17_Gender   ==  2  )  + (  q17_Gender   ==  1  )) > 0

# MNL (Multinomial Logit model), with availability conditions
logprob = bioLogLogit(V,av,chosenAlternative)

# Defines an iterator on the data
rowIterator('obsIter')

# Define the likelihood function for the estimation
BIOGEME_OBJECT.ESTIMATE = Sum(logprob,'obsIter')

# Optimization algorithm
BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "BIO"
BIOGEME_OBJECT.PARAMETERS['stopFileName'] = "STOP"

# Print some statistics:
nullLoglikelihood(av,'obsIter')
choiceSet = [1,2,3]
cteLoglikelihood(choiceSet,chosenAlternative,'obsIter')
availabilityStatistics(av,'obsIter')
BIOGEME_OBJECT.FORMULAS['Opt1'] = Opt1
BIOGEME_OBJECT.FORMULAS['Opt2'] = Opt2
BIOGEME_OBJECT.FORMULAS['Opt3'] = Opt3