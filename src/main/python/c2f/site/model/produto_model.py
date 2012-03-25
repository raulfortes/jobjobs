#!/usr/bin/env python
from c2f.site.model.mysql import MySQL

class Produto( MySQL ):

    '''
        Retorna uma lista de produtos
        @param void
        @return array
    '''
    def obterProdutos( self ):
        self.cursor.execute(
        "SELECT ID_PRODUTO,NOME_PRODUTO,PRECO_PRODUTO "+
        "FROM produtos" )
        return self.cursor.fetchall()

    '''
        Grava dados no banco
        @param produto_nome String
        @param produto_preco String
        @return bool
    '''
    def gravarProduto( self, nome,preco ):
        if self.cursor.execute(
        "INSERT INTO produtos(" +
            "`NOME_PRODUTO`," +
            "`PRECO_PRODUTO`" +
        ") VALUES (" +
            "'" + str(nome)  + "'," +
            "'" + str(preco) + "'"  +
        ")"):
            return True
        else:
            return False

    '''
        Atualiza um linha no banco
        @param produto_id Integer
        @param produto_nome String
        @param produto_preco String
        @return bool
    '''
    def atualizaProduto( self, id, nome, preco ):
        if self.cursor.execute(
            "UPDATE produtos SET " +
                "`NOME_PRODUTO`  = '"+ str(nome)  +"'," +
                "`PRECO_PRODUTO` = '"+ str(preco) +"' "  +
            "WHERE " +
                "`ID_PRODUTO` = " + str(id)
        ):
            return True
        else:
            return False

    '''
        Deleta uma linha do banco
        @param produto_id Integer
        @return bool
    '''
    def deletaProduto( self , id ):
        if self.cursor.execute(
            "DELETE FROM `produtos` "+
            "WHERE `ID_PRODUTO` = "+ str(id) ):
            return True
        else:
            return  False