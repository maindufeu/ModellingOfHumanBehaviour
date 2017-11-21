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
ASC_PT = Beta('ASC_PT',-1.22145,-10000,10000,0,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.00067006,-10000,10000,0,'Beta_time_PT' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0338389,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.000624367,-10000,10000,0,'Beta_Cost' )

ASC_PM  = Beta('ASC_PM ',-0.813034,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0232024,-10000,10000,0,'Beta_time_PM' )

Beta_Distance = Beta('Beta_Distance',-0.659961,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_PT','Beta_Cost','Beta_Distance','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk']
values = [[0.0543553,0.0484016,-2.29661e-05,0.0133699,-2.44941e-05,2.06965e-05,5.19416e-05],[0.0484016,0.0550621,-3.36663e-05,0.0128504,1.70816e-05,4.29299e-05,-0.000149803],[-2.29661e-05,-3.36663e-05,3.57237e-05,5.42293e-05,1.72718e-05,9.88007e-07,2.1564e-06],[0.0133699,0.0128504,5.42293e-05,0.00572524,8.02435e-05,3.52136e-05,1.78722e-05],[-2.44941e-05,1.70816e-05,1.72718e-05,8.02435e-05,3.81334e-05,1.83931e-05,3.91514e-06],[2.06965e-05,4.29299e-05,9.88007e-07,3.52136e-05,1.83931e-05,1.49362e-05,-2.88878e-06],[5.19416e-05,-0.000149803,2.1564e-06,1.78722e-05,3.91514e-06,-2.88878e-06,1.08087e-05]]
vc = bioMatrix(7,names,values)
BIOGEME_OBJECT.VARCOVAR = vc



# Define here arithmetic expressions for name that are not directly available from the data
pm_avail =  DefineVariable('pm_avail', ((CarAvail != 3)+(NbMoto>=1))>0 )
bike_walk_avail =  DefineVariable('bike_walk_avail', ((distance_km)<8 + (NbBicy>0)*(distance_km)<16)>0)

one  = DefineVariable('one',1)
#----time
car_time  = DefineVariable('car_time', TimeCar )
pt_total_time = DefineVariable('pt_total_time', TimePT)
pt_wait_time = DefineVariable('pt_wait_time', WaitingTimePT)
pt_walk_time = DefineVariable('pt_walk_time',WalkingTimePT)
pt_transp_time= DefineVariable('pt_transp_time',InVehicleTime)

distance_trip=DefineVariable('distance_trip',distance_km)
reported_time=DefineVariable('reported_time',ReportedDuration)
#---cost
car_cost=DefineVariable('car_cost',CostCar)
PT_cost=DefineVariable('PT_cost',CostPT)
pt_TOT_time = DefineVariable('pt_TOT_time', TimePT + WaitingTimePT + WalkingTimePT)

# Utilities
## public transport 
_Public_T = ASC_PT*one + Beta_time_PT*(pt_TOT_time - pt_walk_time - pt_wait_time) +Beta_time_PT_walk*(pt_TOT_time - pt_transp_time)+ Beta_Cost* PT_cost
## private mode
_Private_M = ASC_PM*one + Beta_time_PM*car_time + Beta_Cost* car_cost
## soft modes
_soft_M = Beta_Distance*distance_trip

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
