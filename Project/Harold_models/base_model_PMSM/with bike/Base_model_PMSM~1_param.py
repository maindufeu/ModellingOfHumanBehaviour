# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:20:42 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  9 15:42:58 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Time = Beta('Time',-0.0141221,-10000,10000,0,'Time' )

Cost = Beta('Cost',0.0351044,-10000,10000,0,'Cost' )

ASC_PM  = Beta('ASC_PM ',0.658267,-10000,10000,0,'ASC_PM ' )

ASC_SM = Beta('ASC_SM',-1.01041,-10000,10000,0,'ASC_SM' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Cost','Time']
values = [[0.00953591,0.0091165,-1.34336e-05,0.000103992],[0.0091165,0.0237764,-0.000136158,0.000148435],[-1.34336e-05,-0.000136158,2.93561e-05,-6.91696e-06],[0.000103992,0.000148435,-6.91696e-06,3.27795e-06]]
vc = bioMatrix(4,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
