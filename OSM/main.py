from connection import local, nome, senha, banco
from dados_adm import Usuario_adm, Senha_adm
from dados_email import imail, senha_email
from datetime import datetime
import email.message
import mysql.connector
from mysql.connector import Error
from PySimpleGUI import PySimpleGUI as sg
import smtplib
import time
host_name = local
user_name = nome
user_password = senha
db_name = banco


def enviar_email():
    msg = email.message.Message()
    msg['Subject'] = str(Assunto)
    msg['From'] = imail
    msg['To'] = str(To)
    password = senha_email
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(str(corpo_email))
    s = smtplib.SMTP_SSL('mail.frigorificozimmer.com.br', 465)
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name)
    except Error as err:
        print(f"Error: '{err}'")
    return connection


connection = create_server_connection(host_name, user_name, user_password, db_name)  # Connect to the Database
area = ["SEGURANÇA", "MEIO AMBIENTE", "MANUTENÇÃO", "QUALIDADE", "ELETRICIDADE", "PROJETO", "OBRA CIVIL", "MELHORIA",
        "OUTROS"]
setor = ["QUALIDADE", "MANUTENÇÃO", "GERENCIA", "MANUTENÇÃO PREDIAL", "SESMT", "ABATE", "DESOSSA", "CARREGAMENTO",
         "MIUDOS", "TRIPARIA", "BUCHARIA", "PCP", "ADMINISTRATIVO", "ETA", "CURRAIS", "CAIXARIA", "FATURAMENTO",
         "BUCHARIA", "CALDEIRA", "TRIPARIA"]
permissao = ["C", "E"]
email_criar = ["pcp@frigorificozimmer.com.br","pcp2@frigorificozimmer.com.br","industria@frigorificozimmer.com.br","qualidade@frigorificozimmer.com.br","osm@frigorificozimmer.com.br","binotto@frigorificozimmer.com.br","manutencao1@frigorificozimmer.com.br","seguranca1@frigorificozimmer.com.br","neto@frigorificozimmer.com.br"]


# layout
def janela_config():  # 1
    sg.theme('Reddit')
    layout = [

        [sg.Text('      Server  '), sg.Input('192.168.114.199', key='server_config', size=(20, 1))],
        [sg.Text('      Banco  '), sg.Input('osm', key='banco_config', size=(20, 1))],
        [sg.Text('      Usuario'), sg.Input('jona', key='usuario_config', size=(20, 1))],
        [sg.Text('      Senha  '), sg.Input('passpass', key='senha_config', password_char='*', size=(20, 1))],
        [sg.Text('                                                                            ')],
        [sg.Text('                                                                            ')],
        [sg.Button('Ok', key='ok_config'), sg.Button('Voltar', key='voltar_config'),
         sg.Text('', key='mensagem_config')],
        [sg.Text('                                                                            ')],
    ]
    return sg.Window('Configurações', layout=layout, finalize=True)


