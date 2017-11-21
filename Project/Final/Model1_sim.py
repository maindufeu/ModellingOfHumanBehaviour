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
ASC_PT = Beta('ASC_PT',0.938926,-10000,10000,0,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',-0.0103235,-10000,10000,0,'Beta_time_PT' )

Beta_Cost = Beta('Beta_Cost',0.0289582,-10000,10000,0,'Beta_Cost' )

ASC_PM  = Beta('ASC_PM ',1.83128,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0127623,-10000,10000,0,'Beta_time_PM' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_PT','Beta_Cost','Beta_time_PM','Beta_time_PT']
values = [[0.0261478,0.0241045,-0.00033201,-0.000233959,-3.25986e-05],[0.0241045,0.031228,-0.000104451,-0.00023129,-0.000120011],[-0.00033201,-0.000104451,5.2981e-05,5.09419e-06,-7.75925e-06],[-0.000233959,-0.00023129,5.09419e-06,5.83193e-06,1.36315e-06],[-3.25986e-05,-0.000120011,-7.75925e-06,1.36315e-06,2.41238e-06]]
vc = bioMatrix(5,names,values)
BIOGEME_OBJECT.VARCOVAR = vc

pm_avail =  DefineVariable('pm_avail', ((CarAvail != 3)+(NbMoto>=1))>0 )
bike_walk_avail =  DefineVariable('bike_walk_avail', ((distance_km)<8 + (NbBicy>0)*(distance_km)<16)>0)
one  = DefineVariable('one',1)
car_time  = DefineVariable('car_time', TimeCar )
pt_total_time = DefineVariable('pt_total_time', TimePT)
pt_TOT_time = DefineVariable('pt_TOT_time', TimePT + WaitingTimePT + WalkingTimePT)
pt_wait_time = DefineVariable('pt_wait_time', WaitingTimePT)
pt_walk_time = DefineVariable('pt_walk_time',WalkingTimePT)
car_cost=DefineVariable('car_cost',CostCar)
PT_cost=DefineVariable('PT_cost',MarginalCostPT)  #marginal tiens en compte le demi tarif etc

# Utilities
## public transport
_Public_T = ASC_PT*one+ Beta_time_PT*pt_TOT_time + Beta_Cost* PT_cost
## private mode
_Private_M = ASC_PM*one+ Beta_time_PM*car_time+ Beta_Cost*car_cost
## soft modes
_soft_M = 0*one

V = {0: _Public_T,1: _Private_M ,2: _soft_M }
av = {0: one,1: pm_avail,2: bike_walk_avail}



BIOGEME_OBJECT.STATISTICS['SampleSize0'] = Sum(one, 'obsIter')
#Exclude (No need to exclude anything here)
BIOGEME_OBJECT.EXCLUDE = (Choice   ==  -1) + \
                         ((Choice == 1) * (pm_avail != 1) > 0)+ \
                          ((Choice == 2)* (bike_walk_avail!=1)>0)\



BIOGEME_OBJECT.STATISTICS['SampleSize'] = Sum(one, 'obsIter')
x = Sum(one, 'obsIter')
BIOGEME_OBJECT.STATISTICS['UnAdjustedWeightSum']= Sum(Weight, 'obsIter')/x
y = Sum(Weight, 'obsIter')
BIOGEME_OBJECT.WEIGHT =  Weight*(x/y)
AdjWeight = Weight*(x/y)
BIOGEME_OBJECT.STATISTICS['AdjustedWeightSum'] = Sum(AdjWeight, 'obsIter')/x
AdjSum = Sum(AdjWeight, 'obsIter')





#No need for estimating the model (it is already estimated). We want to obtain the individual probabilities and the market shares
probPT = bioLogit(V,av,0)
probPM = bioLogit(V,av,1)
probSM = bioLogit(V,av,2)
#Elasticity

BIOGEME_OBJECT.STATISTICS['Normalization for Elasticities PM'] = Sum(AdjWeight*probPM,'obsIter')
norm_el_PM = 1099.6
BIOGEME_OBJECT.STATISTICS['Normalization for Elasticities PT'] = Sum(AdjWeight*probPT,'obsIter')
norm_el_PT = 515.667
elas_PM_time = Derive(probPM,'car_time')*(car_time/probPM)
elas_PT_time = Derive(probPT,'pt_TOT_time')*(pt_TOT_time/probPT) #ZERO
elas_PM_cost = Derive(probPM,'car_cost')*(car_cost/probPM)
elas_PT_cost = Derive(probPT,'PT_cost')*(PT_cost/probPT) #ZERO
Agg_elasT_PM = elas_PM_time*probPM/norm_el_PM
Agg_elasT_PT = elas_PT_time*probPT/norm_el_PT
Agg_elasC_PM = elas_PM_cost*probPM/norm_el_PM
Agg_elasC_PT = elas_PT_cost*probPT/norm_el_PT

probChosen = bioLogit(V,av,Choice) #Instead of reporting the choice in the simulation file, the probability of the chosen can be printed
VOT_CAR = Derive(probPM,'car_time')/Derive(probPM,'car_cost')
VOT_PT = Derive(probPT,'pt_TOT_time')/Derive(probPT,'PT_cost')
Revenue_PT = probPT * PT_cost
# Defines an itertor on the data
rowIterator('obsIter')

#Simulation output
simulate = {'probPT': probPT,
            'probPM': probPM,
            'probSM': probSM,
            'Agg_elasT_PT': Agg_elasT_PT,
            'Agg_elasT_PM': Agg_elasT_PM,
            'Agg_elasC_PT': Agg_elasC_PT,
            'Agg_elasC_PM': Agg_elasC_PM,
            'VOT_PT': VOT_PT,
            'VOT_CAR':VOT_CAR,
            'Revenue_PT':Revenue_PT
            }

BIOGEME_OBJECT.SIMULATE = Enumerate(simulate,'obsIter')
