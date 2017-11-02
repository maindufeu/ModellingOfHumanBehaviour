# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:20:42 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  2 16:08:58 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Time = Beta('Time',-0.00271675,-10000,10000,0,'Time' )

BetaCost = Beta('BetaCost',-0.00479585,-10000,10000,0,'BetaCost' )

ASC_PM  = Beta('ASC_PM ',0.782101,-10000,10000,0,'ASC_PM ' )

ASC_SM = Beta('ASC_SM',-1.87891,-10000,10000,0,'ASC_SM' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','BetaCost','Time']
values = [[0.006988,0.00786336,-8.08725e-05,4.4301e-05],[0.00786336,0.0328846,0.000137691,0.000111969],[-8.08725e-05,0.000137691,5.63359e-06,-1.82382e-07],[4.4301e-05,0.000111969,-1.82382e-07,5.96931e-07]]
vc = bioMatrix(4,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
