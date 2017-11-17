# Tom Suter
# 19.10.2017

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *


ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.242582,-10000,10000,0,'Beta_time_PT' )

LAMBDA = Beta('LAMBDA',0.0527238,-10000,10000,0,'LAMBDA' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0324538,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',0.00826315,-10000,10000,0,'Beta_Cost' )

Beta_Age1 = Beta('Beta_Age1',-2.59914,-10000,10000,0,'Beta_Age1' )

Beta_Age2 = Beta('Beta_Age2',-0.00148665,-10000,10000,0,'Beta_Age2' )

Beta_Age3 = Beta('Beta_Age3',0.0188449,-10000,10000,0,'Beta_Age3' )

Beta_urb = Beta('Beta_urb',0.122931,-10000,10000,0,'Beta_urb' )

Beta_TripWork = Beta('Beta_TripWork',0.377029,-10000,10000,0,'Beta_TripWork' )

Beta_TripLeisure = Beta('Beta_TripLeisure',0.283024,-10000,10000,0,'Beta_TripLeisure' )

ASC_PM  = Beta('ASC_PM ',2.17575,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0152788,-10000,10000,0,'Beta_time_PM' )

Beta_multi_trips = Beta('Beta_multi_trips',-1.01354,-10000,10000,0,'Beta_multi_trips' )

Beta_roman = Beta('Beta_roman',2.27504,-10000,10000,0,'Beta_roman' )

Beta_german = Beta('Beta_german',2.04052,-10000,10000,0,'Beta_german' )

ASC_SM = Beta('ASC_SM',5.00601,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.765661,-10000,10000,0,'Beta_Distance' )

Beta_Age1_walk = Beta('Beta_Age1_walk',-2.07565,-10000,10000,0,'Beta_Age1_walk' )

Beta_Age2_walk = Beta('Beta_Age2_walk',-0.011644,-10000,10000,0,'Beta_Age2_walk' )

Beta_Age3_walk = Beta('Beta_Age3_walk',-0.00682915,-10000,10000,0,'Beta_Age3_walk' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Age1','Beta_Age1_walk','Beta_Age2','Beta_Age2_walk','Beta_Age3','Beta_Age3_walk','Beta_Cost','Beta_Distance','Beta_TripLeisure','Beta_TripWork','Beta_german','Beta_multi_trips','Beta_roman','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk','Beta_urb','LAMBDA']
values = [[7.3203e+11,-4.27687e+10,-3.64248e+09,1.10312e+10,1.26554e+08,1.01858e+09,7.91027e+07,6.54916e+08,1.43086e+06,-3.59233e+09,-7.69826e+09,-1.13138e+10,-8.41894e+11,1.15706e+10,-5.0816e+11,1.97371e+06,1.58514e+09,-6.58525e+06,1.47808e+08,2.53678e+08],[-2.20223,4.62023,-2.10707,1.62988,0.0422597,-0.0348316,0.0292595,-0.0233747,-0.00232203,-0.0587771,-0.0351421,0.00647153,5.15147,-0.133292,5.15552,0.00178658,0.151147,-0.000413561,0.181442,0.0769232],[11.1454,-2.24897,2.52247,0.173163,-0.0487403,0.000816216,-0.0338052,0.00133001,-9.20024e-05,-0.000550262,0.476383,0.375634,-13.5483,0.0959172,-13.1066,-0.00140691,-0.0607413,0.0031865,-0.142755,-0.0268819],[7.98169,1.53709,0.155102,2.2769,-0.00210293,-0.033877,-0.00149122,-0.0233724,0.000622576,-0.010111,-0.0646478,-0.125953,-8.21852,0.208072,-7.85106,9.49733e-05,0.013911,0.000948775,-0.0271762,0.000811088],[-0.207373,0.0449289,-0.0488163,-0.00249654,0.00101727,-1.90477e-05,0.000669012,-2.93713e-05,4.86499e-06,3.3999e-06,-0.00954367,-0.00892618,0.254947,-0.000773296,0.246906,3.35214e-05,0.00135407,-5.93618e-05,0.00251285,0.000601446],[-0.135153,-0.0322233,-0.00231805,-0.0362708,3.84814e-05,0.000725482,2.43024e-05,0.000462999,-9.22047e-06,0.000667572,0.000571934,0.00101058,0.139363,-0.00199462,0.133464,1.50517e-06,4.26211e-05,-9.51963e-06,0.000395063,3.35085e-05],[-0.150829,0.0311724,-0.0338598,-0.00176687,0.000669038,-1.69222e-05,0.00050993,-2.19124e-05,-4.18742e-06,-1.07766e-05,-0.00698621,-0.0046229,0.183651,-0.000769762,0.178282,1.80906e-05,0.00058676,-2.26849e-05,0.00239524,0.000284649],[-0.0859827,-0.0216392,-0.000800033,-0.0249821,9.75174e-06,0.00046379,6.14113e-06,0.000398485,-8.1894e-06,0.000166888,0.000819399,0.000988377,0.0882574,-0.00161594,0.0844945,1.00254e-07,8.06622e-06,-4.3716e-06,6.5418e-05,1.19835e-05],[-0.0097326,-0.00222458,-4.88123e-05,0.000629981,3.96932e-06,-1.21411e-05,-4.82669e-06,-1.01331e-05,8.25061e-05,6.72467e-05,-0.00173354,-0.00198172,0.00696326,0.00208461,0.00601159,4.69728e-06,-0.000471598,7.3316e-07,0.000520963,-0.000182593],[-0.0361555,-0.0611787,0.00821645,-0.00391316,-0.000159983,0.00055851,-0.000127333,9.53487e-05,5.97645e-05,0.0164247,2.1599e-05,-0.00205113,0.0297377,0.00885808,0.0282717,3.26416e-05,0.00100027,5.38327e-05,-0.000342478,-0.000202667],[2.90084,-0.0634785,0.485595,-0.0557259,-0.00970709,0.00101626,-0.00709889,0.00112796,-0.0017538,-0.00139351,0.554587,0.473478,-2.94422,-0.173488,-2.83307,-0.00076979,-0.023649,0.00278337,-0.0577169,-0.00739491],[1.91673,-0.0144863,0.389479,-0.113807,-0.00917699,0.00120533,-0.0047979,0.00112488,-0.00200376,-0.0030083,0.474073,0.620364,-1.89239,-0.229836,-1.79782,-0.000721227,-0.0321286,0.00260667,-0.0180423,-0.00987183],[-7.3203e+11,4.27687e+10,3.64248e+09,-1.10312e+10,-1.26554e+08,-1.01858e+09,-7.91027e+07,-6.54916e+08,-1.43086e+06,3.59233e+09,7.69826e+09,1.13138e+10,8.41894e+11,-1.15706e+10,5.0816e+11,-1.97371e+06,-1.58514e+09,6.58525e+06,-1.47808e+08,-2.53678e+08],[0.728189,-0.136829,0.0811849,0.196932,-0.000499117,-0.00163715,-0.000576307,-0.00137247,0.00209828,0.0084546,-0.174989,-0.231122,-0.955492,0.32699,-0.944752,0.000295323,0.00181596,0.00101495,-0.00919848,-0.00199329],[-7.3203e+11,4.27687e+10,3.64248e+09,-1.10312e+10,-1.26554e+08,-1.01858e+09,-7.91027e+07,-6.54916e+08,-1.43086e+06,3.59233e+09,7.69826e+09,1.13138e+10,8.41894e+11,-1.15706e+10,5.0816e+11,-1.97371e+06,-1.58514e+09,6.58525e+06,-1.47808e+08,-2.53678e+08],[-0.00498187,0.00183617,-0.00135504,0.000118735,3.25125e-05,-5.24716e-07,1.73597e-05,-1.2587e-06,4.69028e-06,3.66142e-05,-0.000753474,-0.000707281,0.00702215,0.000292544,0.00684563,1.92925e-05,0.000341261,1.12431e-06,0.000110446,0.000141897],[-0.168268,0.153778,-0.0627839,0.0123062,0.00139185,2.27833e-05,0.000613006,-6.08814e-06,-0.00046834,0.0010967,-0.0238407,-0.0322762,0.335794,0.00177303,0.348264,0.000343415,0.0356187,-0.000997194,0.0119107,0.0163178],[0.0336566,-0.000722394,0.00323436,0.000995432,-6.01951e-05,-3.60997e-06,-2.32598e-05,-2.71662e-07,5.88558e-07,3.80889e-05,0.00278687,0.00260266,-0.0350019,0.00103023,-0.0339509,9.55501e-07,-0.000996514,0.000123706,-0.00124423,-0.000499826],[-2.37475,0.20885,-0.142095,-0.0300187,0.00248651,-0.000220815,0.00237634,-0.000352681,0.000528724,0.00133987,-0.0559496,-0.0154281,2.62144,-0.0119218,2.49373,0.000120332,0.0115311,-0.00123424,0.160064,0.00897273],[-0.105446,0.0781687,-0.0272519,0.00052703,0.000608311,1.33434e-05,0.000289309,-2.70493e-06,-0.000181672,-0.000146731,-0.00743963,-0.00990756,0.185528,-0.00199903,0.184785,0.000142769,0.0163191,-0.00049964,0.00904184,0.00869313]]

# Define here arithmetic expressions for name that are not directly available from the data
#--- availability
pm_avail =  DefineVariable('pm_avail', ((CarAvail != 3)+(NbMoto>=1))>0 )
bike_walk_avail =  DefineVariable('bike_walk_avail', ((distance_km)<8 + (NbBicy>0)*(distance_km)<16)>0)
CardOwner = DefineVariable('CardOwners', (HalfFareST == 1) + (LineRelST == 1) + (GenAbST == 1) + (AreaRelST == 1) + (OtherST == 1) > 0)

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
PT_cost=DefineVariable('PT',MarginalCostPT)  #marginal tiens en compte le demi tarif etc
#socioeco
CalcIncome= DefineVariable('CalcIncome', CalculatedIncome*(CalculatedIncome>0) )
age1= DefineVariable('age1', age*(age<=25))
age2= DefineVariable('age2', age*(25<age<=65))
age3= DefineVariable('age3', age*(age>65))
urb= DefineVariable('urb',1*(UrbRur==1))
rur= DefineVariable('rur',1*(UrbRur==2))
roman= DefineVariable('roman',1*(Region<4))
german = DefineVariable('german',1*(Region>=4))
commune1=DefineVariable('commune1',1*(TypeCommune<7))
commune2=DefineVariable('commune2',1*(TypeCommune>7))
Tripwork=DefineVariable('Tripwork',1*(TripPurpose==1))
TripLeisure=DefineVariable('TripLeisure',1*(TripPurpose==3))
#other
Multi_trips = DefineVariable('Multi_trips', NbTrajects > 2)


# Utilities
## public transport
_Public_T = ASC_PT*one \
            +Beta_time_PT*(((pt_transp_time**LAMBDA)-1)/LAMBDA) \
            +Beta_time_PT_walk*(pt_walk_time+pt_wait_time )\
            +Beta_Cost* PT_cost \
            +Beta_Age1*age1+Beta_Age2*age2+Beta_Age3*age3\
            +Beta_urb*urb\
            +Beta_TripWork*Tripwork+Beta_TripLeisure*TripLeisure\

## private mods
_Private_M = ASC_PM*one \
            + Beta_time_PM*car_time \
            + Beta_Cost* car_cost \
            + Beta_multi_trips*Multi_trips\
            + Beta_roman*roman \
            + Beta_german*german

## soft modes
_soft_M = ASC_SM*one \
         + Beta_Distance*distance_trip\
         + Beta_Age1_walk*age1+Beta_Age2_walk*age2+Beta_Age3_walk*age3\

V = {0: _Public_T,1: _Private_M ,2: _soft_M }
av = {0: one,1: pm_avail,2: bike_walk_avail}


#No need for estimating the model (it is already estimated). We want to obtain the individual probabilities and the market shares
probPT = bioLogit(V,av,0)
probPM = bioLogit(V,av,1)
probSM = bioLogit(V,av,2)
probChosen = bioLogit(V,av,Choice) #Instead of reporting the choice in the simulation file, the probability of the chosen can be printed

# Defines an itertor on the data
rowIterator('obsIter')

#Simulation output
simulate = {'Choice':Choice,
            '01 Prob. PT': probPT,
            '02 Prob. PM': probPM,
            '03 Prob. SM': probSM,
            }

BIOGEME_OBJECT.SIMULATE = Enumerate(simulate,'obsIter')
