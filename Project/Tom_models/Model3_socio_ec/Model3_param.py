# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sat Nov  4 11:22:46 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.000951097,-10000,10000,0,'Beta_time_PT' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0331427,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.00836426,-10000,10000,0,'Beta_Cost' )

ASC_PM  = Beta('ASC_PM ',0.305625,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0226191,-10000,10000,0,'Beta_time_PM' )

ASC_SM = Beta('ASC_SM',-0.195428,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.20568,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Cost','Beta_Distance','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk']
values = [[0.0111701,0.00337443,-2.89372e-05,0.000862006,-1.7837e-05,-5.4944e-06,0.000174968],[0.00337443,0.110681,8.51108e-05,-0.016723,-0.000244949,-0.000174257,5.11465e-05],[-2.89372e-05,8.51108e-05,0.00027777,-1.69258e-05,8.25416e-07,2.61442e-06,4.66931e-07],[0.000862006,-0.016723,-1.69258e-05,0.00308666,9.49729e-05,5.86825e-05,2.69438e-05],[-1.7837e-05,-0.000244949,8.25416e-07,9.49729e-05,3.16053e-05,1.84325e-05,4.28325e-06],[-5.4944e-06,-0.000174257,2.61442e-06,5.86825e-05,1.84325e-05,1.45282e-05,-1.71369e-06],[0.000174968,5.11465e-05,4.66931e-07,2.69438e-05,4.28325e-06,-1.71369e-06,9.62213e-06]]
vc = bioMatrix(7,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
