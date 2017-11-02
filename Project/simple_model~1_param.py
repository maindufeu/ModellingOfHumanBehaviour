# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:39 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  2 15:47:18 2017</p>
#
Constant1 = Beta('Constant1',0,-10000,10000,1,'Constant1' )

BetaTT = Beta('BetaTT',0.0162185,-10000,10000,0,'BetaTT' )

BetaCost = Beta('BetaCost',-0.0476396,-10000,10000,0,'BetaCost' )

Constant2 = Beta('Constant2',0.211433,-10000,10000,0,'Constant2' )


## Code for the sensitivity analysis
names = ['BetaCost','BetaTT','Constant2']
values = [[3.93422e-05,-6.48051e-06,0.000166115],[-6.48051e-06,1.70892e-06,-9.46533e-05],[0.000166115,-9.46533e-05,0.0111142]]
vc = bioMatrix(3,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