def janela_login():  # 1
    sg.theme('Reddit')
    layout = [
        [sg.Text('Usuario'), sg.Input(key='usuario', size=(30, 1)), sg.Button('⚙️', key='config')],
        [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(20, 1))],
        [sg.Button('Entrar'), sg.Text('', key='mensagem1')],
        [sg.Button('Fechar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)


def janela_cancelamento():  # 12
    sg.theme('Default1')
    layout = [
        [sg.Text('Motivo do cancelamento:'), sg.Input(key='input_cancelamento', size=(120, 1)),
         sg.Button('Ok', key='ok_cancelar')],
        [sg.Button('Fechar', key='fechar_cancelamento'), sg.Text('', key='mensagem_motivo_cancelamento')]
    ]
    return sg.Window('Motivo do cancelamento', layout=layout, finalize=True)


def janela_sobre():  # 11
    sg.theme('Default1')
    layout = [
        [sg.Text('Data do executavel: 14/10/2022')],
        [sg.Text('Versão do  Aplicativo: Beta 1.0')],
        [sg.Text('Copyright © Jonathan Borges Ferreira')],
        [sg.Button('Voltar', key='voltar_sobre'), sg.Button('Fechar')],
    ]
    return sg.Window('Sobre', layout=layout, finalize=True)


def janela_osm_aberto():  # 9
    sg.theme('Default1')
    layout = [
        [sg.ProgressBar(100, size=(75, 1), key='barra_de_status', bar_color=('Green', 'White'), border_width=8),
         sg.Button('Carregar', key='carregar_osm_aberto'), sg.Button('Voltar', key='voltar_osm_aberto')],
        [sg.Text('Ordem', background_color='white'), sg.Text('          Area           ', background_color='white'),
         sg.Text('Data Solicitação ', background_color='white'), sg.Text('Data inicio      ', background_color='white'),
         sg.Text('Situação', background_color='white'), sg.Text('Prazo  ', background_color='white'),
         sg.Text('Descrição                                             ', background_color='white'),
         sg.Text('Usuario criador ', background_color='white'), sg.Text('Data Limite ', background_color='white')],
        [sg.Text('', key='Ordem0', size=(5, 1)), sg.Text('', key='Area0', size=(14, 1)),
         sg.Text('', key='Data Solicitação0', size=(12, 1)), sg.Text('', key='Data inicio0', size=(11, 1)),
         sg.Text('', key='Situação0', size=(6, 1)), sg.Text('', key='Prazo0', size=(5, 1)),
         sg.Text('', key='Descrição0', size=(30, 1)), sg.Text('', key='Usuario criador0', size=(11, 1)),
         sg.Text('', key='Data Limite0', size=(9, 1))],
        [sg.Text('', key='Ordem1', size=(5, 1)), sg.Text('', key='Area1', size=(14, 1)),
         sg.Text('', key='Data Solicitação1', size=(12, 1)), sg.Text('', key='Data inicio1', size=(11, 1)),
         sg.Text('', key='Situação1', size=(6, 1)), sg.Text('', key='Prazo1', size=(5, 1)),
         sg.Text('', key='Descrição1', size=(30, 1)), sg.Text('', key='Usuario criador1', size=(11, 1)),
         sg.Text('', key='Data Limite1', size=(9, 1))],
        [sg.Text('', key='Ordem2', size=(5, 1)), sg.Text('', key='Area2', size=(14, 1)),
         sg.Text('', key='Data Solicitação2', size=(12, 1)), sg.Text('', key='Data inicio2', size=(11, 1)),
         sg.Text('', key='Situação2', size=(6, 1)), sg.Text('', key='Prazo2', size=(5, 1)),
         sg.Text('', key='Descrição2', size=(30, 1)), sg.Text('', key='Usuario criador2', size=(11, 1)),
         sg.Text('', key='Data Limite2', size=(9, 1))],
        [sg.Text('', key='Ordem3', size=(5, 1)), sg.Text('', key='Area3', size=(14, 1)),
         sg.Text('', key='Data Solicitação3', size=(12, 1)), sg.Text('', key='Data inicio3', size=(11, 1)),
         sg.Text('', key='Situação3', size=(6, 1)), sg.Text('', key='Prazo3', size=(5, 1)),
         sg.Text('', key='Descrição3', size=(30, 1)), sg.Text('', key='Usuario criador3', size=(11, 1)),
         sg.Text('', key='Data Limite3', size=(9, 1))],
        [sg.Text('', key='Ordem4', size=(5, 1)), sg.Text('', key='Area4', size=(14, 1)),
         sg.Text('', key='Data Solicitação4', size=(12, 1)), sg.Text('', key='Data inicio4', size=(11, 1)),
         sg.Text('', key='Situação4', size=(6, 1)), sg.Text('', key='Prazo4', size=(5, 1)),
         sg.Text('', key='Descrição4', size=(30, 1)), sg.Text('', key='Usuario criador4', size=(11, 1)),
         sg.Text('', key='Data Limite4', size=(9, 1))],
        [sg.Text('', key='Ordem5', size=(5, 1)), sg.Text('', key='Area5', size=(14, 1)),
         sg.Text('', key='Data Solicitação5', size=(12, 1)), sg.Text('', key='Data inicio5', size=(11, 1)),
         sg.Text('', key='Situação5', size=(6, 1)), sg.Text('', key='Prazo5', size=(5, 1)),
         sg.Text('', key='Descrição5', size=(30, 1)), sg.Text('', key='Usuario criador5', size=(11, 1)),
         sg.Text('', key='Data Limite5', size=(9, 1))],
        [sg.Text('', key='Ordem6', size=(5, 1)), sg.Text('', key='Area6', size=(14, 1)),
         sg.Text('', key='Data Solicitação6', size=(12, 1)), sg.Text('', key='Data inicio6', size=(11, 1)),
         sg.Text('', key='Situação6', size=(6, 1)), sg.Text('', key='Prazo6', size=(5, 1)),
         sg.Text('', key='Descrição6', size=(30, 1)), sg.Text('', key='Usuario criador6', size=(11, 1)),
         sg.Text('', key='Data Limite6', size=(9, 1))],
        [sg.Text('', key='Ordem7', size=(5, 1)), sg.Text('', key='Area7', size=(14, 1)),
         sg.Text('', key='Data Solicitação7', size=(12, 1)), sg.Text('', key='Data inicio7', size=(11, 1)),
         sg.Text('', key='Situação7', size=(6, 1)), sg.Text('', key='Prazo7', size=(5, 1)),
         sg.Text('', key='Descrição7', size=(30, 1)), sg.Text('', key='Usuario criador7', size=(11, 1)),
         sg.Text('', key='Data Limite7', size=(9, 1))],
        [sg.Text('', key='Ordem8', size=(5, 1)), sg.Text('', key='Area8', size=(14, 1)),
         sg.Text('', key='Data Solicitação8', size=(12, 1)), sg.Text('', key='Data inicio8', size=(11, 1)),
         sg.Text('', key='Situação8', size=(6, 1)), sg.Text('', key='Prazo8', size=(5, 1)),
         sg.Text('', key='Descrição8', size=(30, 1)), sg.Text('', key='Usuario criador8', size=(11, 1)),
         sg.Text('', key='Data Limite8', size=(9, 1))],
        [sg.Text('', key='Ordem9', size=(5, 1)), sg.Text('', key='Area9', size=(14, 1)),
         sg.Text('', key='Data Solicitação9', size=(12, 1)), sg.Text('', key='Data inicio9', size=(11, 1)),
         sg.Text('', key='Situação9', size=(6, 1)), sg.Text('', key='Prazo9', size=(5, 1)),
         sg.Text('', key='Descrição9', size=(30, 1)), sg.Text('', key='Usuario criador9', size=(11, 1)),
         sg.Text('', key='Data Limite9', size=(9, 1))],
        [sg.Text('', key='Ordem10', size=(5, 1)), sg.Text('', key='Area10', size=(14, 1)),
         sg.Text('', key='Data Solicitação10', size=(12, 1)), sg.Text('', key='Data inicio10', size=(11, 1)),
         sg.Text('', key='Situação10', size=(6, 1)), sg.Text('', key='Prazo10', size=(5, 1)),
         sg.Text('', key='Descrição10', size=(30, 1)), sg.Text('', key='Usuario criador10', size=(11, 1)),
         sg.Text('', key='Data Limite10', size=(9, 1))],
        [sg.Text('', key='Ordem11', size=(5, 1)), sg.Text('', key='Area11', size=(14, 1)),
         sg.Text('', key='Data Solicitação11', size=(12, 1)), sg.Text('', key='Data inicio11', size=(11, 1)),
         sg.Text('', key='Situação11', size=(6, 1)), sg.Text('', key='Prazo11', size=(5, 1)),
         sg.Text('', key='Descrição11', size=(30, 1)), sg.Text('', key='Usuario criador11', size=(11, 1)),
         sg.Text('', key='Data Limite11', size=(9, 1))],
        [sg.Text('', key='Ordem12', size=(5, 1)), sg.Text('', key='Area12', size=(14, 1)),
         sg.Text('', key='Data Solicitação12', size=(12, 1)), sg.Text('', key='Data inicio12', size=(11, 1)),
         sg.Text('', key='Situação12', size=(6, 1)), sg.Text('', key='Prazo12', size=(5, 1)),
         sg.Text('', key='Descrição12', size=(30, 1)), sg.Text('', key='Usuario criador12', size=(11, 1)),
         sg.Text('', key='Data Limite12', size=(9, 1))],
        [sg.Text('', key='Ordem13', size=(5, 1)), sg.Text('', key='Area13', size=(14, 1)),
         sg.Text('', key='Data Solicitação13', size=(12, 1)), sg.Text('', key='Data inicio13', size=(11, 1)),
         sg.Text('', key='Situação13', size=(6, 1)), sg.Text('', key='Prazo13', size=(5, 1)),
         sg.Text('', key='Descrição13', size=(30, 1)), sg.Text('', key='Usuario criador13', size=(11, 1)),
         sg.Text('', key='Data Limite13', size=(9, 1))],
        [sg.Text('', key='Ordem14', size=(5, 1)), sg.Text('', key='Area14', size=(14, 1)),
         sg.Text('', key='Data Solicitação14', size=(12, 1)), sg.Text('', key='Data inicio14', size=(11, 1)),
         sg.Text('', key='Situação14', size=(6, 1)), sg.Text('', key='Prazo14', size=(5, 1)),
         sg.Text('', key='Descrição14', size=(30, 1)), sg.Text('', key='Usuario criador14', size=(11, 1)),
         sg.Text('', key='Data Limite14', size=(9, 1))],
        [sg.Text('', key='Ordem15', size=(5, 1)), sg.Text('', key='Area15', size=(14, 1)),
         sg.Text('', key='Data Solicitação15', size=(12, 1)), sg.Text('', key='Data inicio15', size=(11, 1)),
         sg.Text('', key='Situação15', size=(6, 1)), sg.Text('', key='Prazo15', size=(5, 1)),
         sg.Text('', key='Descrição15', size=(30, 1)), sg.Text('', key='Usuario criador15', size=(11, 1)),
         sg.Text('', key='Data Limite15', size=(9, 1))],
        [sg.Text('', key='Ordem16', size=(5, 1)), sg.Text('', key='Area16', size=(14, 1)),
         sg.Text('', key='Data Solicitação16', size=(12, 1)), sg.Text('', key='Data inicio16', size=(11, 1)),
         sg.Text('', key='Situação16', size=(6, 1)), sg.Text('', key='Prazo16', size=(5, 1)),
         sg.Text('', key='Descrição16', size=(30, 1)), sg.Text('', key='Usuario criador16', size=(11, 1)),
         sg.Text('', key='Data Limite16', size=(9, 1))],
        [sg.Text('', key='Ordem17', size=(5, 1)), sg.Text('', key='Area17', size=(14, 1)),
         sg.Text('', key='Data Solicitação17', size=(12, 1)), sg.Text('', key='Data inicio17', size=(11, 1)),
         sg.Text('', key='Situação17', size=(6, 1)), sg.Text('', key='Prazo17', size=(5, 1)),
         sg.Text('', key='Descrição17', size=(30, 1)), sg.Text('', key='Usuario criador17', size=(11, 1)),
         sg.Text('', key='Data Limite17', size=(9, 1))],
        [sg.Text('', key='Ordem18', size=(5, 1)), sg.Text('', key='Area18', size=(14, 1)),
         sg.Text('', key='Data Solicitação18', size=(12, 1)), sg.Text('', key='Data inicio18', size=(11, 1)),
         sg.Text('', key='Situação18', size=(6, 1)), sg.Text('', key='Prazo18', size=(5, 1)),
         sg.Text('', key='Descrição18', size=(30, 1)), sg.Text('', key='Usuario criador18', size=(11, 1)),
         sg.Text('', key='Data Limite18', size=(9, 1))],
        [sg.Text('', key='Ordem19', size=(5, 1)), sg.Text('', key='Area19', size=(14, 1)),
         sg.Text('', key='Data Solicitação19', size=(12, 1)), sg.Text('', key='Data inicio19', size=(11, 1)),
         sg.Text('', key='Situação19', size=(6, 1)), sg.Text('', key='Prazo19', size=(5, 1)),
         sg.Text('', key='Descrição19', size=(30, 1)), sg.Text('', key='Usuario criador19', size=(11, 1)),
         sg.Text('', key='Data Limite19', size=(9, 1))],
        [sg.Text('', key='Ordem20', size=(5, 1)), sg.Text('', key='Area20', size=(14, 1)),
         sg.Text('', key='Data Solicitação20', size=(12, 1)), sg.Text('', key='Data inicio20', size=(11, 1)),
         sg.Text('', key='Situação20', size=(6, 1)), sg.Text('', key='Prazo20', size=(5, 1)),
         sg.Text('', key='Descrição20', size=(30, 1)), sg.Text('', key='Usuario criador20', size=(11, 1)),
         sg.Text('', key='Data Limite20', size=(9, 1))],
        [sg.Text('', key='Ordem21', size=(5, 1)), sg.Text('', key='Area21', size=(14, 1)),
         sg.Text('', key='Data Solicitação21', size=(12, 1)), sg.Text('', key='Data inicio21', size=(11, 1)),
         sg.Text('', key='Situação21', size=(6, 1)), sg.Text('', key='Prazo21', size=(5, 1)),
         sg.Text('', key='Descrição21', size=(30, 1)), sg.Text('', key='Usuario criador21', size=(11, 1)),
         sg.Text('', key='Data Limite21', size=(9, 1))],
        [sg.Text('', key='Ordem22', size=(5, 1)), sg.Text('', key='Area22', size=(14, 1)),
         sg.Text('', key='Data Solicitação22', size=(12, 1)), sg.Text('', key='Data inicio22', size=(11, 1)),
         sg.Text('', key='Situação22', size=(6, 1)), sg.Text('', key='Prazo22', size=(5, 1)),
         sg.Text('', key='Descrição22', size=(30, 1)), sg.Text('', key='Usuario criador22', size=(11, 1)),
         sg.Text('', key='Data Limite22', size=(9, 1))],
        [sg.Text('', key='Ordem23', size=(5, 1)), sg.Text('', key='Area23', size=(14, 1)),
         sg.Text('', key='Data Solicitação23', size=(12, 1)), sg.Text('', key='Data inicio23', size=(11, 1)),
         sg.Text('', key='Situação23', size=(6, 1)), sg.Text('', key='Prazo23', size=(5, 1)),
         sg.Text('', key='Descrição23', size=(30, 1)), sg.Text('', key='Usuario criador23', size=(11, 1)),
         sg.Text('', key='Data Limite23', size=(9, 1))],
        [sg.Text('', key='Ordem24', size=(5, 1)), sg.Text('', key='Area24', size=(14, 1)),
         sg.Text('', key='Data Solicitação24', size=(12, 1)), sg.Text('', key='Data inicio24', size=(11, 1)),
         sg.Text('', key='Situação24', size=(6, 1)), sg.Text('', key='Prazo24', size=(5, 1)),
         sg.Text('', key='Descrição24', size=(30, 1)), sg.Text('', key='Usuario criador24', size=(11, 1)),
         sg.Text('', key='Data Limite24', size=(9, 1))],
        [sg.Text('', key='Ordem25', size=(5, 1)), sg.Text('', key='Area25', size=(14, 1)),
         sg.Text('', key='Data Solicitação25', size=(12, 1)), sg.Text('', key='Data inicio25', size=(11, 1)),
         sg.Text('', key='Situação25', size=(6, 1)), sg.Text('', key='Prazo25', size=(5, 1)),
         sg.Text('', key='Descrição25', size=(30, 1)), sg.Text('', key='Usuario criador25', size=(11, 1)),
         sg.Text('', key='Data Limite25', size=(9, 1))],
        [sg.Text('', key='Ordem26', size=(5, 1)), sg.Text('', key='Area26', size=(14, 1)),
         sg.Text('', key='Data Solicitação26', size=(12, 1)), sg.Text('', key='Data inicio26', size=(11, 1)),
         sg.Text('', key='Situação26', size=(6, 1)), sg.Text('', key='Prazo26', size=(5, 1)),
         sg.Text('', key='Descrição26', size=(30, 1)), sg.Text('', key='Usuario criador26', size=(11, 1)),
         sg.Text('', key='Data Limite26', size=(9, 1))],
        [sg.Text('', key='Ordem27', size=(5, 1)), sg.Text('', key='Area27', size=(14, 1)),
         sg.Text('', key='Data Solicitação27', size=(12, 1)), sg.Text('', key='Data inicio27', size=(11, 1)),
         sg.Text('', key='Situação27', size=(6, 1)), sg.Text('', key='Prazo27', size=(5, 1)),
         sg.Text('', key='Descrição27', size=(30, 1)), sg.Text('', key='Usuario criador27', size=(11, 1)),
         sg.Text('', key='Data Limite27', size=(9, 1))],
        [sg.Text('', key='Ordem28', size=(5, 1)), sg.Text('', key='Area28', size=(14, 1)),
         sg.Text('', key='Data Solicitação28', size=(12, 1)), sg.Text('', key='Data inicio28', size=(11, 1)),
         sg.Text('', key='Situação28', size=(6, 1)), sg.Text('', key='Prazo28', size=(5, 1)),
         sg.Text('', key='Descrição28', size=(30, 1)), sg.Text('', key='Usuario criador28', size=(11, 1)),
         sg.Text('', key='Data Limite28', size=(9, 1))],
        [sg.Text('', key='Ordem29', size=(5, 1)), sg.Text('', key='Area29', size=(14, 1)),
         sg.Text('', key='Data Solicitação29', size=(12, 1)), sg.Text('', key='Data inicio29', size=(11, 1)),
         sg.Text('', key='Situação29', size=(6, 1)), sg.Text('', key='Prazo29', size=(5, 1)),
         sg.Text('', key='Descrição29', size=(30, 1)), sg.Text('', key='Usuario criador29', size=(11, 1)),
         sg.Text('', key='Data Limite29', size=(9, 1))],
        [sg.Text('', key='Ordem30', size=(5, 1)), sg.Text('', key='Area30', size=(14, 1)),
         sg.Text('', key='Data Solicitação30', size=(12, 1)), sg.Text('', key='Data inicio30', size=(11, 1)),
         sg.Text('', key='Situação30', size=(6, 1)), sg.Text('', key='Prazo30', size=(5, 1)),
         sg.Text('', key='Descrição30', size=(30, 1)), sg.Text('', key='Usuario criador30', size=(11, 1)),
         sg.Text('', key='Data Limite30', size=(9, 1))],
        [sg.Button('Fechar')],
    ]
    return sg.Window("OSM's em Aberto", layout=layout, finalize=True, size=(1000, 750))


def janela_osm_atrasadas():  # 9
    sg.theme('Default1')
    layout = [
        [sg.ProgressBar(100, size=(100, 1), key='barra_de_atraso', bar_color=('Green', 'White'), border_width=8),
         sg.Button('Carregar', key='carregar_osm_atrasadas'), sg.Text('', key='mensagem_atraso')],
        [sg.Text('Ordem', background_color='white'), sg.Text('          Area           ', background_color='white'),
         sg.Text('Data Solicitação ', background_color='white'), sg.Text('Data inicio      ', background_color='white'),
         sg.Text('Data Conclusão ', background_color='white'), sg.Text('Situação', background_color='white'),
         sg.Text('Data Cancelamento ', background_color='white'), sg.Text('Prazo  ', background_color='white'),
         sg.Text('Descrição                                             ', background_color='white'),
         sg.Text('Usuario criador ', background_color='white'), sg.Text('Data Limite ', background_color='white'),
         sg.Text('Usuario Cancelamento ', background_color='white'),
         sg.Text('Conclusão                     ', background_color='white'),
         sg.Text('Descrição Cancelamento', background_color='white')],
        [sg.Text('', key='Ordem0', size=(5, 1)), sg.Text('', key='Area0', size=(14, 1)),
         sg.Text('', key='Data Solicitação0', size=(12, 1)), sg.Text('', key='Data inicio0', size=(11, 1)),
         sg.Text('', key='Data Conclusão0', size=(12, 1)), sg.Text('', key='Situação0', size=(6, 1)),
         sg.Text('', key='Data Cancelamento0', size=(15, 1)), sg.Text('', key='Prazo0', size=(5, 1)),
         sg.Text('', key='Descrição0', size=(30, 1)), sg.Text('', key='Usuario criador0', size=(11, 1)),
         sg.Text('', key='Data Limite0', size=(9, 1)), sg.Text('', key='Usuario Cancelamento0', size=(17, 1)),
         sg.Text('', key='Conclusão0', size=(18, 1)), sg.Text('', key='Descrição Cancelamento0', size=(18, 1))],
        [sg.Text('', key='Ordem1', size=(5, 1)), sg.Text('', key='Area1', size=(14, 1)),
         sg.Text('', key='Data Solicitação1', size=(12, 1)), sg.Text('', key='Data inicio1', size=(11, 1)),
         sg.Text('', key='Data Conclusão1', size=(12, 1)), sg.Text('', key='Situação1', size=(6, 1)),
         sg.Text('', key='Data Cancelamento1', size=(15, 1)), sg.Text('', key='Prazo1', size=(5, 1)),
         sg.Text('', key='Descrição1', size=(30, 1)), sg.Text('', key='Usuario criador1', size=(11, 1)),
         sg.Text('', key='Data Limite1', size=(9, 1)), sg.Text('', key='Usuario Cancelamento1', size=(17, 1)),
         sg.Text('', key='Conclusão1', size=(18, 1)), sg.Text('', key='Descrição Cancelamento1', size=(18, 1))],
        [sg.Text('', key='Ordem2', size=(5, 1)), sg.Text('', key='Area2', size=(14, 1)),
         sg.Text('', key='Data Solicitação2', size=(12, 1)), sg.Text('', key='Data inicio2', size=(11, 1)),
         sg.Text('', key='Data Conclusão2', size=(12, 1)), sg.Text('', key='Situação2', size=(6, 1)),
         sg.Text('', key='Data Cancelamento2', size=(15, 1)), sg.Text('', key='Prazo2', size=(5, 1)),
         sg.Text('', key='Descrição2', size=(30, 1)), sg.Text('', key='Usuario criador2', size=(11, 1)),
         sg.Text('', key='Data Limite2', size=(9, 1)), sg.Text('', key='Usuario Cancelamento2', size=(17, 1)),
         sg.Text('', key='Conclusão2', size=(18, 1)), sg.Text('', key='Descrição Cancelamento2', size=(18, 1))],
        [sg.Text('', key='Ordem3', size=(5, 1)), sg.Text('', key='Area3', size=(14, 1)),
         sg.Text('', key='Data Solicitação3', size=(12, 1)), sg.Text('', key='Data inicio3', size=(11, 1)),
         sg.Text('', key='Data Conclusão3', size=(12, 1)), sg.Text('', key='Situação3', size=(6, 1)),
         sg.Text('', key='Data Cancelamento3', size=(15, 1)), sg.Text('', key='Prazo3', size=(5, 1)),
         sg.Text('', key='Descrição3', size=(30, 1)), sg.Text('', key='Usuario criador3', size=(11, 1)),
         sg.Text('', key='Data Limite3', size=(9, 1)), sg.Text('', key='Usuario Cancelamento3', size=(17, 1)),
         sg.Text('', key='Conclusão3', size=(18, 1)), sg.Text('', key='Descrição Cancelamento3', size=(18, 1))],
        [sg.Text('', key='Ordem4', size=(5, 1)), sg.Text('', key='Area4', size=(14, 1)),
         sg.Text('', key='Data Solicitação4', size=(12, 1)), sg.Text('', key='Data inicio4', size=(11, 1)),
         sg.Text('', key='Data Conclusão4', size=(12, 1)), sg.Text('', key='Situação4', size=(6, 1)),
         sg.Text('', key='Data Cancelamento4', size=(15, 1)), sg.Text('', key='Prazo4', size=(5, 1)),
         sg.Text('', key='Descrição4', size=(30, 1)), sg.Text('', key='Usuario criador4', size=(11, 1)),
         sg.Text('', key='Data Limite4', size=(9, 1)), sg.Text('', key='Usuario Cancelamento4', size=(17, 1)),
         sg.Text('', key='Conclusão4', size=(18, 1)), sg.Text('', key='Descrição Cancelamento4', size=(18, 1))],
        [sg.Text('', key='Ordem5', size=(5, 1)), sg.Text('', key='Area5', size=(14, 1)),
         sg.Text('', key='Data Solicitação5', size=(12, 1)), sg.Text('', key='Data inicio5', size=(11, 1)),
         sg.Text('', key='Data Conclusão5', size=(12, 1)), sg.Text('', key='Situação5', size=(6, 1)),
         sg.Text('', key='Data Cancelamento5', size=(15, 1)), sg.Text('', key='Prazo5', size=(5, 1)),
         sg.Text('', key='Descrição5', size=(30, 1)), sg.Text('', key='Usuario criador5', size=(11, 1)),
         sg.Text('', key='Data Limite5', size=(9, 1)), sg.Text('', key='Usuario Cancelamento5', size=(17, 1)),
         sg.Text('', key='Conclusão5', size=(18, 1)), sg.Text('', key='Descrição Cancelamento5', size=(18, 1))],
        [sg.Text('', key='Ordem6', size=(5, 1)), sg.Text('', key='Area6', size=(14, 1)),
         sg.Text('', key='Data Solicitação6', size=(12, 1)), sg.Text('', key='Data inicio6', size=(11, 1)),
         sg.Text('', key='Data Conclusão6', size=(12, 1)), sg.Text('', key='Situação6', size=(6, 1)),
         sg.Text('', key='Data Cancelamento6', size=(15, 1)), sg.Text('', key='Prazo6', size=(5, 1)),
         sg.Text('', key='Descrição6', size=(30, 1)), sg.Text('', key='Usuario criador6', size=(11, 1)),
         sg.Text('', key='Data Limite6', size=(9, 1)), sg.Text('', key='Usuario Cancelamento6', size=(17, 1)),
         sg.Text('', key='Conclusão6', size=(18, 1)), sg.Text('', key='Descrição Cancelamento6', size=(18, 1))],
        [sg.Text('', key='Ordem7', size=(5, 1)), sg.Text('', key='Area7', size=(14, 1)),
         sg.Text('', key='Data Solicitação7', size=(12, 1)), sg.Text('', key='Data inicio7', size=(11, 1)),
         sg.Text('', key='Data Conclusão7', size=(12, 1)), sg.Text('', key='Situação7', size=(6, 1)),
         sg.Text('', key='Data Cancelamento7', size=(15, 1)), sg.Text('', key='Prazo7', size=(5, 1)),
         sg.Text('', key='Descrição7', size=(30, 1)), sg.Text('', key='Usuario criador7', size=(11, 1)),
         sg.Text('', key='Data Limite7', size=(9, 1)), sg.Text('', key='Usuario Cancelamento7', size=(17, 1)),
         sg.Text('', key='Conclusão7', size=(18, 1)), sg.Text('', key='Descrição Cancelamento7', size=(18, 1))],
        [sg.Text('', key='Ordem8', size=(5, 1)), sg.Text('', key='Area8', size=(14, 1)),
         sg.Text('', key='Data Solicitação8', size=(12, 1)), sg.Text('', key='Data inicio8', size=(11, 1)),
         sg.Text('', key='Data Conclusão8', size=(12, 1)), sg.Text('', key='Situação8', size=(6, 1)),
         sg.Text('', key='Data Cancelamento8', size=(15, 1)), sg.Text('', key='Prazo8', size=(5, 1)),
         sg.Text('', key='Descrição8', size=(30, 1)), sg.Text('', key='Usuario criador8', size=(11, 1)),
         sg.Text('', key='Data Limite8', size=(9, 1)), sg.Text('', key='Usuario Cancelamento8', size=(17, 1)),
         sg.Text('', key='Conclusão8', size=(18, 1)), sg.Text('', key='Descrição Cancelamento8', size=(18, 1))],
        [sg.Text('', key='Ordem9', size=(5, 1)), sg.Text('', key='Area9', size=(14, 1)),
         sg.Text('', key='Data Solicitação9', size=(12, 1)), sg.Text('', key='Data inicio9', size=(11, 1)),
         sg.Text('', key='Data Conclusão9', size=(12, 1)), sg.Text('', key='Situação9', size=(6, 1)),
         sg.Text('', key='Data Cancelamento9', size=(15, 1)), sg.Text('', key='Prazo9', size=(5, 1)),
         sg.Text('', key='Descrição9', size=(30, 1)), sg.Text('', key='Usuario criador9', size=(11, 1)),
         sg.Text('', key='Data Limite9', size=(9, 1)), sg.Text('', key='Usuario Cancelamento9', size=(17, 1)),
         sg.Text('', key='Conclusão9', size=(18, 1)), sg.Text('', key='Descrição Cancelamento9', size=(18, 1))],
        [sg.Text('', key='Ordem10', size=(5, 1)), sg.Text('', key='Area10', size=(14, 1)),
         sg.Text('', key='Data Solicitação10', size=(12, 1)), sg.Text('', key='Data inicio10', size=(11, 1)),
         sg.Text('', key='Data Conclusão10', size=(12, 1)), sg.Text('', key='Situação10', size=(6, 1)),
         sg.Text('', key='Data Cancelamento10', size=(15, 1)), sg.Text('', key='Prazo10', size=(5, 1)),
         sg.Text('', key='Descrição10', size=(30, 1)), sg.Text('', key='Usuario criador10', size=(11, 1)),
         sg.Text('', key='Data Limite10', size=(9, 1)), sg.Text('', key='Usuario Cancelamento10', size=(17, 1)),
         sg.Text('', key='Conclusão10', size=(18, 1)), sg.Text('', key='Descrição Cancelamento10', size=(18, 1))],
        [sg.Text('', key='Ordem11', size=(5, 1)), sg.Text('', key='Area11', size=(14, 1)),
         sg.Text('', key='Data Solicitação11', size=(12, 1)), sg.Text('', key='Data inicio11', size=(11, 1)),
         sg.Text('', key='Data Conclusão11', size=(12, 1)), sg.Text('', key='Situação11', size=(6, 1)),
         sg.Text('', key='Data Cancelamento11', size=(15, 1)), sg.Text('', key='Prazo11', size=(5, 1)),
         sg.Text('', key='Descrição11', size=(30, 1)), sg.Text('', key='Usuario criador11', size=(11, 1)),
         sg.Text('', key='Data Limite11', size=(9, 1)), sg.Text('', key='Usuario Cancelamento11', size=(17, 1)),
         sg.Text('', key='Conclusão11', size=(18, 1)), sg.Text('', key='Descrição Cancelamento11', size=(18, 1))],
        [sg.Text('', key='Ordem12', size=(5, 1)), sg.Text('', key='Area12', size=(14, 1)),
         sg.Text('', key='Data Solicitação12', size=(12, 1)), sg.Text('', key='Data inicio12', size=(11, 1)),
         sg.Text('', key='Data Conclusão12', size=(12, 1)), sg.Text('', key='Situação12', size=(6, 1)),
         sg.Text('', key='Data Cancelamento12', size=(15, 1)), sg.Text('', key='Prazo12', size=(5, 1)),
         sg.Text('', key='Descrição12', size=(30, 1)), sg.Text('', key='Usuario criador12', size=(11, 1)),
         sg.Text('', key='Data Limite12', size=(9, 1)), sg.Text('', key='Usuario Cancelamento12', size=(17, 1)),
         sg.Text('', key='Conclusão12', size=(18, 1)), sg.Text('', key='Descrição Cancelamento12', size=(18, 1))],
        [sg.Text('', key='Ordem13', size=(5, 1)), sg.Text('', key='Area13', size=(14, 1)),
         sg.Text('', key='Data Solicitação13', size=(12, 1)), sg.Text('', key='Data inicio13', size=(11, 1)),
         sg.Text('', key='Data Conclusão13', size=(12, 1)), sg.Text('', key='Situação13', size=(6, 1)),
         sg.Text('', key='Data Cancelamento13', size=(15, 1)), sg.Text('', key='Prazo13', size=(5, 1)),
         sg.Text('', key='Descrição13', size=(30, 1)), sg.Text('', key='Usuario criador13', size=(11, 1)),
         sg.Text('', key='Data Limite13', size=(9, 1)), sg.Text('', key='Usuario Cancelamento13', size=(17, 1)),
         sg.Text('', key='Conclusão13', size=(18, 1)), sg.Text('', key='Descrição Cancelamento13', size=(18, 1))],
        [sg.Text('', key='Ordem14', size=(5, 1)), sg.Text('', key='Area14', size=(14, 1)),
         sg.Text('', key='Data Solicitação14', size=(12, 1)), sg.Text('', key='Data inicio14', size=(11, 1)),
         sg.Text('', key='Data Conclusão14', size=(12, 1)), sg.Text('', key='Situação14', size=(6, 1)),
         sg.Text('', key='Data Cancelamento14', size=(15, 1)), sg.Text('', key='Prazo14', size=(5, 1)),
         sg.Text('', key='Descrição14', size=(30, 1)), sg.Text('', key='Usuario criador14', size=(11, 1)),
         sg.Text('', key='Data Limite14', size=(9, 1)), sg.Text('', key='Usuario Cancelamento14', size=(17, 1)),
         sg.Text('', key='Conclusão14', size=(18, 1)), sg.Text('', key='Descrição Cancelamento14', size=(18, 1))],
        [sg.Text('', key='Ordem15', size=(5, 1)), sg.Text('', key='Area15', size=(14, 1)),
         sg.Text('', key='Data Solicitação15', size=(12, 1)), sg.Text('', key='Data inicio15', size=(11, 1)),
         sg.Text('', key='Data Conclusão15', size=(12, 1)), sg.Text('', key='Situação15', size=(6, 1)),
         sg.Text('', key='Data Cancelamento15', size=(15, 1)), sg.Text('', key='Prazo15', size=(5, 1)),
         sg.Text('', key='Descrição15', size=(30, 1)), sg.Text('', key='Usuario criador15', size=(11, 1)),
         sg.Text('', key='Data Limite15', size=(9, 1)), sg.Text('', key='Usuario Cancelamento15', size=(17, 1)),
         sg.Text('', key='Conclusão15', size=(18, 1)), sg.Text('', key='Descrição Cancelamento15', size=(18, 1))],
        [sg.Text('', key='Ordem16', size=(5, 1)), sg.Text('', key='Area16', size=(14, 1)),
         sg.Text('', key='Data Solicitação16', size=(12, 1)), sg.Text('', key='Data inicio16', size=(11, 1)),
         sg.Text('', key='Data Conclusão16', size=(12, 1)), sg.Text('', key='Situação16', size=(6, 1)),
         sg.Text('', key='Data Cancelamento16', size=(15, 1)), sg.Text('', key='Prazo16', size=(5, 1)),
         sg.Text('', key='Descrição16', size=(30, 1)), sg.Text('', key='Usuario criador16', size=(11, 1)),
         sg.Text('', key='Data Limite16', size=(9, 1)), sg.Text('', key='Usuario Cancelamento16', size=(17, 1)),
         sg.Text('', key='Conclusão16', size=(18, 1)), sg.Text('', key='Descrição Cancelamento16', size=(18, 1))],
        [sg.Text('', key='Ordem17', size=(5, 1)), sg.Text('', key='Area17', size=(14, 1)),
         sg.Text('', key='Data Solicitação17', size=(12, 1)), sg.Text('', key='Data inicio17', size=(11, 1)),
         sg.Text('', key='Data Conclusão17', size=(12, 1)), sg.Text('', key='Situação17', size=(6, 1)),
         sg.Text('', key='Data Cancelamento17', size=(15, 1)), sg.Text('', key='Prazo17', size=(5, 1)),
         sg.Text('', key='Descrição17', size=(30, 1)), sg.Text('', key='Usuario criador17', size=(11, 1)),
         sg.Text('', key='Data Limite17', size=(9, 1)), sg.Text('', key='Usuario Cancelamento17', size=(17, 1)),
         sg.Text('', key='Conclusão17', size=(18, 1)), sg.Text('', key='Descrição Cancelamento17', size=(18, 1))],
        [sg.Text('', key='Ordem18', size=(5, 1)), sg.Text('', key='Area18', size=(14, 1)),
         sg.Text('', key='Data Solicitação18', size=(12, 1)), sg.Text('', key='Data inicio18', size=(11, 1)),
         sg.Text('', key='Data Conclusão18', size=(12, 1)), sg.Text('', key='Situação18', size=(6, 1)),
         sg.Text('', key='Data Cancelamento18', size=(15, 1)), sg.Text('', key='Prazo18', size=(5, 1)),
         sg.Text('', key='Descrição18', size=(30, 1)), sg.Text('', key='Usuario criador18', size=(11, 1)),
         sg.Text('', key='Data Limite18', size=(9, 1)), sg.Text('', key='Usuario Cancelamento18', size=(17, 1)),
         sg.Text('', key='Conclusão18', size=(18, 1)), sg.Text('', key='Descrição Cancelamento18', size=(18, 1))],
        [sg.Text('', key='Ordem19', size=(5, 1)), sg.Text('', key='Area19', size=(14, 1)),
         sg.Text('', key='Data Solicitação19', size=(12, 1)), sg.Text('', key='Data inicio19', size=(11, 1)),
         sg.Text('', key='Data Conclusão19', size=(12, 1)), sg.Text('', key='Situação19', size=(6, 1)),
         sg.Text('', key='Data Cancelamento19', size=(15, 1)), sg.Text('', key='Prazo19', size=(5, 1)),
         sg.Text('', key='Descrição19', size=(30, 1)), sg.Text('', key='Usuario criador19', size=(11, 1)),
         sg.Text('', key='Data Limite19', size=(9, 1)), sg.Text('', key='Usuario Cancelamento19', size=(17, 1)),
         sg.Text('', key='Conclusão19', size=(18, 1)), sg.Text('', key='Descrição Cancelamento19', size=(18, 1))],
        [sg.Text('', key='Ordem20', size=(5, 1)), sg.Text('', key='Area20', size=(14, 1)),
         sg.Text('', key='Data Solicitação20', size=(12, 1)), sg.Text('', key='Data inicio20', size=(11, 1)),
         sg.Text('', key='Data Conclusão20', size=(12, 1)), sg.Text('', key='Situação20', size=(6, 1)),
         sg.Text('', key='Data Cancelamento20', size=(15, 1)), sg.Text('', key='Prazo20', size=(5, 1)),
         sg.Text('', key='Descrição20', size=(30, 1)), sg.Text('', key='Usuario criador20', size=(11, 1)),
         sg.Text('', key='Data Limite20', size=(9, 1)), sg.Text('', key='Usuario Cancelamento20', size=(17, 1)),
         sg.Text('', key='Conclusão20', size=(18, 1)), sg.Text('', key='Descrição Cancelamento20', size=(18, 1))],
        [sg.Text('', key='Ordem21', size=(5, 1)), sg.Text('', key='Area21', size=(14, 1)),
         sg.Text('', key='Data Solicitação21', size=(12, 1)), sg.Text('', key='Data inicio21', size=(11, 1)),
         sg.Text('', key='Data Conclusão21', size=(12, 1)), sg.Text('', key='Situação21', size=(6, 1)),
         sg.Text('', key='Data Cancelamento21', size=(15, 1)), sg.Text('', key='Prazo21', size=(5, 1)),
         sg.Text('', key='Descrição21', size=(30, 1)), sg.Text('', key='Usuario criador21', size=(11, 1)),
         sg.Text('', key='Data Limite21', size=(9, 1)), sg.Text('', key='Usuario Cancelamento21', size=(17, 1)),
         sg.Text('', key='Conclusão21', size=(18, 1)), sg.Text('', key='Descrição Cancelamento21', size=(18, 1))],
        [sg.Text('', key='Ordem22', size=(5, 1)), sg.Text('', key='Area22', size=(14, 1)),
         sg.Text('', key='Data Solicitação22', size=(12, 1)), sg.Text('', key='Data inicio22', size=(11, 1)),
         sg.Text('', key='Data Conclusão22', size=(12, 1)), sg.Text('', key='Situação22', size=(6, 1)),
         sg.Text('', key='Data Cancelamento22', size=(15, 1)), sg.Text('', key='Prazo22', size=(5, 1)),
         sg.Text('', key='Descrição22', size=(30, 1)), sg.Text('', key='Usuario criador22', size=(11, 1)),
         sg.Text('', key='Data Limite22', size=(9, 1)), sg.Text('', key='Usuario Cancelamento22', size=(17, 1)),
         sg.Text('', key='Conclusão22', size=(18, 1)), sg.Text('', key='Descrição Cancelamento22', size=(18, 1))],
        [sg.Text('', key='Ordem23', size=(5, 1)), sg.Text('', key='Area23', size=(14, 1)),
         sg.Text('', key='Data Solicitação23', size=(12, 1)), sg.Text('', key='Data inicio23', size=(11, 1)),
         sg.Text('', key='Data Conclusão23', size=(12, 1)), sg.Text('', key='Situação23', size=(6, 1)),
         sg.Text('', key='Data Cancelamento23', size=(15, 1)), sg.Text('', key='Prazo23', size=(5, 1)),
         sg.Text('', key='Descrição23', size=(30, 1)), sg.Text('', key='Usuario criador23', size=(11, 1)),
         sg.Text('', key='Data Limite23', size=(9, 1)), sg.Text('', key='Usuario Cancelamento23', size=(17, 1)),
         sg.Text('', key='Conclusão23', size=(18, 1)), sg.Text('', key='Descrição Cancelamento23', size=(18, 1))],
        [sg.Text('', key='Ordem24', size=(5, 1)), sg.Text('', key='Area24', size=(14, 1)),
         sg.Text('', key='Data Solicitação24', size=(12, 1)), sg.Text('', key='Data inicio24', size=(11, 1)),
         sg.Text('', key='Data Conclusão24', size=(12, 1)), sg.Text('', key='Situação24', size=(6, 1)),
         sg.Text('', key='Data Cancelamento24', size=(15, 1)), sg.Text('', key='Prazo24', size=(5, 1)),
         sg.Text('', key='Descrição24', size=(30, 1)), sg.Text('', key='Usuario criador24', size=(11, 1)),
         sg.Text('', key='Data Limite24', size=(9, 1)), sg.Text('', key='Usuario Cancelamento24', size=(17, 1)),
         sg.Text('', key='Conclusão24', size=(18, 1)), sg.Text('', key='Descrição Cancelamento24', size=(18, 1))],
        [sg.Text('', key='Ordem25', size=(5, 1)), sg.Text('', key='Area25', size=(14, 1)),
         sg.Text('', key='Data Solicitação25', size=(12, 1)), sg.Text('', key='Data inicio25', size=(11, 1)),
         sg.Text('', key='Data Conclusão25', size=(12, 1)), sg.Text('', key='Situação25', size=(6, 1)),
         sg.Text('', key='Data Cancelamento25', size=(15, 1)), sg.Text('', key='Prazo25', size=(5, 1)),
         sg.Text('', key='Descrição25', size=(30, 1)), sg.Text('', key='Usuario criador25', size=(11, 1)),
         sg.Text('', key='Data Limite25', size=(9, 1)), sg.Text('', key='Usuario Cancelamento25', size=(17, 1)),
         sg.Text('', key='Conclusão25', size=(18, 1)), sg.Text('', key='Descrição Cancelamento25', size=(18, 1))],
        [sg.Text('', key='Ordem26', size=(5, 1)), sg.Text('', key='Area26', size=(14, 1)),
         sg.Text('', key='Data Solicitação26', size=(12, 1)), sg.Text('', key='Data inicio26', size=(11, 1)),
         sg.Text('', key='Data Conclusão26', size=(12, 1)), sg.Text('', key='Situação26', size=(6, 1)),
         sg.Text('', key='Data Cancelamento26', size=(15, 1)), sg.Text('', key='Prazo26', size=(5, 1)),
         sg.Text('', key='Descrição26', size=(30, 1)), sg.Text('', key='Usuario criador26', size=(11, 1)),
         sg.Text('', key='Data Limite26', size=(9, 1)), sg.Text('', key='Usuario Cancelamento26', size=(17, 1)),
         sg.Text('', key='Conclusão26', size=(18, 1)), sg.Text('', key='Descrição Cancelamento26', size=(18, 1))],
        [sg.Text('', key='Ordem27', size=(5, 1)), sg.Text('', key='Area27', size=(14, 1)),
         sg.Text('', key='Data Solicitação27', size=(12, 1)), sg.Text('', key='Data inicio27', size=(11, 1)),
         sg.Text('', key='Data Conclusão27', size=(12, 1)), sg.Text('', key='Situação27', size=(6, 1)),
         sg.Text('', key='Data Cancelamento27', size=(15, 1)), sg.Text('', key='Prazo27', size=(5, 1)),
         sg.Text('', key='Descrição27', size=(30, 1)), sg.Text('', key='Usuario criador27', size=(11, 1)),
         sg.Text('', key='Data Limite27', size=(9, 1)), sg.Text('', key='Usuario Cancelamento27', size=(17, 1)),
         sg.Text('', key='Conclusão27', size=(18, 1)), sg.Text('', key='Descrição Cancelamento27', size=(18, 1))],
        [sg.Text('', key='Ordem28', size=(5, 1)), sg.Text('', key='Area28', size=(14, 1)),
         sg.Text('', key='Data Solicitação28', size=(12, 1)), sg.Text('', key='Data inicio28', size=(11, 1)),
         sg.Text('', key='Data Conclusão28', size=(12, 1)), sg.Text('', key='Situação28', size=(6, 1)),
         sg.Text('', key='Data Cancelamento28', size=(15, 1)), sg.Text('', key='Prazo28', size=(5, 1)),
         sg.Text('', key='Descrição28', size=(30, 1)), sg.Text('', key='Usuario criador28', size=(11, 1)),
         sg.Text('', key='Data Limite28', size=(9, 1)), sg.Text('', key='Usuario Cancelamento28', size=(17, 1)),
         sg.Text('', key='Conclusão28', size=(18, 1)), sg.Text('', key='Descrição Cancelamento28', size=(18, 1))],
        [sg.Text('', key='Ordem29', size=(5, 1)), sg.Text('', key='Area29', size=(14, 1)),
         sg.Text('', key='Data Solicitação29', size=(12, 1)), sg.Text('', key='Data inicio29', size=(11, 1)),
         sg.Text('', key='Data Conclusão29', size=(12, 1)), sg.Text('', key='Situação29', size=(6, 1)),
         sg.Text('', key='Data Cancelamento29', size=(15, 1)), sg.Text('', key='Prazo29', size=(5, 1)),
         sg.Text('', key='Descrição29', size=(30, 1)), sg.Text('', key='Usuario criador29', size=(11, 1)),
         sg.Text('', key='Data Limite29', size=(9, 1)), sg.Text('', key='Usuario Cancelamento29', size=(17, 1)),
         sg.Text('', key='Conclusão29', size=(18, 1)), sg.Text('', key='Descrição Cancelamento29', size=(18, 1))],
        [sg.Text('', key='Ordem30', size=(5, 1)), sg.Text('', key='Area30', size=(14, 1)),
         sg.Text('', key='Data Solicitação30', size=(12, 1)), sg.Text('', key='Data inicio30', size=(11, 1)),
         sg.Text('', key='Data Conclusão30', size=(12, 1)), sg.Text('', key='Situação30', size=(6, 1)),
         sg.Text('', key='Data Cancelamento30', size=(15, 1)), sg.Text('', key='Prazo30', size=(5, 1)),
         sg.Text('', key='Descrição30', size=(30, 1)), sg.Text('', key='Usuario criador30', size=(11, 1)),
         sg.Text('', key='Data Limite30', size=(9, 1)), sg.Text('', key='Usuario Cancelamento30', size=(17, 1)),
         sg.Text('', key='Conclusão30', size=(18, 1)), sg.Text('', key='Descrição Cancelamento30', size=(18, 1))],
        [sg.Button('Voltar', key='voltar_osm_atrasadas'), sg.Button('Fechar')],
    ]
    return sg.Window("OSM's Atrasadas", layout=layout, finalize=True)


def janela_menu_completo():  # 3
    sg.theme('Default1')
    layout = [
        [sg.Text('')],
        [sg.Button('Criar OSM'), sg.Button('Gerenciar OSM'), sg.Button('Usuarios'), sg.Button('OSM em aberto'),
         sg.Button('OSM atrasadas'), sg.Button('Sobre')],
        [sg.Text('')],
        [sg.Button('Fechar')]]
    return sg.Window('Menu', layout=layout, finalize=True)


def janela_menu_criar():  # 7
    sg.theme('Default1')
    layout = [
        [sg.Text('')],
        [sg.Button('Criar OSM'),
         sg.Text('                                                                                                 '),
         sg.Button('Sobre')],
        [sg.Text('')],
        [sg.Button('Fechar')], ]
    return sg.Window('Menu', layout=layout, finalize=True)


def janela_menu_gerenciar():  # 8
    sg.theme('Default1')
    layout = [
        [sg.Text('')],
        [sg.Text('                '), sg.Button('Gerenciar OSM'), sg.Text('               '),
         sg.Button('OSM em aberto'), sg.Button('OSM atrasadas'), sg.Button('Sobre')],
        [sg.Text('')],
        [sg.Button('Fechar')], ]
    return sg.Window('Menu', layout=layout, finalize=True)


def janela_register():  # 6
    sg.theme('Default1')
    layout = [
        [sg.Text('Usuario:                      '), sg.Input(key='usuario_register', size=(30, 1))],
        [sg.Text('Senha:                        '), sg.Input(key='senha_register', password_char='*', size=(20, 1))],
        [sg.Text('Confirmação de Senha: '), sg.Input(key='senha_confirmacao', password_char='*', size=(20, 1))],
        [sg.Text('Setor:'), sg.Combo(setor, key='setor', size=(25, 1)), sg.Text('Permissão:'),
         sg.Combo(permissao, key='permissao', size=(5, 1)), sg.CB('Administrador', key='administrador')],
        [sg.Button('Criar Usuario', key='register'), sg.Text('', key='mensagem_register')],
        [sg.Button('Voltar', key='voltar_register'), sg.Button('Fechar')],
    ]
    return sg.Window('Register', layout=layout, finalize=True)


def janela_confirmação():  # 2
    sg.theme('Reddit')
    layout = [
        [sg.Text('Usuario'), sg.Input(key='usuario2', size=(30, 1))],
        [sg.Text('Senha  '), sg.Input(key='senha2', password_char='*', size=(20, 1))],
        [sg.Button('Entrar', key='entrar2'), sg.Button('Cancelar', key='cancelar_confirmacao')],
        [sg.Text('', key='mensagem1')]
    ]
    return sg.Window('Usuario', layout=layout, finalize=True)


def janela_criar():  # 5
    sg.theme('Default1')
    layout = [
        [sg.Text('Finalidade:                                        '), sg.Text('Local:                           '),
         sg.Text('Descrição:')],
        [sg.Combo(area, key='area', size=(30, 1)), sg.Input(key='local', size=(20, 1)),
         sg.Input(key='descricao', size=(100, 4))],
        [sg.Button('Confirmar', key='confirmarcriar'), sg.Text('', key='mensagem1')],
        [sg.Button('Voltar', key='voltar_criar'), sg.Button('Fechar')],
    ]
    return sg.Window('Criar OSM', layout=layout, finalize=True)


def janela_editar():  # 4
    sg.theme('Default1')
    layout = [
        [sg.Text('Ordem:', font='Comics 16 bold ', text_color='black'), sg.Input(key='localizar_seq', size=(8, 2), ),
         sg.Button('Localizar'), sg.Text('', key='mensagem3')],
        [sg.Text('Sequencia:', font='Comics 16 bold', text_color='black'), sg.Text('', key='mensagemseq')],
        [sg.Text('Local:', font='Comics 16 bold', text_color='black'), sg.Text('', key='mensagemlocal')],
        [sg.Text('Data de inicio:', font='Comics 16 bold ', text_color='black'), sg.Text('', key='mensagemdtinicio')],
        [sg.Text('Usuario:', font='Comics 16 bold ', text_color='black'), sg.Text('', key='mensagemusuario')],
        [sg.Text('Situação:', font='Comics 16 bold ', text_color='black'), sg.Text('', key='situacao')],
        [sg.Text('Finalidade:', font='Comics 16 bold ', text_color='black'), sg.Text('', key='mensagemarea')],
        [sg.Text('Data de Solicitação:', font='Comics 16 bold ', text_color='black'),
         sg.Text('', key='mensagemdtsolicitacao')],
        [sg.Text('Prazo:', font='Comics 16 bold ', text_color='black'), sg.Input(key='prazo', size=(5, 5), font=18),
         sg.Text('', key='mensagemprazo')],
        [sg.Text('Data Limite:', font='Comics 16 bold ', text_color='black'), sg.Text('', key='mensagemdtlimite')],
        [sg.Text('Descrição:', font=18, text_color='black', size=(10, 5)),
         sg.Text('', key='mensagemdescricao', size=(80, 5), background_color='white')],
        [sg.Text('Conclusão:', font=18, text_color='black', size=(10, 1)),
         sg.Input('', key='mensagemconclusao', size=(92, 1), background_color='white', text_color='black')],
        [sg.Text('Escolha um e-mail para enviar o relatório:'),
         sg.Combo(email_criar, key='email_gerenciar', size=(40, 1))],
        [sg.Button('Iniciar Ordem'), sg.Button('Concluir Ordem'), sg.Button('Cancelar Ordem'),
         sg.Text('', key='mensagem2')],
        [sg.Button('Voltar', key='voltar_editar'), sg.Button('Fechar')],
    ]
    return sg.Window('Gerenciar OSM', layout=layout, finalize=True)


janela1, janela2, janela3, janela4, janela5, janela6, janela7, janela8, janela9, janela10, janela11, janela12, janela13 = janela_login(), None, None, None, None, None, None, None, None, None, None, None, None
# janela1 = janela_login()
# janela2 = janela_confirmação()
# janela3 = janela_menu_completo()
# janela4 = janela_editar()
# janela5 = janela_criar()
# janela6 = janela_register()
# janela7 = janela_menu_criar()
# janela8 = janela_menu_gerenciar()
# janela9 = janela_osm_aberto()
# janela10 = janela_osm_atrasadas()
# janela11 = janela_sobre()
# janela12 = janela_cancelamento()
# janela13 = janela_config()
while True:
    window, eventos, values = sg.read_all_windows()
    if eventos == 'Entrar':
        usuario1 = values['usuario']
        query1 = f"select usuario, senha, permissao,administrador from osm.usuarios_osm where usuario = '{usuario1}'"
        cursor = connection.cursor()
        try:
            cursor.execute(query1)
            result1 = cursor.fetchall()
        except:
            print("Erro ao validar o login")
        usuario = values['usuario']
        senha = values['senha']
        query = f"select usuario, senha, permissao,administrador from osm.usuarios_osm where usuario = '{usuario}' and senha = '{senha}'"
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except:
            print("Erro ao validar o login")
        if values['usuario'] == '' or values['senha'] == '':
            window['mensagem1'].update('Preencha os campos de usuario e senha para fazer login!', text_color='red')
        elif result == []:
            window['mensagem1'].update('Problema no login!', text_color='red')
        elif values['usuario'] == result[0][0] and values['senha'] == result[0][1] and result[0][3] == '1':
            window['mensagem1'].update('Login Feito com SUCESSO!', text_color='green')
            janela3 = janela_menu_completo()
            janela1.hide()
        elif values['usuario'] == result[0][0] and values['senha'] == result[0][1] and result[0][2] == 'E':
            window['mensagem1'].update('Login Feito com SUCESSO!', text_color='green')
            janela8 = janela_menu_gerenciar()
            janela1.hide()
        elif values['usuario'] == result[0][0] and values['senha'] == result[0][1] and result[0][2] == 'C':
            window['mensagem1'].update('Login Feito com SUCESSO!', text_color='green')
            if result1[0][2] == 'C' and result1[0][3] == '0':
                janela1.hide()
                janela7 = janela_menu_criar()
            elif result1[0][2] == 'E' and result1[0][3] == '0':
                janela1.hide()
                janela8 = janela_menu_gerenciar()
            else:
                janela1.hide()
                janela3 = janela_menu_completo()

        elif values['usuario'] != result[0][0] and values['senha'] != result[0][1]:
            window['mensagem1'].update('Falha no login!', text_color='red')
    elif eventos == 'ok_config':
        host_name = values['server_config']
        user_name = values['usuario_config']
        user_password = values['senha_config']
        db_name = values['banco_config']
        window['server_config'].update(host_name)
        window['usuario_config'].update(user_name)
        window['senha_config'].update(user_password)
        window['banco_config'].update(db_name)
        window['mensagem_config'].update('Dados atualizados!')
    elif eventos == 'config':
        janela13 = janela_config()
    elif eventos == 'voltar_config':
        janela13.hide()
    elif eventos == 'OSM em aberto':
        query_quantas_osm_abertas = 'select count(seq) from osm.dado_osm where situacao in ("lancado","iniciado")'
        cursor12 = connection.cursor()
        try:
            cursor12.execute(query_quantas_osm_abertas)
            result_aberto = cursor.fetchall()
            print(result_aberto[0][0])
        except:
            print("Erro ao validar o login")
        query_osm_abertas = """
select
	seq as Ordem,
    Area,
    Dt_solicitacao as 'Data Solicitação',
    dt_inicio as 'Data Inicio',
    dt_conclusao as 'Data Conclusão',
    situacao as 'Situação',
    dt_cancelamento as 'Data Cancelamento',
    Prazo,
    Descricao as 'Descrição',
    usuario as 'Usuario criador',
    dt_limite as 'Data Limite',
    usuario_canc as 'Usuario Cancelamento',
    Conclusao as 'Conclusão',
    descr_cancelamento as 'Descrição Cancelamento'    
from 
	osm.dado_osm 
where 
	situacao in ('lancado','iniciado')"""
        cursor13 = connection.cursor()
        try:
            cursor13.execute(query_osm_abertas)
            result_abertas = cursor.fetchall()
        except:
            print("Erro ao validar o login")
        if result1[0][2] == 'E' and result1[0][3] == '0':
            janela9 = janela_osm_aberto()
            janela8.hide()
        else:
            janela9 = janela_osm_aberto()
            janela3.hide()
    elif eventos == 'carregar_osm_aberto':
        for x in range(0, int(result_aberto[0][0])):
            numero = (100 / int(result_aberto[0][0]))
            valor = numero * (x + 1)
            window[f'Ordem{x}'].update(str(result_abertas[int(x)][0]))
            window[f'Area{x}'].update(str(result_abertas[int(x)][1]))
            window[f'Data Solicitação{x}'].update(str(result_abertas[x][2]))
            window[f'Data inicio{x}'].update(str(result_abertas[x][3]))
            window[f'Situação{x}'].update(str(result_abertas[x][5]))
            window[f'Prazo{x}'].update(str(result_abertas[x][7]))
            window[f'Descrição{x}'].update(str(result_abertas[x][8]))
            window[f'Usuario criador{x}'].update(str(result_abertas[x][9]))
            window[f'Data Limite{x}'].update(str(result_abertas[x][10]))
            window['barra_de_status'].update(str(f'{valor}'))
            time.sleep(0.05)
    elif eventos == 'OSM atrasadas':
        query_quantas_osm_atraso = 'select count(seq) from osm.dado_osm where dt_limite <= CURDATE() and situacao <> "cancelado" and situacao <> "concluido"'
        cursor1 = connection.cursor()
        try:
            cursor1.execute(query_quantas_osm_atraso)
            result_atraso = cursor.fetchall()
        except:
            print("Erro ao validar o login")
        query_osm_atrasadas = "select * from osm.dado_osm where dt_limite <= CURDATE()and situacao <> 'cancelado' situacao <> 'concluido'"
        cursor = connection.cursor()
        try:
            cursor.execute(query_osm_atrasadas)
            result_atrasadas = cursor.fetchall()
        except:
            print("Erro ao validar o login")
        if result1[0][2] == 'E' and result1[0][3] == '0':
            janela10 = janela_osm_atrasadas()
            janela8.hide()
        else:
            janela10 = janela_osm_atrasadas()
            janela3.hide()
    elif eventos == 'carregar_osm_atrasadas':
        os = result_atraso[0][0]
        print(os)
        if result_atraso[0][0] == 0:
            window['mensagem_atraso'].update('Não foi encontrado nenhuma ordem em atraso!', text_color='Red', font=18)
        else:
            print(result_atraso[0][0])
            for x in range(0, int(result_atraso[0][0])):
                numero = (100 / int(result_atraso[0][0]))
                valor = numero * (x + 1)
                window[f'Ordem{x}'].update(str(result_atrasadas[int(x)][0]))
                window[f'Area{x}'].update(str(result_atrasadas[int(x)][1]))
                window[f'Data Solicitação{x}'].update(str(result_atrasadas[x][2]))
                window[f'Data inicio{x}'].update(str(result_atrasadas[x][3]))
                window[f'Data Conclusão{x}'].update(str(result_atrasadas[x][4]))
                window[f'Situação{x}'].update(str(result_atrasadas[x][5]))
                window[f'Data Cancelamento{x}'].update(str(result_atrasadas[x][6]))
                window[f'Prazo{x}'].update(str(result_atrasadas[x][7]))
                window[f'Descrição{x}'].update(str(result_atrasadas[x][8]))
                window[f'Usuario criador{x}'].update(str(result_atrasadas[x][9]))
                window[f'Data Limite{x}'].update(str(result_atrasadas[x][10]))
                window[f'Usuario Cancelamento{x}'].update(str(result_atrasadas[x][11]))
                window[f'Conclusão{x}'].update(str(result_atrasadas[x][12]))
                window[f'Descrição Cancelamento{x}'].update(str(result_atrasadas[x][13]))
                window['barra_de_atraso'].update(str(f'{valor}'))
    elif eventos == 'Criar OSM':
        if result1[0][2] == 'C' and result1[0][3] == '0':
            janela5 = janela_criar()
            janela7.hide()
        elif result1[0][2] == 'E' and result1[0][3] == '0':
            janela5 = janela_criar()
            janela8.hide()
        else:
            janela5 = janela_criar()
            janela3.hide()
    elif eventos == 'Gerenciar OSM':
        if result1[0][2] == 'E' and result1[0][3] == '0':
            janela4 = janela_editar()
            janela8.hide()
        else:
            janela4 = janela_editar()
            janela3.hide()
    elif eventos == 'Usuarios':
        janela6 = janela_register()
        janela3.hide()
    elif eventos == 'voltar_register':
        janela6.hide()
        janela3 = janela_menu_completo()
    elif eventos == 'voltar_criar':
        if result1[0][2] == 'C' and result1[0][3] == '0':
            janela5.hide()
            janela7 = janela_menu_criar()
        elif result1[0][2] == 'E' and result1[0][3] == '0':
            janela5.hide()
            janela8 = janela_menu_gerenciar
        else:
            janela5.hide()
            janela3 = janela_menu_completo()
    elif eventos == 'voltar_osm_aberto':
        if result1[0][2] == 'E' and result1[0][3] == '0':
            janela9.hide()
            janela8 = janela_menu_gerenciar()
        else:
            janela9.hide()
            janela3 = janela_menu_completo()
    elif eventos == 'voltar_osm_atrasadas':
        if result1[0][2] == 'E' and result1[0][3] == '0':
            janela10.hide()
            janela8 = janela_menu_gerenciar()
        else:
            janela10.hide()
            janela3 = janela_menu_completo()
    elif eventos == 'voltar_editar':
        if result1[0][2] == 'E' and result1[0][3] == '0':
            janela4.hide()
            janela8.un_hide()
        else:
            janela4.hide()
            janela3.un_hide()
    elif eventos == 'voltar_sobre':
        if result1[0][2] == 'C' and result1[0][3] == '0':
            janela7 = janela_menu_criar()
            janela11.hide()
        elif result1[0][2] == 'E' and result1[0][3] == '0':
            janela11.hide()
            jjanela8 = janela_menu_gerenciar()
        elif result1[0][3] == '1':
            janela11.hide()
            janela3 = janela_menu_completo()
    elif eventos == 'Sobre':
        if result1[0][2] == 'C' and result1[0][3] == '0':
            janela11 = janela_sobre()
            janela7.hide()
        elif result1[0][2] == 'E' and result1[0][3] == '0':
            janela11 = janela_sobre()
            janela8.hide()
        else:
            janela11 = janela_sobre()
            janela3.hide()
    elif eventos == 'register':
        if values['administrador'] == True:
            administrador = 1
        elif values['administrador'] == False:
            administrador = 0
        print(administrador)
        usuario = values['usuario_register']
        senha = values['senha_register']
        permissao = values['permissao']
        setor1 = values['setor']
        query = f"select usuario from osm.usuarios_osm where usuario = '{usuario}'"
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except:
            print("Erro ao validar o login")
        if values['usuario_register'] == '' or values['senha_register'] == '' or values['senha_confirmacao'] == '' or \
                values['permissao'] == '' or values['setor'] == '':
            window['mensagem_register'].update('Preencha todos os campos para continuar.', text_color='red')
        elif result != []:
            window['mensagem_register'].update('Usuario já cadastrado!', text_color='red', font=20)
        elif values['senha_register'] != values['senha_confirmacao']:
            window['mensagem_register'].update('As senhas inseridas são diferentes! Tente novamente!', text_color='red')
        else:
            janela2 = janela_confirmação()
    elif eventos == 'Fechar' or eventos == sg.WIN_CLOSED:
        break
    elif eventos == 'Localizar':
        ordem = values['localizar_seq']
        query = f'select seq,area,local,dt_solicitacao,dt_inicio,prazo,usuario,dt_limite,descricao,situacao from osm.dado_osm where seq = "{ordem}"'
        print(query)
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
        except:
            print("Erro ao validar o login")
        if ordem == '':
            window['mensagem3'].update('Preencha o campo de ordem!', text_color='orange', font=22)

        elif result == []:
            window['mensagem3'].update('Ordem solicitada não encontrada!', text_color='orange', font=22)
            window['mensagemseq'].update('')
            window['mensagemarea'].update('')
            window['mensagemlocal'].update('')
            window['mensagemdtsolicitacao'].update('')
            window['mensagemdtinicio'].update('')
            window['mensagemprazo'].update('')
            window['mensagemusuario'].update('')
            window['mensagemdtlimite'].update('')
            window['mensagemdescricao'].update('')
        else:
            window['mensagemseq'].update(str(result[0][0]), font=14)
            window['mensagemarea'].update(str(result[0][1]), font=14)
            window['mensagemlocal'].update(str(result[0][2]), font=14)
            window['mensagemdtsolicitacao'].update(str(result[0][3]), font=14)
            window['mensagemdtinicio'].update(str(result[0][4]), font=14)
            window['mensagemprazo'].update(str(result[0][5]), font=14)
            window['mensagemusuario'].update(str(result[0][6]), font=14)
            window['mensagemdtlimite'].update(str(result[0][7]), font=14)
            window['mensagemdescricao'].update(str(result[0][8]), font=14)
            window['situacao'].update(str(result[0][9]), font=14)
            window['mensagem3'].update('')
    elif eventos == 'Iniciar Ordem':
        ordem_iniciar = values['localizar_seq']
        query = f'select seq,area,local,dt_solicitacao,dt_inicio,prazo,usuario,dt_limite,descricao,situacao from osm.dado_osm where seq = "{ordem_iniciar}"'
        print(query)
        cursor4 = connection.cursor()
        try:
            cursor4.execute(query)
            result_iniciar = cursor.fetchall()
            print(result)
        except:
            print("Erro ao validar o login")

        if values['localizar_seq'] == '':
            ''
        elif result_iniciar[0][9] == "iniciado":
            window['mensagem2'].update(f'Não é permitido iniciar esta ordem, Ordem já iniciada!', text_color='red',
                                       font=22)
        elif result_iniciar[0][9] == 'concluido':
            window['mensagem2'].update(f'Não é permitido iniciar esta ordem, Ordem já concluida!', text_color='red',
                                       font=22)
        elif values['prazo'] == '':
            window['mensagem2'].update(f'Preencher o campo de Prazo!', text_color='red', font=22)
        elif values['email_gerenciar'] == '':
            window['mensagem2'].update(f'Favor escolher e-mail para enviar os dados!', text_color='red', font=22)
        elif result[0][9] == 'lançado':
            email_iniciar = values['email_gerenciar']
            ordem_iniciar = values['localizar_seq']
            area_iniciar = result_iniciar[0][1]
            local_lançado = result_iniciar[0][3]
            usuario_lancou_ordem = result_iniciar[0][6]
            ordem_com0000 = str(ordem_iniciar).zfill(5)
            agora1 = datetime.now().strftime('%d-%m-%Y %H:%M')
            agora3 = datetime.now().strftime('%Y-%m-%d')
            agora_ano_iniciar = datetime.now().strftime('%y')
            prazo = values['prazo']
            query_iniciar = f'update osm.dado_osm set prazo = {prazo}, dt_inicio = "{agora3}", situacao = "iniciado", dt_limite = (cast("{agora3}" as date)  + interval {prazo} day) where seq = {ordem_iniciar}'


            def execute_query(connection, query_iniciar):
                cursor = connection.cursor()
                cursor.execute(query_iniciar)
                return cursor


            execute_query(connection, query_iniciar)
            connection.commit()
            Assunto = f'{ordem_com0000}/{area_iniciar}/{agora_ano_iniciar}'
            To = f"{email_iniciar}"
            corpo_email = f" Ordem iniciada pelo usuario {usuario}, com o prazo de {prazo} dias."
            enviar_email()
            window['mensagemseq'].update('')
            window['mensagemarea'].update('')
            window['mensagemlocal'].update('')
            window['mensagemdtsolicitacao'].update('')
            window['mensagemdtinicio'].update('')
            window['mensagemprazo'].update('')
            window['mensagemusuario'].update('')
            window['mensagemdtlimite'].update('')
            window['mensagemdescricao'].update('')
            window['situacao'].update('')
            window['mensagemconclusao'].update('')
            window['localizar_seq'].update('')
            window['mensagem3'].update('')
            window['prazo'].update('')
            window['mensagem2'].update(f'Ordem Iniciada em {agora1}', text_color='orange', font=22)
    elif eventos == 'Concluir Ordem':
        if values['localizar_seq'] == '':
            ''
        elif values['mensagemconclusao'] == '':
            window['mensagem2'].update(f'Preencher o campo da descrição da conclusão!', text_color='red', font=22)
        elif result[0][9] == "cancelado":
            window['mensagem2'].update(f'Não é permitido concluir esta ordem, Ordem já cancelada!', text_color='red',
                                       font=22)
        elif values['mensagemconclusao'] == 0:
            window['mensagem2'].update(f'Preencher o campo de conclusão!', text_color='red', font=22)
        elif result[0][9] == 'cancelado':
            window['mensagem2'].update(f'Ordem cancelada, não pode ser concluida!', text_color='red', font=22)
        elif result[0][9] == 'concluido':
            window['mensagem2'].update(f'Ordem já concluida!', text_color='red', font=22)
        elif result[0][9] == 'lançado':
            window['mensagem2'].update(f'Ordem não iniciada!', text_color='red', font=22)
        elif values['email_gerenciar'] == '':
            window['mensagem2'].update(f'Favor escolher e-mail para enviar os dados!', text_color='red', font=22)
        elif result[0][9] == "iniciado":
            email_gerenciar1 = values['email_gerenciar']
            ordem1 = values['localizar_seq']
            area1 = result[0][1]
            local = result[0][2]
            usuario_lancador1 = result[0][6]
            ordem_com5000 = str(ordem).zfill(5)
            agora2 = datetime.now().strftime('%y')
            conclusao = values['mensagemconclusao']
            agora = datetime.now().strftime('%d/%m/%Y %H:%M')
            agora1 = datetime.now().strftime('%Y-%m-%d')
            window['mensagem2'].update(f'Ordem {ordem} Concluida em {agora}', text_color='green', font=22)
            query_concluir = f'update osm.dado_osm set dt_conclusao = "{agora1}", situacao = "concluido", conclusao = "{conclusao}" where seq = {ordem}'
            Assunto = f'{ordem_com5000}/{area1}/{agora2}'
            To = f"{email_gerenciar1}"
            corpo_email = f" Ordem concluida pelo usuario {usuario}, conclusão: {conclusao} "
            enviar_email()


            def execute_query(connection, query_concluir):
                cursor = connection.cursor()
                result = None
                cursor.execute(query_concluir)
                print(cursor)
                return cursor


            execute_query(connection, query_concluir)
            connection.commit()
            window['mensagemseq'].update('')
            window['mensagemarea'].update('')
            window['mensagemlocal'].update('')
            window['mensagemdtsolicitacao'].update('')
            window['mensagemdtinicio'].update('')
            window['mensagemprazo'].update('')
            window['mensagemusuario'].update('')
            window['mensagemdtlimite'].update('')
            window['mensagemdescricao'].update('')
            window['situacao'].update('')
            window['mensagemconclusao'].update('')
            window['localizar_seq'].update('')
            window['mensagem3'].update('')
            window['prazo'].update('')
    elif eventos == 'Cancelar Ordem':
        ordem = values['localizar_seq']
        email_gerenciar = values['email_gerenciar']
        if values['localizar_seq'] == '':
            ''
        elif result[0][9] == 'concluido':
            window['mensagem2'].update(f'Não é permitido cancelar esta ordem,  ordem já concluida!', text_color='red',
                                       font=22)
        elif result[0][9] == 'cancelado':
            window['mensagem2'].update(f'Ordem já cancelada!', text_color='red', font=22)
        elif values['email_gerenciar'] == '':
            window['mensagem2'].update(f'Favor escolher e-mail para enviar os dados!', text_color='red', font=22)
        elif result[0][9] == 'lançado':
            agora = datetime.now().strftime('%d/%m/%Y %H:%M')
            agora1 = datetime.now().strftime('%Y-%m-%d')
            window['mensagemseq'].update('')
            window['mensagemarea'].update('')
            window['mensagemlocal'].update('')
            window['mensagemdtsolicitacao'].update('')
            window['mensagemdtinicio'].update('')
            window['mensagemprazo'].update('')
            window['mensagemusuario'].update('')
            window['mensagemdtlimite'].update('')
            window['mensagemdescricao'].update('')
            window['situacao'].update('')
            window['mensagemconclusao'].update('')
            window['localizar_seq'].update('')
            window['mensagem3'].update('')
            window['prazo'].update('')
            janela12 = janela_cancelamento()
    elif eventos == 'entrar2':
        if values['usuario2'] == Usuario_adm and values['senha2'] == Senha_adm:
            print('cadastrado')
            agora = datetime.now().strftime('%Y-%m-%d')
            query = f"INSERT INTO  osm.usuarios_osm  VALUES ('{setor1}','{usuario}','{senha}','{agora}','{permissao}','{administrador}');"
            # query = 'select * from osm.usuarios_osm where permissao = "a" and usuario = "jonathan"'
            print(query)
            janela2.hide()
            # window['mensagem_register'].update(f'Usuario {usuario} criado com sucesso!',text_color='green',font=22)
            # window['usuario_register'].update('')
            # window['senha_resgister'].update('')
            # window['senha_confirmacao'].update('')
            # window['setor'].update('')
            # window['permissao'].update('')
            # window['administrador'].update('')
        else:
            window['mensagem1'].update(f'Usuario ou senha incorreta!', text_color='green', font=22)


        def execute_query(connection, query):
            cursor = connection.cursor()
            result = None
            cursor.execute(query)
            print(cursor)
            return cursor


        execute_query(connection, query)
        connection.commit()
    elif eventos == 'cancelar_confirmacao':
        janela4.hide()
    elif eventos == 'fechar_cancelamento':
        janela12.hide()
    elif eventos == 'ok_cancelar':
        motivo_cancelamento = values['input_cancelamento']
        if values['input_cancelamento'] == '':
            window['mensagem_motivo_cancelamento'].update(f'Preencha um motivo para cancelar a etiqueta',
                                                          text_color='red', font=22)
        elif values['input_cancelamento'] != '':
            motivo_cancelamento = values['input_cancelamento']
            area1 = result[0][1]
            local = result[0][2]
            usuario_lancador = result[0][6]
            ordem1 = str(ordem).zfill(5)
            agora2 = datetime.now().strftime('%y')
            Assunto = f'{ordem}/{area1}/{agora2}  {usuario_lancador} - {local}'
            To = f"{email_gerenciar}"
            corpo_email = f" Ordem cancelada pelo usuario {usuario}. Motivo do cancelamento: {motivo_cancelamento} "
            enviar_email()
            query_cancelamento = f'update osm.dado_osm set situacao = "cancelado", dt_cancelamento = "{agora1}",usuario_canc = "{usuario}", descr_cancelamento = "{motivo_cancelamento}" where seq = "{ordem}"'


            def execute_query(connection, query_cancelamento):
                cursor = connection.cursor()
                result = None
                cursor.execute(query_cancelamento)
                print(cursor)
                return cursor


            execute_query(connection, query_cancelamento)
            connection.commit()
            janela12.hide()
    elif eventos == 'confirmarcriar':
        if values['area'] == '' or values['local'] == '' or values['descricao'] == '':
            window['mensagem1'].update('Preencha todos os campos para continuar!', text_color='red')
        else:
            agora = datetime.now().strftime('%Y-%m-%d')
            agora_ano = datetime.now().strftime('%y')
            area = values['area']
            local = values['local']
            local_maiusculo = local.upper()
            descricao = values['descricao']
            query_criar = f'select seq from osm.dado_osm  order by seq desc limit 1;'
            cursor = connection.cursor()
            try:
                cursor.execute(query_criar)
                result_criar = cursor.fetchall()
            except:
                print("Erro ao validar o login")
            ultima_seq = result_criar[0][0]
            nova_seq = str(ultima_seq + 1)
            nova_seq1 = str(nova_seq).zfill(5)
            Assunto = str(f'{nova_seq1}/{area}/{agora_ano}')
            corpo_email = str(f" Ordem lancada pelo usuario: {usuario}, no local: {str(local_maiusculo)}, com a seguinte tarefa: {descricao}")
            for x in range(0,9):
                To = email_criar[x]
                enviar_email()
            query1 = f'insert into osm.dado_osm (seq,area,local,descricao,dt_solicitacao,situacao,usuario) values("{nova_seq}","{area}","{local_maiusculo}","{descricao}","{agora}","lançado","{usuario}")'
            def execute_query(connection, query1):
                cursor = connection.cursor()
                result = None
                cursor.execute(query1)
                print(cursor)
                return cursor
            execute_query(connection, query1)
            connection.commit()
            window['mensagem1'].update(f'Ordem {nova_seq} cadastrada com sucesso!', text_color='green')
            window['area'].update('')
            window['local'].update('')
            window['descricao'].update('')









