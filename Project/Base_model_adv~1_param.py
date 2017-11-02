# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:20:42 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  2 16:50:40 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Time_PT_in = Beta('Time_PT_in',0.00186817,-10000,10000,0,'Time_PT_in' )

Time_PT_out = Beta('Time_PT_out',-0.0324214,-10000,10000,0,'Time_PT_out' )

BetaCost = Beta('BetaCost',0.000254066,-10000,10000,0,'BetaCost' )

ASC_Nb_trans = Beta('ASC_Nb_trans',-0.0353525,-10000,10000,0,'ASC_Nb_trans' )

ASC_PM  = Beta('ASC_PM ',0.312651,-10000,10000,0,'ASC_PM ' )

Time_car = Beta('Time_car',-0.0226591,-10000,10000,0,'Time_car' )

ASC_SM = Beta('ASC_SM',-0.186074,-10000,10000,0,'ASC_SM' )

Distance = Beta('Distance',-0.205593,-10000,10000,0,'Distance' )


## Code for the sensitivity analysis
names = ['ASC_Nb_trans','ASC_PM ','ASC_SM','BetaCost','Distance','Time_PT_in','Time_PT_out','Time_car']
values = [[0.00350306,-0.000654353,-0.000663803,-4.18695e-05,-4.14431e-06,-8.36986e-05,-4.48603e-05,4.13749e-05],[-0.000654353,0.0112901,0.00341298,1.10391e-05,0.000865488,8.61974e-06,0.000181218,-3.24826e-05],[-0.000663803,0.00341298,0.109096,-0.000222225,-0.0166979,-0.000221849,5.29124e-05,-0.00026182],[-4.18695e-05,1.10391e-05,-0.000222225,3.63833e-05,5.42299e-05,2.95607e-06,-8.64476e-07,-1.30639e-05],[-4.14431e-06,0.000865488,-0.0166979,5.42299e-05,0.00312149,6.65092e-05,2.68416e-05,8.50635e-05],[-8.36986e-05,8.61974e-06,-0.000221849,2.95607e-06,6.65092e-05,1.51611e-05,-8.04536e-07,1.4637e-05],[-4.48603e-05,0.000181218,5.29124e-05,-8.64476e-07,2.68416e-05,-8.04536e-07,1.00871e-05,4.00502e-06],[4.13749e-05,-3.24826e-05,-0.00026182,-1.30639e-05,8.50635e-05,1.4637e-05,4.00502e-06,3.33882e-05]]
vc = bioMatrix(8,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
