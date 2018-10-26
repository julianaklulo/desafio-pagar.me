import pagarme

# adicionar chave de autenticação da API
pagarme.authentication_key('SUA_CHAVE_AQUI')

recipient1_data = {
    'anticipatable_volume_percentage': '80',
    'automatic_anticipation_enabled': 'true',
    'transfer_day': '5',
    'transfer_enabled': 'true',
    'transfer_interval': 'weekly',
    'bank_account':{
		'agencia': '0123',
		'agencia_dv': '2',
		'bank_code': '123',
		'conta': '32101',
		'conta_dv': '3',
		'document_number': '51336010002',
		'legal_name': 'Recipient 1'
    }
}

recipient1 = pagarme.recipient.create(recipient1_data)
print(recipient1)

recipient2_data = {
    'anticipatable_volume_percentage': '80',
    'automatic_anticipation_enabled': 'true',
    'transfer_day': '5',
    'transfer_enabled': 'true',
    'transfer_interval': 'weekly',
    'bank_account':{
		'agencia': '0234',
		'agencia_dv': '5',
		'bank_code': '345',
		'conta': '12458',
		'conta_dv': '4',
		'document_number': '85093081019',
		'legal_name': 'Recipient 2'
    }
}

recipient2 = pagarme.recipient.create(recipient2_data)
print(recipient2)