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
ASC_PT = Beta('ASC_PT',-2.01174,-10000,10000,0,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.288961,-10000,10000,0,'Beta_time_PT' )

LAMBDA = Beta('LAMBDA',0.198343,-10000,10000,0,'LAMBDA' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0377992,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost_age1 = Beta('Beta_Cost_age1',-0.00749963,-10000,10000,0,'Beta_Cost_age1' )

Beta_Cost_age2 = Beta('Beta_Cost_age2',-0.00183024,-10000,10000,0,'Beta_Cost_age2' )

Beta_Cost_age3 = Beta('Beta_Cost_age3',-0.000575644,-10000,10000,0,'Beta_Cost_age3' )

Beta_Age1_PT = Beta('Beta_Age1_PT',2.24035,-10000,10000,0,'Beta_Age1_PT' )

Beta_Age2_PT = Beta('Beta_Age2_PT',-0.0123765,-10000,10000,0,'Beta_Age2_PT' )

Beta_urb = Beta('Beta_urb',1.10425,-10000,10000,0,'Beta_urb' )

Beta_TripWork = Beta('Beta_TripWork',0.212946,-10000,10000,0,'Beta_TripWork' )

Beta_TripLeisure = Beta('Beta_TripLeisure',-0.238564,-10000,10000,0,'Beta_TripLeisure' )

ASC_PM  = Beta('ASC_PM ',-1.07326,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0188009,-10000,10000,0,'Beta_time_PM' )

Beta_Age1_PM = Beta('Beta_Age1_PM',2.15719,-10000,10000,0,'Beta_Age1_PM' )

Beta_Age2_PM = Beta('Beta_Age2_PM',-0.00972481,-10000,10000,0,'Beta_Age2_PM' )

Beta_roman = Beta('Beta_roman',0.928179,-10000,10000,0,'Beta_roman' )

Beta_Distance = Beta('Beta_Distance',-0.745272,-10000,10000,0,'Beta_Distance' )

Beta_inc_car_0_4 = Beta('Beta_inc_car_0_4',-0.420743,-10000,10000,0,'Beta_inc_car_0_4' )

Beta_inc_car_4_8 = Beta('Beta_inc_car_4_8',0.787521,-10000,10000,0,'Beta_inc_car_4_8' )

Beta_inc_car_8_12 = Beta('Beta_inc_car_8_12',-1.00877,-10000,10000,0,'Beta_inc_car_8_12' )

Beta_inc_car_12_16 = Beta('Beta_inc_car_12_16',0.8249,-10000,10000,0,'Beta_inc_car_12_16' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_PT','Beta_Age1_PM','Beta_Age1_PT','Beta_Age2_PM','Beta_Age2_PT','Beta_Cost_age1','Beta_Cost_age2','Beta_Cost_age3','Beta_Distance','Beta_TripLeisure','Beta_TripWork','Beta_inc_car_0_4','Beta_inc_car_12_16','Beta_inc_car_4_8','Beta_inc_car_8_12','Beta_roman','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk','Beta_urb','LAMBDA']
values = [[1.26123,1.24446,0.609624,0.609819,-0.00298375,-0.00281481,-3.35934e-05,-8.32578e-08,-1.51621e-06,0.0056102,-0.0021328,-0.00270999,0.2829,0.00927439,-0.0187323,0.0027639,0.0022988,0.000158059,0.00234982,-2.19329e-05,-0.0531053,0.00173859],[1.24446,1.34984,0.61285,0.612449,-0.00296088,-0.00335964,1.53406e-05,-7.72632e-06,-3.12925e-05,0.00363269,-0.0497267,-0.040331,0.28428,0.0138089,-0.0223083,0.00040023,0.00861058,-0.000605912,-0.0107174,-0.000401958,-0.0495388,0.00165175],[0.609624,0.61285,0.727065,0.727084,-0.00328175,-0.00330634,-3.54525e-05,-1.45305e-06,-6.87624e-06,-0.0167143,-0.00234298,0.00147439,0.13032,0.0519367,0.00312308,-0.047776,0.000894454,1.81462e-05,-0.00179118,-2.03544e-06,0.0434536,0.00242471],[0.609819,0.612449,0.727084,0.727503,-0.00328426,-0.00330138,-6.60752e-05,-1.03898e-06,-6.47749e-06,-0.0167322,-0.00183169,0.00168099,0.130357,0.0519609,0.00316499,-0.0478065,0.00126217,1.23071e-05,-0.00185011,8.22826e-07,0.0435405,0.00236339],[-0.00298375,-0.00296088,-0.00328175,-0.00328426,7.81716e-05,7.57432e-05,1.44802e-07,-1.4111e-08,1.25647e-08,3.78332e-05,2.51022e-05,-6.54669e-07,0.000133147,-0.000864255,-0.000306321,0.000963355,-7.52631e-05,-1.53292e-06,4.2801e-05,2.22676e-07,-0.00014133,-7.14882e-05],[-0.00281481,-0.00335964,-0.00330634,-0.00330138,7.57432e-05,8.72856e-05,3.89321e-08,-4.68952e-07,3.90628e-07,4.15453e-05,0.000124095,-6.49338e-05,0.000126581,-0.000853293,-0.000279288,0.000944134,-8.46719e-05,-6.15913e-07,7.63322e-05,7.04072e-08,-0.000182402,-7.7185e-05],[-3.35934e-05,1.53406e-05,-3.54525e-05,-6.60752e-05,1.44802e-07,3.89321e-08,7.91224e-06,-1.12061e-07,-2.38749e-08,1.25246e-06,-3.46671e-05,-2.68665e-05,-8.55815e-06,3.47212e-07,3.01207e-07,-6.91452e-07,-6.02502e-06,3.63318e-07,5.55375e-06,-6.63626e-07,-3.68037e-06,4.1032e-06],[-8.32578e-08,-7.72632e-06,-1.45305e-06,-1.03898e-06,-1.4111e-08,-4.68952e-07,-1.12061e-07,1.30289e-07,1.11073e-08,1.40911e-06,3.30213e-06,7.06696e-06,-6.65423e-08,-9.97355e-10,-3.81245e-07,3.2923e-07,-3.12567e-06,5.50891e-07,3.68105e-07,1.52898e-07,-5.27986e-07,3.16841e-06],[-1.51621e-06,-3.12925e-05,-6.87624e-06,-6.47749e-06,1.25647e-08,3.90628e-07,-2.38749e-08,1.11073e-08,1.2898e-07,9.1548e-07,6.5133e-07,4.56711e-06,-2.1067e-07,4.33956e-08,6.55664e-07,-3.19449e-07,4.51516e-06,4.52375e-07,8.51076e-07,3.73145e-07,7.40799e-07,1.29076e-06],[0.0056102,0.00363269,-0.0167143,-0.0167322,3.78332e-05,4.15453e-05,1.25246e-06,1.40911e-06,9.1548e-07,0.00779728,0.000278264,6.59118e-05,-0.00286686,-0.0062032,-0.00259688,0.00780127,-9.52778e-05,5.51867e-05,0.000518819,2.21902e-06,-0.00923611,0.000230269],[-0.0021328,-0.0497267,-0.00234298,-0.00183169,2.51022e-05,0.000124095,-3.46671e-05,3.30213e-06,6.5133e-07,0.000278264,0.0491822,0.0358184,-7.20459e-05,-0.000386575,-0.000375738,0.000474757,0.000133034,2.17819e-05,0.000360577,0.000230397,-7.13965e-05,-0.00111211],[-0.00270999,-0.040331,0.00147439,0.00168099,-6.54669e-07,-6.49338e-05,-2.68665e-05,7.06696e-06,4.56711e-06,6.59118e-05,0.0358184,0.0464247,-0.00058324,0.00119553,-0.00016555,-0.00073067,-0.000677151,4.77203e-05,-0.000304416,0.000246283,0.000175592,-0.00115959],[0.2829,0.28428,0.13032,0.130357,0.000133147,0.000126581,-8.55815e-06,-6.65423e-08,-2.1067e-07,-0.00286686,-7.20459e-05,-0.00058324,0.0904234,-0.0271279,-0.0261043,0.0301735,0.00142714,-1.51542e-06,-0.000247982,5.80306e-06,8.87238e-05,0.000136622],[0.00927439,0.0138089,0.0519367,0.0519609,-0.000864255,-0.000853293,3.47212e-07,-9.97355e-10,4.33956e-08,-0.0062032,-0.000386575,0.00119553,-0.0271279,0.355155,0.0652678,-0.294344,0.00108123,-5.58397e-06,-0.00198301,4.17094e-06,0.018053,0.00154347],[-0.0187323,-0.0223083,0.00312308,0.00316499,-0.000306321,-0.000279288,3.01207e-07,-3.81245e-07,6.55664e-07,-0.00259688,-0.000375738,-0.00016555,-0.0261043,0.0652678,0.0375259,-0.0667081,0.00166073,1.44653e-05,0.000810918,-2.99131e-07,0.010228,-0.000281724],[0.0027639,0.00040023,-0.047776,-0.0478065,0.000963355,0.000944134,-6.91452e-07,3.2923e-07,-3.19449e-07,0.00780127,0.000474757,-0.00073067,0.0301735,-0.294344,-0.0667081,0.263498,-0.0010871,-7.09163e-06,0.0014293,-4.80272e-06,-0.0245952,-0.00139866],[0.0022988,0.00861058,0.000894454,0.00126217,-7.52631e-05,-8.46719e-05,-6.02502e-06,-3.12567e-06,4.51516e-06,-9.52778e-05,0.000133034,-0.000677151,0.00142714,0.00108123,0.00166073,-0.0010871,0.0260246,-5.42139e-05,-0.000384893,-3.91237e-06,0.00664921,-0.000123484],[0.000158059,-0.000605912,1.81462e-05,1.23071e-05,-1.53292e-06,-6.15913e-07,3.63318e-07,5.50891e-07,4.52375e-07,5.51867e-05,2.17819e-05,4.77203e-05,-1.51542e-06,-5.58397e-06,1.44653e-05,-7.09163e-06,-5.42139e-05,2.78331e-05,0.00013219,5.53036e-06,-2.53726e-05,0.000193577],[0.00234982,-0.0107174,-0.00179118,-0.00185011,4.2801e-05,7.63322e-05,5.55375e-06,3.68105e-07,8.51076e-07,0.000518819,0.000360577,-0.000304416,-0.000247982,-0.00198301,0.000810918,0.0014293,-0.000384893,0.00013219,0.00445997,-5.75273e-05,-0.000436084,-0.00136309],[-2.19329e-05,-0.000401958,-2.03544e-06,8.22826e-07,2.22676e-07,7.04072e-08,-6.63626e-07,1.52898e-07,3.73145e-07,2.21902e-06,0.000230397,0.000246283,5.80306e-06,4.17094e-06,-2.99131e-07,-4.80272e-06,-3.91237e-06,5.53036e-06,-5.75273e-05,1.54169e-05,8.91476e-06,-3.11228e-06],[-0.0531053,-0.0495388,0.0434536,0.0435405,-0.00014133,-0.000182402,-3.68037e-06,-5.27986e-07,7.40799e-07,-0.00923611,-7.13965e-05,0.000175592,8.87238e-05,0.018053,0.010228,-0.0245952,0.00664921,-2.53726e-05,-0.000436084,8.91476e-06,0.108113,2.60983e-05],[0.00173859,0.00165175,0.00242471,0.00236339,-7.14882e-05,-7.7185e-05,4.1032e-06,3.16841e-06,1.29076e-06,0.000230269,-0.00111211,-0.00115959,0.000136622,0.00154347,-0.000281724,-0.00139866,-0.000123484,0.000193577,-0.00136309,-3.11228e-06,2.60983e-05,0.0044151]]
vc = bioMatrix(22,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
############## MODEL 3 ##############
# Define here arithmetic expressions for name that are not directly available from the data
pm_avail =  DefineVariable('pm_avail', ((CarAvail != 3)+(NbMoto>=1))>0 )
bike_walk_avail =  DefineVariable('bike_walk_avail', ((distance_km)<8 + (NbBicy>0)*(distance_km)<16)>0)

one  = DefineVariable('one',1)
#----time
car_time  = DefineVariable('car_time', TimeCar )
pt_transp_time= DefineVariable('pt_transp_time',InVehicleTime*(InVehicleTime>0))
pt_ww_time = DefineVariable('pt_ww_time',  WaitingTimePT + WalkingTimePT)

distance_trip=DefineVariable('distance_trip',distance_km)
reported_time=DefineVariable('reported_time',ReportedDuration)
#---cost
car_cost=DefineVariable('car_cost',CostCar)
PT_cost=DefineVariable('PT_cost',MarginalCostPT)  #marginal tiens en compte le demi tarif etc
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
            + Beta_time_PT*((((pt_transp_time)**LAMBDA)-1)/LAMBDA) \
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
        + Beta_inc_car_0_4*inc0_4 + Beta_inc_car_4_8*inc4_8 + Beta_inc_car_8_12*inc8_12 + Beta_inc_car_12_16*inc12_16

V = {0: _Public_T,1: _Private_M ,2: _soft_M }
av = {0: one,1: pm_avail,2: bike_walk_avail}

#Exclude
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
norm_el_PM = 5.21668
BIOGEME_OBJECT.STATISTICS['Normalization for Elasticities PT'] = Sum(AdjWeight*probPT,'obsIter')
norm_el_PT = 1684.57
elas_PM_time = Derive(probPM,'car_time')*(car_time/probPM)
elas_PT_time = Derive(probPT,'pt_transp_time')*(TimePT/probPT) #ZERO
elas_PM_cost = Derive(probPM,'car_cost')*(car_cost/probPM)
elas_PT_cost = Derive(probPT,'PT_cost')*(PT_cost/probPT) #ZERO
Agg_elasT_PM = elas_PM_time*probPM/norm_el_PM
Agg_elasT_PT = elas_PT_time*probPT/norm_el_PT
Agg_elasC_PM = elas_PM_cost*probPM/norm_el_PM
Agg_elasC_PT = elas_PT_cost*probPT/norm_el_PT

probChosen = bioLogit(V,av,Choice) #Instead of reporting the choice in the simulation file, the probability of the chosen can be printed
VOT_CAR = Derive(_Private_M,'car_time')/Derive(_Private_M,'car_cost')
VOT_PT = Derive(_Public_T,'pt_transp_time')/Derive(_Public_T,'PT_cost')
VOT_walk=Derive(_Public_T,'pt_ww_time')/Derive(_Public_T,'PT_cost')
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
            'VOT_PTwalking':VOT_walk,
            'Revenue_PT':Revenue_PT
            }

BIOGEME_OBJECT.SIMULATE = Enumerate(simulate,'obsIter')
