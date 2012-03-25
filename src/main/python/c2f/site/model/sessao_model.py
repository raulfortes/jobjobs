#!/usr/bin/env python
from c2f.site.model.mongodb import MongoDB

class Sessao( MongoDB ):

    def obterSessoes( self ):
        mongo_collection = self.mongodb['sessao']
        return mongo_collection.find({})

    '''
        Grava dados no banco
        @param produto_nome String
        @param produto_preco String
        @return bool
    '''
    def gravarSessao( self, id, nome ):
        mongo_collection = self.mongodb['sessao']

        insert_id = mongo_collection.insert({
            'id': id,
            'nome': nome
        })
