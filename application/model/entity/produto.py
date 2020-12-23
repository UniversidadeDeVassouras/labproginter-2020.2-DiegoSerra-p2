class Produto:
    def __init__(self, id, nome, imagem, preco_antes, preco, descricao,parcela,valor_parcela):
        self._id = id
        self._nome = nome
        self._imagem = imagem
        self._preco_antes = preco_antes
        self._preco = preco
        self._descricao = descricao
        self._parcela = parcela
        self._valor_parcela = valor_parcela


    def get_nome(self):
        return self._nome

    def get_id(self):
        return self._id

    def get_imagem(self):
        return self._imagem

    def get_preco_antes(self):
        return self._preco_antes

    def get_preco(self):
        return self._preco

    def get_descricao(self):
        return self._descricao

    def get_parcela(self):
        return self._parcela

    def get_valor_parcela(self):
        return self._valor_parcela
    