# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:20:42 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  9 12:25:29 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Time = Beta('Time',-0.00885153,-10000,10000,0,'Time' )

Cost = Beta('Cost',0.0324317,-10000,10000,0,'Cost' )

ASC_PM  = Beta('ASC_PM ',0.81229,-10000,10000,0,'ASC_PM ' )

ASC_SM = Beta('ASC_SM',-1.85598,-10000,10000,0,'ASC_SM' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Cost','Time']
values = [[0.00635055,0.0100903,-2.66383e-06,4.82122e-05],[0.0100903,0.031002,-0.000157447,0.000151906],[-2.66383e-06,-0.000157447,2.29638e-05,-4.9734e-06],[4.82122e-05,0.000151906,-4.9734e-06,1.75373e-06]]
vc = bioMatrix(4,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
