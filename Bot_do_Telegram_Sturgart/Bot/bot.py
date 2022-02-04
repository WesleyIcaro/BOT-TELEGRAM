import telebot

CHAVE_API = 'TOKEN'

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=['opcao1_1'])
def opcao1_1(mensagem):
    bot.send_message(mensagem.chat.id, '''Enviamos o seu pedido de hamburguer de alface para a cozinha, obrigado!
Clique em iniciar para voltar /Iniciar''')


@bot.message_handler(commands=['opcao2_1'])
def opcao2_1(mensagem):
    bot.send_message(mensagem.chat.id, '''Enviamos o seu pedido de pizza de manjericão para a cozinha, obrigado!
Clique em iniciar para voltar /Iniciar''')


@bot.message_handler(commands=['opcao3_1'])
def opcao3_1(mensagem):
    bot.send_message(mensagem.chat.id, '''Enviamos o seu pedido de caldo de mandioca para a cozinha, obrigado!
Clique em iniciar para voltar /Iniciar''')


@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    texto = '''Escolha um dos produtos da lista:
    /opcao1_1 - Hamburgue de alface
    /opcao2_1 - Pizza de Manjericão
    /opcao3_1 - caldo de mandioca'''
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, 'Pedido cancelado com sucesso!')


@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, 'PIX - (31) 98877-6655')


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def resposta(mensagem):
    texto = """
   Escolha uma opção para seguirmos com o atendimento (clique em uma das opções):
    /opcao1 - Fazer um pedido
    /opcao2 - Cancelar um pedido
    /opcao3 - Ver os dados para fazer o pagamento
Responder qualquer outra coisa não vai funcionar, escolha uma opção!"""
    bot.reply_to(mensagem, texto)


bot.polling()
