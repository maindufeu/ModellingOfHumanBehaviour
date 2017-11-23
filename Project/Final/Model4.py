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
########### MODEL3 #####################
ASC_PT = Beta('ASC_PT',0,-10000,10000,0)
ASC_PM =  Beta('ASC_PM ',0,-10000,10000,0)
Beta_time_PT= Beta('Beta_time_PT',0,-10000,10000,0)
Beta_time_PT_wait=Beta('Beta_time_PT_wait',0,-10000,10000,0)
Beta_time_PT_walk=Beta('Beta_time_PT_walk',0,-10000,10000,0)
Beta_time_PM= Beta('Beta_time_PM',0,-10000,10000,0)
Beta_Distance= Beta('Beta_Distance',0,-10000,10000,0)
Beta_Cost_age1 = Beta('Beta_Cost_age1',0,-10000,10000,0)
Beta_Cost_age2 = Beta('Beta_Cost_age2',0,-10000,10000,0)
Beta_Cost_age3 = Beta('Beta_Cost_age3',0,-10000,10000,0)

Beta_Age1_PT=Beta('Beta_Age1_PT',0,-10000,10000,0)
Beta_Age2_PT=Beta('Beta_Age2_PT',0,-10000,10000,0)

Beta_Age1_PM=Beta('Beta_Age1_PM',0,-10000,10000,0)
Beta_Age2_PM=Beta('Beta_Age2_PM',0,-10000,10000,0)

Beta_roman = Beta('Beta_roman', 0, -10000, 10000, 0)

Beta_urb =Beta('Beta_urb', 0, -10000, 10000, 0)

################ MODEL 4 ####################
Beta_Income=Beta('Beta_Income',0,-10000,10000,0)

LAMBDA   = Beta('LAMBDA',1,-10000,10000,0)

Beta_tc=Beta('Beta_tc',0,-10000,10000,0)
Beta_have_ga            = Beta('Beta_have_ga', 0, -10000, 10000, 0)
Beta_multi_trips  =Beta('Beta_multi_trips', 0, -10000, 10000, 0)
Beta_region = Beta('Beta_region', 0, -10000, 10000, 0)

Beta_TripWork=Beta('Beta_TripWork',0, -10000, 10000, 0)
Beta_TripLeisure=Beta('Beta_TripLeisure',0, -10000, 10000, 0)

Beta_inc_car_0_4    = Beta('Beta_inc_car_0_4',0,-10000,10000,0)
Beta_inc_car_4_8        = Beta('Beta_inc_car_4_8',0,-10000,10000,0)
Beta_inc_car_8_12       = Beta('Beta_inc_car_8_12',0,-10000,10000,0)
Beta_inc_car_12_16      = Beta('Beta_inc_car_12_16',0,-10000,10000,0)

Beta_inc_pt_0_4 = Beta('Beta_inc_pt_0_4',0,-10000,10000,0)
Beta_inc_pt_4_8     = Beta('Beta_inc_pt_4_8',0,-10000,10000,0)
Beta_inc_pt_8_12        = Beta('Beta_inc_pt_8_12',0,-10000,10000,0)
Beta_inc_pt_12_16       = Beta('Beta_inc_pt_12_16',0,-10000,10000,0)

############## MODEL 3 ##############
# Define here arithmetic expressions for name that are not directly available from the data
pm_avail =  DefineVariable('pm_avail', ((CarAvail != 3)+(NbMoto>=1))>0 )
bike_walk_avail =  DefineVariable('bike_walk_avail', ((distance_km)<8 + (NbBicy>0)*(distance_km)<16)>0)

one  = DefineVariable('one',1)
#----time
car_time  = DefineVariable('car_time', TimeCar )
pt_ww_time = DefineVariable('pt_ww_time',  WaitingTimePT + WalkingTimePT)
pt_transp_time= DefineVariable('pt_transp_time',InVehicleTime*(InVehicleTime>0))

distance_trip=DefineVariable('distance_trip',distance_km)
reported_time=DefineVariable('reported_time',ReportedDuration)
#---cost
car_cost=DefineVariable('car_cost',CostCar)
PT_cost=DefineVariable('PT',MarginalCostPT)  #marginal tiens en compte le demi tarif etc
#socioeco
age1= DefineVariable('age1', age*(age<=25))
age2= DefineVariable('age2', age*(25<age<=65))
age3= DefineVariable('age3', age*(age>65))

urb= DefineVariable('urb',1*(UrbRur==1))

roman= DefineVariable('roman',1*(Region<4))

Tripwork=DefineVariable('Tripwork',1*(TripPurpose==1))
TripLeisure=DefineVariable('TripLeisure',1*(TripPurpose==3))

############ MODEL 4 ##############
ScaledIncome = DefineVariable('ScaledIncome', CalculatedIncome / 1000*(CalculatedIncome>0))

inc0_4 = DefineVariable('inc0_4',min(ScaledIncome,4))
inc4_8 = DefineVariable('inc4_8',max(0,min(ScaledIncome-4,4)))
inc8_12 = DefineVariable('inc8_12',max(0,min(ScaledIncome-8,4)))
inc12_16 = DefineVariable('inc12_16',max(0,min(ScaledIncome-12,4)))

# Utilities
## public transport
_Public_T = ASC_PT*one \
            + Beta_time_PT*(((pt_transp_time**LAMBDA)-1)/LAMBDA) \
            + Beta_time_PT_walk*(pt_ww_time)\
            + Beta_Cost_age1* PT_cost*age1\
            + Beta_Cost_age2* PT_cost*age2\
            + Beta_Cost_age3* PT_cost*age3\
            + Beta_Age1_PT*age1+Beta_Age2_PT*age2\
            + Beta_urb*urb\
            + Beta_TripWork*Tripwork+Beta_TripLeisure*TripLeisure
## private mods
_Private_M = ASC_PM*one \
            + Beta_time_PM*car_time \
            + Beta_Cost_age1* car_cost*age1\
            + Beta_Cost_age2* car_cost*age2\
            + Beta_Cost_age3* car_cost*age3\
            + Beta_Age1_PM*age1+Beta_Age2_PM*age2\
            + Beta_urb*urb\
            + Beta_roman*roman \

## soft modes
_soft_M =  \
         Beta_Distance*distance_trip\
        + Beta_inc_car_0_4*inc0_4 + Beta_inc_car_4_8*inc4_8 \
        + Beta_inc_car_8_12*inc8_12 + Beta_inc_car_12_16*inc12_16

V = {0: _Public_T,1: _Private_M ,2: _soft_M }
av = {0: one,1: pm_avail,2: bike_walk_avail}

#Exclude
BIOGEME_OBJECT.EXCLUDE = (Choice   ==  -1) + \
                         ((Choice == 1) * (pm_avail != 1) > 0)+ \
                          ((Choice == 2)* (bike_walk_avail!=1)>0)


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
BIOGEME_OBJECT.FORMULAS['Opt1'] = _Public_T
BIOGEME_OBJECT.FORMULAS['Opt2'] = _Private_M
BIOGEME_OBJECT.FORMULAS['Opt3'] = _soft_M
