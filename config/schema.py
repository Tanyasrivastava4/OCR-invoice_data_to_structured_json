SCHEMA = """
{
  "invoice_number": null,
  "invoice_date": null,
  "due_date": null,
  "seller": {
    "name": null,
    "address": null
  },
  "buyer": {
    "name": null,
    "address": null
  },
  "line_items": [
    {
      "item_no": null,
      "description": null,
      "quantity": null,
      "unit_price": null,
      "total": null
    }
  ],
  "subtotal": null,
  "tax_rate": null,
  "total": null,
  "balance_due": null,
  "terms": null,

  "extra_fields": {}
}
"""





#SCHEMA = """
#{
#  "invoice_number": null,
#  "invoice_date": null,
#  "due_date": null,
#  "seller": {
#    "name": null,
#    "address": null
#  },
#  "buyer": {
#    "name": null,
#    "address": null
#  },
#  "line_items": [
#    {
#      "item_no": null,
#      "description": null,
#      "hsn_sac": null,
#      "quantity": null,
#      "net_price": null,
#      "vat_percent": null,
#      "gross_value": null,
#      "unit_price": null,
#      "amount": null,
#      "um": null,
#      "total": null
#    }
#  ],
#  "subtotal": null,
#  "tax_rate": null,
#  "total": null,
#  "balance_due": null,
#  "terms": null,
#
#  "extra_fields": {}
#}
#"""
#



#SCHEMA = """
#{
#  "invoice_number": null,
#  "invoice_date": null,
#  "due_date": null,
#
#  "seller":"hsn_sac": null, {
#    "name": null,
#    "address": null,
#    "gstin": null
#  },
#
#  "buyer": {
#    "name": null,
#    "address": null,
#    "gstin": null
#  },
#
#  "line_items": [
#    {
#      "item_no": null,
#      "description": null,
#
#      "hsn_sac": null,
#
#      "quantity": null,
#      "unit_of_measure": null,
#
#      "unit_price": null,
#      "net_price": null,
#
#      "tax_rate": null,
#      "tax_amount": null,
#
#      "total": null
#    }
#  ],
#
#  "subtotal": null,
#
#  "tax_summary": {
#    "gst": null,
#    "vat": null,
#    "other_tax": null
#  },
#
#  "total": null,
#  "balance_due": null,
#
#  "terms": null,
#
#  "extra_fields": {}
#}
#"""
#







#SCHEMA = """
#{
#  "invoice_number": null,
#  "invoice_date": null,
#  "due_date": null,
#
#  "seller": {
#    "name": null,
#    "address": null,
#    "gstin": null
#  },
#
#  "buyer": {
#    "name": null,
#    "address": null,
#    "gstin": null
#  },
#
#  "line_items": [
#    {
#      "item_no": null,{
#  "invoice_number": "89174655",
#  "invoice_date": "1/19/2016",
#  "due_date": null,
#  "seller": {
#    "name": "Hayden-Young",
#    "address": "5394 David Motorway Apt. 573, South Amandaville, NV 46198"
#  },
#  "buyer": {
#    "name": "Guerrero Group",
#    "address": "53693 Donna Neck, Brownburgh, OH 92017"
#  },
#  "line_items": [
#    {
#      "item_no": "1",
#      "description": "The Great One: The Complete 2,00 Wayne Gretzky Collection",
#      "quantity": "each",
#      "unit_price": "4,89",
#      "total": "101,19"
#    },
#    {
#      "item_no": "2",
#      "description": "Care & Repair of Furniture",
#      "quantity": "each",
#      "unit_price": "4,25",
#      "total": "4,25"
#    },
#    {
#      "item_no": "3",
#      "description": "The Puzzle Palace",
#      "quantity": "each",
#      "unit_price": "4,49",
#      "total": "17,96"
#    },
#    {
#      "item_no": "4",
#      "description": "Pictures From a Distant Country: Seeing America Through Old Paper Money",
#      "quantity": "each",
#      "unit_price": "13,84",
#      "total": "69,20"
#    }
#  ],
#  "subtotal": "111,31",
#  "tax_rate": "10%",
#  "total": "111,31",
#  "balance_due": "111,31",
#  "terms": null,
#  "extra_fields": {
#    "seller_tax_id": "911-87-3432",
#    "seller_iban": "GB89JRLS95828897014080",
#    "buyer_tax_id": "970-77-2494",
#    "net_price": "4,89",
#    "net_worth": "101,19",
#    "net_worth_vat_percentage": "10%",
#    "vat_amount": "10,12",
#    "gross_worth": "111,31"
#  }
#}
#      "description": null,
#
#      "hsn_sac": null,
#
#      "quantity": null,
#      "unit_of_measure": null,
#
#      "unit_price": null,
#      "net_price": null,
#
#      "tax_rate": null,
#      "tax_amount": null,
#
#      "total": null
#    }
#  ],
#
#  "subtotal": null,
#
#  "tax_summary": {
#    "gst": null,
#    "vat": null,
#    "other_tax": null
#  },
#
#  "total": null,
#  "balance_due": null,
#
#  "terms": null,
#
#  "extra_fields": {}
#}
#"""


# This is the one(successfull)
#SCHEMA = """
#{
#  "invoice_number": null,
#  "invoice_date": null,
#  "due_date": null,
#  "seller": {
#    "name": null,
#    "address": null
#  },
#  "buyer": {
#    "name": null,
#    "address": null
#  },
#  "line_items": [
#    {
#      "item_no": null,
#      "description": null,
#      "quantity": null,
#      "unit_price": null,
#      "total": null
#    }
#  ],
#  "subtotal": null,
#  "tax_rate": null,
#  "total": null,
#  "balance_due": null,
#  "terms": null,
#
#  "extra_fields": {}
#}
#"""





#SCHEMA = """
#{
#  "invoice_number": null,
#  "invoice_date": null,
#  "due_date": null,
#
#  "seller": {
#    "name": null,
#    "address": null
#  },
#
#  "buyer": {
#    "name": null,
#    "address": null
#  },
#
#  "line_items": [
#    {
#      "item_no": null,
#      "description": null,
#      "quantity": null,
#      "unit_price": null,
#      "total": null
#    }
#  ],
#
#  "subtotal": null,
#  "tax_rate": null,
#  "total": null,
#  "balance_due": null,
#  "terms": null,
#
#  "extra_fields": {}
#}
#"""
#