# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:20:42 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  2 16:06:42 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Time = Beta('Time',-0.0151381,-10000,10000,0,'Time' )

BetaCost = Beta('BetaCost',-0.0348305,-10000,10000,0,'BetaCost' )

ASC_PM  = Beta('ASC_PM ',0.46011,-10000,10000,0,'ASC_PM ' )

ASC_SM = Beta('ASC_SM',-0.0710881,-10000,10000,0,'ASC_SM' )

Distance = Beta('Distance',-0.218954,-10000,10000,0,'Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','BetaCost','Distance','Time']
values = [[0.0100508,0.00106694,3.1121e-05,0.00132735,0.000120744],[0.00106694,0.113282,-0.000316216,-0.0176641,-7.91187e-05],[3.1121e-05,-0.000316216,2.50095e-05,9.75503e-05,6.07654e-06],[0.00132735,-0.0176641,9.75503e-05,0.00335854,4.32552e-05],[0.000120744,-7.91187e-05,6.07654e-06,4.32552e-05,3.33818e-06]]
vc = bioMatrix(5,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
