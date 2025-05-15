from model.model import Model

mymodel = Model()

mymodel.buildGraph()
print("Num nodi: ", mymodel.getNumNodes(), "; Num Edges: ", mymodel.getNumEdges())

mymodel.getInfoConnessa(1234)