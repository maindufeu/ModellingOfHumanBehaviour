# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:20:42 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  2 16:33:42 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Time_PT_in = Beta('Time_PT_in',0.000959857,-10000,10000,0,'Time_PT_in' )

Time_PT_out = Beta('Time_PT_out',-0.0330824,-10000,10000,0,'Time_PT_out' )

BetaCost = Beta('BetaCost',-7.58691e-05,-10000,10000,0,'BetaCost' )

ASC_PM  = Beta('ASC_PM ',0.304684,-10000,10000,0,'ASC_PM ' )

Time_car = Beta('Time_car',-0.0225891,-10000,10000,0,'Time_car' )

ASC_SM = Beta('ASC_SM',-0.196051,-10000,10000,0,'ASC_SM' )

Distance = Beta('Distance',-0.205745,-10000,10000,0,'Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','BetaCost','Distance','Time_PT_in','Time_PT_out','Time_car']
values = [[0.0111731,0.00331108,2.57157e-06,0.000870419,-6.15928e-06,0.000174755,-2.07001e-05],[0.00331108,0.109239,-0.000231361,-0.016737,-0.000238999,4.83889e-05,-0.000250867],[2.57157e-06,-0.000231361,3.54822e-05,5.38681e-05,1.65648e-06,-1.38531e-06,-1.27805e-05],[0.000870419,-0.016737,5.38681e-05,0.00312954,6.72807e-05,2.62523e-05,8.56378e-05],[-6.15928e-06,-0.000238999,1.65648e-06,6.72807e-05,1.35466e-05,-1.97939e-06,1.61358e-05],[0.000174755,4.83889e-05,-1.38531e-06,2.62523e-05,-1.97939e-06,9.63593e-06,4.4577e-06],[-2.07001e-05,-0.000250867,-1.27805e-05,8.56378e-05,1.61358e-05,4.4577e-06,3.34512e-05]]
vc = bioMatrix(7,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
