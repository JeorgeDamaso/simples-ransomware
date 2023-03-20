
from cryptography.fernet import  Fernet
from os import walk, sep, path, rename

class encriptador:
    def __init__(self, caminho):
        self.caminho = caminho
        self.arquivos=[]
        self.desencriptar
        self.encriptar
        
        if path.isfile('/'.join([caminho,'senha.txt'])):
            print('já há um arquivo de senha e os arquivos já foram incriptados')
            self.lista_arquivos()
            self.desencriptar()
        else:
            self.lista_arquivos()
            self.encriptar()         
    
    def lista_arquivos(self):
        
        for caminho,_,arquivos in walk(self.caminho):
           for arquivo in arquivos:
               self.arquivos.append('/'.join([caminho, arquivo]))
        
        return self.lista_arquivos
    
    def encriptar(self):
        key = Fernet.generate_key()
        f = Fernet(key)
        for arquivo in self.arquivos:
            with open(arquivo, 'rb') as arq:
                arquivo_aberto = arq.read()
            
            with open(arquivo, 'wb') as arq2:
                arq2.write(f.encrypt(arquivo_aberto))
            print(f'{arquivo} foi encriptado')
            
            rename(arquivo, arquivo +'.ENCRIPTADO')
            
        with open(f'{self.caminho}/senha.txt', 'wb') as arq3:
            arq3.write(key)
             
    def desencriptar(self):
        with open(f'{self.caminho}/senha.txt', 'rb') as fd:
            chave = fd.read()
        f = Fernet(chave)        
        if f'{self.caminho}/senha.txt' in self.arquivos:
            self.arquivos.remove(f'{self.caminho}/senha.txt')
        else:
            pass
 
        for arquivo in self.arquivos:
            
            novo_nome = arquivo.removesuffix('.ENCRIPTADO')
            rename(arquivo, novo_nome)

            with open(novo_nome, 'rb') as arq:
                arquivo_aberto = arq.read()
            
            with open(novo_nome, 'wb') as arq2:
                arq2.write(f.decrypt(arquivo_aberto))
            print(novo_nome, 'foi desencriptado')
            
        
    
a = encriptador('/home/damaso/Downloads/linux-x64/ProjectIgnis/arquivos')
