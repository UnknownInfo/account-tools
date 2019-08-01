# -*- coding: utf-8 -*-
{
    'name': "Filtro Factura de Proveedor por Albaran",

    'summary': """
        Filtra las cantidades recepcionadas por albarán en la factura
        cuando un producto es marcado para facturar sobre cantidades recibidas,
    """,

    'description': """
        Filtra las cantidades recepcionadas por albarán en la factura
        cuando un producto es marcado para facturar sobre cantidades recibidas,
        Crea una factura de proveedor,  al seleccionar el pedido de compra odoo
        se trae las lineas de todas las recepciones 
        (Albaranes que tiene el pedido compras), filtrando 
        por las lineas recepcionadas de los albaranes especificados.

    """,

    'author': "Praxya, Juan Carlos Montoya",
    'website': "http://www.praxya.com",

    'category': 'Accounting',
    'version': '0.4',

    'depends': ['account', 'purchase', 'stock'],

    # always loaded
    'data': [
        'views/account_invoice.xml',
    ],
    'installable': True,
}
