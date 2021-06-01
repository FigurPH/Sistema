function callPython() {
    eel.sql()
}

function callHello(){
    eel.hello()
}

function goHome() {
    feedTela("home")
}

function goEstoque() {
    feedTela("estoque")
}

function goEntradas() {
    feedTela("entradas")
}

function feedTela(tela) {
    $(document).ready(function () {
        $(function () {
            $("#main_body").load("app/MVC/view/"+tela + ".html");
        });
    });
}
