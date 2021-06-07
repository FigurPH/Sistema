from www.app.MVC.controller.controllerDB import Run
from www.app.MVC.controller import controllerMain
from www.app.MVC.model import modelProduto

produto = modelProduto.Produto('', "7898959897184", "pó papa pé", "17.4", "meu pé tradicional", "outros", "6")

print(produto.dump())
sql = "insert into produtos(cod_barras, nome, preco, desc, cat, qtd) values('"+produto.barcode+"','"+produto.nome+"','"+produto.preco+"','"+produto.desc+"','"+produto.cat+"','"+produto.qtd+"')"
run = Run(sql)
run.testRun()
run.runQuery()
