# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:20:42 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  9 12:28:01 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Time = Beta('Time',-0.00116586,-10000,10000,0,'Time' )

Cost = Beta('Cost',0.0242018,-10000,10000,0,'Cost' )

ASC_PM  = Beta('ASC_PM ',1.9516,-10000,10000,0,'ASC_PM ' )

ASC_SM = Beta('ASC_SM',-1.2227,-10000,10000,0,'ASC_SM' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Cost','Time']
values = [[0.0183522,0.0138194,8.53074e-05,7.77709e-05],[0.0138194,0.0276014,-8.292e-05,0.000150229],[8.53074e-05,-8.292e-05,4.15928e-05,-8.0889e-06],[7.77709e-05,0.000150229,-8.0889e-06,2.55726e-06]]
vc = bioMatrix(4,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
