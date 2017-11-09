# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:20:42 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  9 12:32:14 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Time = Beta('Time',-0.00853863,-10000,10000,0,'Time' )

Cost = Beta('Cost',0.0319452,-10000,10000,0,'Cost' )

ASC_PM  = Beta('ASC_PM ',0.948992,-10000,10000,0,'ASC_PM ' )

ASC_SM = Beta('ASC_SM',-1.99864,-10000,10000,0,'ASC_SM' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Cost','Time']
values = [[0.0065908,0.0102699,-1.03021e-06,4.90709e-05],[0.0102699,0.034305,-0.000172142,0.000162884],[-1.03021e-06,-0.000172142,2.29927e-05,-5.01714e-06],[4.90709e-05,0.000162884,-5.01714e-06,1.79203e-06]]
vc = bioMatrix(4,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
