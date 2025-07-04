import os
#1 retornar pasta atual
print(os.getcwd())

#listar arquivos e pastas
print(os.listdir())

## versao do sistema operacional
os.system('ver')

#configuraçoes da maquina
os.system('systeminfo')

#limpar a tela do terminal
os.system('cls')

#desligar o computador
#os.system('shutdown /s /t 1')
#os.system('shutdown /a) #cancelar o desligamento

#funçao desligar em uma hora
def tunoff_in_one_hour():
    os.system('shutdown /s /t 3600')

def cancel_shutdown():
    os.system('shutdown /a')


cancel_shutdown()
