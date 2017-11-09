# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  9 21:14:09 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',-0.0103235,-10000,10000,0,'Beta_time_PT' )

Beta_Cost = Beta('Beta_Cost',0.0289582,-10000,10000,0,'Beta_Cost' )

ASC_PM  = Beta('ASC_PM ',0.892357,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0127623,-10000,10000,0,'Beta_time_PM' )

ASC_SM = Beta('ASC_SM',-0.938926,-10000,10000,0,'ASC_SM' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Cost','Beta_time_PM','Beta_time_PT']
values = [[0.00916686,0.00712357,-0.000227558,-2.66878e-06,8.74125e-05],[0.00712357,0.031228,0.000104451,0.00023129,0.000120011],[-0.000227558,0.000104451,5.2981e-05,5.09419e-06,-7.75925e-06],[-2.66878e-06,0.00023129,5.09419e-06,5.83193e-06,1.36315e-06],[8.74125e-05,0.000120011,-7.75925e-06,1.36315e-06,2.41238e-06]]
vc = bioMatrix(5,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
