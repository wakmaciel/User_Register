import sqlite3

class Conexao:
    def __init__(self):
        self.conexao = None
        self.dbPath = 'banco.db'

    def connect(self):
        try:
            self.conexao = sqlite3.connect(self.dbPath)

        except sqlite3.DatabaseError as err:
            print(f'Erro ao tentar conectar com o Banco de Dados! \nErro: {err}')

        return self.conexao

    def createTableClientes(self, conexao, cursor):
        #cursor.execute('DROP TABLE IF EXISTS Clientes')

        sql = """CREATE TABLE IF NOT EXISTS Clientes (
            idCliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nomeCliente varchar NOT NULL,
            sobrenomeCliente varchar,
            CPF varchar(14) NOT NULL,
            telefoneCliente varchar(14) NOT NULL, 
            enderecoCliente varchar NOT NULL, 
            emailCliente varchar NOT NULL
        );"""

        cursor.execute(sql)
        conexao.commit()
 
    def createTableProdutos(self, conexao, cursor):
        cursor.execute('DROP TABLE IF EXISTS Produtos')

        sql = """CREATE TABLE IF NOT EXISTS Produtos (
            idProduto INTEGER PRIMARY KEY AUTOINCREMENT,
            nomeProduto varchar NOT NULL,
            descricaoProduto varchar
        );"""
        cursor.execute(sql)
        conexao.commit()
    
    def createTableProblemas(self, conexao, cursor):
        cursor.execute('DROP TABLE IF EXISTS Problemas')

        sql = """CREATE TABLE IF NOT EXISTS Problemas (
            idProblema INTEGER PRIMARY KEY AUTOINCREMENT,
            descricaoProblema varchar NOT NULL
        );"""
        cursor.execute(sql)
        conexao.commit()

    def createTableIncidentes(self, conexao, cursor):
        cursor.execute('DROP TABLE IF EXISTS Incidentes')

        sql = """CREATE TABLE IF NOT EXISTS Incidentes (
            idIncidente INTEGER PRIMARY KEY AUTOINCREMENT,
            fk_idCliente INTEGER NOT NULL,
            fk_idProduto INTEGER NOT NULL,
            descricaoIncidente varchar NOT NULL, 
            dataAberturaIncidente date NOT NULL,
            statusIncidente boolean NOT NULL,
            descricaoResolucao varchar,
            FOREIGN KEY (fk_idCliente) REFERENCES Clientes(idCliente)
            FOREIGN KEY (fk_idProduto) REFERENCES Produtos(idProduto)
        );"""
        cursor.execute(sql)
        conexao.commit()

    def createTableIncidentesProblemas(self, conexao, cursor):
        cursor.execute('DROP TABLE IF EXISTS IncidentesProblemas')

        sql = """CREATE TABLE IF NOT EXISTS IncidentesProblemas (
            fk_idIncidente INTEGER,
            fk_idProblema INTEGER,
            PRIMARY KEY (fk_idIncidente, fk_idProblema),
            FOREIGN KEY (fk_idIncidente) REFERENCES Incidentes(idIncidente),
            FOREIGN KEY (fk_idProblema) REFERENCES Problemas(idProblema)
        );"""
        cursor.execute(sql)
        conexao.commit()


    def createTables(self):
        conexao = self.connect()
        cursor = conexao.cursor()
        self.createTableClientes(conexao, cursor)
        self.createTableProdutos(conexao,cursor)
        self.createTableProblemas(conexao, cursor)
        self.createTableIncidentes(conexao, cursor)
        self.createTableIncidentesProblemas(conexao, cursor)


banco = Conexao()
banco.createTables()