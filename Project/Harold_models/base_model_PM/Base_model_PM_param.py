# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:20:42 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  9 12:29:22 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Time = Beta('Time',-0.00836955,-10000,10000,0,'Time' )

Cost = Beta('Cost',0.0321313,-10000,10000,0,'Cost' )

ASC_PM  = Beta('ASC_PM ',0.958292,-10000,10000,0,'ASC_PM ' )

ASC_SM = Beta('ASC_SM',-1.80235,-10000,10000,0,'ASC_SM' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Cost','Time']
values = [[0.00633751,0.00939662,7.00638e-08,4.53603e-05],[0.00939662,0.0297724,-0.000154127,0.000145064],[7.00638e-08,-0.000154127,2.29466e-05,-4.96944e-06],[4.53603e-05,0.000145064,-4.96944e-06,1.72142e-06]]
vc = bioMatrix(4,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
