# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:20:42 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  2 16:04:09 2017</p>
#
Constant1 = Beta('Constant1',0,-10000,10000,1,'Constant1' )

BetaTT = Beta('BetaTT',0.0262464,-10000,10000,0,'BetaTT' )

BetaCost = Beta('BetaCost',-0.0526483,-10000,10000,0,'BetaCost' )

Constant2 = Beta('Constant2',0.333424,-10000,10000,0,'Constant2' )


## Code for the sensitivity analysis
names = ['BetaCost','BetaTT','Constant2']
values = [[4.67085e-05,-1.05273e-05,7.76149e-05],[-1.05273e-05,4.55402e-06,-0.000151769],[7.76149e-05,-0.000151769,0.0117164]]
vc = bioMatrix(3,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
