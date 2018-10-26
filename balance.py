import pagarme


# adicionar chave de autenticação da API
pagarme.authentication_key('SUA_CHAVE_AQUI')

recipient1_id = 're_cjbfmzwxq00xqkq6dbmev1zb0'
recipient2_id = 're_cjbfmzxhy00z3rs6e8caj6t84'

saldo_default = pagarme.balance.default_recipient_balance()
a_receber = saldo_default['waiting_funds']['amount']
disponivel = saldo_default['available']['amount']
print("Saldo do recipient default: {} a receber e {} disponível".format(a_receber, disponivel))

saldo_recipient1 = pagarme.recipient.recipient_balance(recipient1_id)
a_receber = saldo_recipient1['waiting_funds']['amount']
disponivel = saldo_recipient1['available']['amount']
print("Saldo do recipient1: {} a receber e {} disponível".format(a_receber, disponivel))

saldo_recipient2 = pagarme.recipient.recipient_balance(recipient2_id)
a_receber = saldo_recipient2['waiting_funds']['amount']
disponivel = saldo_recipient2['available']['amount']
print("Saldo do recipient2 {} a receber e {} disponível".format(a_receber, disponivel))
