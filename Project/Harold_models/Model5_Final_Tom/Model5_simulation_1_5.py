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
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.282875,-10000,10000,0,'Beta_time_PT' )

LAMBDA = Beta('LAMBDA',0.205604,-10000,10000,0,'LAMBDA' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0396421,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.0486532,-10000,10000,0,'Beta_Cost' )

Beta_Age1 = Beta('Beta_Age1',0.0520672,-10000,10000,0,'Beta_Age1' )

Beta_Age2 = Beta('Beta_Age2',-0.00881873,-10000,10000,0,'Beta_Age2' )

Beta_Age3 = Beta('Beta_Age3',0.0033125,-10000,10000,0,'Beta_Age3' )

Beta_urb = Beta('Beta_urb',-0.208572,-10000,10000,0,'Beta_urb' )

Beta_TripWork = Beta('Beta_TripWork',0.356507,-10000,10000,0,'Beta_TripWork' )

Beta_TripLeisure = Beta('Beta_TripLeisure',-0.237489,-10000,10000,0,'Beta_TripLeisure' )

Beta_have_ga = Beta('Beta_have_ga',1.65946,-10000,10000,0,'Beta_have_ga' )

ASC_PM  = Beta('ASC_PM ',0.572261,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0157026,-10000,10000,0,'Beta_time_PM' )

Beta_multi_trips = Beta('Beta_multi_trips',-0.418267,-10000,10000,0,'Beta_multi_trips' )

Beta_roman = Beta('Beta_roman',1.09728,-10000,10000,0,'Beta_roman' )

Beta_german = Beta('Beta_german',0.249163,-10000,10000,0,'Beta_german' )

ASC_SM = Beta('ASC_SM',1.75024,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.625355,-10000,10000,0,'Beta_Distance' )

Beta_Age1_walk = Beta('Beta_Age1_walk',-1.16356,-10000,10000,0,'Beta_Age1_walk' )

Beta_Age2_walk = Beta('Beta_Age2_walk',-0.00289481,-10000,10000,0,'Beta_Age2_walk' )

