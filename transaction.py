import pagarme


# adicionar chave de autenticação da API
pagarme.authentication_key('SUA_CHAVE_AQUI')

recipient1_id = 're_cjbfmzwxq00xqkq6dbmev1zb0'
recipient2_id = 're_cjbfmzxhy00z3rs6e8caj6t84'

transaction_data = {
		"amount": 25000,
	    "card_number": "4111111111111111",
	    "card_cvv": "123",
	    "card_expiration_date": "0922",
	    "card_holder_name": "Cliente Fiel",
	    "customer": {
	      "external_id": "#1234",
	      "name": "Cliente Fiel",
	      "type": "individual",
	      "country": "br",
	      "email": "cliente@cli.com",
	      "documents": [
		      {
		      "type": "cpf",
		      "number": "00000000000"
		      }
      ],
      "phone_numbers": ["+5511999999999", "+5511888889999"],
      "birthday": "1990-01-01"
    },
    "billing": {
      "name": "Cliente Fiel",
      "address": {
        "country": "br",
        "state": "sp",
        "city": "Franca",
        "neighborhood": "Centro",
        "street": "Rua Feliz",
        "street_number": "123",
        "zipcode": "14400123"
      }
    },
    "items": [
      {
        "id": "1",
        "title": "Item 1",
        "unit_price": 25000,
        "quantity": 1,
        "tangible": False
      }
    ],
    "split_rules": [
	    {
	      "recipient_id": recipient1_id,
	      "percentage": 70,
	      "liable": True,
	      "charge_processing_fee": True
	    },{
	      "recipient_id": recipient2_id,
	      "percentage": 30,
	      "liable": True,
	      "charge_processing_fee": True
	    }
	  ]
}

transaction1 = pagarme.transaction.create(transaction_data)

print(transaction1)