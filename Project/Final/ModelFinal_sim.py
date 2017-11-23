# Tom Suter
# 19.10.2017

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *


ASC_PT = Beta('ASC_PT',-1.17018,-10000,10000,0,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.273818,-10000,10000,0,'Beta_time_PT' )

LAMBDA = Beta('LAMBDA',0.202045,-10000,10000,0,'LAMBDA' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0398866,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost_age1 = Beta('Beta_Cost_age1',-0.00766337,-10000,10000,0,'Beta_Cost_age1' )

Beta_Cost_age2 = Beta('Beta_Cost_age2',-0.00125481,-10000,10000,0,'Beta_Cost_age2' )

Beta_Cost_age3 = Beta('Beta_Cost_age3',-0.000373663,-10000,10000,0,'Beta_Cost_age3' )

Beta_Age1_PT = Beta('Beta_Age1_PT',2.00729,-10000,10000,0,'Beta_Age1_PT' )

Beta_Age2_PT = Beta('Beta_Age2_PT',-0.0165051,-10000,10000,0,'Beta_Age2_PT' )

Beta_urb = Beta('Beta_urb',-0.215937,-10000,10000,0,'Beta_urb' )

Beta_TripWork = Beta('Beta_TripWork',0.373504,-10000,10000,0,'Beta_TripWork' )

Beta_TripLeisure = Beta('Beta_TripLeisure',-0.140781,-10000,10000,0,'Beta_TripLeisure' )

Beta_have_ga = Beta('Beta_have_ga',1.62284,-10000,10000,0,'Beta_have_ga' )

ASC_PM  = Beta('ASC_PM ',-0.254718,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.015757,-10000,10000,0,'Beta_time_PM' )

Beta_Age1_PM = Beta('Beta_Age1_PM',1.93134,-10000,10000,0,'Beta_Age1_PM' )

Beta_Age2_PM = Beta('Beta_Age2_PM',-0.0110577,-10000,10000,0,'Beta_Age2_PM' )

Beta_multi_trips = Beta('Beta_multi_trips',-0.419119,-10000,10000,0,'Beta_multi_trips' )

Beta_roman = Beta('Beta_roman',0.86798,-10000,10000,0,'Beta_roman' )

Beta_Distance = Beta('Beta_Distance',-0.627691,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_PT','Beta_Age1_PM','Beta_Age1_PT','Beta_Age2_PM','Beta_Age2_PT','Beta_Cost_age1','Beta_Cost_age2','Beta_Cost_age3','Beta_Distance','Beta_TripLeisure','Beta_TripWork','Beta_have_ga','Beta_multi_trips','Beta_roman','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk','Beta_urb','LAMBDA']
values = [[0.181593,0.166972,0.133036,0.132984,-0.00295033,-0.00284488,-7.23786e-06,5.82458e-07,-1.01388e-06,0.0141898,0.00118828,0.0017243,0.00148485,-0.00613927,-0.00685765,9.86536e-05,0.00156119,-6.99432e-05,0.0030369,0.000978452],[0.166972,0.28684,0.138123,0.137538,-0.00289989,-0.00334917,7.1033e-05,-9.18922e-06,-2.46908e-05,0.0120817,-0.0541262,-0.0452609,-0.0069768,0.0156938,0.00299715,-0.000587986,-0.0127361,-0.000276541,-0.00684709,0.00288711],[0.133036,0.138123,0.436372,0.436231,-0.00284552,-0.00290209,-2.97925e-05,-8.81839e-07,-5.11278e-06,-0.00379683,-0.0002208,0.00475601,-0.00160324,-0.0049467,-0.00473975,-1.14349e-05,-0.00222517,-1.34192e-05,0.000422645,0.00175893],[0.132984,0.137538,0.436231,0.436487,-0.00284717,-0.00289578,-5.97284e-05,-5.15108e-07,-4.82664e-06,-0.00381389,0.000333464,0.00498724,-0.00157058,-0.00473402,-0.004415,-1.64973e-05,-0.00230243,-8.60769e-06,0.00035292,0.00169519],[-0.00295033,-0.00289989,-0.00284552,-0.00284717,7.01378e-05,6.74967e-05,1.35093e-07,-1.04567e-08,-5.53944e-09,-3.64437e-05,-7.10335e-06,-9.99366e-06,-9.29091e-06,4.57804e-05,-7.77269e-06,-1.00994e-06,3.3823e-05,3.52015e-07,-2.62244e-05,-4.87569e-05],[-0.00284488,-0.00334917,-0.00290209,-0.00289578,6.74967e-05,7.8787e-05,-3.20136e-07,-3.5573e-07,2.69238e-07,-3.37203e-05,0.000103643,-7.72477e-05,-0.000134518,6.08535e-05,-1.36746e-05,-1.1258e-07,6.57803e-05,-7.67408e-08,-1.8955e-05,-5.2182e-05],[-7.23786e-06,7.1033e-05,-2.97925e-05,-5.97284e-05,1.35093e-07,-3.20136e-07,1.01395e-05,-8.3239e-08,-1.42859e-08,8.87507e-07,-7.1987e-05,-8.25278e-05,8.23196e-06,4.02371e-05,9.98472e-06,1.58252e-07,3.17545e-06,-2.31283e-07,2.33969e-05,5.9731e-06],[5.82458e-07,-9.18922e-06,-8.81839e-07,-5.15108e-07,-1.04567e-08,-3.5573e-07,-8.3239e-08,9.80437e-08,1.45726e-08,9.15097e-07,5.54622e-06,9.26054e-06,3.76005e-05,-8.52941e-06,-1.46497e-06,4.32076e-07,1.57508e-07,1.00194e-07,3.98699e-07,1.66761e-06],[-1.01388e-06,-2.46908e-05,-5.11278e-06,-4.82664e-06,-5.53944e-09,2.69238e-07,-1.42859e-08,1.45726e-08,9.7043e-08,8.24226e-07,-7.50392e-07,2.94212e-06,1.75985e-05,2.0699e-06,4.18408e-06,4.28586e-07,8.74712e-07,3.22515e-07,2.98911e-08,1.08403e-06],[0.0141898,0.0120817,-0.00379683,-0.00381389,-3.64437e-05,-3.37203e-05,8.87507e-07,9.15097e-07,8.24226e-07,0.00542708,0.000347076,0.000203884,0.000697468,-0.000332109,-0.000241417,4.33319e-05,0.000540054,-9.88865e-08,0.00024893,6.22562e-05],[0.00118828,-0.0541262,-0.0002208,0.000333464,-7.10335e-06,0.000103643,-7.1987e-05,5.54622e-06,-7.50392e-07,0.000347076,0.057143,0.0446885,-0.00503051,-0.0147284,0.000479323,7.47068e-05,0.000918324,0.000187909,-0.0018074,-0.00117568],[0.0017243,-0.0452609,0.00475601,0.00498724,-9.99366e-06,-7.72477e-05,-8.25278e-05,9.26054e-06,2.94212e-06,0.000203884,0.0446885,0.0582093,-0.00288271,-0.0213297,-4.48724e-05,0.000125538,0.000471398,0.000179932,-0.00318664,-0.00111356],[0.00148485,-0.0069768,-0.00160324,-0.00157058,-9.29091e-06,-0.000134518,8.23196e-06,3.76005e-05,1.75985e-05,0.000697468,-0.00503051,-0.00288271,0.0725458,-0.00555466,0.000656033,0.000392103,0.00270387,-0.00013551,0.00145429,0.00205093],[-0.00613927,0.0156938,-0.0049467,-0.00473402,4.57804e-05,6.08535e-05,4.02371e-05,-8.52941e-06,2.0699e-06,-0.000332109,-0.0147284,-0.0213297,-0.00555466,0.0585538,0.00320551,-0.000265996,-0.00292911,0.000356434,-0.00384334,-0.000796663],[-0.00685765,0.00299715,-0.00473975,-0.004415,-7.77269e-06,-1.36746e-05,9.98472e-06,-1.46497e-06,4.18408e-06,-0.000241417,0.000479323,-4.48724e-05,0.000656033,0.00320551,0.0267248,-3.27227e-05,-0.000932861,5.45568e-05,-0.00611923,0.00023186],[9.86536e-05,-0.000587986,-1.14349e-05,-1.64973e-05,-1.00994e-06,-1.1258e-07,1.58252e-07,4.32076e-07,4.28586e-07,4.33319e-05,7.47068e-05,0.000125538,0.000392103,-0.000265996,-3.27227e-05,2.26428e-05,0.000111546,3.10915e-06,6.71978e-06,0.00015264],[0.00156119,-0.0127361,-0.00222517,-0.00230243,3.3823e-05,6.57803e-05,3.17545e-06,1.57508e-07,8.74712e-07,0.000540054,0.000918324,0.000471398,0.00270387,-0.00292911,-0.000932861,0.000111546,0.00467795,-8.72615e-05,0.0010244,-0.00182835],[-6.99432e-05,-0.000276541,-1.34192e-05,-8.60769e-06,3.52015e-07,-7.67408e-08,-2.31283e-07,1.00194e-07,3.22515e-07,-9.88865e-08,0.000187909,0.000179932,-0.00013551,0.000356434,5.45568e-05,3.10915e-06,-8.72615e-05,1.88875e-05,-0.000128751,-1.34332e-05],[0.0030369,-0.00684709,0.000422645,0.00035292,-2.62244e-05,-1.8955e-05,2.33969e-05,3.98699e-07,2.98911e-08,0.00024893,-0.0018074,-0.00318664,0.00145429,-0.00384334,-0.00611923,6.71978e-06,0.0010244,-0.000128751,0.0211898,-0.000171908],[0.000978452,0.00288711,0.00175893,0.00169519,-4.87569e-05,-5.2182e-05,5.9731e-06,1.66761e-06,1.08403e-06,6.22562e-05,-0.00117568,-0.00111356,0.00205093,-0.000796663,0.00023186,0.00015264,-0.00182835,-1.34332e-05,-0.000171908,0.00449258]]
vc = bioMatrix(20,names,values)
BIOGEME_OBJECT.VARCOVAR = vc

# Define here arithmetic expressions for name that are not directly available from the data
#--- availability
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
PT_cost=DefineVariable('PT_cost',MarginalCostPT)  #marginal tiens en compte le demi tarif etc
#socioeco
CalcIncome= DefineVariable('CalcIncome', CalculatedIncome*(CalculatedIncome>0) )
age1= DefineVariable('age1', age*(age<=25))
age2= DefineVariable('age2', age*(25<age<=65))
age3= DefineVariable('age3', age*(age>65))

urb= DefineVariable('urb',1*(UrbRur==1))

roman= DefineVariable('roman',1*(Region<4))

Tripwork=DefineVariable('Tripwork',1*(TripPurpose==1))
TripLeisure=DefineVariable('TripLeisure',1*(TripPurpose==3))
#other
Have_GA = DefineVariable('have_GA', GenAbST == 1)
Multi_trips = DefineVariable('Multi_trips', NbTrajects > 2)
Have_GA_LT = DefineVariable('Have_GA_LT',((GenAbST==1)+(LineRelST ==1))>0)


# Utilities
## public transport
_Public_T = ASC_PT*one \
            +Beta_time_PT*((((pt_transp_time)**LAMBDA)-1)/LAMBDA) \
            +Beta_time_PT_walk*(pt_ww_time)\
            + Beta_Cost_age1* PT_cost*age1*Have_GA_LT\
            + Beta_Cost_age2* PT_cost*age2*Have_GA_LT\
            + Beta_Cost_age3* PT_cost*age3*Have_GA_LT\
            + Beta_Age1_PT*age1+Beta_Age2_PT*age2\
            +Beta_urb*urb\
            +Beta_TripWork*Tripwork+Beta_TripLeisure*TripLeisure\
            +Beta_have_ga * Have_GA
## private mods
_Private_M = ASC_PM*one \
            + Beta_time_PM*car_time \
            + Beta_Cost_age1* car_cost*age1\
            + Beta_Cost_age2* car_cost*age2\
            + Beta_Cost_age3* car_cost*age3\
            + Beta_Age1_PM*age1+Beta_Age2_PM*age2\
            + Beta_multi_trips*Multi_trips\
            + Beta_roman*roman
## soft modes
_soft_M = \
         Beta_Distance*distance_trip

V = {0: _Public_T,1: _Private_M ,2: _soft_M }
av = {0: one,1: pm_avail,2: bike_walk_avail}


BIOGEME_OBJECT.STATISTICS['SampleSize0'] = Sum(one, 'obsIter')
#Exclude (No need to exclude anything here)
BIOGEME_OBJECT.EXCLUDE = (Choice   ==  -1) + \
                         ((Choice == 1) * (pm_avail != 1) > 0)+ \
                          ((Choice == 2)* (bike_walk_avail!=1)>0)\
                        + (Have_GA_LT==0)


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
VOT_walk= Derive(_Public_T,'pt_ww_time')/Derive(_Public_T,'PT_cost')
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