Beta_Age3_walk = Beta('Beta_Age3_walk',-0.010363,-10000,10000,0,'Beta_Age3_walk' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Age1','Beta_Age1_walk','Beta_Age2','Beta_Age2_walk','Beta_Age3','Beta_Age3_walk','Beta_Cost','Beta_Distance','Beta_TripLeisure','Beta_TripWork','Beta_german','Beta_have_ga','Beta_multi_trips','Beta_roman','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk','Beta_urb','LAMBDA']
values = [[8.54644e+10,-3.142e+10,-6.47914e+09,-1.08316e+11,-5.92537e+09,-3.41047e+09,-4.88053e+09,-5.43771e+08,-5.39618e+09,4.10932e+10,9.05652e+10,9.57093e+10,-1.05382e+11,-8.22578e+10,-3.61598e+10,-1.07943e+11,-5.98381e+09,1.99057e+11,-2.08324e+09,1.24876e+10,-2.81511e+11],[-0.387154,0.647198,-0.0417726,0.157682,-0.0371536,-0.0383354,-0.0296493,-0.0189168,-0.0140589,0.301595,0.439171,0.474101,0.255263,-0.30731,-0.124628,0.3344,-0.0328697,1.34578,-0.00940204,0.0879231,-1.92113],[-0.000429403,0.000993199,0.000186171,-0.000280893,-3.58146e-05,-3.98359e-05,-2.93882e-05,-1.84506e-05,3.29461e-06,0.000490344,0.000707289,0.000675739,0.00106354,-0.000411507,6.34545e-05,0.00146452,-4.81362e-05,0.0019806,-8.46467e-06,8.83949e-05,-0.00297153],[-0.606365,0.43015,-0.061839,0.261673,-0.0551751,-0.0501657,-0.0439243,-0.0236171,-0.0237445,0.455184,0.580308,0.634861,0.220565,-0.482683,-0.17676,0.335132,-0.0490119,1.93199,-0.0144528,0.117114,-2.77644],[0.000227372,0.00084383,-1.16771e-05,-0.000259213,-5.28661e-06,-1.62279e-05,-9.62109e-06,-6.50102e-06,-7.34697e-06,0.000251573,0.000338174,0.000290065,0.000671825,-0.000260095,-2.13705e-05,0.000704898,-2.36007e-05,0.00105927,-7.67466e-06,7.72363e-05,-0.00149053],[0.00659783,-0.0101186,0.000668113,-0.0051491,0.00059678,0.000662205,0.00047412,0.000326298,0.000254313,-0.00479214,-0.00621956,-0.00681502,-0.00223619,0.00516956,0.00183008,-0.00346217,0.000526591,-0.0207129,0.000154215,-0.00121446,0.0297587],[0.000282228,0.000566603,3.9871e-06,-8.18672e-05,3.35045e-06,-4.70273e-06,7.05798e-06,5.76281e-07,1.35529e-06,8.82123e-05,3.24576e-06,0.000126109,0.000365125,-4.01128e-05,4.53249e-05,0.00037341,-7.98936e-06,0.000364404,-1.64842e-06,3.74562e-05,-0.000513978],[0.00447717,-0.00659101,0.000443698,-0.00343634,0.000395534,0.000430389,0.000316432,0.000251336,0.000166508,-0.0032123,-0.00410489,-0.00449707,-0.00155025,0.0033898,0.0012067,-0.00239066,0.000348002,-0.0137255,0.000102246,-0.000818066,0.0197125],[-0.000862769,0.00116357,-3.11374e-05,-0.00015877,-3.92875e-05,-3.53979e-05,-2.72282e-05,-2.17281e-05,0.000164694,0.0004458,0.000383759,0.000593168,0.00144866,0.00165877,-0.000197553,0.00180432,-9.0295e-06,0.00152369,2.49514e-06,6.32914e-05,-0.00219026],[-0.00554508,-0.016483,-0.00129166,-0.0110897,-0.00114725,-0.000718935,-0.000920126,-0.000281039,-0.000551792,0.0145377,0.0135413,0.0145636,0.000294563,-0.0104801,-0.00481114,0.001881,-0.00100766,0.0403938,-0.000321037,0.00266534,-0.0572167],[-0.102978,0.0215291,-0.0112151,-0.115794,-0.010082,-0.00704838,-0.00813303,-0.00301779,-0.00372281,0.0844583,0.158457,0.156199,0.0802709,-0.0879305,-0.0441818,0.102481,-0.00875679,0.356916,-0.00234884,0.0202308,-0.513963],[-0.103812,0.0140454,-0.0115695,-0.124218,-0.0103979,-0.00715086,-0.00821467,-0.00302,-0.00375479,0.085982,0.148471,0.172931,0.0760835,-0.0892172,-0.0517391,0.0976678,-0.00896155,0.364367,-0.00244999,0.0193064,-0.52513],[-8.54644e+10,3.142e+10,6.47914e+09,1.08316e+11,5.92537e+09,3.41047e+09,4.88053e+09,5.43771e+08,5.39618e+09,-4.10932e+10,-9.05652e+10,-9.57093e+10,1.05382e+11,8.22578e+10,3.61598e+10,1.07943e+11,5.98381e+09,-1.99057e+11,2.08324e+09,-1.24876e+10,2.81511e+11],[0.0142544,0.0138575,2.70597e-05,0.000870097,7.80945e-06,1.47809e-05,6.51227e-05,4.63863e-06,0.0017248,0.000167397,-0.00383845,-0.00222798,-0.00055951,0.0756894,-0.00497452,0.00162614,0.00041118,0.000744318,-0.000108187,0.000497573,0.00411673],[0.056661,0.0159403,0.00640801,0.0776593,0.00558206,0.00359874,0.00446231,0.00144671,0.00211774,-0.0455594,-0.0693125,-0.081511,-0.0315351,0.0428226,0.0750775,-0.0405631,0.00465124,-0.195901,0.0017901,-0.0152871,0.277686],[-8.54644e+10,3.142e+10,6.47914e+09,1.08316e+11,5.92537e+09,3.41047e+09,4.88053e+09,5.43771e+08,5.39618e+09,-4.10932e+10,-9.05652e+10,-9.57093e+10,1.05382e+11,8.22578e+10,3.61598e+10,1.07943e+11,5.98381e+09,-1.99057e+11,2.08324e+09,-1.24876e+10,2.81511e+11],[-0.00042934,0.000610632,-3.00935e-05,-0.000159145,-2.43065e-05,-2.00119e-05,-1.92137e-05,-1.20943e-05,2.22787e-05,0.000281112,0.00027873,0.000336327,0.00086804,0.000286645,-0.000249413,0.000958825,-1.21857e-07,0.00103588,-1.64891e-06,5.47526e-05,-0.00124773],[0.00279763,0.0102805,-0.000219376,-0.000457975,-0.000118397,-0.00010903,-0.000105875,-5.74134e-05,4.56726e-05,0.0018798,0.00139264,0.00109239,0.00908439,0.0022907,-0.00246569,0.00891396,-3.17932e-06,0.00985711,-0.000106623,0.00123862,-0.00951571],[-0.0004685,0.000370992,-2.18712e-05,-9.35853e-05,-2.35933e-05,-1.95216e-05,-1.70124e-05,-1.03691e-05,7.10531e-06,0.000209813,0.00039606,0.000400748,0.000515027,-0.00022479,0.000317178,0.000645257,-1.54819e-05,0.000736889,1.47353e-05,-6.32849e-05,-0.00122743],[0.0136997,0.00570371,0.000632847,0.00246653,0.000607044,0.000504142,0.000483876,0.000230422,0.000175227,-0.00482619,-0.00788367,-0.00995073,0.000576232,0.00529568,-0.0014058,-0.006603,0.000511416,-0.0199781,3.16849e-05,0.019542,0.0301046],[-0.000187988,-0.000552134,-2.26363e-05,-8.05523e-06,7.66241e-06,4.69893e-06,8.36866e-06,-1.75219e-05,-6.30838e-06,-4.83708e-05,-0.000560701,-0.000449103,-0.00109057,0.00103014,-0.0007149,-0.00112345,0.000111587,-0.00198806,-2.61701e-05,-0.000148833,0.0042635]]


# Define here arithmetic expressions for name that are not directly available from the data
#--- availability
pm_avail =  DefineVariable('pm_avail', ((CarAvail != 3)+(NbMoto>=1))>0 )
bike_walk_avail =  DefineVariable('bike_walk_avail', ((distance_km)<8 + (NbBicy>0)*(distance_km)<16)>0)

one  = DefineVariable('one',1)
#----time
pt_transp_time= DefineVariable('pt_transp_time',InVehicleTime*(InVehicleTime>0))

#---cost
PT_cost=DefineVariable('PT',MarginalCostPT*1.5)  #marginal tiens en compte le demi tarif etc
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
Have_GA = DefineVariable('have_GA', GenAbST == 1)
Multi_trips = DefineVariable('Multi_trips', NbTrajects > 2)


# Utilities
## public transport
_Public_T = ASC_PT*one \
            +Beta_time_PT*(((pt_transp_time**LAMBDA)-1)/LAMBDA) \
            +Beta_time_PT_walk*(WalkingTimePT+WaitingTimePT )\
            +Beta_Cost* PT_cost\
            +Beta_Age1*age1+Beta_Age2*age2+Beta_Age3*age3\
            +Beta_urb*urb\
            +Beta_TripWork*Tripwork+Beta_TripLeisure*TripLeisure\
            +Beta_have_ga * Have_GA
## private mods
_Private_M = ASC_PM*one \
            + Beta_time_PM*TimeCar \
            + Beta_Cost* CostCar \
            + Beta_multi_trips*Multi_trips\
            + Beta_roman*roman \
            + Beta_german*german

## soft modes
_soft_M = ASC_SM*one \
         + Beta_Distance*distance_km\
         + Beta_Age1_walk*age1+Beta_Age2_walk*age2+Beta_Age3_walk*age3\

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
