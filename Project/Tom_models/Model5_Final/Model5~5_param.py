# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sat Nov  4 13:47:43 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.328268,-10000,10000,0,'Beta_time_PT' )

LAMBDA = Beta('LAMBDA',0.197706,-10000,10000,0,'LAMBDA' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0391306,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.0577076,-10000,10000,0,'Beta_Cost' )

Beta_Income = Beta('Beta_Income',-7.05171e-05,-10000,10000,0,'Beta_Income' )

Beta_Age = Beta('Beta_Age',-0.00607451,-10000,10000,0,'Beta_Age' )

Beta_typeBus = Beta('Beta_typeBus',-0.116362,-10000,10000,0,'Beta_typeBus' )

Beta_have_ga = Beta('Beta_have_ga',1.58982,-10000,10000,0,'Beta_have_ga' )

ASC_PM  = Beta('ASC_PM ',0.512938,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0148748,-10000,10000,0,'Beta_time_PM' )

Beta_multi_trips = Beta('Beta_multi_trips',-0.293002,-10000,10000,0,'Beta_multi_trips' )

ASC_SM = Beta('ASC_SM',-0.51735,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.192606,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Age','Beta_Cost','Beta_Distance','Beta_Income','Beta_have_ga','Beta_multi_trips','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk','Beta_typeBus','LAMBDA']
values = [[0.102901,0.0513336,0.000587955,0.000899412,0.00408758,-1.23642e-07,0.0152793,0.0021879,0.000499204,0.0110218,0.000146228,0.00521616,-0.0016506],[0.0513336,0.195813,-5.74832e-05,0.000443892,-0.0141435,5.65578e-06,0.00699541,-0.0139327,0.000184725,0.00703345,-6.16124e-05,0.00522747,-0.00243204],[0.000587955,-5.74832e-05,1.15001e-05,3.67703e-06,1.65316e-05,-1.74064e-09,1.21914e-05,5.17869e-05,9.61725e-07,-1.78349e-06,6.73561e-07,4.51225e-06,9.31577e-06],[0.000899412,0.000443892,3.67703e-06,0.000179656,9.4317e-05,-9.30509e-09,0.0019494,-7.27102e-06,2.51369e-05,5.01759e-06,1.0395e-05,1.22308e-06,2.17969e-05],[0.00408758,-0.0141435,1.65316e-05,9.4317e-05,0.00293831,-7.1245e-08,0.00138554,0.00245096,7.0622e-05,0.000679147,3.3441e-05,4.13466e-06,0.000229055],[-1.23642e-07,5.65578e-06,-1.74064e-09,-9.30509e-09,-7.1245e-08,6.55921e-10,-3.82841e-07,-2.69315e-07,-3.52567e-09,-1.78617e-08,-5.54586e-09,3.28078e-08,8.64007e-09],[0.0152793,0.00699541,1.21914e-05,0.0019494,0.00138554,-3.82841e-07,0.0747427,-0.00325738,0.000399009,0.00198465,-5.2489e-05,-0.000139162,0.00108942],[0.0021879,-0.0139327,5.17869e-05,-7.27102e-06,0.00245096,-2.69315e-07,-0.00325738,0.042208,-8.55929e-05,-0.00121421,0.000333626,-0.000535034,-0.00022432],[0.000499204,0.000184725,9.61725e-07,2.51369e-05,7.0622e-05,-3.52567e-09,0.000399009,-8.55929e-05,1.83863e-05,7.37687e-05,3.42492e-06,3.38861e-07,0.000105186],[0.0110218,0.00703345,-1.78349e-06,5.01759e-06,0.000679147,-1.78617e-08,0.00198465,-0.00121421,7.37687e-05,0.00443981,-7.46845e-05,6.26158e-05,-0.00186152],[0.000146228,-6.16124e-05,6.73561e-07,1.0395e-05,3.3441e-05,-5.54586e-09,-5.2489e-05,0.000333626,3.42492e-06,-7.46845e-05,1.71207e-05,-5.0386e-06,-1.1897e-05],[0.00521616,0.00522747,4.51225e-06,1.22308e-06,4.13467e-06,3.28078e-08,-0.000139162,-0.000535034,3.38861e-07,6.26158e-05,-5.0386e-06,0.00105313,-0.000145672],[-0.0016506,-0.00243204,9.31577e-06,2.17969e-05,0.000229055,8.64007e-09,0.00108942,-0.00022432,0.000105186,-0.00186152,-1.1897e-05,-0.000145672,0.0032569]]
vc = bioMatrix(13,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
