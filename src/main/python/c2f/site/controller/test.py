## -*- coding: utf-8 -*-

import logging
from c2f.site import app, request, response, redirect
from c2f.site.model.produto_model import Produto 
from c2f.site.model.sessao_model import Sessao 
from c2f.site.utils import cookie

logger = logging.getLogger(__name__)


@app.route("/test/cookie")
def test_cookie():
    return cookie.get_cookie(name="jss")

@app.route("/test/set_cookie")
def test_set_cookie():
    cookie.set_cookie(name="jss", value="Teste de cookie")
    redirect("/test/cookie")

@app.route("/test/del_cookie")
def test_del_cookie():
    cookie.del_cookie(name="jss")
    redirect("/test/cookie")


@app.route("/mongoinsert")
def mongoinsert():
    sessao = Sessao()  
  
    ''''' Create - Grava os dados no banco '''  
    id  = "1"  
    nome = "Sessao nova"  
    sessao.gravarSessao(id, nome)  

@app.route("/mongolist")
def mongolist():
    sessao = Sessao()  
    
    sessoes = sessao.obterSessoes()  
    for item in sessoes:  
        logger.info(item)  



@app.route("/insert")
def insert():
    prod = Produto()  
  
    ''''' Create - Grava os dados no banco '''  
    produto_nome  = "Produto 1"  
    produto_preco = "2000.00"  
    if prod.gravarProduto( produto_nome, produto_preco ):  
        logger.info("Produto inserido com sucesso!")  
    else:  
        logger.info("Falha!")
    
@app.route("/list")
def lista():
    logger.info("lista:\n")
    prod = Produto()  
  
    ''''' Read - Rerorna todos os produtos '''  
    produtos = prod.obterProdutos()  
    for item in produtos:  
        logger.info("\nProduto")  
        logger.info("-------")  
        logger.info("Id: %s",    item["ID_PRODUTO"])  
        logger.info("Nome: %s",  item["NOME_PRODUTO"])  
        logger.info("PreÃ§o: %s", item["PRECO_PRODUTO"]) 
        
@app.route("/update")
def update():
    prod = Produto()  
  
    ''''' Update - Atualiza os dados '''  
    produto_id = 1  
    produto_nome  = 'Produto 1 - atualizado'  
    produto_preco = '1000.00'  
    if prod.atualizaProduto( produto_id, produto_nome, produto_preco ):  
        logger.info( "Produto atualizado com sucesso!" ) 
    else:  
        logger.info( "Falha na atualizaÃ§Ã£o!")

@app.route("/delete")
def delete():
    prod = Produto()  
  
    ''''' Delete - Deleta uma linha do banco '''  
    produto_id = 1  
    if prod.deletaProduto( produto_id ):  
        logger.info( "Produto excluÃ­do com sucesso!"  )
    else:  
       logger.info( "Falha ao exluir produto!"  )
    