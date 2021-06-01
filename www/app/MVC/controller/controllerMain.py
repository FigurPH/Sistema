#   IMPORTS ESSENCIAIS
import eel
#######################

#   IMPORTS DESTE SISTEMA
from www.app.MVC.controller import controllerDB
from www.app.MVC.controller import controllerEstoque
#########################

@eel.expose
def hello():
    print("Hello World")
