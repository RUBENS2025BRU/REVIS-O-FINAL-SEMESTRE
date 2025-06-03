def test_aceitacao_fluxo_completo():
    assert cadastrar_usuario("gustavo", "gustavoguilher@gmail.com, "guilher") == "Usuário cadastrado com sucesso!"
    assert login_usuario("gustavoguilher@gmail.com, "guilher"") == "Login bem-sucedido"
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("CadeiraGamer")
    assert carrinho.finalizar_compra() == "Compra finalizada com sucesso!"
    print("Teste de aceitação do fluxo completo passou!")

test_aceitacao_fluxo_completo()

Saida: Teste de aceitação do fluxo completo passou
