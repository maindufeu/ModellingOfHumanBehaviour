# Tom Suter
# 19.10.2017

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *


ASC_PT = Beta('ASC_PT',-1.28488,-10000,10000,0,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.242507,-10000,10000,0,'Beta_time_PT' )

LAMBDA = Beta('LAMBDA',0.155883,-10000,10000,0,'LAMBDA' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0403533,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost_age1 = Beta('Beta_Cost_age1',-0.148051,-10000,10000,0,'Beta_Cost_age1' )

Beta_Cost_age2 = Beta('Beta_Cost_age2',-0.000325014,-10000,10000,0,'Beta_Cost_age2' )

Beta_Cost_age3 = Beta('Beta_Cost_age3',0.0027848,-10000,10000,0,'Beta_Cost_age3' )

Beta_Age1_PT = Beta('Beta_Age1_PT',2.35631,-10000,10000,0,'Beta_Age1_PT' )

Beta_Age2_PT = Beta('Beta_Age2_PT',-0.0133422,-10000,10000,0,'Beta_Age2_PT' )

Beta_urb = Beta('Beta_urb',-0.223754,-10000,10000,0,'Beta_urb' )

Beta_TripWork = Beta('Beta_TripWork',0.380994,-10000,10000,0,'Beta_TripWork' )

Beta_TripLeisure = Beta('Beta_TripLeisure',-0.221868,-10000,10000,0,'Beta_TripLeisure' )

Beta_have_ga = Beta('Beta_have_ga',2.27836,-10000,10000,0,'Beta_have_ga' )

ASC_PM  = Beta('ASC_PM ',-0.6704,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0143517,-10000,10000,0,'Beta_time_PM' )

Beta_Age1_PM = Beta('Beta_Age1_PM',2.29864,-10000,10000,0,'Beta_Age1_PM' )

Beta_Age2_PM = Beta('Beta_Age2_PM',-0.00261384,-10000,10000,0,'Beta_Age2_PM' )

Beta_multi_trips = Beta('Beta_multi_trips',-0.394746,-10000,10000,0,'Beta_multi_trips' )

Beta_roman = Beta('Beta_roman',0.939736,-10000,10000,0,'Beta_roman' )

Beta_Distance = Beta('Beta_Distance',-0.619126,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_PT','Beta_Age1_PM','Beta_Age1_PT','Beta_Age2_PM','Beta_Age2_PT','Beta_Cost_age1','Beta_Cost_age2','Beta_Cost_age3','Beta_Distance','Beta_TripLeisure','Beta_TripWork','Beta_have_ga','Beta_multi_trips','Beta_roman','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk','Beta_urb','LAMBDA']
values = [[0.404584,0.401637,0.35736,0.357299,-0.00744658,-0.00740425,-1.80139e-05,-7.56756e-06,-0.00189554,0.0136841,0.00272371,0.00388928,7.82743e-05,-0.00852673,-0.00672057,4.79425e-05,-0.00263127,-5.78799e-05,0.00435851,0.00411841],[0.401637,0.517734,0.363276,0.363074,-0.00758571,-0.00798802,0.00147147,-1.81326e-05,-0.00199812,0.0120561,-0.0493321,-0.0402569,-0.00189206,0.00754853,0.00224727,-0.000363776,-0.0148077,-0.00027242,-0.00524642,0.00582165],[0.35736,0.363276,1.38479,1.38474,-0.00743406,-0.0074503,-0.103758,-3.27498e-05,-0.0019642,-0.00734475,0.0072542,0.00906419,3.34236e-05,-0.0225533,-0.00343121,-1.90933e-05,-0.00619899,-7.64959e-05,0.00464444,0.00532191],[0.357299,0.363074,1.38474,1.38495,-0.00743504,-0.00744516,-0.103778,-3.2732e-05,-0.00196401,-0.00736005,0.0074483,0.00907089,-9.97188e-05,-0.022433,-0.00316501,-2.27042e-05,-0.00628247,-7.36611e-05,0.00455901,0.00529144],[-0.00744658,-0.00758571,-0.00743406,-0.00743504,0.000161168,0.000159786,1.91486e-07,-5.48585e-08,3.8098e-05,-3.98152e-05,-6.09417e-05,-7.5375e-05,4.23358e-05,0.000119871,8.21594e-07,-3.10583e-08,0.000109482,3.95058e-07,-6.10423e-05,-0.000102117],[-0.00740425,-0.00798802,-0.0074503,-0.00744516,0.000159786,0.000169687,-1.37793e-05,-7.6142e-08,3.86746e-05,-3.74236e-05,4.67929e-05,-0.000119948,8.19629e-06,0.000114761,-1.32304e-05,8.51298e-07,0.000132222,-7.6177e-07,-5.4754e-05,-0.00010384],[-1.80139e-05,0.00147147,-0.103758,-0.103778,1.91486e-07,-1.37793e-05,0.0135511,-3.01791e-07,-3.92118e-07,2.80438e-05,-0.000866181,-0.000252801,-0.000113168,0.00189881,0.000235372,1.24375e-07,1.57682e-05,1.06358e-05,-0.000491716,-0.000115266],[-7.56756e-06,-1.81326e-05,-3.27498e-05,-3.2732e-05,-5.48585e-08,-7.6142e-08,-3.01791e-07,1.26727e-07,1.40782e-07,6.84174e-06,6.12874e-06,8.25043e-06,-9.82331e-06,-3.22923e-06,-2.21512e-06,-2.55141e-08,6.66825e-07,-4.31359e-08,6.92502e-07,3.25461e-07],[-0.00189554,-0.00199812,-0.0019642,-0.00196401,3.8098e-05,3.86746e-05,-3.92118e-07,1.40782e-07,1.67295e-05,4.88178e-06,-2.15624e-05,-2.00239e-05,7.9065e-06,3.43574e-05,-8.51864e-06,1.64235e-07,3.53174e-05,2.36883e-08,-9.29031e-06,-2.5783e-05],[0.0136841,0.0120561,-0.00734475,-0.00736005,-3.98152e-05,-3.74236e-05,2.80438e-05,6.84174e-06,4.88178e-06,0.0054857,0.000282129,9.65817e-05,7.07696e-05,-3.73146e-05,-0.000359306,2.25241e-05,0.000484787,-3.4693e-06,0.000272165,-1.35326e-05],[0.00272371,-0.0493321,0.0072542,0.0074483,-6.09417e-05,4.67929e-05,-0.000866181,6.12874e-06,-2.15624e-05,0.000282129,0.0537118,0.0422445,-0.00512761,-0.0113489,0.000841441,5.8028e-05,0.000247997,0.000233496,-0.00150822,-0.00081556],[0.00388928,-0.0402569,0.00906419,0.00907089,-7.5375e-05,-0.000119948,-0.000252801,8.25043e-06,-2.00239e-05,9.65817e-05,0.0422445,0.0555744,-0.00585822,-0.0183129,0.000178327,4.41218e-05,-0.00012502,0.000187491,-0.00304215,-0.00103173],[7.82743e-05,-0.00189206,3.34236e-05,-9.97188e-05,4.23358e-05,8.19629e-06,-0.000113168,-9.82331e-06,7.9065e-06,7.07696e-05,-0.00512761,-0.00585822,0.0557845,-0.00256029,0.000575647,0.000147383,0.00265507,-0.000157485,0.00159506,0.000298232],[-0.00852673,0.00754853,-0.0225533,-0.022433,0.000119871,0.000114761,0.00189881,-3.22923e-06,3.43574e-05,-3.73146e-05,-0.0113489,-0.0183129,-0.00256029,0.0518964,0.00097005,-0.000112184,-0.00213955,0.000308972,-0.0028803,-9.09047e-05],[-0.00672057,0.00224727,-0.00343121,-0.00316501,8.21594e-07,-1.32304e-05,0.000235372,-2.21512e-06,-8.51864e-06,-0.000359306,0.000841441,0.000178327,0.000575647,0.00097005,0.0257142,-2.52402e-05,-0.000651722,1.19622e-05,-0.00479432,0.00023491],[4.79425e-05,-0.000363776,-1.90933e-05,-2.27042e-05,-3.10583e-08,8.51298e-07,1.24375e-07,-2.55141e-08,1.64235e-07,2.25241e-05,5.8028e-05,4.41218e-05,0.000147383,-0.000112184,-2.52402e-05,1.0639e-05,9.38395e-05,2.74677e-06,1.01788e-05,4.96711e-05],[-0.00263127,-0.0148077,-0.00619899,-0.00628247,0.000109482,0.000132222,1.57682e-05,6.66825e-07,3.53174e-05,0.000484787,0.000247997,-0.00012502,0.00265507,-0.00213955,-0.000651722,9.38395e-05,0.00414062,-9.30356e-05,0.000985517,-0.000945351],[-5.78799e-05,-0.00027242,-7.64959e-05,-7.36611e-05,3.95058e-07,-7.6177e-07,1.06358e-05,-4.31359e-08,2.36883e-08,-3.4693e-06,0.000233496,0.000187491,-0.000157485,0.000308972,1.19622e-05,2.74677e-06,-9.30356e-05,1.79252e-05,-0.000104167,-6.76124e-06],[0.00435851,-0.00524642,0.00464444,0.00455901,-6.10423e-05,-5.4754e-05,-0.000491716,6.92502e-07,-9.29031e-06,0.000272165,-0.00150822,-0.00304215,0.00159506,-0.0028803,-0.00479432,1.01788e-05,0.000985517,-0.000104167,0.0200266,-6.91249e-05],[0.00411841,0.00582165,0.00532191,0.00529144,-0.000102117,-0.00010384,-0.000115266,3.25461e-07,-2.5783e-05,-1.35326e-05,-0.00081556,-0.00103173,0.000298232,-9.09047e-05,0.00023491,4.96711e-05,-0.000945351,-6.76124e-06,-6.91249e-05,0.00229763]]
vc = bioMatrix(20,names,values)
BIOGEME_OBJECT.VARCOVAR = vc

# Define here arithmetic expressions for name that are not directly available from the data
#--- availability
pm_avail =  DefineVariable('pm_avail', ((CarAvail != 3)+(NbMoto>=1))>0 )
bike_walk_avail =  DefineVariable('bike_walk_avail', ((distance_km)<8 + (NbBicy>0)*(distance_km)<16)>0)

one  = DefineVariable('one',1)
#----time
car_time  = DefineVariable('car_time', TimeCar )
pt_total_time = DefineVariable('pt_total_time', TimePT)
pt_wait_time = DefineVariable('pt_wait_time', WaitingTimePT)
pt_walk_time = DefineVariable('pt_walk_time',WalkingTimePT)
pt_transp_time= DefineVariable('pt_transp_time',InVehicleTime*(InVehicleTime>0))
distance_trip=DefineVariable('distance_trip',distance_km)
reported_time=DefineVariable('reported_time',ReportedDuration)
#---cost
car_cost=DefineVariable('car_cost',CostCar)
PT_cost=DefineVariable('PT',MarginalCostPT*2)  #marginal tiens en compte le demi tarif etc
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


# Utilities
## public transport
_Public_T = ASC_PT*one \
            +Beta_time_PT*(((pt_transp_time**LAMBDA)-1)/LAMBDA) \
            +Beta_time_PT_walk*(pt_walk_time+pt_wait_time )\
            + Beta_Cost_age1* PT_cost*age1\
            + Beta_Cost_age2* PT_cost*age2\
            + Beta_Cost_age3* PT_cost*age3\
            + Beta_Age1_PT*age1+Beta_Age2_PT*age2\
            +Beta_urb*urb\
            +Beta_TripWork*Tripwork+Beta_TripLeisure*TripLeisure\
            +Beta_have_ga * Have_GA
## private mods
_Private_M = ASC_PM*one \
            + Beta_time_PM*car_time \
            + Beta_Cost_age1* PT_cost*age1\
            + Beta_Cost_age2* PT_cost*age2\
            + Beta_Cost_age3* PT_cost*age3\
            + Beta_Age1_PM*age1+Beta_Age2_PM*age2\
            + Beta_multi_trips*Multi_trips\
            + Beta_roman*roman
## soft modes
_soft_M = \
         Beta_Distance*distance_trip

V = {0: _Public_T,1: _Private_M ,2: _soft_M }
av = {0: one,1: pm_avail,2: bike_walk_avail}



#Exclude
BIOGEME_OBJECT.EXCLUDE = (Choice   ==  -1) + \
                         ((Choice == 1) * (pm_avail != 1) > 0)+ \
                          ((Choice == 2)* (bike_walk_avail!=1)>0)


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
probChosen = bioLogit(V,av,Choice) #Instead of reporting the choice in the simulation file, the probability of the chosen can be printed
VOT_CAR = Derive(probPM,'TimeCar')/Derive(probPM,'CostCar')
VOT_PT = Derive(probPT,'pt_transp_time')/Derive(probPT,'CostPT')
# Defines an itertor on the data
rowIterator('obsIter')

#Simulation output
simulate = {'Choice':Choice,
            '01 Prob. PT': probPT,
            '02 Prob. PM': probPM,
            '03 Prob. SM': probSM,
            '04 VOT_CAR' : VOT_CAR,
            'Revenue PT': probPT * PT_cost
            }

BIOGEME_OBJECT.SIMULATE = Enumerate(simulate,'obsIter')
