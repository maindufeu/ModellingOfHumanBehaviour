# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  9 21:16:32 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Time = Beta('Time',-0.0108352,-10000,10000,0,'Time' )

Cost = Beta('Cost',0.0337039,-10000,10000,0,'Cost' )

ASC_PM  = Beta('ASC_PM ',0.834256,-10000,10000,0,'ASC_PM ' )

ASC_SM = Beta('ASC_SM',-0.926068,-10000,10000,0,'ASC_SM' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Cost','Time']
values = [[0.00763159,0.00891029,-2.13839e-07,6.57216e-05],[0.00891029,0.0286239,-0.000132402,0.000136619],[-2.13839e-07,-0.000132402,2.56732e-05,-5.70875e-06],[6.57216e-05,0.000136619,-5.70875e-06,2.25811e-06]]
vc = bioMatrix(4,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
