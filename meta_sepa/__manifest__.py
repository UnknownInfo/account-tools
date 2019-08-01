# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright :
#        (c) 2015 Company Name
#                 Juan Carlos Montoya <jcmontoya@praxya.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Meta SEPA",
    "version": "0.1",
    "author": "Juan Carlos Montoya, Praxya",
    "website": "http://praxya.com",
    "license": "AGPL-3",
    "category": "Accounting",
    "depends": [
        'account',
        'l10n_es',
        'account_banking_sepa_credit_transfer',
        'account_banking_sepa_direct_debit',
    ],
    "installable": True,
}
