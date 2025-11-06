#!/usr/bin/env python3
"""
Master Controller for Bitcoin Puzzle Environment
Auto-generated integration controller
"""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.append(str(Path(__file__).parent))

class MasterController:
    """Master controller for all integrated crypto tools"""
    
    def __init__(self):
        self.tools = {}
        self._load_all_tools()
        
    def _load_all_tools(self):
        """Load all integrated tools"""
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.util import *
            self.tools['util'] = 'thonlibs.libthon3.11.site-packages.qrcode.util'
        except ImportError as e:
            print(f"Could not import util: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_dialect import *
            self.tools['test_dialect'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_dialect'
        except ImportError as e:
            print(f"Could not import test_dialect: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcash.network.transaction import *
            self.tools['transaction'] = 'thonlibs.libthon3.11.site-packages.bitcash.network.transaction'
        except ImportError as e:
            print(f"Could not import transaction: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcash.wallet import *
            self.tools['wallet'] = 'thonlibs.libthon3.11.site-packages.bitcash.wallet'
        except ImportError as e:
            print(f"Could not import wallet: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.__init__ import *
            self.tools['__init__'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.__init__'
        except ImportError as e:
            print(f"Could not import __init__: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_wallet import *
            self.tools['test_wallet'] = 'thonlibs.libthon3.11.site-packages.tests.test_wallet'
        except ImportError as e:
            print(f"Could not import test_wallet: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_services import *
            self.tools['test_services'] = 'thonlibs.libthon3.11.site-packages.tests.test_services'
        except ImportError as e:
            print(f"Could not import test_services: {e}")
            
        try:
            from src.dual_utxo_transaction import *
            self.tools['dual_utxo_transaction'] = 'src.dual_utxo_transaction'
        except ImportError as e:
            print(f"Could not import dual_utxo_transaction: {e}")
            
        try:
            from src.qr_generator import *
            self.tools['qr_generator'] = 'src.qr_generator'
        except ImportError as e:
            print(f"Could not import qr_generator: {e}")
            
        try:
            from src.real_tx_parser import *
            self.tools['real_tx_parser'] = 'src.real_tx_parser'
        except ImportError as e:
            print(f"Could not import real_tx_parser: {e}")
            
        try:
            from src.complete_transaction_builder import *
            self.tools['complete_transaction_builder'] = 'src.complete_transaction_builder'
        except ImportError as e:
            print(f"Could not import complete_transaction_builder: {e}")
            
        try:
            from src.transaction_chain_analyzer import *
            self.tools['transaction_chain_analyzer'] = 'src.transaction_chain_analyzer'
        except ImportError as e:
            print(f"Could not import transaction_chain_analyzer: {e}")
            
        try:
            from src.blockchain_state_checker import *
            self.tools['blockchain_state_checker'] = 'src.blockchain_state_checker'
        except ImportError as e:
            print(f"Could not import blockchain_state_checker: {e}")
            
        try:
            from src.secure_wallet_manager import *
            self.tools['secure_wallet_manager'] = 'src.secure_wallet_manager'
        except ImportError as e:
            print(f"Could not import secure_wallet_manager: {e}")
            
        try:
            from puzzle160_tx_builder import *
            self.tools['puzzle160_tx_builder'] = 'puzzle160_tx_builder'
        except ImportError as e:
            print(f"Could not import puzzle160_tx_builder: {e}")
            
        try:
            from puzzle160_solver_demo import *
            self.tools['puzzle160_solver_demo'] = 'puzzle160_solver_demo'
        except ImportError as e:
            print(f"Could not import puzzle160_solver_demo: {e}")
            
        try:
            from src.web_interface import *
            self.tools['web_interface'] = 'src.web_interface'
        except ImportError as e:
            print(f"Could not import web_interface: {e}")
            
        try:
            from src.bitcoin_puzzle_toolkit import *
            self.tools['bitcoin_puzzle_toolkit'] = 'src.bitcoin_puzzle_toolkit'
        except ImportError as e:
            print(f"Could not import bitcoin_puzzle_toolkit: {e}")
            
        try:
            from src.memo_cash_backend import *
            self.tools['memo_cash_backend'] = 'src.memo_cash_backend'
        except ImportError as e:
            print(f"Could not import memo_cash_backend: {e}")
            
        try:
            from puzzle71-analysis.puzzle71_solver import *
            self.tools['puzzle71_solver'] = 'puzzle71-analysis.puzzle71_solver'
        except ImportError as e:
            print(f"Could not import puzzle71_solver: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.click._winconsole import *
            self.tools['_winconsole'] = 'thonlibs.libthon3.11.site-packages.click._winconsole'
        except ImportError as e:
            print(f"Could not import _winconsole: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.middleware.proxy_fix import *
            self.tools['proxy_fix'] = 'thonlibs.libthon3.11.site-packages.werkzeug.middleware.proxy_fix'
        except ImportError as e:
            print(f"Could not import proxy_fix: {e}")
            
        try:
            from memo-desktop.node_modules.dmg-builder.vendor.mac_alias.utils import *
            self.tools['utils'] = 'memo-desktop.node_modules.dmg-builder.vendor.mac_alias.utils'
        except ImportError as e:
            print(f"Could not import utils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.requests.help import *
            self.tools['help'] = 'thonlibs.libthon3.11.site-packages.requests.help'
        except ImportError as e:
            print(f"Could not import help: {e}")
            
        try:
            from memo-desktop.node_modules.dmg-builder.vendor.dmgbuild.core import *
            self.tools['core'] = 'memo-desktop.node_modules.dmg-builder.vendor.dmgbuild.core'
        except ImportError as e:
            print(f"Could not import core: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3._base_connection import *
            self.tools['_base_connection'] = 'thonlibs.libthon3.11.site-packages.urllib3._base_connection'
        except ImportError as e:
            print(f"Could not import _base_connection: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3.poolmanager import *
            self.tools['poolmanager'] = 'thonlibs.libthon3.11.site-packages.urllib3.poolmanager'
        except ImportError as e:
            print(f"Could not import poolmanager: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.wrappers.response import *
            self.tools['response'] = 'thonlibs.libthon3.11.site-packages.werkzeug.wrappers.response'
        except ImportError as e:
            print(f"Could not import response: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._sync.connection import *
            self.tools['connection'] = 'thonlibs.libthon3.11.site-packages.httpcore._sync.connection'
        except ImportError as e:
            print(f"Could not import connection: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3.util.ssl_ import *
            self.tools['ssl_'] = 'thonlibs.libthon3.11.site-packages.urllib3.util.ssl_'
        except ImportError as e:
            print(f"Could not import ssl_: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.keys import *
            self.tools['keys'] = 'thonlibs.libthon3.11.site-packages.ecdsa.keys'
        except ImportError as e:
            print(f"Could not import keys: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Util.asn1 import *
            self.tools['asn1'] = 'thonlibs.libthon3.11.site-packages.Crypto.Util.asn1'
        except ImportError as e:
            print(f"Could not import asn1: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.fastecdsa.encoding.sec1 import *
            self.tools['sec1'] = 'thonlibs.libthon3.11.site-packages.fastecdsa.encoding.sec1'
        except ImportError as e:
            print(f"Could not import sec1: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql._selectable_constructors import *
            self.tools['_selectable_constructors'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql._selectable_constructors'
        except ImportError as e:
            print(f"Could not import _selectable_constructors: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.pickleable import *
            self.tools['pickleable'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.pickleable'
        except ImportError as e:
            print(f"Could not import pickleable: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.engines import *
            self.tools['engines'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.engines'
        except ImportError as e:
            print(f"Could not import engines: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_reflection import *
            self.tools['test_reflection'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_reflection'
        except ImportError as e:
            print(f"Could not import test_reflection: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.image.styles.moduledrawers.base import *
            self.tools['base'] = 'thonlibs.libthon3.11.site-packages.qrcode.image.styles.moduledrawers.base'
        except ImportError as e:
            print(f"Could not import base: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.json import *
            self.tools['json'] = 'thonlibs.libthon3.11.site-packagesdantic.json'
        except ImportError as e:
            print(f"Could not import json: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysqlodbc import *
            self.tools['pyodbc'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysqlodbc'
        except ImportError as e:
            print(f"Could not import pyodbc: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.state_changes import *
            self.tools['state_changes'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.state_changes'
        except ImportError as e:
            print(f"Could not import state_changes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.persistence import *
            self.tools['persistence'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.persistence'
        except ImportError as e:
            print(f"Could not import persistence: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.baked import *
            self.tools['baked'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.baked'
        except ImportError as e:
            print(f"Could not import baked: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.mutable import *
            self.tools['mutable'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.mutable'
        except ImportError as e:
            print(f"Could not import mutable: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher.DES import *
            self.tools['DES'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher.DES'
        except ImportError as e:
            print(f"Could not import DES: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_ctr import *
            self.tools['_mode_ctr'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_ctr'
        except ImportError as e:
            print(f"Could not import _mode_ctr: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher.CAST import *
            self.tools['CAST'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher.CAST'
        except ImportError as e:
            print(f"Could not import CAST: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher._pkcs1_oaep_decode import *
            self.tools['_pkcs1_oaep_decode'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher._pkcs1_oaep_decode'
        except ImportError as e:
            print(f"Could not import _pkcs1_oaep_decode: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_ofb import *
            self.tools['_mode_ofb'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_ofb'
        except ImportError as e:
            print(f"Could not import _mode_ofb: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher.ChaCha20_Poly1305 import *
            self.tools['ChaCha20_Poly1305'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher.ChaCha20_Poly1305'
        except ImportError as e:
            print(f"Could not import ChaCha20_Poly1305: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher.DES3 import *
            self.tools['DES3'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher.DES3'
        except ImportError as e:
            print(f"Could not import DES3: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher.Blowfish import *
            self.tools['Blowfish'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher.Blowfish'
        except ImportError as e:
            print(f"Could not import Blowfish: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher.PKCS1_OAEP import *
            self.tools['PKCS1_OAEP'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher.PKCS1_OAEP'
        except ImportError as e:
            print(f"Could not import PKCS1_OAEP: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher.AES import *
            self.tools['AES'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher.AES'
        except ImportError as e:
            print(f"Could not import AES: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_ecb import *
            self.tools['_mode_ecb'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_ecb'
        except ImportError as e:
            print(f"Could not import _mode_ecb: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher.ARC2 import *
            self.tools['ARC2'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher.ARC2'
        except ImportError as e:
            print(f"Could not import ARC2: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_cbc import *
            self.tools['_mode_cbc'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_cbc'
        except ImportError as e:
            print(f"Could not import _mode_cbc: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_cfb import *
            self.tools['_mode_cfb'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_cfb'
        except ImportError as e:
            print(f"Could not import _mode_cfb: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.IO._PBES import *
            self.tools['_PBES'] = 'thonlibs.libthon3.11.site-packages.Crypto.IO._PBES'
        except ImportError as e:
            print(f"Could not import _PBES: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.IO.PKCS8 import *
            self.tools['PKCS8'] = 'thonlibs.libthon3.11.site-packages.Crypto.IO.PKCS8'
        except ImportError as e:
            print(f"Could not import PKCS8: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.IO.PEM import *
            self.tools['PEM'] = 'thonlibs.libthon3.11.site-packages.Crypto.IO.PEM'
        except ImportError as e:
            print(f"Could not import PEM: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.loader import *
            self.tools['loader'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.loader'
        except ImportError as e:
            print(f"Could not import loader: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.__main__ import *
            self.tools['__main__'] = 'thonlibs.libthon3.11.site-packages.PIL.__main__'
        except ImportError as e:
            print(f"Could not import __main__: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.st_common import *
            self.tools['st_common'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.st_common'
        except ImportError as e:
            print(f"Could not import st_common: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_OpenPGP import *
            self.tools['test_OpenPGP'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_OpenPGP'
        except ImportError as e:
            print(f"Could not import test_OpenPGP: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_OCB import *
            self.tools['test_OCB'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_OCB'
        except ImportError as e:
            print(f"Could not import test_OCB: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_AES import *
            self.tools['test_AES'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_AES'
        except ImportError as e:
            print(f"Could not import test_AES: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_DES3 import *
            self.tools['test_DES3'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_DES3'
        except ImportError as e:
            print(f"Could not import test_DES3: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_ARC2 import *
            self.tools['test_ARC2'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_ARC2'
        except ImportError as e:
            print(f"Could not import test_ARC2: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_OFB import *
            self.tools['test_OFB'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_OFB'
        except ImportError as e:
            print(f"Could not import test_OFB: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_Blowfish import *
            self.tools['test_Blowfish'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_Blowfish'
        except ImportError as e:
            print(f"Could not import test_Blowfish: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_CBC import *
            self.tools['test_CBC'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_CBC'
        except ImportError as e:
            print(f"Could not import test_CBC: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_CCM import *
            self.tools['test_CCM'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_CCM'
        except ImportError as e:
            print(f"Could not import test_CCM: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_CAST import *
            self.tools['test_CAST'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_CAST'
        except ImportError as e:
            print(f"Could not import test_CAST: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_Salsa20 import *
            self.tools['test_Salsa20'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_Salsa20'
        except ImportError as e:
            print(f"Could not import test_Salsa20: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_GCM import *
            self.tools['test_GCM'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_GCM'
        except ImportError as e:
            print(f"Could not import test_GCM: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_pkcs1_oaep import *
            self.tools['test_pkcs1_oaep'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_pkcs1_oaep'
        except ImportError as e:
            print(f"Could not import test_pkcs1_oaep: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Signature.test_pkcs1_15 import *
            self.tools['test_pkcs1_15'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Signature.test_pkcs1_15'
        except ImportError as e:
            print(f"Could not import test_pkcs1_15: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_DES import *
            self.tools['test_DES'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_DES'
        except ImportError as e:
            print(f"Could not import test_DES: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_SIV import *
            self.tools['test_SIV'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_SIV'
        except ImportError as e:
            print(f"Could not import test_SIV: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.common import *
            self.tools['common'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.common'
        except ImportError as e:
            print(f"Could not import common: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_CFB import *
            self.tools['test_CFB'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_CFB'
        except ImportError as e:
            print(f"Could not import test_CFB: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_CTR import *
            self.tools['test_CTR'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_CTR'
        except ImportError as e:
            print(f"Could not import test_CTR: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.IO.test_PKCS8 import *
            self.tools['test_PKCS8'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.IO.test_PKCS8'
        except ImportError as e:
            print(f"Could not import test_PKCS8: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.IO.test_PBES import *
            self.tools['test_PBES'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.IO.test_PBES'
        except ImportError as e:
            print(f"Could not import test_PBES: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.random.tests.test_random import *
            self.tools['test_random'] = 'thonlibs.libthon3.11.site-packages.numpy.random.tests.test_random'
        except ImportError as e:
            print(f"Could not import test_random: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_MD5 import *
            self.tools['test_MD5'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_MD5'
        except ImportError as e:
            print(f"Could not import test_MD5: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_MD2 import *
            self.tools['test_MD2'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_MD2'
        except ImportError as e:
            print(f"Could not import test_MD2: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_CMAC import *
            self.tools['test_CMAC'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_CMAC'
        except ImportError as e:
            print(f"Could not import test_CMAC: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA224 import *
            self.tools['test_SHA224'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA224'
        except ImportError as e:
            print(f"Could not import test_SHA224: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_MD4 import *
            self.tools['test_MD4'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_MD4'
        except ImportError as e:
            print(f"Could not import test_MD4: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_KangarooTwelve import *
            self.tools['test_KangarooTwelve'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_KangarooTwelve'
        except ImportError as e:
            print(f"Could not import test_KangarooTwelve: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA256 import *
            self.tools['test_SHA256'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA256'
        except ImportError as e:
            print(f"Could not import test_SHA256: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA512 import *
            self.tools['test_SHA512'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA512'
        except ImportError as e:
            print(f"Could not import test_SHA512: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_keccak import *
            self.tools['test_keccak'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_keccak'
        except ImportError as e:
            print(f"Could not import test_keccak: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA1 import *
            self.tools['test_SHA1'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA1'
        except ImportError as e:
            print(f"Could not import test_SHA1: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_TupleHash import *
            self.tools['test_TupleHash'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_TupleHash'
        except ImportError as e:
            print(f"Could not import test_TupleHash: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_TurboSHAKE import *
            self.tools['test_TurboSHAKE'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_TurboSHAKE'
        except ImportError as e:
            print(f"Could not import test_TurboSHAKE: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA3_384 import *
            self.tools['test_SHA3_384'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA3_384'
        except ImportError as e:
            print(f"Could not import test_SHA3_384: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA3_224 import *
            self.tools['test_SHA3_224'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA3_224'
        except ImportError as e:
            print(f"Could not import test_SHA3_224: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHAKE import *
            self.tools['test_SHAKE'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHAKE'
        except ImportError as e:
            print(f"Could not import test_SHAKE: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA3_256 import *
            self.tools['test_SHA3_256'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA3_256'
        except ImportError as e:
            print(f"Could not import test_SHA3_256: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA384 import *
            self.tools['test_SHA384'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA384'
        except ImportError as e:
            print(f"Could not import test_SHA384: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_cSHAKE import *
            self.tools['test_cSHAKE'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_cSHAKE'
        except ImportError as e:
            print(f"Could not import test_cSHAKE: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA3_512 import *
            self.tools['test_SHA3_512'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_SHA3_512'
        except ImportError as e:
            print(f"Could not import test_SHA3_512: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Math.test_Numbers import *
            self.tools['test_Numbers'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Math.test_Numbers'
        except ImportError as e:
            print(f"Could not import test_Numbers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Math.test_modexp import *
            self.tools['test_modexp'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Math.test_modexp'
        except ImportError as e:
            print(f"Could not import test_modexp: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Math.test_Primality import *
            self.tools['test_Primality'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Math.test_Primality'
        except ImportError as e:
            print(f"Could not import test_Primality: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Math.test_modmult import *
            self.tools['test_modmult'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Math.test_modmult'
        except ImportError as e:
            print(f"Could not import test_modmult: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Util.test_rfc1751 import *
            self.tools['test_rfc1751'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Util.test_rfc1751'
        except ImportError as e:
            print(f"Could not import test_rfc1751: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Protocol.test_SecretSharing import *
            self.tools['test_SecretSharing'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Protocol.test_SecretSharing'
        except ImportError as e:
            print(f"Could not import test_SecretSharing: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.test_ecdh import *
            self.tools['test_ecdh'] = 'thonlibs.libthon3.11.site-packages.ecdsa.test_ecdh'
        except ImportError as e:
            print(f"Could not import test_ecdh: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_DSA import *
            self.tools['test_DSA'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_DSA'
        except ImportError as e:
            print(f"Could not import test_DSA: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_ECC_Ed25519 import *
            self.tools['test_ECC_Ed25519'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_ECC_Ed25519'
        except ImportError as e:
            print(f"Could not import test_ECC_Ed25519: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_ElGamal import *
            self.tools['test_ElGamal'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_ElGamal'
        except ImportError as e:
            print(f"Could not import test_ElGamal: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_ECC_Curve25519 import *
            self.tools['test_ECC_Curve25519'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_ECC_Curve25519'
        except ImportError as e:
            print(f"Could not import test_ECC_Curve25519: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_RSA import *
            self.tools['test_RSA'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_RSA'
        except ImportError as e:
            print(f"Could not import test_RSA: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_import_Curve25519 import *
            self.tools['test_import_Curve25519'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_import_Curve25519'
        except ImportError as e:
            print(f"Could not import test_import_Curve25519: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_import_RSA import *
            self.tools['test_import_RSA'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_import_RSA'
        except ImportError as e:
            print(f"Could not import test_import_RSA: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_ECC_Curve448 import *
            self.tools['test_ECC_Curve448'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_ECC_Curve448'
        except ImportError as e:
            print(f"Could not import test_ECC_Curve448: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_import_ECC import *
            self.tools['test_import_ECC'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_import_ECC'
        except ImportError as e:
            print(f"Could not import test_import_ECC: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_import_Curve448 import *
            self.tools['test_import_Curve448'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_import_Curve448'
        except ImportError as e:
            print(f"Could not import test_import_Curve448: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_ECC_Ed448 import *
            self.tools['test_ECC_Ed448'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_ECC_Ed448'
        except ImportError as e:
            print(f"Could not import test_ECC_Ed448: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_ECC_NIST import *
            self.tools['test_ECC_NIST'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_ECC_NIST'
        except ImportError as e:
            print(f"Could not import test_ECC_NIST: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Util.test_asn1 import *
            self.tools['test_asn1'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Util.test_asn1'
        except ImportError as e:
            print(f"Could not import test_asn1: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Util.test_strxor import *
            self.tools['test_strxor'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Util.test_strxor'
        except ImportError as e:
            print(f"Could not import test_strxor: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Util.test_Counter import *
            self.tools['test_Counter'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Util.test_Counter'
        except ImportError as e:
            print(f"Could not import test_Counter: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Util.test_Padding import *
            self.tools['test_Padding'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Util.test_Padding'
        except ImportError as e:
            print(f"Could not import test_Padding: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.test_eddsa import *
            self.tools['test_eddsa'] = 'thonlibs.libthon3.11.site-packages.ecdsa.test_eddsa'
        except ImportError as e:
            print(f"Could not import test_eddsa: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Signature.test_pss import *
            self.tools['test_pss'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Signature.test_pss'
        except ImportError as e:
            print(f"Could not import test_pss: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.random import *
            self.tools['random'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.random'
        except ImportError as e:
            print(f"Could not import random: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.KangarooTwelve import *
            self.tools['KangarooTwelve'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.KangarooTwelve'
        except ImportError as e:
            print(f"Could not import KangarooTwelve: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA3_256 import *
            self.tools['SHA3_256'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA3_256'
        except ImportError as e:
            print(f"Could not import SHA3_256: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA1 import *
            self.tools['SHA1'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA1'
        except ImportError as e:
            print(f"Could not import SHA1: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.HMAC import *
            self.tools['HMAC'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.HMAC'
        except ImportError as e:
            print(f"Could not import HMAC: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.MD5 import *
            self.tools['MD5'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.MD5'
        except ImportError as e:
            print(f"Could not import MD5: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.SHAKE256 import *
            self.tools['SHAKE256'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.SHAKE256'
        except ImportError as e:
            print(f"Could not import SHAKE256: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.KMAC256 import *
            self.tools['KMAC256'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.KMAC256'
        except ImportError as e:
            print(f"Could not import KMAC256: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA3_224 import *
            self.tools['SHA3_224'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA3_224'
        except ImportError as e:
            print(f"Could not import SHA3_224: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA512 import *
            self.tools['SHA512'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA512'
        except ImportError as e:
            print(f"Could not import SHA512: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.cSHAKE256 import *
            self.tools['cSHAKE256'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.cSHAKE256'
        except ImportError as e:
            print(f"Could not import cSHAKE256: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA import *
            self.tools['SHA'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA'
        except ImportError as e:
            print(f"Could not import SHA: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA3_512 import *
            self.tools['SHA3_512'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA3_512'
        except ImportError as e:
            print(f"Could not import SHA3_512: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA384 import *
            self.tools['SHA384'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA384'
        except ImportError as e:
            print(f"Could not import SHA384: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.cSHAKE128 import *
            self.tools['cSHAKE128'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.cSHAKE128'
        except ImportError as e:
            print(f"Could not import cSHAKE128: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.TurboSHAKE128 import *
            self.tools['TurboSHAKE128'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.TurboSHAKE128'
        except ImportError as e:
            print(f"Could not import TurboSHAKE128: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.Poly1305 import *
            self.tools['Poly1305'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.Poly1305'
        except ImportError as e:
            print(f"Could not import Poly1305: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA3_384 import *
            self.tools['SHA3_384'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA3_384'
        except ImportError as e:
            print(f"Could not import SHA3_384: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.SHAKE128 import *
            self.tools['SHAKE128'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.SHAKE128'
        except ImportError as e:
            print(f"Could not import SHAKE128: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.RIPEMD import *
            self.tools['RIPEMD'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.RIPEMD'
        except ImportError as e:
            print(f"Could not import RIPEMD: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.CMAC import *
            self.tools['CMAC'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.CMAC'
        except ImportError as e:
            print(f"Could not import CMAC: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.MD2 import *
            self.tools['MD2'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.MD2'
        except ImportError as e:
            print(f"Could not import MD2: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.keccak import *
            self.tools['keccak'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.keccak'
        except ImportError as e:
            print(f"Could not import keccak: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA224 import *
            self.tools['SHA224'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA224'
        except ImportError as e:
            print(f"Could not import SHA224: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.RIPEMD160 import *
            self.tools['RIPEMD160'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.RIPEMD160'
        except ImportError as e:
            print(f"Could not import RIPEMD160: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.TupleHash128 import *
            self.tools['TupleHash128'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.TupleHash128'
        except ImportError as e:
            print(f"Could not import TupleHash128: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA256 import *
            self.tools['SHA256'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.SHA256'
        except ImportError as e:
            print(f"Could not import SHA256: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Math._IntegerBase import *
            self.tools['_IntegerBase'] = 'thonlibs.libthon3.11.site-packages.Crypto.Math._IntegerBase'
        except ImportError as e:
            print(f"Could not import _IntegerBase: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Math.Numbers import *
            self.tools['Numbers'] = 'thonlibs.libthon3.11.site-packages.Crypto.Math.Numbers'
        except ImportError as e:
            print(f"Could not import Numbers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Math._IntegerCustom import *
            self.tools['_IntegerCustom'] = 'thonlibs.libthon3.11.site-packages.Crypto.Math._IntegerCustom'
        except ImportError as e:
            print(f"Could not import _IntegerCustom: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Math._IntegerGMP import *
            self.tools['_IntegerGMP'] = 'thonlibs.libthon3.11.site-packages.Crypto.Math._IntegerGMP'
        except ImportError as e:
            print(f"Could not import _IntegerGMP: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Math._IntegerNative import *
            self.tools['_IntegerNative'] = 'thonlibs.libthon3.11.site-packages.Crypto.Math._IntegerNative'
        except ImportError as e:
            print(f"Could not import _IntegerNative: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Math.Primality import *
            self.tools['Primality'] = 'thonlibs.libthon3.11.site-packages.Crypto.Math.Primality'
        except ImportError as e:
            print(f"Could not import Primality: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Protocol.DH import *
            self.tools['DH'] = 'thonlibs.libthon3.11.site-packages.Crypto.Protocol.DH'
        except ImportError as e:
            print(f"Could not import DH: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Protocol.SecretSharing import *
            self.tools['SecretSharing'] = 'thonlibs.libthon3.11.site-packages.Crypto.Protocol.SecretSharing'
        except ImportError as e:
            print(f"Could not import SecretSharing: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.PublicKey._edwards import *
            self.tools['_edwards'] = 'thonlibs.libthon3.11.site-packages.Crypto.PublicKey._edwards'
        except ImportError as e:
            print(f"Could not import _edwards: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.PublicKey._nist_ecc import *
            self.tools['_nist_ecc'] = 'thonlibs.libthon3.11.site-packages.Crypto.PublicKey._nist_ecc'
        except ImportError as e:
            print(f"Could not import _nist_ecc: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.PublicKey.ElGamal import *
            self.tools['ElGamal'] = 'thonlibs.libthon3.11.site-packages.Crypto.PublicKey.ElGamal'
        except ImportError as e:
            print(f"Could not import ElGamal: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.PublicKey._point import *
            self.tools['_point'] = 'thonlibs.libthon3.11.site-packages.Crypto.PublicKey._point'
        except ImportError as e:
            print(f"Could not import _point: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Util.number import *
            self.tools['number'] = 'thonlibs.libthon3.11.site-packages.Crypto.Util.number'
        except ImportError as e:
            print(f"Could not import number: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Util.strxor import *
            self.tools['strxor'] = 'thonlibs.libthon3.11.site-packages.Crypto.Util.strxor'
        except ImportError as e:
            print(f"Could not import strxor: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Util._file_system import *
            self.tools['_file_system'] = 'thonlibs.libthon3.11.site-packages.Crypto.Util._file_system'
        except ImportError as e:
            print(f"Could not import _file_system: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Util._cpu_features import *
            self.tools['_cpu_features'] = 'thonlibs.libthon3.11.site-packages.Crypto.Util._cpu_features'
        except ImportError as e:
            print(f"Could not import _cpu_features: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Util3compat import *
            self.tools['py3compat'] = 'thonlibs.libthon3.11.site-packages.Crypto.Util3compat'
        except ImportError as e:
            print(f"Could not import py3compat: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Util.Padding import *
            self.tools['Padding'] = 'thonlibs.libthon3.11.site-packages.Crypto.Util.Padding'
        except ImportError as e:
            print(f"Could not import Padding: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Signature.PKCS1_PSS import *
            self.tools['PKCS1_PSS'] = 'thonlibs.libthon3.11.site-packages.Crypto.Signature.PKCS1_PSS'
        except ImportError as e:
            print(f"Could not import PKCS1_PSS: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher.PKCS1_v1_5 import *
            self.tools['PKCS1_v1_5'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher.PKCS1_v1_5'
        except ImportError as e:
            print(f"Could not import PKCS1_v1_5: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.random._examples.cffi.extending import *
            self.tools['extending'] = 'thonlibs.libthon3.11.site-packages.numpy.random._examples.cffi.extending'
        except ImportError as e:
            print(f"Could not import extending: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.random._examples.numba.extending_distributions import *
            self.tools['extending_distributions'] = 'thonlibs.libthon3.11.site-packages.numpy.random._examples.numba.extending_distributions'
        except ImportError as e:
            print(f"Could not import extending_distributions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.ccompiler_opt import *
            self.tools['ccompiler_opt'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.ccompiler_opt'
        except ImportError as e:
            print(f"Could not import ccompiler_opt: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.ufuncs import *
            self.tools['ufuncs'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.ufuncs'
        except ImportError as e:
            print(f"Could not import ufuncs: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_mem_policy import *
            self.tools['test_mem_policy'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_mem_policy'
        except ImportError as e:
            print(f"Could not import test_mem_policy: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.matrixlib.tests.test_numeric import *
            self.tools['test_numeric'] = 'thonlibs.libthon3.11.site-packages.numpy.matrixlib.tests.test_numeric'
        except ImportError as e:
            print(f"Could not import test_numeric: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_records import *
            self.tools['test_records'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_records'
        except ImportError as e:
            print(f"Could not import test_records: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.socketio.server import *
            self.tools['server'] = 'thonlibs.libthon3.11.site-packages.socketio.server'
        except ImportError as e:
            print(f"Could not import server: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.socketio.client import *
            self.tools['client'] = 'thonlibs.libthon3.11.site-packages.socketio.client'
        except ImportError as e:
            print(f"Could not import client: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.ecdh import *
            self.tools['ecdh'] = 'thonlibs.libthon3.11.site-packages.ecdsa.ecdh'
        except ImportError as e:
            print(f"Could not import ecdh: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.coincurve.ecdsa import *
            self.tools['ecdsa'] = 'thonlibs.libthon3.11.site-packages.coincurve.ecdsa'
        except ImportError as e:
            print(f"Could not import ecdsa: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Signature.eddsa import *
            self.tools['eddsa'] = 'thonlibs.libthon3.11.site-packages.Crypto.Signature.eddsa'
        except ImportError as e:
            print(f"Could not import eddsa: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.numbertheory import *
            self.tools['numbertheory'] = 'thonlibs.libthon3.11.site-packages.ecdsa.numbertheory'
        except ImportError as e:
            print(f"Could not import numbertheory: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.test_ecdsa import *
            self.tools['test_ecdsa'] = 'thonlibs.libthon3.11.site-packages.ecdsa.test_ecdsa'
        except ImportError as e:
            print(f"Could not import test_ecdsa: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_keys import *
            self.tools['test_keys'] = 'thonlibs.libthon3.11.site-packages.tests.test_keys'
        except ImportError as e:
            print(f"Could not import test_keys: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcash.base58 import *
            self.tools['base58'] = 'thonlibs.libthon3.11.site-packages.bitcash.base58'
        except ImportError as e:
            print(f"Could not import base58: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcash.cashaddress import *
            self.tools['cashaddress'] = 'thonlibs.libthon3.11.site-packages.bitcash.cashaddress'
        except ImportError as e:
            print(f"Could not import cashaddress: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcash.cashtoken import *
            self.tools['cashtoken'] = 'thonlibs.libthon3.11.site-packages.bitcash.cashtoken'
        except ImportError as e:
            print(f"Could not import cashtoken: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask_sqlalchemy.cli import *
            self.tools['cli'] = 'thonlibs.libthon3.11.site-packages.flask_sqlalchemy.cli'
        except ImportError as e:
            print(f"Could not import cli: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.exceptions import *
            self.tools['exceptions'] = 'thonlibs.libthon3.11.site-packages.qrcode.exceptions'
        except ImportError as e:
            print(f"Could not import exceptions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.format import *
            self.tools['format'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.format'
        except ImportError as e:
            print(f"Could not import format: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcash.keygen import *
            self.tools['keygen'] = 'thonlibs.libthon3.11.site-packages.bitcash.keygen'
        except ImportError as e:
            print(f"Could not import keygen: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcash.op import *
            self.tools['op'] = 'thonlibs.libthon3.11.site-packages.bitcash.op'
        except ImportError as e:
            print(f"Could not import op: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.meta import *
            self.tools['meta'] = 'thonlibs.libthon3.11.site-packages.jinja2.meta'
        except ImportError as e:
            print(f"Could not import meta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcash.network.rates import *
            self.tools['rates'] = 'thonlibs.libthon3.11.site-packages.bitcash.network.rates'
        except ImportError as e:
            print(f"Could not import rates: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.samples import *
            self.tools['samples'] = 'thonlibs.libthon3.11.site-packages.tests.samples'
        except ImportError as e:
            print(f"Could not import samples: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_base58 import *
            self.tools['test_base58'] = 'thonlibs.libthon3.11.site-packages.tests.test_base58'
        except ImportError as e:
            print(f"Could not import test_base58: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_cashaddress import *
            self.tools['test_cashaddress'] = 'thonlibs.libthon3.11.site-packages.tests.test_cashaddress'
        except ImportError as e:
            print(f"Could not import test_cashaddress: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_cashtoken import *
            self.tools['test_cashtoken'] = 'thonlibs.libthon3.11.site-packages.tests.test_cashtoken'
        except ImportError as e:
            print(f"Could not import test_cashtoken: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_format import *
            self.tools['test_format'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_format'
        except ImportError as e:
            print(f"Could not import test_format: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_transaction import *
            self.tools['test_transaction'] = 'thonlibs.libthon3.11.site-packages.tests.test_transaction'
        except ImportError as e:
            print(f"Could not import test_transaction: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.network.test_rates import *
            self.tools['test_rates'] = 'thonlibs.libthon3.11.site-packages.tests.network.test_rates'
        except ImportError as e:
            print(f"Could not import test_rates: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.der import *
            self.tools['der'] = 'thonlibs.libthon3.11.site-packages.ecdsa.der'
        except ImportError as e:
            print(f"Could not import der: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bip32utils.BIP32Key import *
            self.tools['BIP32Key'] = 'thonlibs.libthon3.11.site-packages.bip32utils.BIP32Key'
        except ImportError as e:
            print(f"Could not import BIP32Key: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bip32utils.Base58 import *
            self.tools['Base58'] = 'thonlibs.libthon3.11.site-packages.bip32utils.Base58'
        except ImportError as e:
            print(f"Could not import Base58: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.mnemonic import *
            self.tools['mnemonic'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.mnemonic'
        except ImportError as e:
            print(f"Could not import mnemonic: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.command.bdist_wheel import *
            self.tools['bdist_wheel'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.command.bdist_wheel'
        except ImportError as e:
            print(f"Could not import bdist_wheel: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpx._main import *
            self.tools['_main'] = 'thonlibs.libthon3.11.site-packages.httpx._main'
        except ImportError as e:
            print(f"Could not import _main: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.engine.default import *
            self.tools['default'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.engine.default'
        except ImportError as e:
            print(f"Could not import default: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyiotest_plugin import *
            self.tools['pytest_plugin'] = 'thonlibs.libthon3.11.site-packages.anyiotest_plugin'
        except ImportError as e:
            print(f"Could not import pytest_plugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio._backends._asyncio import *
            self.tools['_asyncio'] = 'thonlibs.libthon3.11.site-packages.anyio._backends._asyncio'
        except ImportError as e:
            print(f"Could not import _asyncio: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio._backends._trio import *
            self.tools['_trio'] = 'thonlibs.libthon3.11.site-packages.anyio._backends._trio'
        except ImportError as e:
            print(f"Could not import _trio: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio._core._eventloop import *
            self.tools['_eventloop'] = 'thonlibs.libthon3.11.site-packages.anyio._core._eventloop'
        except ImportError as e:
            print(f"Could not import _eventloop: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio._core._sockets import *
            self.tools['_sockets'] = 'thonlibs.libthon3.11.site-packages.anyio._core._sockets'
        except ImportError as e:
            print(f"Could not import _sockets: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._backends.anyio import *
            self.tools['anyio'] = 'thonlibs.libthon3.11.site-packages.httpcore._backends.anyio'
        except ImportError as e:
            print(f"Could not import anyio: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._backends.auto import *
            self.tools['auto'] = 'thonlibs.libthon3.11.site-packages.httpcore._backends.auto'
        except ImportError as e:
            print(f"Could not import auto: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpx._transports.mock import *
            self.tools['mock'] = 'thonlibs.libthon3.11.site-packages.httpx._transports.mock'
        except ImportError as e:
            print(f"Could not import mock: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.sync import *
            self.tools['sync'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.sync'
        except ImportError as e:
            print(f"Could not import sync: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._utils._httpx import *
            self.tools['_httpx'] = 'thonlibs.libthon3.11.site-packages.anthropic._utils._httpx'
        except ImportError as e:
            print(f"Could not import _httpx: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.metadata_param import *
            self.tools['metadata_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.metadata_param'
        except ImportError as e:
            print(f"Could not import metadata_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_metadata_param import *
            self.tools['beta_metadata_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_metadata_param'
        except ImportError as e:
            print(f"Could not import beta_metadata_param: {e}")
            
        try:
            from .cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.socketpool.pool import *
            self.tools['pool'] = '.cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.socketpool.pool'
        except ImportError as e:
            print(f"Could not import pool: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.itsdangerous._json import *
            self.tools['_json'] = 'thonlibs.libthon3.11.site-packages.itsdangerous._json'
        except ImportError as e:
            print(f"Could not import _json: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.declarative.extensions import *
            self.tools['extensions'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.declarative.extensions'
        except ImportError as e:
            print(f"Could not import extensions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.TiffTags import *
            self.tools['TiffTags'] = 'thonlibs.libthon3.11.site-packages.PIL.TiffTags'
        except ImportError as e:
            print(f"Could not import TiffTags: {e}")
            
        try:
            from .cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.examples.test_gevent import *
            self.tools['test_gevent'] = '.cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.examples.test_gevent'
        except ImportError as e:
            print(f"Could not import test_gevent: {e}")
            
        try:
            from .cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.examples.test_threaded import *
            self.tools['test_threaded'] = '.cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.examples.test_threaded'
        except ImportError as e:
            print(f"Could not import test_threaded: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.examples.cython.setup import *
            self.tools['setup'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.examples.cython.setup'
        except ImportError as e:
            print(f"Could not import setup: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.cli.convert import *
            self.tools['convert'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.cli.convert'
        except ImportError as e:
            print(f"Could not import convert: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.test import *
            self.tools['test'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.test'
        except ImportError as e:
            print(f"Could not import test: {e}")
            
        try:
            from src.real_utxo_handler import *
            self.tools['real_utxo_handler'] = 'src.real_utxo_handler'
        except ImportError as e:
            print(f"Could not import real_utxo_handler: {e}")
            
        try:
            from src.utxo_scanner import *
            self.tools['utxo_scanner'] = 'src.utxo_scanner'
        except ImportError as e:
            print(f"Could not import utxo_scanner: {e}")
            
        try:
            from src.hd_wallet_derivation import *
            self.tools['hd_wallet_derivation'] = 'src.hd_wallet_derivation'
        except ImportError as e:
            print(f"Could not import hd_wallet_derivation: {e}")
            
        try:
            from src.multi_blockchain_scanner import *
            self.tools['multi_blockchain_scanner'] = 'src.multi_blockchain_scanner'
        except ImportError as e:
            print(f"Could not import multi_blockchain_scanner: {e}")
            
        try:
            from memo-desktop.node_modules.dmg-builder.vendor.ds_store.buddy import *
            self.tools['buddy'] = 'memo-desktop.node_modules.dmg-builder.vendor.ds_store.buddy'
        except ImportError as e:
            print(f"Could not import buddy: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.input import *
            self.tools['input'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.input'
        except ImportError as e:
            print(f"Could not import input: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.xcode import *
            self.tools['xcode'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.xcode'
        except ImportError as e:
            print(f"Could not import xcode: {e}")
            
        try:
            from btckeygen.keygen_script import *
            self.tools['keygen_script'] = 'btckeygen.keygen_script'
        except ImportError as e:
            print(f"Could not import keygen_script: {e}")
            
        try:
            from main_crypto_environment import *
            self.tools['main_crypto_environment'] = 'main_crypto_environment'
        except ImportError as e:
            print(f"Could not import main_crypto_environment: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.itsdangerous.serializer import *
            self.tools['serializer'] = 'thonlibs.libthon3.11.site-packages.itsdangerous.serializer'
        except ImportError as e:
            print(f"Could not import serializer: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.itsdangerous.signer import *
            self.tools['signer'] = 'thonlibs.libthon3.11.site-packages.itsdangerous.signer'
        except ImportError as e:
            print(f"Could not import signer: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask.sansio.app import *
            self.tools['app'] = 'thonlibs.libthon3.11.site-packages.flask.sansio.app'
        except ImportError as e:
            print(f"Could not import app: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask.sansio.blueprints import *
            self.tools['blueprints'] = 'thonlibs.libthon3.11.site-packages.flask.sansio.blueprints'
        except ImportError as e:
            print(f"Could not import blueprints: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.deprecated.config import *
            self.tools['config'] = 'thonlibs.libthon3.11.site-packagesdantic.deprecated.config'
        except ImportError as e:
            print(f"Could not import config: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask.ctx import *
            self.tools['ctx'] = 'thonlibs.libthon3.11.site-packages.flask.ctx'
        except ImportError as e:
            print(f"Could not import ctx: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask.debughelpers import *
            self.tools['debughelpers'] = 'thonlibs.libthon3.11.site-packages.flask.debughelpers'
        except ImportError as e:
            print(f"Could not import debughelpers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.click.globals import *
            self.tools['globals'] = 'thonlibs.libthon3.11.site-packages.click.globals'
        except ImportError as e:
            print(f"Could not import globals: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.integration.helpers import *
            self.tools['helpers'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.integration.helpers'
        except ImportError as e:
            print(f"Could not import helpers: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.logging import *
            self.tools['logging'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.logging'
        except ImportError as e:
            print(f"Could not import logging: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask.sessions import *
            self.tools['sessions'] = 'thonlibs.libthon3.11.site-packages.flask.sessions'
        except ImportError as e:
            print(f"Could not import sessions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask.signals import *
            self.tools['signals'] = 'thonlibs.libthon3.11.site-packages.flask.signals'
        except ImportError as e:
            print(f"Could not import signals: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask.templating import *
            self.tools['templating'] = 'thonlibs.libthon3.11.site-packages.flask.templating'
        except ImportError as e:
            print(f"Could not import templating: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.click.testing import *
            self.tools['testing'] = 'thonlibs.libthon3.11.site-packages.click.testing'
        except ImportError as e:
            print(f"Could not import testing: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.typing import *
            self.tools['typing'] = 'thonlibs.libthon3.11.site-packagesdantic.typing'
        except ImportError as e:
            print(f"Could not import typing: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask.views import *
            self.tools['views'] = 'thonlibs.libthon3.11.site-packages.flask.views'
        except ImportError as e:
            print(f"Could not import views: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask.wrappers import *
            self.tools['wrappers'] = 'thonlibs.libthon3.11.site-packages.flask.wrappers'
        except ImportError as e:
            print(f"Could not import wrappers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask.json.provider import *
            self.tools['provider'] = 'thonlibs.libthon3.11.site-packages.flask.json.provider'
        except ImportError as e:
            print(f"Could not import provider: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask.json.tag import *
            self.tools['tag'] = 'thonlibs.libthon3.11.site-packages.flask.json.tag'
        except ImportError as e:
            print(f"Could not import tag: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask.sansio.scaffold import *
            self.tools['scaffold'] = 'thonlibs.libthon3.11.site-packages.flask.sansio.scaffold'
        except ImportError as e:
            print(f"Could not import scaffold: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._utils._compat import *
            self.tools['_compat'] = 'thonlibs.libthon3.11.site-packages.anthropic._utils._compat'
        except ImportError as e:
            print(f"Could not import _compat: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.click._termui_impl import *
            self.tools['_termui_impl'] = 'thonlibs.libthon3.11.site-packages.click._termui_impl'
        except ImportError as e:
            print(f"Could not import _termui_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.click.decorators import *
            self.tools['decorators'] = 'thonlibs.libthon3.11.site-packages.click.decorators'
        except ImportError as e:
            print(f"Could not import decorators: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.click.shell_completion import *
            self.tools['shell_completion'] = 'thonlibs.libthon3.11.site-packages.click.shell_completion'
        except ImportError as e:
            print(f"Could not import shell_completion: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.click.termui import *
            self.tools['termui'] = 'thonlibs.libthon3.11.site-packages.click.termui'
        except ImportError as e:
            print(f"Could not import termui: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.sansio.http import *
            self.tools['http'] = 'thonlibs.libthon3.11.site-packages.werkzeug.sansio.http'
        except ImportError as e:
            print(f"Could not import http: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.security import *
            self.tools['security'] = 'thonlibs.libthon3.11.site-packages.werkzeug.security'
        except ImportError as e:
            print(f"Could not import security: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.serving import *
            self.tools['serving'] = 'thonlibs.libthon3.11.site-packages.werkzeug.serving'
        except ImportError as e:
            print(f"Could not import serving: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.testapp import *
            self.tools['testapp'] = 'thonlibs.libthon3.11.site-packages.werkzeug.testapp'
        except ImportError as e:
            print(f"Could not import testapp: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpx._transports.wsgi import *
            self.tools['wsgi'] = 'thonlibs.libthon3.11.site-packages.httpx._transports.wsgi'
        except ImportError as e:
            print(f"Could not import wsgi: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.datastructures.accept import *
            self.tools['accept'] = 'thonlibs.libthon3.11.site-packages.werkzeug.datastructures.accept'
        except ImportError as e:
            print(f"Could not import accept: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.datastructures.file_storage import *
            self.tools['file_storage'] = 'thonlibs.libthon3.11.site-packages.werkzeug.datastructures.file_storage'
        except ImportError as e:
            print(f"Could not import file_storage: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.datastructures.headers import *
            self.tools['headers'] = 'thonlibs.libthon3.11.site-packages.werkzeug.datastructures.headers'
        except ImportError as e:
            print(f"Could not import headers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.requests.structures import *
            self.tools['structures'] = 'thonlibs.libthon3.11.site-packages.requests.structures'
        except ImportError as e:
            print(f"Could not import structures: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.debug.console import *
            self.tools['console'] = 'thonlibs.libthon3.11.site-packages.werkzeug.debug.console'
        except ImportError as e:
            print(f"Could not import console: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.debug.repr import *
            self.tools['repr'] = 'thonlibs.libthon3.11.site-packages.werkzeug.debug.repr'
        except ImportError as e:
            print(f"Could not import repr: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.debug.tbtools import *
            self.tools['tbtools'] = 'thonlibs.libthon3.11.site-packages.werkzeug.debug.tbtools'
        except ImportError as e:
            print(f"Could not import tbtools: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.middleware.dispatcher import *
            self.tools['dispatcher'] = 'thonlibs.libthon3.11.site-packages.werkzeug.middleware.dispatcher'
        except ImportError as e:
            print(f"Could not import dispatcher: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._sync.http_proxy import *
            self.tools['http_proxy'] = 'thonlibs.libthon3.11.site-packages.httpcore._sync.http_proxy'
        except ImportError as e:
            print(f"Could not import http_proxy: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.middleware.shared_data import *
            self.tools['shared_data'] = 'thonlibs.libthon3.11.site-packages.werkzeug.middleware.shared_data'
        except ImportError as e:
            print(f"Could not import shared_data: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.routing.map import *
            self.tools['map'] = 'thonlibs.libthon3.11.site-packages.werkzeug.routing.map'
        except ImportError as e:
            print(f"Could not import map: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.routing.matcher import *
            self.tools['matcher'] = 'thonlibs.libthon3.11.site-packages.werkzeug.routing.matcher'
        except ImportError as e:
            print(f"Could not import matcher: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.routing.rules import *
            self.tools['rules'] = 'thonlibs.libthon3.11.site-packages.werkzeug.routing.rules'
        except ImportError as e:
            print(f"Could not import rules: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3.util.request import *
            self.tools['request'] = 'thonlibs.libthon3.11.site-packages.urllib3.util.request'
        except ImportError as e:
            print(f"Could not import request: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.bccache import *
            self.tools['bccache'] = 'thonlibs.libthon3.11.site-packages.jinja2.bccache'
        except ImportError as e:
            print(f"Could not import bccache: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.compiler import *
            self.tools['compiler'] = 'thonlibs.libthon3.11.site-packages.jinja2.compiler'
        except ImportError as e:
            print(f"Could not import compiler: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.debug import *
            self.tools['debug'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.debug'
        except ImportError as e:
            print(f"Could not import debug: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.environment import *
            self.tools['environment'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.environment'
        except ImportError as e:
            print(f"Could not import environment: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.ext import *
            self.tools['ext'] = 'thonlibs.libthon3.11.site-packages.jinja2.ext'
        except ImportError as e:
            print(f"Could not import ext: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.filters import *
            self.tools['filters'] = 'thonlibs.libthon3.11.site-packages.jinja2.filters'
        except ImportError as e:
            print(f"Could not import filters: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.idtracking import *
            self.tools['idtracking'] = 'thonlibs.libthon3.11.site-packages.jinja2.idtracking'
        except ImportError as e:
            print(f"Could not import idtracking: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.lexer import *
            self.tools['lexer'] = 'thonlibs.libthon3.11.site-packages.jinja2.lexer'
        except ImportError as e:
            print(f"Could not import lexer: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.loaders import *
            self.tools['loaders'] = 'thonlibs.libthon3.11.site-packages.jinja2.loaders'
        except ImportError as e:
            print(f"Could not import loaders: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.nativetypes import *
            self.tools['nativetypes'] = 'thonlibs.libthon3.11.site-packages.jinja2.nativetypes'
        except ImportError as e:
            print(f"Could not import nativetypes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.nodes import *
            self.tools['nodes'] = 'thonlibs.libthon3.11.site-packages.jinja2.nodes'
        except ImportError as e:
            print(f"Could not import nodes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.click.parser import *
            self.tools['parser'] = 'thonlibs.libthon3.11.site-packages.click.parser'
        except ImportError as e:
            print(f"Could not import parser: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.runtime import *
            self.tools['runtime'] = 'thonlibs.libthon3.11.site-packages.jinja2.runtime'
        except ImportError as e:
            print(f"Could not import runtime: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.sandbox import *
            self.tools['sandbox'] = 'thonlibs.libthon3.11.site-packages.setuptools.sandbox'
        except ImportError as e:
            print(f"Could not import sandbox: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.tests import *
            self.tools['tests'] = 'thonlibs.libthon3.11.site-packages.jinja2.tests'
        except ImportError as e:
            print(f"Could not import tests: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.requests.adapters import *
            self.tools['adapters'] = 'thonlibs.libthon3.11.site-packages.requests.adapters'
        except ImportError as e:
            print(f"Could not import adapters: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.requests.cookies import *
            self.tools['cookies'] = 'thonlibs.libthon3.11.site-packages.requests.cookies'
        except ImportError as e:
            print(f"Could not import cookies: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.typing_extensions import *
            self.tools['typing_extensions'] = 'thonlibs.libthon3.11.site-packages.typing_extensions'
        except ImportError as e:
            print(f"Could not import typing_extensions: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.importlib_metadata._collections import *
            self.tools['_collections'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.importlib_metadata._collections'
        except ImportError as e:
            print(f"Could not import _collections: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3.connectionpool import *
            self.tools['connectionpool'] = 'thonlibs.libthon3.11.site-packages.urllib3.connectionpool'
        except ImportError as e:
            print(f"Could not import connectionpool: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.v1.fields import *
            self.tools['fields'] = 'thonlibs.libthon3.11.site-packagesdantic.v1.fields'
        except ImportError as e:
            print(f"Could not import fields: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3.contribopenssl import *
            self.tools['pyopenssl'] = 'thonlibs.libthon3.11.site-packages.urllib3.contribopenssl'
        except ImportError as e:
            print(f"Could not import pyopenssl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3.contrib.socks import *
            self.tools['socks'] = 'thonlibs.libthon3.11.site-packages.urllib3.contrib.socks'
        except ImportError as e:
            print(f"Could not import socks: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3.contrib.emscripten.fetch import *
            self.tools['fetch'] = 'thonlibs.libthon3.11.site-packages.urllib3.contrib.emscripten.fetch'
        except ImportError as e:
            print(f"Could not import fetch: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3.util.retry import *
            self.tools['retry'] = 'thonlibs.libthon3.11.site-packages.urllib3.util.retry'
        except ImportError as e:
            print(f"Could not import retry: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3.util.ssl_match_hostname import *
            self.tools['ssl_match_hostname'] = 'thonlibs.libthon3.11.site-packages.urllib3.util.ssl_match_hostname'
        except ImportError as e:
            print(f"Could not import ssl_match_hostname: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.engine.url import *
            self.tools['url'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.engine.url'
        except ImportError as e:
            print(f"Could not import url: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcash.curve import *
            self.tools['curve'] = 'thonlibs.libthon3.11.site-packages.bitcash.curve'
        except ImportError as e:
            print(f"Could not import curve: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.fastecdsa.encoding.pem import *
            self.tools['pem'] = 'thonlibs.libthon3.11.site-packages.fastecdsa.encoding.pem'
        except ImportError as e:
            print(f"Could not import pem: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.blocks import *
            self.tools['blocks'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.blocks'
        except ImportError as e:
            print(f"Could not import blocks: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.db import *
            self.tools['db'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.db'
        except ImportError as e:
            print(f"Could not import db: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.db_cache import *
            self.tools['db_cache'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.db_cache'
        except ImportError as e:
            print(f"Could not import db_cache: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.itsdangerous.encoding import *
            self.tools['encoding'] = 'thonlibs.libthon3.11.site-packages.itsdangerous.encoding'
        except ImportError as e:
            print(f"Could not import encoding: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.main import *
            self.tools['main'] = 'thonlibs.libthon3.11.site-packages.qrcode.main'
        except ImportError as e:
            print(f"Could not import main: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.v1.networks import *
            self.tools['networks'] = 'thonlibs.libthon3.11.site-packagesdantic.v1.networks'
        except ImportError as e:
            print(f"Could not import networks: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.scripts import *
            self.tools['scripts'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.scripts'
        except ImportError as e:
            print(f"Could not import scripts: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.transactions import *
            self.tools['transactions'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.transactions'
        except ImportError as e:
            print(f"Could not import transactions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.values import *
            self.tools['values'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.values'
        except ImportError as e:
            print(f"Could not import values: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.wallets import *
            self.tools['wallets'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.wallets'
        except ImportError as e:
            print(f"Could not import wallets: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.config.opcodes import *
            self.tools['opcodes'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.config.opcodes'
        except ImportError as e:
            print(f"Could not import opcodes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.config.secp256k1 import *
            self.tools['secp256k1'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.config.secp256k1'
        except ImportError as e:
            print(f"Could not import secp256k1: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.baseclient import *
            self.tools['baseclient'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.baseclient'
        except ImportError as e:
            print(f"Could not import baseclient: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.bcoin import *
            self.tools['bcoin'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.bcoin'
        except ImportError as e:
            print(f"Could not import bcoin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.bitaps import *
            self.tools['bitaps'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.bitaps'
        except ImportError as e:
            print(f"Could not import bitaps: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.bitcoind import *
            self.tools['bitcoind'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.bitcoind'
        except ImportError as e:
            print(f"Could not import bitcoind: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.bitcoinlibtest import *
            self.tools['bitcoinlibtest'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.bitcoinlibtest'
        except ImportError as e:
            print(f"Could not import bitcoinlibtest: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.bitflyer import *
            self.tools['bitflyer'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.bitflyer'
        except ImportError as e:
            print(f"Could not import bitflyer: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.bitgo import *
            self.tools['bitgo'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.bitgo'
        except ImportError as e:
            print(f"Could not import bitgo: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.blockbook import *
            self.tools['blockbook'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.blockbook'
        except ImportError as e:
            print(f"Could not import blockbook: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.blockchaininfo import *
            self.tools['blockchaininfo'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.blockchaininfo'
        except ImportError as e:
            print(f"Could not import blockchaininfo: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.blockchair import *
            self.tools['blockchair'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.blockchair'
        except ImportError as e:
            print(f"Could not import blockchair: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.blockcypher import *
            self.tools['blockcypher'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.blockcypher'
        except ImportError as e:
            print(f"Could not import blockcypher: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.blocksmurfer import *
            self.tools['blocksmurfer'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.blocksmurfer'
        except ImportError as e:
            print(f"Could not import blocksmurfer: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.blockstream import *
            self.tools['blockstream'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.blockstream'
        except ImportError as e:
            print(f"Could not import blockstream: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.chainso import *
            self.tools['chainso'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.chainso'
        except ImportError as e:
            print(f"Could not import chainso: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.cryptoid import *
            self.tools['cryptoid'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.cryptoid'
        except ImportError as e:
            print(f"Could not import cryptoid: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.dogecoind import *
            self.tools['dogecoind'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.dogecoind'
        except ImportError as e:
            print(f"Could not import dogecoind: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.litecoinblockexplorer import *
            self.tools['litecoinblockexplorer'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.litecoinblockexplorer'
        except ImportError as e:
            print(f"Could not import litecoinblockexplorer: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.litecoind import *
            self.tools['litecoind'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.litecoind'
        except ImportError as e:
            print(f"Could not import litecoind: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.litecoreio import *
            self.tools['litecoreio'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.litecoreio'
        except ImportError as e:
            print(f"Could not import litecoreio: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.mempool import *
            self.tools['mempool'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.mempool'
        except ImportError as e:
            print(f"Could not import mempool: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcash.network.services import *
            self.tools['services'] = 'thonlibs.libthon3.11.site-packages.bitcash.network.services'
        except ImportError as e:
            print(f"Could not import services: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.fastecdsa.benchmark import *
            self.tools['benchmark'] = 'thonlibs.libthon3.11.site-packages.fastecdsa.benchmark'
        except ImportError as e:
            print(f"Could not import benchmark: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.tools.clw import *
            self.tools['clw'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.tools.clw'
        except ImportError as e:
            print(f"Could not import clw: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.tools.import_database import *
            self.tools['import_database'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.tools.import_database'
        except ImportError as e:
            print(f"Could not import import_database: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.tools.mnemonic_key_create import *
            self.tools['mnemonic_key_create'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.tools.mnemonic_key_create'
        except ImportError as e:
            print(f"Could not import mnemonic_key_create: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.tools.sign_raw import *
            self.tools['sign_raw'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.tools.sign_raw'
        except ImportError as e:
            print(f"Could not import sign_raw: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.tools.wallet_multisig_2of3 import *
            self.tools['wallet_multisig_2of3'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.tools.wallet_multisig_2of3'
        except ImportError as e:
            print(f"Could not import wallet_multisig_2of3: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_blocks import *
            self.tools['test_blocks'] = 'thonlibs.libthon3.11.site-packages.tests.test_blocks'
        except ImportError as e:
            print(f"Could not import test_blocks: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_custom import *
            self.tools['test_custom'] = 'thonlibs.libthon3.11.site-packages.tests.test_custom'
        except ImportError as e:
            print(f"Could not import test_custom: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_db import *
            self.tools['test_db'] = 'thonlibs.libthon3.11.site-packages.tests.test_db'
        except ImportError as e:
            print(f"Could not import test_db: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_encoding import *
            self.tools['test_encoding'] = 'thonlibs.libthon3.11.site-packages.tests.test_encoding'
        except ImportError as e:
            print(f"Could not import test_encoding: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_mnemonic import *
            self.tools['test_mnemonic'] = 'thonlibs.libthon3.11.site-packages.tests.test_mnemonic'
        except ImportError as e:
            print(f"Could not import test_mnemonic: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_networks import *
            self.tools['test_networks'] = 'thonlibs.libthon3.11.site-packages.tests.test_networks'
        except ImportError as e:
            print(f"Could not import test_networks: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.tests.test_script import *
            self.tools['test_script'] = 'thonlibs.libthon3.11.site-packages.qrcode.tests.test_script'
        except ImportError as e:
            print(f"Could not import test_script: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_security import *
            self.tools['test_security'] = 'thonlibs.libthon3.11.site-packages.tests.test_security'
        except ImportError as e:
            print(f"Could not import test_security: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_tools import *
            self.tools['test_tools'] = 'thonlibs.libthon3.11.site-packages.tests.test_tools'
        except ImportError as e:
            print(f"Could not import test_tools: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_transactions import *
            self.tools['test_transactions'] = 'thonlibs.libthon3.11.site-packages.tests.test_transactions'
        except ImportError as e:
            print(f"Could not import test_transactions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_values import *
            self.tools['test_values'] = 'thonlibs.libthon3.11.site-packages.tests.test_values'
        except ImportError as e:
            print(f"Could not import test_values: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_wallets import *
            self.tools['test_wallets'] = 'thonlibs.libthon3.11.site-packages.tests.test_wallets'
        except ImportError as e:
            print(f"Could not import test_wallets: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.pool.events import *
            self.tools['events'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.pool.events'
        except ImportError as e:
            print(f"Could not import events: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.itsdangerous.exc import *
            self.tools['exc'] = 'thonlibs.libthon3.11.site-packages.itsdangerous.exc'
        except ImportError as e:
            print(f"Could not import exc: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.inspection import *
            self.tools['inspection'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.inspection'
        except ImportError as e:
            print(f"Could not import inspection: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.engine.cursor import *
            self.tools['cursor'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.engine.cursor'
        except ImportError as e:
            print(f"Could not import cursor: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.engine.create import *
            self.tools['create'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.engine.create'
        except ImportError as e:
            print(f"Could not import create: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.engine.row import *
            self.tools['row'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.engine.row'
        except ImportError as e:
            print(f"Could not import row: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql._py_util import *
            self.tools['_py_util'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql._py_util'
        except ImportError as e:
            print(f"Could not import _py_util: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.engine.characteristics import *
            self.tools['characteristics'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.engine.characteristics'
        except ImportError as e:
            print(f"Could not import characteristics: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.reflection import *
            self.tools['reflection'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.reflection'
        except ImportError as e:
            print(f"Could not import reflection: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.asyncio.result import *
            self.tools['result'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.asyncio.result'
        except ImportError as e:
            print(f"Could not import result: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._sync.interfaces import *
            self.tools['interfaces'] = 'thonlibs.libthon3.11.site-packages.httpcore._sync.interfaces'
        except ImportError as e:
            print(f"Could not import interfaces: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.ddl import *
            self.tools['ddl'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.ddl'
        except ImportError as e:
            print(f"Could not import ddl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.coercions import *
            self.tools['coercions'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.coercions'
        except ImportError as e:
            print(f"Could not import coercions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.sqlite.dml import *
            self.tools['dml'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.sqlite.dml'
        except ImportError as e:
            print(f"Could not import dml: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.cache_key import *
            self.tools['cache_key'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.cache_key'
        except ImportError as e:
            print(f"Could not import cache_key: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.sqltypes import *
            self.tools['sqltypes'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.sqltypes'
        except ImportError as e:
            print(f"Could not import sqltypes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.naming import *
            self.tools['naming'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.naming'
        except ImportError as e:
            print(f"Could not import naming: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.schema import *
            self.tools['schema'] = 'thonlibs.libthon3.11.site-packagesdantic.schema'
        except ImportError as e:
            print(f"Could not import schema: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.selectable import *
            self.tools['selectable'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.selectable'
        except ImportError as e:
            print(f"Could not import selectable: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.functions import *
            self.tools['functions'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.functions'
        except ImportError as e:
            print(f"Could not import functions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.visitors import *
            self.tools['visitors'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.visitors'
        except ImportError as e:
            print(f"Could not import visitors: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.type_api import *
            self.tools['type_api'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.type_api'
        except ImportError as e:
            print(f"Could not import type_api: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.operators import *
            self.tools['operators'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.operators'
        except ImportError as e:
            print(f"Could not import operators: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.elements import *
            self.tools['elements'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.elements'
        except ImportError as e:
            print(f"Could not import elements: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging.requirements import *
            self.tools['requirements'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging.requirements'
        except ImportError as e:
            print(f"Could not import requirements: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.assertions import *
            self.tools['assertions'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.assertions'
        except ImportError as e:
            print(f"Could not import assertions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_select import *
            self.tools['test_select'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_select'
        except ImportError as e:
            print(f"Could not import test_select: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.plugintestplugin import *
            self.tools['pytestplugin'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.plugintestplugin'
        except ImportError as e:
            print(f"Could not import pytestplugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.plugin.plugin_base import *
            self.tools['plugin_base'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.plugin.plugin_base'
        except ImportError as e:
            print(f"Could not import plugin_base: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mssql.provision import *
            self.tools['provision'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mssql.provision'
        except ImportError as e:
            print(f"Could not import provision: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.v1.types import *
            self.tools['types'] = 'thonlibs.libthon3.11.site-packagesdantic.v1.types'
        except ImportError as e:
            print(f"Could not import types: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.oracle.oracledb import *
            self.tools['oracledb'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.oracle.oracledb'
        except ImportError as e:
            print(f"Could not import oracledb: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.oracle.dictionary import *
            self.tools['dictionary'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.oracle.dictionary'
        except ImportError as e:
            print(f"Could not import dictionary: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.oracle.cx_oracle import *
            self.tools['cx_oracle'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.oracle.cx_oracle'
        except ImportError as e:
            print(f"Could not import cx_oracle: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.reserved_words import *
            self.tools['reserved_words'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.reserved_words'
        except ImportError as e:
            print(f"Could not import reserved_words: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.mysqlconnector import *
            self.tools['mysqlconnector'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.mysqlconnector'
        except ImportError as e:
            print(f"Could not import mysqlconnector: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.asyncmy import *
            self.tools['asyncmy'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.asyncmy'
        except ImportError as e:
            print(f"Could not import asyncmy: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.cymysql import *
            self.tools['cymysql'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.cymysql'
        except ImportError as e:
            print(f"Could not import cymysql: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.aiomysql import *
            self.tools['aiomysql'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.aiomysql'
        except ImportError as e:
            print(f"Could not import aiomysql: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.psycopg import *
            self.tools['psycopg'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.psycopg'
        except ImportError as e:
            print(f"Could not import psycopg: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.psycopg2 import *
            self.tools['psycopg2'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.psycopg2'
        except ImportError as e:
            print(f"Could not import psycopg2: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.pg8000 import *
            self.tools['pg8000'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.pg8000'
        except ImportError as e:
            print(f"Could not import pg8000: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.asyncpg import *
            self.tools['asyncpg'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.asyncpg'
        except ImportError as e:
            print(f"Could not import asyncpg: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.named_types import *
            self.tools['named_types'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.named_types'
        except ImportError as e:
            print(f"Could not import named_types: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.ranges import *
            self.tools['ranges'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.ranges'
        except ImportError as e:
            print(f"Could not import ranges: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql._psycopg_common import *
            self.tools['_psycopg_common'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql._psycopg_common'
        except ImportError as e:
            print(f"Could not import _psycopg_common: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.sqlite.aiosqlite import *
            self.tools['aiosqlite'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.sqlite.aiosqlite'
        except ImportError as e:
            print(f"Could not import aiosqlite: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.sqlitesqlite import *
            self.tools['pysqlite'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.sqlitesqlite'
        except ImportError as e:
            print(f"Could not import pysqlite: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mssqlmssql import *
            self.tools['pymssql'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mssqlmssql'
        except ImportError as e:
            print(f"Could not import pymssql: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mssql.aioodbc import *
            self.tools['aioodbc'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mssql.aioodbc'
        except ImportError as e:
            print(f"Could not import aioodbc: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.collections import *
            self.tools['collections'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.collections'
        except ImportError as e:
            print(f"Could not import collections: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.properties import *
            self.tools['properties'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.properties'
        except ImportError as e:
            print(f"Could not import properties: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.state import *
            self.tools['state'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.state'
        except ImportError as e:
            print(f"Could not import state: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.coincurve.context import *
            self.tools['context'] = 'thonlibs.libthon3.11.site-packages.coincurve.context'
        except ImportError as e:
            print(f"Could not import context: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.unitofwork import *
            self.tools['unitofwork'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.unitofwork'
        except ImportError as e:
            print(f"Could not import unitofwork: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask_sqlalchemy.session import *
            self.tools['session'] = 'thonlibs.libthon3.11.site-packages.flask_sqlalchemy.session'
        except ImportError as e:
            print(f"Could not import session: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.strategy_options import *
            self.tools['strategy_options'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.strategy_options'
        except ImportError as e:
            print(f"Could not import strategy_options: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask_sqlalchemy.query import *
            self.tools['query'] = 'thonlibs.libthon3.11.site-packages.flask_sqlalchemy.query'
        except ImportError as e:
            print(f"Could not import query: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.bulk_persistence import *
            self.tools['bulk_persistence'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.bulk_persistence'
        except ImportError as e:
            print(f"Could not import bulk_persistence: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL._typing import *
            self.tools['_typing'] = 'thonlibs.libthon3.11.site-packages.PIL._typing'
        except ImportError as e:
            print(f"Could not import _typing: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.asyncio.scoping import *
            self.tools['scoping'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.asyncio.scoping'
        except ImportError as e:
            print(f"Could not import scoping: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.clsregistry import *
            self.tools['clsregistry'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.clsregistry'
        except ImportError as e:
            print(f"Could not import clsregistry: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm._orm_constructors import *
            self.tools['_orm_constructors'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm._orm_constructors'
        except ImportError as e:
            print(f"Could not import _orm_constructors: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.writeonly import *
            self.tools['writeonly'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.writeonly'
        except ImportError as e:
            print(f"Could not import writeonly: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.path_registry import *
            self.tools['path_registry'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.path_registry'
        except ImportError as e:
            print(f"Could not import path_registry: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.attributes import *
            self.tools['attributes'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.attributes'
        except ImportError as e:
            print(f"Could not import attributes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.engine.strategies import *
            self.tools['strategies'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.engine.strategies'
        except ImportError as e:
            print(f"Could not import strategies: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.descriptor_props import *
            self.tools['descriptor_props'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.descriptor_props'
        except ImportError as e:
            print(f"Could not import descriptor_props: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.dependency import *
            self.tools['dependency'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.dependency'
        except ImportError as e:
            print(f"Could not import dependency: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.relationships import *
            self.tools['relationships'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.relationships'
        except ImportError as e:
            print(f"Could not import relationships: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.mapper import *
            self.tools['mapper'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.mapper'
        except ImportError as e:
            print(f"Could not import mapper: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.decl_api import *
            self.tools['decl_api'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.decl_api'
        except ImportError as e:
            print(f"Could not import decl_api: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.instrumentation import *
            self.tools['instrumentation'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.instrumentation'
        except ImportError as e:
            print(f"Could not import instrumentation: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.loading import *
            self.tools['loading'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.loading'
        except ImportError as e:
            print(f"Could not import loading: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.decl_base import *
            self.tools['decl_base'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.decl_base'
        except ImportError as e:
            print(f"Could not import decl_base: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.util.langhelpers import *
            self.tools['langhelpers'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.util.langhelpers'
        except ImportError as e:
            print(f"Could not import langhelpers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.util.topological import *
            self.tools['topological'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.util.topological'
        except ImportError as e:
            print(f"Could not import topological: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.util._concurrency_py3k import *
            self.tools['_concurrency_py3k'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.util._concurrency_py3k'
        except ImportError as e:
            print(f"Could not import _concurrency_py3k: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.util.deprecations import *
            self.tools['deprecations'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.util.deprecations'
        except ImportError as e:
            print(f"Could not import deprecations: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.hybrid import *
            self.tools['hybrid'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.hybrid'
        except ImportError as e:
            print(f"Could not import hybrid: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.automap import *
            self.tools['automap'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.automap'
        except ImportError as e:
            print(f"Could not import automap: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.horizontal_shard import *
            self.tools['horizontal_shard'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.horizontal_shard'
        except ImportError as e:
            print(f"Could not import horizontal_shard: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.associationproxy import *
            self.tools['associationproxy'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.associationproxy'
        except ImportError as e:
            print(f"Could not import associationproxy: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.indexable import *
            self.tools['indexable'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.indexable'
        except ImportError as e:
            print(f"Could not import indexable: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.mypy.names import *
            self.tools['names'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.mypy.names'
        except ImportError as e:
            print(f"Could not import names: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.mypy.decl_class import *
            self.tools['decl_class'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.mypy.decl_class'
        except ImportError as e:
            print(f"Could not import decl_class: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.mypy.apply import *
            self.tools['apply'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.mypy.apply'
        except ImportError as e:
            print(f"Could not import apply: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.mypy.infer import *
            self.tools['infer'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.mypy.infer'
        except ImportError as e:
            print(f"Could not import infer: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.mypy.plugin import *
            self.tools['plugin'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.mypy.plugin'
        except ImportError as e:
            print(f"Could not import plugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.future.engine import *
            self.tools['engine'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.future.engine'
        except ImportError as e:
            print(f"Could not import engine: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.charset_normalizer.api import *
            self.tools['api'] = 'thonlibs.libthon3.11.site-packages.charset_normalizer.api'
        except ImportError as e:
            print(f"Could not import api: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.event.attr import *
            self.tools['attr'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.event.attr'
        except ImportError as e:
            print(f"Could not import attr: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.pool.impl import *
            self.tools['impl'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.pool.impl'
        except ImportError as e:
            print(f"Could not import impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher._EKSBlowfish import *
            self.tools['_EKSBlowfish'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher._EKSBlowfish'
        except ImportError as e:
            print(f"Could not import _EKSBlowfish: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_ccm import *
            self.tools['_mode_ccm'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_ccm'
        except ImportError as e:
            print(f"Could not import _mode_ccm: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_siv import *
            self.tools['_mode_siv'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_siv'
        except ImportError as e:
            print(f"Could not import _mode_siv: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher.ChaCha20 import *
            self.tools['ChaCha20'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher.ChaCha20'
        except ImportError as e:
            print(f"Could not import ChaCha20: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_eax import *
            self.tools['_mode_eax'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_eax'
        except ImportError as e:
            print(f"Could not import _mode_eax: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher.ARC4 import *
            self.tools['ARC4'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher.ARC4'
        except ImportError as e:
            print(f"Could not import ARC4: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_ocb import *
            self.tools['_mode_ocb'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_ocb'
        except ImportError as e:
            print(f"Could not import _mode_ocb: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher.Salsa20 import *
            self.tools['Salsa20'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher.Salsa20'
        except ImportError as e:
            print(f"Could not import Salsa20: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_gcm import *
            self.tools['_mode_gcm'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_gcm'
        except ImportError as e:
            print(f"Could not import _mode_gcm: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_openpgp import *
            self.tools['_mode_openpgp'] = 'thonlibs.libthon3.11.site-packages.Crypto.Cipher._mode_openpgp'
        except ImportError as e:
            print(f"Could not import _mode_openpgp: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_ChaCha20 import *
            self.tools['test_ChaCha20'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_ChaCha20'
        except ImportError as e:
            print(f"Could not import test_ChaCha20: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_ChaCha20_Poly1305 import *
            self.tools['test_ChaCha20_Poly1305'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_ChaCha20_Poly1305'
        except ImportError as e:
            print(f"Could not import test_ChaCha20_Poly1305: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_ARC4 import *
            self.tools['test_ARC4'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_ARC4'
        except ImportError as e:
            print(f"Could not import test_ARC4: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_EAX import *
            self.tools['test_EAX'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Cipher.test_EAX'
        except ImportError as e:
            print(f"Could not import test_EAX: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_KMAC import *
            self.tools['test_KMAC'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_KMAC'
        except ImportError as e:
            print(f"Could not import test_KMAC: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_Poly1305 import *
            self.tools['test_Poly1305'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_Poly1305'
        except ImportError as e:
            print(f"Could not import test_Poly1305: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_BLAKE2 import *
            self.tools['test_BLAKE2'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_BLAKE2'
        except ImportError as e:
            print(f"Could not import test_BLAKE2: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_HMAC import *
            self.tools['test_HMAC'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_HMAC'
        except ImportError as e:
            print(f"Could not import test_HMAC: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_RIPEMD160 import *
            self.tools['test_RIPEMD160'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Hash.test_RIPEMD160'
        except ImportError as e:
            print(f"Could not import test_RIPEMD160: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Protocol.test_KDF import *
            self.tools['test_KDF'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Protocol.test_KDF'
        except ImportError as e:
            print(f"Could not import test_KDF: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_import_DSA import *
            self.tools['test_import_DSA'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.PublicKey.test_import_DSA'
        except ImportError as e:
            print(f"Could not import test_import_DSA: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Util.test_number import *
            self.tools['test_number'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Util.test_number'
        except ImportError as e:
            print(f"Could not import test_number: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Signature.test_dss import *
            self.tools['test_dss'] = 'thonlibs.libthon3.11.site-packages.Crypto.SelfTest.Signature.test_dss'
        except ImportError as e:
            print(f"Could not import test_dss: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.BLAKE2s import *
            self.tools['BLAKE2s'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.BLAKE2s'
        except ImportError as e:
            print(f"Could not import BLAKE2s: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.BLAKE2b import *
            self.tools['BLAKE2b'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.BLAKE2b'
        except ImportError as e:
            print(f"Could not import BLAKE2b: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.MD4 import *
            self.tools['MD4'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.MD4'
        except ImportError as e:
            print(f"Could not import MD4: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.KMAC128 import *
            self.tools['KMAC128'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.KMAC128'
        except ImportError as e:
            print(f"Could not import KMAC128: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Protocol.KDF import *
            self.tools['KDF'] = 'thonlibs.libthon3.11.site-packages.Crypto.Protocol.KDF'
        except ImportError as e:
            print(f"Could not import KDF: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.PublicKey.ECC import *
            self.tools['ECC'] = 'thonlibs.libthon3.11.site-packages.Crypto.PublicKey.ECC'
        except ImportError as e:
            print(f"Could not import ECC: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.PublicKey._openssh import *
            self.tools['_openssh'] = 'thonlibs.libthon3.11.site-packages.Crypto.PublicKey._openssh'
        except ImportError as e:
            print(f"Could not import _openssh: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.PublicKey.DSA import *
            self.tools['DSA'] = 'thonlibs.libthon3.11.site-packages.Crypto.PublicKey.DSA'
        except ImportError as e:
            print(f"Could not import DSA: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.PublicKey.RSA import *
            self.tools['RSA'] = 'thonlibs.libthon3.11.site-packages.Crypto.PublicKey.RSA'
        except ImportError as e:
            print(f"Could not import RSA: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.PublicKey._montgomery import *
            self.tools['_montgomery'] = 'thonlibs.libthon3.11.site-packages.Crypto.PublicKey._montgomery'
        except ImportError as e:
            print(f"Could not import _montgomery: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Util.RFC1751 import *
            self.tools['RFC1751'] = 'thonlibs.libthon3.11.site-packages.Crypto.Util.RFC1751'
        except ImportError as e:
            print(f"Could not import RFC1751: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Util._raw_api import *
            self.tools['_raw_api'] = 'thonlibs.libthon3.11.site-packages.Crypto.Util._raw_api'
        except ImportError as e:
            print(f"Could not import _raw_api: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Signature.pss import *
            self.tools['pss'] = 'thonlibs.libthon3.11.site-packages.Crypto.Signature.pss'
        except ImportError as e:
            print(f"Could not import pss: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Signature.DSS import *
            self.tools['DSS'] = 'thonlibs.libthon3.11.site-packages.Crypto.Signature.DSS'
        except ImportError as e:
            print(f"Could not import DSS: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Signature.pkcs1_15 import *
            self.tools['pkcs1_15'] = 'thonlibs.libthon3.11.site-packages.Crypto.Signature.pkcs1_15'
        except ImportError as e:
            print(f"Could not import pkcs1_15: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.ctypeslib import *
            self.tools['ctypeslib'] = 'thonlibs.libthon3.11.site-packages.numpy.ctypeslib'
        except ImportError as e:
            print(f"Could not import ctypeslib: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.matlib import *
            self.tools['matlib'] = 'thonlibs.libthon3.11.site-packages.numpy.matlib'
        except ImportError as e:
            print(f"Could not import matlib: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.conftest import *
            self.tools['conftest'] = 'thonlibs.libthon3.11.site-packages.numpy.conftest'
        except ImportError as e:
            print(f"Could not import conftest: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._array_api_info import *
            self.tools['_array_api_info'] = 'thonlibs.libthon3.11.site-packages.numpy._array_api_info'
        except ImportError as e:
            print(f"Could not import _array_api_info: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.random.tests.test_direct import *
            self.tools['test_direct'] = 'thonlibs.libthon3.11.site-packages.numpy.random.tests.test_direct'
        except ImportError as e:
            print(f"Could not import test_direct: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.random.tests.test_randomstate import *
            self.tools['test_randomstate'] = 'thonlibs.libthon3.11.site-packages.numpy.random.tests.test_randomstate'
        except ImportError as e:
            print(f"Could not import test_randomstate: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.random.tests.test_generator_mt19937 import *
            self.tools['test_generator_mt19937'] = 'thonlibs.libthon3.11.site-packages.numpy.random.tests.test_generator_mt19937'
        except ImportError as e:
            print(f"Could not import test_generator_mt19937: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._typing._dtype_like import *
            self.tools['_dtype_like'] = 'thonlibs.libthon3.11.site-packages.numpy._typing._dtype_like'
        except ImportError as e:
            print(f"Could not import _dtype_like: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.from_template import *
            self.tools['from_template'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.from_template'
        except ImportError as e:
            print(f"Could not import from_template: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.conv_template import *
            self.tools['conv_template'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.conv_template'
        except ImportError as e:
            print(f"Could not import conv_template: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.system_info import *
            self.tools['system_info'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.system_info'
        except ImportError as e:
            print(f"Could not import system_info: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.cpuinfo import *
            self.tools['cpuinfo'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.cpuinfo'
        except ImportError as e:
            print(f"Could not import cpuinfo: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.mingw32ccompiler import *
            self.tools['mingw32ccompiler'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.mingw32ccompiler'
        except ImportError as e:
            print(f"Could not import mingw32ccompiler: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.misc_util import *
            self.tools['misc_util'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.misc_util'
        except ImportError as e:
            print(f"Could not import misc_util: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_from_template import *
            self.tools['test_from_template'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_from_template'
        except ImportError as e:
            print(f"Could not import test_from_template: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_ccompiler_opt import *
            self.tools['test_ccompiler_opt'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_ccompiler_opt'
        except ImportError as e:
            print(f"Could not import test_ccompiler_opt: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.command.build import *
            self.tools['build'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.command.build'
        except ImportError as e:
            print(f"Could not import build: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.command.build_src import *
            self.tools['build_src'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.command.build_src'
        except ImportError as e:
            print(f"Could not import build_src: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.build_ext import *
            self.tools['build_ext'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.build_ext'
        except ImportError as e:
            print(f"Could not import build_ext: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.func2subr import *
            self.tools['func2subr'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.func2subr'
        except ImportError as e:
            print(f"Could not import func2subr: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.crackfortran import *
            self.tools['crackfortran'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.crackfortran'
        except ImportError as e:
            print(f"Could not import crackfortran: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.f2py2e import *
            self.tools['f2py2e'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.f2py2e'
        except ImportError as e:
            print(f"Could not import f2py2e: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.cb_rules import *
            self.tools['cb_rules'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.cb_rules'
        except ImportError as e:
            print(f"Could not import cb_rules: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py._src_pyf import *
            self.tools['_src_pyf'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py._src_pyf'
        except ImportError as e:
            print(f"Could not import _src_pyf: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.cfuncs import *
            self.tools['cfuncs'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.cfuncs'
        except ImportError as e:
            print(f"Could not import cfuncs: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.f90mod_rules import *
            self.tools['f90mod_rules'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.f90mod_rules'
        except ImportError as e:
            print(f"Could not import f90mod_rules: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.capi_maps import *
            self.tools['capi_maps'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.capi_maps'
        except ImportError as e:
            print(f"Could not import capi_maps: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py._backends._meson import *
            self.tools['_meson'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py._backends._meson'
        except ImportError as e:
            print(f"Could not import _meson: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_pyf_src import *
            self.tools['test_pyf_src'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_pyf_src'
        except ImportError as e:
            print(f"Could not import test_pyf_src: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_return_real import *
            self.tools['test_return_real'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_return_real'
        except ImportError as e:
            print(f"Could not import test_return_real: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_crackfortran import *
            self.tools['test_crackfortran'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_crackfortran'
        except ImportError as e:
            print(f"Could not import test_crackfortran: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_f2py2e import *
            self.tools['test_f2py2e'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_f2py2e'
        except ImportError as e:
            print(f"Could not import test_f2py2e: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_abstract_interface import *
            self.tools['test_abstract_interface'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_abstract_interface'
        except ImportError as e:
            print(f"Could not import test_abstract_interface: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_semicolon_split import *
            self.tools['test_semicolon_split'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_semicolon_split'
        except ImportError as e:
            print(f"Could not import test_semicolon_split: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.tests.test_ctypeslib import *
            self.tools['test_ctypeslib'] = 'thonlibs.libthon3.11.site-packages.numpy.tests.test_ctypeslib'
        except ImportError as e:
            print(f"Could not import test_ctypeslib: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.tests.test_public_api import *
            self.tools['test_public_api'] = 'thonlibs.libthon3.11.site-packages.numpy.tests.test_public_api'
        except ImportError as e:
            print(f"Could not import test_public_api: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._polynomial_impl import *
            self.tools['_polynomial_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._polynomial_impl'
        except ImportError as e:
            print(f"Could not import _polynomial_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._array_utils_impl import *
            self.tools['_array_utils_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._array_utils_impl'
        except ImportError as e:
            print(f"Could not import _array_utils_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.datastructures.mixins import *
            self.tools['mixins'] = 'thonlibs.libthon3.11.site-packages.werkzeug.datastructures.mixins'
        except ImportError as e:
            print(f"Could not import mixins: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._function_base_impl import *
            self.tools['_function_base_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._function_base_impl'
        except ImportError as e:
            print(f"Could not import _function_base_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._iotools import *
            self.tools['_iotools'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._iotools'
        except ImportError as e:
            print(f"Could not import _iotools: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._stride_tricks_impl import *
            self.tools['_stride_tricks_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._stride_tricks_impl'
        except ImportError as e:
            print(f"Could not import _stride_tricks_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._npyio_impl import *
            self.tools['_npyio_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._npyio_impl'
        except ImportError as e:
            print(f"Could not import _npyio_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._datasource import *
            self.tools['_datasource'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._datasource'
        except ImportError as e:
            print(f"Could not import _datasource: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_nanfunctions import *
            self.tools['test_nanfunctions'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_nanfunctions'
        except ImportError as e:
            print(f"Could not import test_nanfunctions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_function_base import *
            self.tools['test_function_base'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_function_base'
        except ImportError as e:
            print(f"Could not import test_function_base: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_loadtxt import *
            self.tools['test_loadtxt'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_loadtxt'
        except ImportError as e:
            print(f"Could not import test_loadtxt: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_array_utils import *
            self.tools['test_array_utils'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_array_utils'
        except ImportError as e:
            print(f"Could not import test_array_utils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test__datasource import *
            self.tools['test__datasource'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test__datasource'
        except ImportError as e:
            print(f"Could not import test__datasource: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.linalg._linalg import *
            self.tools['_linalg'] = 'thonlibs.libthon3.11.site-packages.numpy.linalg._linalg'
        except ImportError as e:
            print(f"Could not import _linalg: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.linalg.tests.test_linalg import *
            self.tools['test_linalg'] = 'thonlibs.libthon3.11.site-packages.numpy.linalg.tests.test_linalg'
        except ImportError as e:
            print(f"Could not import test_linalg: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.mypy_plugin import *
            self.tools['mypy_plugin'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.mypy_plugin'
        except ImportError as e:
            print(f"Could not import mypy_plugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._pyinstaller.hook-numpy import *
            self.tools['hook-numpy'] = 'thonlibs.libthon3.11.site-packages.numpy._pyinstaller.hook-numpy'
        except ImportError as e:
            print(f"Could not import hook-numpy: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.matrixlib.defmatrix import *
            self.tools['defmatrix'] = 'thonlibs.libthon3.11.site-packages.numpy.matrixlib.defmatrix'
        except ImportError as e:
            print(f"Could not import defmatrix: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug._internal import *
            self.tools['_internal'] = 'thonlibs.libthon3.11.site-packages.werkzeug._internal'
        except ImportError as e:
            print(f"Could not import _internal: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.core.overrides import *
            self.tools['overrides'] = 'thonlibs.libthon3.11.site-packages.numpy.core.overrides'
        except ImportError as e:
            print(f"Could not import overrides: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.core.defchararray import *
            self.tools['defchararray'] = 'thonlibs.libthon3.11.site-packages.numpy.core.defchararray'
        except ImportError as e:
            print(f"Could not import defchararray: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.core.arrayprint import *
            self.tools['arrayprint'] = 'thonlibs.libthon3.11.site-packages.numpy.core.arrayprint'
        except ImportError as e:
            print(f"Could not import arrayprint: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.core.einsumfunc import *
            self.tools['einsumfunc'] = 'thonlibs.libthon3.11.site-packages.numpy.core.einsumfunc'
        except ImportError as e:
            print(f"Could not import einsumfunc: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.core.records import *
            self.tools['records'] = 'thonlibs.libthon3.11.site-packages.numpy.core.records'
        except ImportError as e:
            print(f"Could not import records: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core._add_newdocs import *
            self.tools['_add_newdocs'] = 'thonlibs.libthon3.11.site-packages.numpy._core._add_newdocs'
        except ImportError as e:
            print(f"Could not import _add_newdocs: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.core.fromnumeric import *
            self.tools['fromnumeric'] = 'thonlibs.libthon3.11.site-packages.numpy.core.fromnumeric'
        except ImportError as e:
            print(f"Could not import fromnumeric: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.ma.tests.test_regression import *
            self.tools['test_regression'] = 'thonlibs.libthon3.11.site-packages.numpy.ma.tests.test_regression'
        except ImportError as e:
            print(f"Could not import test_regression: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_scalarprint import *
            self.tools['test_scalarprint'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_scalarprint'
        except ImportError as e:
            print(f"Could not import test_scalarprint: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_overrides import *
            self.tools['test_overrides'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_overrides'
        except ImportError as e:
            print(f"Could not import test_overrides: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_nditer import *
            self.tools['test_nditer'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_nditer'
        except ImportError as e:
            print(f"Could not import test_nditer: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_umath_complex import *
            self.tools['test_umath_complex'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_umath_complex'
        except ImportError as e:
            print(f"Could not import test_umath_complex: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_scalarmath import *
            self.tools['test_scalarmath'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_scalarmath'
        except ImportError as e:
            print(f"Could not import test_scalarmath: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_array_coercion import *
            self.tools['test_array_coercion'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_array_coercion'
        except ImportError as e:
            print(f"Could not import test_array_coercion: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_stringdtype import *
            self.tools['test_stringdtype'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_stringdtype'
        except ImportError as e:
            print(f"Could not import test_stringdtype: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_array_interface import *
            self.tools['test_array_interface'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_array_interface'
        except ImportError as e:
            print(f"Could not import test_array_interface: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_item_selection import *
            self.tools['test_item_selection'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_item_selection'
        except ImportError as e:
            print(f"Could not import test_item_selection: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_einsum import *
            self.tools['test_einsum'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_einsum'
        except ImportError as e:
            print(f"Could not import test_einsum: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.matrixlib.tests.test_multiarray import *
            self.tools['test_multiarray'] = 'thonlibs.libthon3.11.site-packages.numpy.matrixlib.tests.test_multiarray'
        except ImportError as e:
            print(f"Could not import test_multiarray: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_half import *
            self.tools['test_half'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_half'
        except ImportError as e:
            print(f"Could not import test_half: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_scalarbuffer import *
            self.tools['test_scalarbuffer'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_scalarbuffer'
        except ImportError as e:
            print(f"Could not import test_scalarbuffer: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_mem_overlap import *
            self.tools['test_mem_overlap'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_mem_overlap'
        except ImportError as e:
            print(f"Could not import test_mem_overlap: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_datetime import *
            self.tools['test_datetime'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_datetime'
        except ImportError as e:
            print(f"Could not import test_datetime: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_api import *
            self.tools['test_api'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_api'
        except ImportError as e:
            print(f"Could not import test_api: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.ma.tests.test_old_ma import *
            self.tools['test_old_ma'] = 'thonlibs.libthon3.11.site-packages.numpy.ma.tests.test_old_ma'
        except ImportError as e:
            print(f"Could not import test_old_ma: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_core import *
            self.tools['test_core'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_core'
        except ImportError as e:
            print(f"Could not import test_core: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.chebyshev import *
            self.tools['chebyshev'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.chebyshev'
        except ImportError as e:
            print(f"Could not import chebyshev: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.pkg_resources import *
            self.tools['pkg_resources'] = 'thonlibs.libthon3.11.site-packages.pkg_resources'
        except ImportError as e:
            print(f"Could not import pkg_resources: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.archive_util import *
            self.tools['archive_util'] = 'thonlibs.libthon3.11.site-packages.setuptools.archive_util'
        except ImportError as e:
            print(f"Could not import archive_util: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.util.compat import *
            self.tools['compat'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.util.compat'
        except ImportError as e:
            print(f"Could not import compat: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.dist import *
            self.tools['dist'] = 'thonlibs.libthon3.11.site-packages.setuptools.dist'
        except ImportError as e:
            print(f"Could not import dist: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.package_index import *
            self.tools['package_index'] = 'thonlibs.libthon3.11.site-packages.setuptools.package_index'
        except ImportError as e:
            print(f"Could not import package_index: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.ssl_support import *
            self.tools['ssl_support'] = 'thonlibs.libthon3.11.site-packages.setuptools.ssl_support'
        except ImportError as e:
            print(f"Could not import ssl_support: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.svn_utils import *
            self.tools['svn_utils'] = 'thonlibs.libthon3.11.site-packages.setuptools.svn_utils'
        except ImportError as e:
            print(f"Could not import svn_utils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.easy_install import *
            self.tools['easy_install'] = 'thonlibs.libthon3.11.site-packages.easy_install'
        except ImportError as e:
            print(f"Could not import easy_install: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.command.egg_info import *
            self.tools['egg_info'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.command.egg_info'
        except ImportError as e:
            print(f"Could not import egg_info: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.command.sdist import *
            self.tools['sdist'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.command.sdist'
        except ImportError as e:
            print(f"Could not import sdist: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.doctest import *
            self.tools['doctest'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.doctest'
        except ImportError as e:
            print(f"Could not import doctest: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.test_packageindex import *
            self.tools['test_packageindex'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.test_packageindex'
        except ImportError as e:
            print(f"Could not import test_packageindex: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.test_resources import *
            self.tools['test_resources'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.test_resources'
        except ImportError as e:
            print(f"Could not import test_resources: {e}")
            
        try:
            from .cache.uv.archive-v0.ewElvJ7lbFnivoa93_pQm.setuptools.tests.test_sandbox import *
            self.tools['test_sandbox'] = '.cache.uv.archive-v0.ewElvJ7lbFnivoa93_pQm.setuptools.tests.test_sandbox'
        except ImportError as e:
            print(f"Could not import test_sandbox: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.test_sdist import *
            self.tools['test_sdist'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.test_sdist'
        except ImportError as e:
            print(f"Could not import test_sdist: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.test_upload_docs import *
            self.tools['test_upload_docs'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.test_upload_docs'
        except ImportError as e:
            print(f"Could not import test_upload_docs: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.pkg_resources.tests.test_integration_zope_interface import *
            self.tools['test_integration_zope_interface'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.pkg_resources.tests.test_integration_zope_interface'
        except ImportError as e:
            print(f"Could not import test_integration_zope_interface: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._core_metadata import *
            self.tools['_core_metadata'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._core_metadata'
        except ImportError as e:
            print(f"Could not import _core_metadata: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.build_meta import *
            self.tools['build_meta'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.build_meta'
        except ImportError as e:
            print(f"Could not import build_meta: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.discovery import *
            self.tools['discovery'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.discovery'
        except ImportError as e:
            print(f"Could not import discovery: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.psycopg2.errors import *
            self.tools['errors'] = 'thonlibs.libthon3.11.site-packages.psycopg2.errors'
        except ImportError as e:
            print(f"Could not import errors: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.msvc import *
            self.tools['msvc'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.msvc'
        except ImportError as e:
            print(f"Could not import msvc: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.warnings import *
            self.tools['warnings'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.warnings'
        except ImportError as e:
            print(f"Could not import warnings: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils._msvccompiler import *
            self.tools['_msvccompiler'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils._msvccompiler'
        except ImportError as e:
            print(f"Could not import _msvccompiler: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.ccompiler import *
            self.tools['ccompiler'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.ccompiler'
        except ImportError as e:
            print(f"Could not import ccompiler: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.filelist import *
            self.tools['filelist'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.filelist'
        except ImportError as e:
            print(f"Could not import filelist: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.text_file import *
            self.tools['text_file'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.text_file'
        except ImportError as e:
            print(f"Could not import text_file: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.v1.version import *
            self.tools['version'] = 'thonlibs.libthon3.11.site-packagesdantic.v1.version'
        except ImportError as e:
            print(f"Could not import version: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.command.bdist import *
            self.tools['bdist'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.command.bdist'
        except ImportError as e:
            print(f"Could not import bdist: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.build_py import *
            self.tools['build_py'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.build_py'
        except ImportError as e:
            print(f"Could not import build_py: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.install import *
            self.tools['install'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.install'
        except ImportError as e:
            print(f"Could not import install: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.install_lib import *
            self.tools['install_lib'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.install_lib'
        except ImportError as e:
            print(f"Could not import install_lib: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.test_build_ext import *
            self.tools['test_build_ext'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.test_build_ext'
        except ImportError as e:
            print(f"Could not import test_build_ext: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_filelist import *
            self.tools['test_filelist'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_filelist'
        except ImportError as e:
            print(f"Could not import test_filelist: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.more_itertools.recipes import *
            self.tools['recipes'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.more_itertools.recipes'
        except ImportError as e:
            print(f"Could not import recipes: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging._elffile import *
            self.tools['_elffile'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging._elffile'
        except ImportError as e:
            print(f"Could not import _elffile: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging.tags import *
            self.tools['tags'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging.tags'
        except ImportError as e:
            print(f"Could not import tags: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.packaging.licenses._spdx import *
            self.tools['_spdx'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.packaging.licenses._spdx'
        except ImportError as e:
            print(f"Could not import _spdx: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.android import *
            self.tools['android'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.android'
        except ImportError as e:
            print(f"Could not import android: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.platformdirs.macos import *
            self.tools['macos'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.platformdirs.macos'
        except ImportError as e:
            print(f"Could not import macos: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.unix import *
            self.tools['unix'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.unix'
        except ImportError as e:
            print(f"Could not import unix: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._checkers import *
            self.tools['_checkers'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._checkers'
        except ImportError as e:
            print(f"Could not import _checkers: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.macosx_libfile import *
            self.tools['macosx_libfile'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.macosx_libfile'
        except ImportError as e:
            print(f"Could not import macosx_libfile: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.command._requirestxt import *
            self.tools['_requirestxt'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.command._requirestxt'
        except ImportError as e:
            print(f"Could not import _requirestxt: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.bdist_egg import *
            self.tools['bdist_egg'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.bdist_egg'
        except ImportError as e:
            print(f"Could not import bdist_egg: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.command.editable_wheel import *
            self.tools['editable_wheel'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.command.editable_wheel'
        except ImportError as e:
            print(f"Could not import editable_wheel: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config._apply_pyprojecttoml import *
            self.tools['_apply_pyprojecttoml'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config._apply_pyprojecttoml'
        except ImportError as e:
            print(f"Could not import _apply_pyprojecttoml: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.configprojecttoml import *
            self.tools['pyprojecttoml'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.configprojecttoml'
        except ImportError as e:
            print(f"Could not import pyprojecttoml: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config.setupcfg import *
            self.tools['setupcfg'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config.setupcfg'
        except ImportError as e:
            print(f"Could not import setupcfg: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config._validate_pyproject.error_reporting import *
            self.tools['error_reporting'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config._validate_pyproject.error_reporting'
        except ImportError as e:
            print(f"Could not import error_reporting: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config._validate_pyproject.fastjsonschema_validations import *
            self.tools['fastjsonschema_validations'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config._validate_pyproject.fastjsonschema_validations'
        except ImportError as e:
            print(f"Could not import fastjsonschema_validations: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_config_discovery import *
            self.tools['test_config_discovery'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_config_discovery'
        except ImportError as e:
            print(f"Could not import test_config_discovery: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_dist import *
            self.tools['test_dist'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_dist'
        except ImportError as e:
            print(f"Could not import test_dist: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.test_easy_install import *
            self.tools['test_easy_install'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.test_easy_install'
        except ImportError as e:
            print(f"Could not import test_easy_install: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_editable_install import *
            self.tools['test_editable_install'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_editable_install'
        except ImportError as e:
            print(f"Could not import test_editable_install: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.test_egg_info import *
            self.tools['test_egg_info'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.test_egg_info'
        except ImportError as e:
            print(f"Could not import test_egg_info: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.test_find_packages import *
            self.tools['test_find_packages'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.test_find_packages'
        except ImportError as e:
            print(f"Could not import test_find_packages: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_manifest import *
            self.tools['test_manifest'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_manifest'
        except ImportError as e:
            print(f"Could not import test_manifest: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.tests.test_warnings import *
            self.tools['test_warnings'] = 'thonlibs.libthon3.11.site-packages.numpy.tests.test_warnings'
        except ImportError as e:
            print(f"Could not import test_warnings: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_windows_wrappers import *
            self.tools['test_windows_wrappers'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_windows_wrappers'
        except ImportError as e:
            print(f"Could not import test_windows_wrappers: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.config.test_apply_pyprojecttoml import *
            self.tools['test_apply_pyprojecttoml'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.config.test_apply_pyprojecttoml'
        except ImportError as e:
            print(f"Could not import test_apply_pyprojecttoml: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.config.test_pyprojecttoml import *
            self.tools['test_pyprojecttoml'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.config.test_pyprojecttoml'
        except ImportError as e:
            print(f"Could not import test_pyprojecttoml: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.integration.test_pip_install_sdist import *
            self.tools['test_pip_install_sdist'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.integration.test_pip_install_sdist'
        except ImportError as e:
            print(f"Could not import test_pip_install_sdist: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.six import *
            self.tools['six'] = 'thonlibs.libthon3.11.site-packages.six'
        except ImportError as e:
            print(f"Could not import six: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.ellipticcurve import *
            self.tools['ellipticcurve'] = 'thonlibs.libthon3.11.site-packages.ecdsa.ellipticcurve'
        except ImportError as e:
            print(f"Could not import ellipticcurve: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.rfc6979 import *
            self.tools['rfc6979'] = 'thonlibs.libthon3.11.site-packages.ecdsa.rfc6979'
        except ImportError as e:
            print(f"Could not import rfc6979: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.test_pyecdsa import *
            self.tools['test_pyecdsa'] = 'thonlibs.libthon3.11.site-packages.ecdsa.test_pyecdsa'
        except ImportError as e:
            print(f"Could not import test_pyecdsa: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcash.network.APIs.BitcoinDotComAPI import *
            self.tools['BitcoinDotComAPI'] = 'thonlibs.libthon3.11.site-packages.bitcash.network.APIs.BitcoinDotComAPI'
        except ImportError as e:
            print(f"Could not import BitcoinDotComAPI: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcash.network.APIs.ChaingraphAPI import *
            self.tools['ChaingraphAPI'] = 'thonlibs.libthon3.11.site-packages.bitcash.network.APIs.ChaingraphAPI'
        except ImportError as e:
            print(f"Could not import ChaingraphAPI: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcash.network.APIs.FulcrumProtocolAPI import *
            self.tools['FulcrumProtocolAPI'] = 'thonlibs.libthon3.11.site-packages.bitcash.network.APIs.FulcrumProtocolAPI'
        except ImportError as e:
            print(f"Could not import FulcrumProtocolAPI: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._scripts import *
            self.tools['_scripts'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._scripts'
        except ImportError as e:
            print(f"Could not import _scripts: {e}")
            
        try:
            from .cache.uv.archive-v0.ewElvJ7lbFnivoa93_pQm.setuptools.tests.fixtures import *
            self.tools['fixtures'] = '.cache.uv.archive-v0.ewElvJ7lbFnivoa93_pQm.setuptools.tests.fixtures'
        except ImportError as e:
            print(f"Could not import fixtures: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.h11._abnf import *
            self.tools['_abnf'] = 'thonlibs.libthon3.11.site-packages.h11._abnf'
        except ImportError as e:
            print(f"Could not import _abnf: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.h11._connection import *
            self.tools['_connection'] = 'thonlibs.libthon3.11.site-packages.h11._connection'
        except ImportError as e:
            print(f"Could not import _connection: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.h11._events import *
            self.tools['_events'] = 'thonlibs.libthon3.11.site-packages.h11._events'
        except ImportError as e:
            print(f"Could not import _events: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.h11._headers import *
            self.tools['_headers'] = 'thonlibs.libthon3.11.site-packages.h11._headers'
        except ImportError as e:
            print(f"Could not import _headers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.lib.vertex._auth import *
            self.tools['_auth'] = 'thonlibs.libthon3.11.site-packages.anthropic.lib.vertex._auth'
        except ImportError as e:
            print(f"Could not import _auth: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.lib.vertex._client import *
            self.tools['_client'] = 'thonlibs.libthon3.11.site-packages.anthropic.lib.vertex._client'
        except ImportError as e:
            print(f"Could not import _client: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpx._content import *
            self.tools['_content'] = 'thonlibs.libthon3.11.site-packages.httpx._content'
        except ImportError as e:
            print(f"Could not import _content: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpx._decoders import *
            self.tools['_decoders'] = 'thonlibs.libthon3.11.site-packages.httpx._decoders'
        except ImportError as e:
            print(f"Could not import _decoders: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._models import *
            self.tools['_models'] = 'thonlibs.libthon3.11.site-packages.anthropic._models'
        except ImportError as e:
            print(f"Could not import _models: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpx._multipart import *
            self.tools['_multipart'] = 'thonlibs.libthon3.11.site-packages.httpx._multipart'
        except ImportError as e:
            print(f"Could not import _multipart: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpx._status_codes import *
            self.tools['_status_codes'] = 'thonlibs.libthon3.11.site-packages.httpx._status_codes'
        except ImportError as e:
            print(f"Could not import _status_codes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpx._urlparse import *
            self.tools['_urlparse'] = 'thonlibs.libthon3.11.site-packages.httpx._urlparse'
        except ImportError as e:
            print(f"Could not import _urlparse: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpx._urls import *
            self.tools['_urls'] = 'thonlibs.libthon3.11.site-packages.httpx._urls'
        except ImportError as e:
            print(f"Could not import _urls: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._utils import *
            self.tools['_utils'] = 'thonlibs.libthon3.11.site-packages.httpcore._utils'
        except ImportError as e:
            print(f"Could not import _utils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.distro.distro import *
            self.tools['distro'] = 'thonlibs.libthon3.11.site-packages.distro.distro'
        except ImportError as e:
            print(f"Could not import distro: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio._core._fileio import *
            self.tools['_fileio'] = 'thonlibs.libthon3.11.site-packages.anyio._core._fileio'
        except ImportError as e:
            print(f"Could not import _fileio: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio._core._tempfile import *
            self.tools['_tempfile'] = 'thonlibs.libthon3.11.site-packages.anyio._core._tempfile'
        except ImportError as e:
            print(f"Could not import _tempfile: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._utils._streams import *
            self.tools['_streams'] = 'thonlibs.libthon3.11.site-packages.anthropic._utils._streams'
        except ImportError as e:
            print(f"Could not import _streams: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.text import *
            self.tools['text'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.text'
        except ImportError as e:
            print(f"Could not import text: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._trace import *
            self.tools['_trace'] = 'thonlibs.libthon3.11.site-packages.httpcore._trace'
        except ImportError as e:
            print(f"Could not import _trace: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._sync.connection_pool import *
            self.tools['connection_pool'] = 'thonlibs.libthon3.11.site-packages.httpcore._sync.connection_pool'
        except ImportError as e:
            print(f"Could not import connection_pool: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._sync.http11 import *
            self.tools['http11'] = 'thonlibs.libthon3.11.site-packages.httpcore._sync.http11'
        except ImportError as e:
            print(f"Could not import http11: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._sync.http2 import *
            self.tools['http2'] = 'thonlibs.libthon3.11.site-packages.httpcore._sync.http2'
        except ImportError as e:
            print(f"Could not import http2: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._sync.socks_proxy import *
            self.tools['socks_proxy'] = 'thonlibs.libthon3.11.site-packages.httpcore._sync.socks_proxy'
        except ImportError as e:
            print(f"Could not import socks_proxy: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._backends.trio import *
            self.tools['trio'] = 'thonlibs.libthon3.11.site-packages.httpcore._backends.trio'
        except ImportError as e:
            print(f"Could not import trio: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic_core.core_schema import *
            self.tools['core_schema'] = 'thonlibs.libthon3.11.site-packagesdantic_core.core_schema'
        except ImportError as e:
            print(f"Could not import core_schema: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._migration import *
            self.tools['_migration'] = 'thonlibs.libthon3.11.site-packagesdantic._migration'
        except ImportError as e:
            print(f"Could not import _migration: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.v1.color import *
            self.tools['color'] = 'thonlibs.libthon3.11.site-packagesdantic.v1.color'
        except ImportError as e:
            print(f"Could not import color: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.v1.dataclasses import *
            self.tools['dataclasses'] = 'thonlibs.libthon3.11.site-packagesdantic.v1.dataclasses'
        except ImportError as e:
            print(f"Could not import dataclasses: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.json_schema import *
            self.tools['json_schema'] = 'thonlibs.libthon3.11.site-packagesdantic.json_schema'
        except ImportError as e:
            print(f"Could not import json_schema: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.fixtures.mypy import *
            self.tools['mypy'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.fixtures.mypy'
        except ImportError as e:
            print(f"Could not import mypy: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.type_adapter import *
            self.tools['type_adapter'] = 'thonlibs.libthon3.11.site-packagesdantic.type_adapter'
        except ImportError as e:
            print(f"Could not import type_adapter: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpx._config import *
            self.tools['_config'] = 'thonlibs.libthon3.11.site-packages.httpx._config'
        except ImportError as e:
            print(f"Could not import _config: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._fields import *
            self.tools['_fields'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._fields'
        except ImportError as e:
            print(f"Could not import _fields: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._generate_schema import *
            self.tools['_generate_schema'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._generate_schema'
        except ImportError as e:
            print(f"Could not import _generate_schema: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._generics import *
            self.tools['_generics'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._generics'
        except ImportError as e:
            print(f"Could not import _generics: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._repr import *
            self.tools['_repr'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._repr'
        except ImportError as e:
            print(f"Could not import _repr: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._typing_extra import *
            self.tools['_typing_extra'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._typing_extra'
        except ImportError as e:
            print(f"Could not import _typing_extra: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._validators import *
            self.tools['_validators'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._validators'
        except ImportError as e:
            print(f"Could not import _validators: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.v1.class_validators import *
            self.tools['class_validators'] = 'thonlibs.libthon3.11.site-packagesdantic.v1.class_validators'
        except ImportError as e:
            print(f"Could not import class_validators: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.v1.tools import *
            self.tools['tools'] = 'thonlibs.libthon3.11.site-packagesdantic.v1.tools'
        except ImportError as e:
            print(f"Could not import tools: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.v1._hypothesis_plugin import *
            self.tools['_hypothesis_plugin'] = 'thonlibs.libthon3.11.site-packagesdantic.v1._hypothesis_plugin'
        except ImportError as e:
            print(f"Could not import _hypothesis_plugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.error_wrappers import *
            self.tools['error_wrappers'] = 'thonlibs.libthon3.11.site-packagesdantic.error_wrappers'
        except ImportError as e:
            print(f"Could not import error_wrappers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.validators import *
            self.tools['validators'] = 'thonlibs.libthon3.11.site-packagesdantic.validators'
        except ImportError as e:
            print(f"Could not import validators: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._base_client import *
            self.tools['_base_client'] = 'thonlibs.libthon3.11.site-packages.anthropic._base_client'
        except ImportError as e:
            print(f"Could not import _base_client: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._streaming import *
            self.tools['_streaming'] = 'thonlibs.libthon3.11.site-packages.anthropic._streaming'
        except ImportError as e:
            print(f"Could not import _streaming: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.lib.streaming._types import *
            self.tools['_types'] = 'thonlibs.libthon3.11.site-packages.anthropic.lib.streaming._types'
        except ImportError as e:
            print(f"Could not import _types: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._utils._sync import *
            self.tools['_sync'] = 'thonlibs.libthon3.11.site-packages.anthropic._utils._sync'
        except ImportError as e:
            print(f"Could not import _sync: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._utils._transform import *
            self.tools['_transform'] = 'thonlibs.libthon3.11.site-packages.anthropic._utils._transform'
        except ImportError as e:
            print(f"Could not import _transform: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.resources.completions import *
            self.tools['completions'] = 'thonlibs.libthon3.11.site-packages.anthropic.resources.completions'
        except ImportError as e:
            print(f"Could not import completions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.resources.messages.batches import *
            self.tools['batches'] = 'thonlibs.libthon3.11.site-packages.anthropic.resources.messages.batches'
        except ImportError as e:
            print(f"Could not import batches: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.resources.messages.messages import *
            self.tools['messages'] = 'thonlibs.libthon3.11.site-packages.anthropic.resources.messages.messages'
        except ImportError as e:
            print(f"Could not import messages: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.base64_image_source_param import *
            self.tools['base64_image_source_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.base64_image_source_param'
        except ImportError as e:
            print(f"Could not import base64_image_source_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.citation_web_search_result_location_param import *
            self.tools['citation_web_search_result_location_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.citation_web_search_result_location_param'
        except ImportError as e:
            print(f"Could not import citation_web_search_result_location_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.citations_delta import *
            self.tools['citations_delta'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.citations_delta'
        except ImportError as e:
            print(f"Could not import citations_delta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.citations_web_search_result_location import *
            self.tools['citations_web_search_result_location'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.citations_web_search_result_location'
        except ImportError as e:
            print(f"Could not import citations_web_search_result_location: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.completion_create_params import *
            self.tools['completion_create_params'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.completion_create_params'
        except ImportError as e:
            print(f"Could not import completion_create_params: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.content_block import *
            self.tools['content_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.content_block'
        except ImportError as e:
            print(f"Could not import content_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.content_block_param import *
            self.tools['content_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.content_block_param'
        except ImportError as e:
            print(f"Could not import content_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.message_count_tokens_params import *
            self.tools['message_count_tokens_params'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.message_count_tokens_params'
        except ImportError as e:
            print(f"Could not import message_count_tokens_params: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.message_count_tokens_tool_param import *
            self.tools['message_count_tokens_tool_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.message_count_tokens_tool_param'
        except ImportError as e:
            print(f"Could not import message_count_tokens_tool_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.message_create_params import *
            self.tools['message_create_params'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.message_create_params'
        except ImportError as e:
            print(f"Could not import message_create_params: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.message_param import *
            self.tools['message_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.message_param'
        except ImportError as e:
            print(f"Could not import message_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.raw_content_block_start_event import *
            self.tools['raw_content_block_start_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.raw_content_block_start_event'
        except ImportError as e:
            print(f"Could not import raw_content_block_start_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.server_tool_usage import *
            self.tools['server_tool_usage'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.server_tool_usage'
        except ImportError as e:
            print(f"Could not import server_tool_usage: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.server_tool_use_block import *
            self.tools['server_tool_use_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.server_tool_use_block'
        except ImportError as e:
            print(f"Could not import server_tool_use_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.server_tool_use_block_param import *
            self.tools['server_tool_use_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.server_tool_use_block_param'
        except ImportError as e:
            print(f"Could not import server_tool_use_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.text_citation import *
            self.tools['text_citation'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.text_citation'
        except ImportError as e:
            print(f"Could not import text_citation: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.text_citation_param import *
            self.tools['text_citation_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.text_citation_param'
        except ImportError as e:
            print(f"Could not import text_citation_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.tool_union_param import *
            self.tools['tool_union_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.tool_union_param'
        except ImportError as e:
            print(f"Could not import tool_union_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.web_search_result_block import *
            self.tools['web_search_result_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.web_search_result_block'
        except ImportError as e:
            print(f"Could not import web_search_result_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.web_search_result_block_param import *
            self.tools['web_search_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.web_search_result_block_param'
        except ImportError as e:
            print(f"Could not import web_search_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.web_search_tool_20250305_param import *
            self.tools['web_search_tool_20250305_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.web_search_tool_20250305_param'
        except ImportError as e:
            print(f"Could not import web_search_tool_20250305_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.web_search_tool_request_error_param import *
            self.tools['web_search_tool_request_error_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.web_search_tool_request_error_param'
        except ImportError as e:
            print(f"Could not import web_search_tool_request_error_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.web_search_tool_result_block import *
            self.tools['web_search_tool_result_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.web_search_tool_result_block'
        except ImportError as e:
            print(f"Could not import web_search_tool_result_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.web_search_tool_result_block_content import *
            self.tools['web_search_tool_result_block_content'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.web_search_tool_result_block_content'
        except ImportError as e:
            print(f"Could not import web_search_tool_result_block_content: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.web_search_tool_result_block_param import *
            self.tools['web_search_tool_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.web_search_tool_result_block_param'
        except ImportError as e:
            print(f"Could not import web_search_tool_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.web_search_tool_result_block_param_content_param import *
            self.tools['web_search_tool_result_block_param_content_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.web_search_tool_result_block_param_content_param'
        except ImportError as e:
            print(f"Could not import web_search_tool_result_block_param_content_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.web_search_tool_result_error import *
            self.tools['web_search_tool_result_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.web_search_tool_result_error'
        except ImportError as e:
            print(f"Could not import web_search_tool_result_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_base64_image_source_param import *
            self.tools['beta_base64_image_source_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_base64_image_source_param'
        except ImportError as e:
            print(f"Could not import beta_base64_image_source_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_web_search_result_location_param import *
            self.tools['beta_citation_web_search_result_location_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_web_search_result_location_param'
        except ImportError as e:
            print(f"Could not import beta_citation_web_search_result_location_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citations_delta import *
            self.tools['beta_citations_delta'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citations_delta'
        except ImportError as e:
            print(f"Could not import beta_citations_delta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citations_web_search_result_location import *
            self.tools['beta_citations_web_search_result_location'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citations_web_search_result_location'
        except ImportError as e:
            print(f"Could not import beta_citations_web_search_result_location: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_content_block import *
            self.tools['beta_content_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_content_block'
        except ImportError as e:
            print(f"Could not import beta_content_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_content_block_param import *
            self.tools['beta_content_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_content_block_param'
        except ImportError as e:
            print(f"Could not import beta_content_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_content_block_start_event import *
            self.tools['beta_raw_content_block_start_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_content_block_start_event'
        except ImportError as e:
            print(f"Could not import beta_raw_content_block_start_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_server_tool_usage import *
            self.tools['beta_server_tool_usage'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_server_tool_usage'
        except ImportError as e:
            print(f"Could not import beta_server_tool_usage: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_server_tool_use_block import *
            self.tools['beta_server_tool_use_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_server_tool_use_block'
        except ImportError as e:
            print(f"Could not import beta_server_tool_use_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_server_tool_use_block_param import *
            self.tools['beta_server_tool_use_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_server_tool_use_block_param'
        except ImportError as e:
            print(f"Could not import beta_server_tool_use_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_citation import *
            self.tools['beta_text_citation'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_citation'
        except ImportError as e:
            print(f"Could not import beta_text_citation: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_citation_param import *
            self.tools['beta_text_citation_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_citation_param'
        except ImportError as e:
            print(f"Could not import beta_text_citation_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_union_param import *
            self.tools['beta_tool_union_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_union_param'
        except ImportError as e:
            print(f"Could not import beta_tool_union_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_block import *
            self.tools['beta_web_fetch_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_block'
        except ImportError as e:
            print(f"Could not import beta_web_fetch_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_block_param import *
            self.tools['beta_web_fetch_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_block_param'
        except ImportError as e:
            print(f"Could not import beta_web_fetch_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_tool_20250910_param import *
            self.tools['beta_web_fetch_tool_20250910_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_tool_20250910_param'
        except ImportError as e:
            print(f"Could not import beta_web_fetch_tool_20250910_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_tool_result_block import *
            self.tools['beta_web_fetch_tool_result_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_tool_result_block'
        except ImportError as e:
            print(f"Could not import beta_web_fetch_tool_result_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_tool_result_block_param import *
            self.tools['beta_web_fetch_tool_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_tool_result_block_param'
        except ImportError as e:
            print(f"Could not import beta_web_fetch_tool_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_tool_result_error_block import *
            self.tools['beta_web_fetch_tool_result_error_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_tool_result_error_block'
        except ImportError as e:
            print(f"Could not import beta_web_fetch_tool_result_error_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_tool_result_error_block_param import *
            self.tools['beta_web_fetch_tool_result_error_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_tool_result_error_block_param'
        except ImportError as e:
            print(f"Could not import beta_web_fetch_tool_result_error_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_tool_result_error_code import *
            self.tools['beta_web_fetch_tool_result_error_code'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_fetch_tool_result_error_code'
        except ImportError as e:
            print(f"Could not import beta_web_fetch_tool_result_error_code: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_result_block import *
            self.tools['beta_web_search_result_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_result_block'
        except ImportError as e:
            print(f"Could not import beta_web_search_result_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_result_block_param import *
            self.tools['beta_web_search_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_result_block_param'
        except ImportError as e:
            print(f"Could not import beta_web_search_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_20250305_param import *
            self.tools['beta_web_search_tool_20250305_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_20250305_param'
        except ImportError as e:
            print(f"Could not import beta_web_search_tool_20250305_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_request_error_param import *
            self.tools['beta_web_search_tool_request_error_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_request_error_param'
        except ImportError as e:
            print(f"Could not import beta_web_search_tool_request_error_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_result_block import *
            self.tools['beta_web_search_tool_result_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_result_block'
        except ImportError as e:
            print(f"Could not import beta_web_search_tool_result_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_result_block_content import *
            self.tools['beta_web_search_tool_result_block_content'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_result_block_content'
        except ImportError as e:
            print(f"Could not import beta_web_search_tool_result_block_content: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_result_block_param import *
            self.tools['beta_web_search_tool_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_result_block_param'
        except ImportError as e:
            print(f"Could not import beta_web_search_tool_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_result_block_param_content_param import *
            self.tools['beta_web_search_tool_result_block_param_content_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_result_block_param_content_param'
        except ImportError as e:
            print(f"Could not import beta_web_search_tool_result_block_param_content_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_result_error import *
            self.tools['beta_web_search_tool_result_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_result_error'
        except ImportError as e:
            print(f"Could not import beta_web_search_tool_result_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_result_error_code import *
            self.tools['beta_web_search_tool_result_error_code'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_web_search_tool_result_error_code'
        except ImportError as e:
            print(f"Could not import beta_web_search_tool_result_error_code: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.extension import *
            self.tools['extension'] = 'thonlibs.libthon3.11.site-packages.setuptools.extension'
        except ImportError as e:
            print(f"Could not import extension: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.model import *
            self.tools['model'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.model'
        except ImportError as e:
            print(f"Could not import model: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.pagination import *
            self.tools['pagination'] = 'thonlibs.libthon3.11.site-packages.anthropic.pagination'
        except ImportError as e:
            print(f"Could not import pagination: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask_sqlalchemy.record_queries import *
            self.tools['record_queries'] = 'thonlibs.libthon3.11.site-packages.flask_sqlalchemy.record_queries'
        except ImportError as e:
            print(f"Could not import record_queries: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask_sqlalchemy.track_modifications import *
            self.tools['track_modifications'] = 'thonlibs.libthon3.11.site-packages.flask_sqlalchemy.track_modifications'
        except ImportError as e:
            print(f"Could not import track_modifications: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.ma.extras import *
            self.tools['extras'] = 'thonlibs.libthon3.11.site-packages.numpy.ma.extras'
        except ImportError as e:
            print(f"Could not import extras: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.fixtures.sql import *
            self.tools['sql'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.fixtures.sql'
        except ImportError as e:
            print(f"Could not import sql: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.psycopg2._range import *
            self.tools['_range'] = 'thonlibs.libthon3.11.site-packages.psycopg2._range'
        except ImportError as e:
            print(f"Could not import _range: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.psycopg2._ipaddress import *
            self.tools['_ipaddress'] = 'thonlibs.libthon3.11.site-packages.psycopg2._ipaddress'
        except ImportError as e:
            print(f"Could not import _ipaddress: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.psycopg2.tz import *
            self.tools['tz'] = 'thonlibs.libthon3.11.site-packages.psycopg2.tz'
        except ImportError as e:
            print(f"Could not import tz: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.psycopg2.errorcodes import *
            self.tools['errorcodes'] = 'thonlibs.libthon3.11.site-packages.psycopg2.errorcodes'
        except ImportError as e:
            print(f"Could not import errorcodes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.BlpImagePlugin import *
            self.tools['BlpImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.BlpImagePlugin'
        except ImportError as e:
            print(f"Could not import BlpImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.BmpImagePlugin import *
            self.tools['BmpImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.BmpImagePlugin'
        except ImportError as e:
            print(f"Could not import BmpImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.DdsImagePlugin import *
            self.tools['DdsImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.DdsImagePlugin'
        except ImportError as e:
            print(f"Could not import DdsImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.EpsImagePlugin import *
            self.tools['EpsImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.EpsImagePlugin'
        except ImportError as e:
            print(f"Could not import EpsImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.FitsImagePlugin import *
            self.tools['FitsImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.FitsImagePlugin'
        except ImportError as e:
            print(f"Could not import FitsImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.GifImagePlugin import *
            self.tools['GifImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.GifImagePlugin'
        except ImportError as e:
            print(f"Could not import GifImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.Image import *
            self.tools['Image'] = 'thonlibs.libthon3.11.site-packages.PIL.Image'
        except ImportError as e:
            print(f"Could not import Image: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageCms import *
            self.tools['ImageCms'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageCms'
        except ImportError as e:
            print(f"Could not import ImageCms: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageColor import *
            self.tools['ImageColor'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageColor'
        except ImportError as e:
            print(f"Could not import ImageColor: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageDraw import *
            self.tools['ImageDraw'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageDraw'
        except ImportError as e:
            print(f"Could not import ImageDraw: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageDraw2 import *
            self.tools['ImageDraw2'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageDraw2'
        except ImportError as e:
            print(f"Could not import ImageDraw2: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageEnhance import *
            self.tools['ImageEnhance'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageEnhance'
        except ImportError as e:
            print(f"Could not import ImageEnhance: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageFile import *
            self.tools['ImageFile'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageFile'
        except ImportError as e:
            print(f"Could not import ImageFile: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageFont import *
            self.tools['ImageFont'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageFont'
        except ImportError as e:
            print(f"Could not import ImageFont: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImagePath import *
            self.tools['ImagePath'] = 'thonlibs.libthon3.11.site-packages.PIL.ImagePath'
        except ImportError as e:
            print(f"Could not import ImagePath: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageQt import *
            self.tools['ImageQt'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageQt'
        except ImportError as e:
            print(f"Could not import ImageQt: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageTk import *
            self.tools['ImageTk'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageTk'
        except ImportError as e:
            print(f"Could not import ImageTk: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageWin import *
            self.tools['ImageWin'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageWin'
        except ImportError as e:
            print(f"Could not import ImageWin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.JpegImagePlugin import *
            self.tools['JpegImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.JpegImagePlugin'
        except ImportError as e:
            print(f"Could not import JpegImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.JpegPresets import *
            self.tools['JpegPresets'] = 'thonlibs.libthon3.11.site-packages.PIL.JpegPresets'
        except ImportError as e:
            print(f"Could not import JpegPresets: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.MspImagePlugin import *
            self.tools['MspImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.MspImagePlugin'
        except ImportError as e:
            print(f"Could not import MspImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.PSDraw import *
            self.tools['PSDraw'] = 'thonlibs.libthon3.11.site-packages.PIL.PSDraw'
        except ImportError as e:
            print(f"Could not import PSDraw: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.PpmImagePlugin import *
            self.tools['PpmImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.PpmImagePlugin'
        except ImportError as e:
            print(f"Could not import PpmImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.QoiImagePlugin import *
            self.tools['QoiImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.QoiImagePlugin'
        except ImportError as e:
            print(f"Could not import QoiImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.SgiImagePlugin import *
            self.tools['SgiImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.SgiImagePlugin'
        except ImportError as e:
            print(f"Could not import SgiImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.SpiderImagePlugin import *
            self.tools['SpiderImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.SpiderImagePlugin'
        except ImportError as e:
            print(f"Could not import SpiderImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.TiffImagePlugin import *
            self.tools['TiffImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.TiffImagePlugin'
        except ImportError as e:
            print(f"Could not import TiffImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.WalImageFile import *
            self.tools['WalImageFile'] = 'thonlibs.libthon3.11.site-packages.PIL.WalImageFile'
        except ImportError as e:
            print(f"Could not import WalImageFile: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.WebPImagePlugin import *
            self.tools['WebPImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.WebPImagePlugin'
        except ImportError as e:
            print(f"Could not import WebPImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.WmfImagePlugin import *
            self.tools['WmfImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.WmfImagePlugin'
        except ImportError as e:
            print(f"Could not import WmfImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.XpmImagePlugin import *
            self.tools['XpmImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.XpmImagePlugin'
        except ImportError as e:
            print(f"Could not import XpmImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.features import *
            self.tools['features'] = 'thonlibs.libthon3.11.site-packages.PIL.features'
        except ImportError as e:
            print(f"Could not import features: {e}")
            
        try:
            from .cache.uv.sdists-v6pi.socketio-client.0.7.2.xltyDdGjrKXXB9sOqai7i.src.socketIO_client.transports import *
            self.tools['transports'] = '.cache.uv.sdists-v6pi.socketio-client.0.7.2.xltyDdGjrKXXB9sOqai7i.src.socketIO_client.transports'
        except ImportError as e:
            print(f"Could not import transports: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages._virtualenv import *
            self.tools['_virtualenv'] = 'thonlibs.libthon3.11.site-packages._virtualenv'
        except ImportError as e:
            print(f"Could not import _virtualenv: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.v1.decorator import *
            self.tools['decorator'] = 'thonlibs.libthon3.11.site-packagesdantic.v1.decorator'
        except ImportError as e:
            print(f"Could not import decorator: {e}")
            
        try:
            from src.codebase_analyzer import *
            self.tools['codebase_analyzer'] = 'src.codebase_analyzer'
        except ImportError as e:
            print(f"Could not import codebase_analyzer: {e}")
            
        try:
            from src.crypto_environment_manager import *
            self.tools['crypto_environment_manager'] = 'src.crypto_environment_manager'
        except ImportError as e:
            print(f"Could not import crypto_environment_manager: {e}")
            
        try:
            from src.integration_hub import *
            self.tools['integration_hub'] = 'src.integration_hub'
        except ImportError as e:
            print(f"Could not import integration_hub: {e}")
            
        try:
            from src.wallet_utxo_finder import *
            self.tools['wallet_utxo_finder'] = 'src.wallet_utxo_finder'
        except ImportError as e:
            print(f"Could not import wallet_utxo_finder: {e}")
            
        try:
            from src.main3 import *
            self.tools['main3'] = 'src.main3'
        except ImportError as e:
            print(f"Could not import main3: {e}")
            
        try:
            from memo-desktop.node_modules.dmg-builder.vendor.ds_store.store import *
            self.tools['store'] = 'memo-desktop.node_modules.dmg-builder.vendor.ds_store.store'
        except ImportError as e:
            print(f"Could not import store: {e}")
            
        try:
            from memo-desktop.node_modules.dmg-builder.vendor.mac_alias.bookmark import *
            self.tools['bookmark'] = 'memo-desktop.node_modules.dmg-builder.vendor.mac_alias.bookmark'
        except ImportError as e:
            print(f"Could not import bookmark: {e}")
            
        try:
            from memo-desktop.node_modules.dmg-builder.vendor.mac_alias.osx import *
            self.tools['osx'] = 'memo-desktop.node_modules.dmg-builder.vendor.mac_alias.osx'
        except ImportError as e:
            print(f"Could not import osx: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.easy_xml_test import *
            self.tools['easy_xml_test'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.easy_xml_test'
        except ImportError as e:
            print(f"Could not import easy_xml_test: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.mac_tool import *
            self.tools['mac_tool'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.mac_tool'
        except ImportError as e:
            print(f"Could not import mac_tool: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.msvs_emulation import *
            self.tools['msvs_emulation'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.msvs_emulation'
        except ImportError as e:
            print(f"Could not import msvs_emulation: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSNew import *
            self.tools['MSVSNew'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSNew'
        except ImportError as e:
            print(f"Could not import MSVSNew: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSProject import *
            self.tools['MSVSProject'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSProject'
        except ImportError as e:
            print(f"Could not import MSVSProject: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSSettings_test import *
            self.tools['MSVSSettings_test'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSSettings_test'
        except ImportError as e:
            print(f"Could not import MSVSSettings_test: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSSettings import *
            self.tools['MSVSSettings'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSSettings'
        except ImportError as e:
            print(f"Could not import MSVSSettings: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.win_tool import *
            self.tools['win_tool'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.win_tool'
        except ImportError as e:
            print(f"Could not import win_tool: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.xcode_emulation import *
            self.tools['xcode_emulation'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.xcode_emulation'
        except ImportError as e:
            print(f"Could not import xcode_emulation: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.xcodeproj_file import *
            self.tools['xcodeproj_file'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.xcodeproj_file'
        except ImportError as e:
            print(f"Could not import xcodeproj_file: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.cmake import *
            self.tools['cmake'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.cmake'
        except ImportError as e:
            print(f"Could not import cmake: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.make import *
            self.tools['make'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.make'
        except ImportError as e:
            print(f"Could not import make: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.msvs import *
            self.tools['msvs'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.msvs'
        except ImportError as e:
            print(f"Could not import msvs: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.ninja import *
            self.tools['ninja'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.ninja'
        except ImportError as e:
            print(f"Could not import ninja: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.markupsafe._native import *
            self.tools['_native'] = 'thonlibs.libthon3.11.site-packages.markupsafe._native'
        except ImportError as e:
            print(f"Could not import _native: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.blinker._utilities import *
            self.tools['_utilities'] = 'thonlibs.libthon3.11.site-packages.blinker._utilities'
        except ImportError as e:
            print(f"Could not import _utilities: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.itsdangerous.timed import *
            self.tools['timed'] = 'thonlibs.libthon3.11.site-packages.itsdangerous.timed'
        except ImportError as e:
            print(f"Could not import timed: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.itsdangerous.url_safe import *
            self.tools['url_safe'] = 'thonlibs.libthon3.11.site-packages.itsdangerous.url_safe'
        except ImportError as e:
            print(f"Could not import url_safe: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.click._textwrap import *
            self.tools['_textwrap'] = 'thonlibs.libthon3.11.site-packages.click._textwrap'
        except ImportError as e:
            print(f"Could not import _textwrap: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.click.formatting import *
            self.tools['formatting'] = 'thonlibs.libthon3.11.site-packages.click.formatting'
        except ImportError as e:
            print(f"Could not import formatting: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug._reloader import *
            self.tools['_reloader'] = 'thonlibs.libthon3.11.site-packages.werkzeug._reloader'
        except ImportError as e:
            print(f"Could not import _reloader: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.formparser import *
            self.tools['formparser'] = 'thonlibs.libthon3.11.site-packages.werkzeug.formparser'
        except ImportError as e:
            print(f"Could not import formparser: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.local import *
            self.tools['local'] = 'thonlibs.libthon3.11.site-packages.werkzeug.local'
        except ImportError as e:
            print(f"Could not import local: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.urls import *
            self.tools['urls'] = 'thonlibs.libthon3.11.site-packages.werkzeug.urls'
        except ImportError as e:
            print(f"Could not import urls: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.user_agent import *
            self.tools['user_agent'] = 'thonlibs.libthon3.11.site-packages.werkzeug.user_agent'
        except ImportError as e:
            print(f"Could not import user_agent: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.datastructures.auth import *
            self.tools['auth'] = 'thonlibs.libthon3.11.site-packages.werkzeug.datastructures.auth'
        except ImportError as e:
            print(f"Could not import auth: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.datastructures.cache_control import *
            self.tools['cache_control'] = 'thonlibs.libthon3.11.site-packages.werkzeug.datastructures.cache_control'
        except ImportError as e:
            print(f"Could not import cache_control: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.datastructures.csp import *
            self.tools['csp'] = 'thonlibs.libthon3.11.site-packages.werkzeug.datastructures.csp'
        except ImportError as e:
            print(f"Could not import csp: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.datastructures.etag import *
            self.tools['etag'] = 'thonlibs.libthon3.11.site-packages.werkzeug.datastructures.etag'
        except ImportError as e:
            print(f"Could not import etag: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.datastructures.range import *
            self.tools['range'] = 'thonlibs.libthon3.11.site-packages.werkzeug.datastructures.range'
        except ImportError as e:
            print(f"Could not import range: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.middleware.lint import *
            self.tools['lint'] = 'thonlibs.libthon3.11.site-packages.werkzeug.middleware.lint'
        except ImportError as e:
            print(f"Could not import lint: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.middleware.profiler import *
            self.tools['profiler'] = 'thonlibs.libthon3.11.site-packages.werkzeug.middleware.profiler'
        except ImportError as e:
            print(f"Could not import profiler: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.routing.converters import *
            self.tools['converters'] = 'thonlibs.libthon3.11.site-packages.werkzeug.routing.converters'
        except ImportError as e:
            print(f"Could not import converters: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.werkzeug.sansio.multipart import *
            self.tools['multipart'] = 'thonlibs.libthon3.11.site-packages.werkzeug.sansio.multipart'
        except ImportError as e:
            print(f"Could not import multipart: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2._identifier import *
            self.tools['_identifier'] = 'thonlibs.libthon3.11.site-packages.jinja2._identifier'
        except ImportError as e:
            print(f"Could not import _identifier: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.async_utils import *
            self.tools['async_utils'] = 'thonlibs.libthon3.11.site-packages.jinja2.async_utils'
        except ImportError as e:
            print(f"Could not import async_utils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.constants import *
            self.tools['constants'] = 'thonlibs.libthon3.11.site-packages.qrcode.constants'
        except ImportError as e:
            print(f"Could not import constants: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.defaults import *
            self.tools['defaults'] = 'thonlibs.libthon3.11.site-packages.jinja2.defaults'
        except ImportError as e:
            print(f"Could not import defaults: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.optimizer import *
            self.tools['optimizer'] = 'thonlibs.libthon3.11.site-packages.jinja2.optimizer'
        except ImportError as e:
            print(f"Could not import optimizer: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.jinja2.visitor import *
            self.tools['visitor'] = 'thonlibs.libthon3.11.site-packages.jinja2.visitor'
        except ImportError as e:
            print(f"Could not import visitor: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpx.__version__ import *
            self.tools['__version__'] = 'thonlibs.libthon3.11.site-packages.httpx.__version__'
        except ImportError as e:
            print(f"Could not import __version__: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.requests._internal_utils import *
            self.tools['_internal_utils'] = 'thonlibs.libthon3.11.site-packages.requests._internal_utils'
        except ImportError as e:
            print(f"Could not import _internal_utils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.requests.certs import *
            self.tools['certs'] = 'thonlibs.libthon3.11.site-packages.requests.certs'
        except ImportError as e:
            print(f"Could not import certs: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.requests.hooks import *
            self.tools['hooks'] = 'thonlibs.libthon3.11.site-packages.requests.hooks'
        except ImportError as e:
            print(f"Could not import hooks: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.resources.beta.models import *
            self.tools['models'] = 'thonlibs.libthon3.11.site-packages.anthropic.resources.beta.models'
        except ImportError as e:
            print(f"Could not import models: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.requests.packages import *
            self.tools['packages'] = 'thonlibs.libthon3.11.site-packages.requests.packages'
        except ImportError as e:
            print(f"Could not import packages: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.requests.status_codes import *
            self.tools['status_codes'] = 'thonlibs.libthon3.11.site-packages.requests.status_codes'
        except ImportError as e:
            print(f"Could not import status_codes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.idna.codec import *
            self.tools['codec'] = 'thonlibs.libthon3.11.site-packages.idna.codec'
        except ImportError as e:
            print(f"Could not import codec: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.idna.idnadata import *
            self.tools['idnadata'] = 'thonlibs.libthon3.11.site-packages.idna.idnadata'
        except ImportError as e:
            print(f"Could not import idnadata: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.idna.intranges import *
            self.tools['intranges'] = 'thonlibs.libthon3.11.site-packages.idna.intranges'
        except ImportError as e:
            print(f"Could not import intranges: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.idna.package_data import *
            self.tools['package_data'] = 'thonlibs.libthon3.11.site-packages.idna.package_data'
        except ImportError as e:
            print(f"Could not import package_data: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.idna.uts46data import *
            self.tools['uts46data'] = 'thonlibs.libthon3.11.site-packages.idna.uts46data'
        except ImportError as e:
            print(f"Could not import uts46data: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.charset_normalizer.md import *
            self.tools['md'] = 'thonlibs.libthon3.11.site-packages.charset_normalizer.md'
        except ImportError as e:
            print(f"Could not import md: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.charset_normalizer.constant import *
            self.tools['constant'] = 'thonlibs.libthon3.11.site-packages.charset_normalizer.constant'
        except ImportError as e:
            print(f"Could not import constant: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.charset_normalizer.cd import *
            self.tools['cd'] = 'thonlibs.libthon3.11.site-packages.charset_normalizer.cd'
        except ImportError as e:
            print(f"Could not import cd: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.event.legacy import *
            self.tools['legacy'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.event.legacy'
        except ImportError as e:
            print(f"Could not import legacy: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3._request_methods import *
            self.tools['_request_methods'] = 'thonlibs.libthon3.11.site-packages.urllib3._request_methods'
        except ImportError as e:
            print(f"Could not import _request_methods: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL._version import *
            self.tools['_version'] = 'thonlibs.libthon3.11.site-packages.PIL._version'
        except ImportError as e:
            print(f"Could not import _version: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3.filepost import *
            self.tools['filepost'] = 'thonlibs.libthon3.11.site-packages.urllib3.filepost'
        except ImportError as e:
            print(f"Could not import filepost: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3.http2.probe import *
            self.tools['probe'] = 'thonlibs.libthon3.11.site-packages.urllib3.http2.probe'
        except ImportError as e:
            print(f"Could not import probe: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3.util.proxy import *
            self.tools['proxy'] = 'thonlibs.libthon3.11.site-packages.urllib3.util.proxy'
        except ImportError as e:
            print(f"Could not import proxy: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3.util.ssltransport import *
            self.tools['ssltransport'] = 'thonlibs.libthon3.11.site-packages.urllib3.util.ssltransport'
        except ImportError as e:
            print(f"Could not import ssltransport: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3.util.timeout import *
            self.tools['timeout'] = 'thonlibs.libthon3.11.site-packages.urllib3.util.timeout'
        except ImportError as e:
            print(f"Could not import timeout: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.urllib3.util.wait import *
            self.tools['wait'] = 'thonlibs.libthon3.11.site-packages.urllib3.util.wait'
        except ImportError as e:
            print(f"Could not import wait: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.fastecdsa.point import *
            self.tools['point'] = 'thonlibs.libthon3.11.site-packages.fastecdsa.point'
        except ImportError as e:
            print(f"Could not import point: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.fail_initialstub_already_started import *
            self.tools['fail_initialstub_already_started'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.fail_initialstub_already_started'
        except ImportError as e:
            print(f"Could not import fail_initialstub_already_started: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.test_greenlet import *
            self.tools['test_greenlet'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.test_greenlet'
        except ImportError as e:
            print(f"Could not import test_greenlet: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.fail_switch_three_greenlets import *
            self.tools['fail_switch_three_greenlets'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.fail_switch_three_greenlets'
        except ImportError as e:
            print(f"Could not import fail_switch_three_greenlets: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.test_stack_saved import *
            self.tools['test_stack_saved'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.test_stack_saved'
        except ImportError as e:
            print(f"Could not import test_stack_saved: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.test_leaks import *
            self.tools['test_leaks'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.test_leaks'
        except ImportError as e:
            print(f"Could not import test_leaks: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.leakcheck import *
            self.tools['leakcheck'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.leakcheck'
        except ImportError as e:
            print(f"Could not import leakcheck: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.test_tracing import *
            self.tools['test_tracing'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.test_tracing'
        except ImportError as e:
            print(f"Could not import test_tracing: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.test_version import *
            self.tools['test_version'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.test_version'
        except ImportError as e:
            print(f"Could not import test_version: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.test_cpp import *
            self.tools['test_cpp'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.test_cpp'
        except ImportError as e:
            print(f"Could not import test_cpp: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.fail_slp_switch import *
            self.tools['fail_slp_switch'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.fail_slp_switch'
        except ImportError as e:
            print(f"Could not import fail_slp_switch: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.test_greenlet_trash import *
            self.tools['test_greenlet_trash'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.test_greenlet_trash'
        except ImportError as e:
            print(f"Could not import test_greenlet_trash: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.test_contextvars import *
            self.tools['test_contextvars'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.test_contextvars'
        except ImportError as e:
            print(f"Could not import test_contextvars: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.test_extension_interface import *
            self.tools['test_extension_interface'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.test_extension_interface'
        except ImportError as e:
            print(f"Could not import test_extension_interface: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.test_gc import *
            self.tools['test_gc'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.test_gc'
        except ImportError as e:
            print(f"Could not import test_gc: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.fail_switch_three_greenlets2 import *
            self.tools['fail_switch_three_greenlets2'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.fail_switch_three_greenlets2'
        except ImportError as e:
            print(f"Could not import fail_switch_three_greenlets2: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.fail_clearing_run_switches import *
            self.tools['fail_clearing_run_switches'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.fail_clearing_run_switches'
        except ImportError as e:
            print(f"Could not import fail_clearing_run_switches: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.test_generator_nested import *
            self.tools['test_generator_nested'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.test_generator_nested'
        except ImportError as e:
            print(f"Could not import test_generator_nested: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.test_generator import *
            self.tools['test_generator'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.test_generator'
        except ImportError as e:
            print(f"Could not import test_generator: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.test_weakref import *
            self.tools['test_weakref'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.test_weakref'
        except ImportError as e:
            print(f"Could not import test_weakref: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.fail_switch_two_greenlets import *
            self.tools['fail_switch_two_greenlets'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.fail_switch_two_greenlets'
        except ImportError as e:
            print(f"Could not import fail_switch_two_greenlets: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.test_throw import *
            self.tools['test_throw'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.test_throw'
        except ImportError as e:
            print(f"Could not import test_throw: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.greenlet.tests.fail_cpp_exception import *
            self.tools['fail_cpp_exception'] = 'thonlibs.libthon3.11.site-packages.greenlet.tests.fail_cpp_exception'
        except ImportError as e:
            print(f"Could not import fail_cpp_exception: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcoinlib.services.authproxy import *
            self.tools['authproxy'] = 'thonlibs.libthon3.11.site-packages.bitcoinlib.services.authproxy'
        except ImportError as e:
            print(f"Could not import authproxy: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.log import *
            self.tools['log'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.log'
        except ImportError as e:
            print(f"Could not import log: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.engine._py_row import *
            self.tools['_py_row'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.engine._py_row'
        except ImportError as e:
            print(f"Could not import _py_row: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.engine._py_processors import *
            self.tools['_py_processors'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.engine._py_processors'
        except ImportError as e:
            print(f"Could not import _py_processors: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.engine.processors import *
            self.tools['processors'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.engine.processors'
        except ImportError as e:
            print(f"Could not import processors: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.roles import *
            self.tools['roles'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.roles'
        except ImportError as e:
            print(f"Could not import roles: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql._elements_constructors import *
            self.tools['_elements_constructors'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql._elements_constructors'
        except ImportError as e:
            print(f"Could not import _elements_constructors: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.traversals import *
            self.tools['traversals'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.traversals'
        except ImportError as e:
            print(f"Could not import traversals: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.default_comparator import *
            self.tools['default_comparator'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.default_comparator'
        except ImportError as e:
            print(f"Could not import default_comparator: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.expression import *
            self.tools['expression'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.expression'
        except ImportError as e:
            print(f"Could not import expression: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.crud import *
            self.tools['crud'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.crud'
        except ImportError as e:
            print(f"Could not import crud: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.annotation import *
            self.tools['annotation'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.annotation'
        except ImportError as e:
            print(f"Could not import annotation: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql.lambdas import *
            self.tools['lambdas'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql.lambdas'
        except ImportError as e:
            print(f"Could not import lambdas: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql._orm_types import *
            self.tools['_orm_types'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql._orm_types'
        except ImportError as e:
            print(f"Could not import _orm_types: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.sql._dml_constructors import *
            self.tools['_dml_constructors'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.sql._dml_constructors'
        except ImportError as e:
            print(f"Could not import _dml_constructors: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.assertsql import *
            self.tools['assertsql'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.assertsql'
        except ImportError as e:
            print(f"Could not import assertsql: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.connectors.asyncio import *
            self.tools['asyncio'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.connectors.asyncio'
        except ImportError as e:
            print(f"Could not import asyncio: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.profiling import *
            self.tools['profiling'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.profiling'
        except ImportError as e:
            print(f"Could not import profiling: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.entities import *
            self.tools['entities'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.entities'
        except ImportError as e:
            print(f"Could not import entities: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.exclusions import *
            self.tools['exclusions'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.exclusions'
        except ImportError as e:
            print(f"Could not import exclusions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.ma.tests.test_deprecations import *
            self.tools['test_deprecations'] = 'thonlibs.libthon3.11.site-packages.numpy.ma.tests.test_deprecations'
        except ImportError as e:
            print(f"Could not import test_deprecations: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_rowcount import *
            self.tools['test_rowcount'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_rowcount'
        except ImportError as e:
            print(f"Could not import test_rowcount: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_cte import *
            self.tools['test_cte'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_cte'
        except ImportError as e:
            print(f"Could not import test_cte: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_ddl import *
            self.tools['test_ddl'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_ddl'
        except ImportError as e:
            print(f"Could not import test_ddl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_sequence import *
            self.tools['test_sequence'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_sequence'
        except ImportError as e:
            print(f"Could not import test_sequence: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_results import *
            self.tools['test_results'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_results'
        except ImportError as e:
            print(f"Could not import test_results: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_types import *
            self.tools['test_types'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_types'
        except ImportError as e:
            print(f"Could not import test_types: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_unicode_ddl import *
            self.tools['test_unicode_ddl'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_unicode_ddl'
        except ImportError as e:
            print(f"Could not import test_unicode_ddl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_insert import *
            self.tools['test_insert'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_insert'
        except ImportError as e:
            print(f"Could not import test_insert: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_update_delete import *
            self.tools['test_update_delete'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.suite.test_update_delete'
        except ImportError as e:
            print(f"Could not import test_update_delete: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.plugin.bootstrap import *
            self.tools['bootstrap'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.plugin.bootstrap'
        except ImportError as e:
            print(f"Could not import bootstrap: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.testing.fixtures.orm import *
            self.tools['orm'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.testing.fixtures.orm'
        except ImportError as e:
            print(f"Could not import orm: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.mariadb import *
            self.tools['mariadb'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.mariadb'
        except ImportError as e:
            print(f"Could not import mariadb: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.mariadbconnector import *
            self.tools['mariadbconnector'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.mariadbconnector'
        except ImportError as e:
            print(f"Could not import mariadbconnector: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.enumerated import *
            self.tools['enumerated'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.enumerated'
        except ImportError as e:
            print(f"Could not import enumerated: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysqlmysql import *
            self.tools['pymysql'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysqlmysql'
        except ImportError as e:
            print(f"Could not import pymysql: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.mysqldb import *
            self.tools['mysqldb'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mysql.mysqldb'
        except ImportError as e:
            print(f"Could not import mysqldb: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.pg_catalog import *
            self.tools['pg_catalog'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.pg_catalog'
        except ImportError as e:
            print(f"Could not import pg_catalog: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.psycopg2cffi import *
            self.tools['psycopg2cffi'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.psycopg2cffi'
        except ImportError as e:
            print(f"Could not import psycopg2cffi: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.hstore import *
            self.tools['hstore'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.hstore'
        except ImportError as e:
            print(f"Could not import hstore: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.array import *
            self.tools['array'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.postgresql.array'
        except ImportError as e:
            print(f"Could not import array: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.sqlitesqlcipher import *
            self.tools['pysqlcipher'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.sqlitesqlcipher'
        except ImportError as e:
            print(f"Could not import pysqlcipher: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mssql.information_schema import *
            self.tools['information_schema'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.dialects.mssql.information_schema'
        except ImportError as e:
            print(f"Could not import information_schema: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.evaluator import *
            self.tools['evaluator'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.evaluator'
        except ImportError as e:
            print(f"Could not import evaluator: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.identity import *
            self.tools['identity'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.identity'
        except ImportError as e:
            print(f"Could not import identity: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.dynamic import *
            self.tools['dynamic'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.dynamic'
        except ImportError as e:
            print(f"Could not import dynamic: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.orm.mapped_collection import *
            self.tools['mapped_collection'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.orm.mapped_collection'
        except ImportError as e:
            print(f"Could not import mapped_collection: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.util._has_cy import *
            self.tools['_has_cy'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.util._has_cy'
        except ImportError as e:
            print(f"Could not import _has_cy: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.util.concurrency import *
            self.tools['concurrency'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.util.concurrency'
        except ImportError as e:
            print(f"Could not import concurrency: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.util.preloaded import *
            self.tools['preloaded'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.util.preloaded'
        except ImportError as e:
            print(f"Could not import preloaded: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.util.tool_support import *
            self.tools['tool_support'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.util.tool_support'
        except ImportError as e:
            print(f"Could not import tool_support: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.util._py_collections import *
            self.tools['_py_collections'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.util._py_collections'
        except ImportError as e:
            print(f"Could not import _py_collections: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.util.queue import *
            self.tools['queue'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.util.queue'
        except ImportError as e:
            print(f"Could not import queue: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.ext.orderinglist import *
            self.tools['orderinglist'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.ext.orderinglist'
        except ImportError as e:
            print(f"Could not import orderinglist: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sqlalchemy.event.registry import *
            self.tools['registry'] = 'thonlibs.libthon3.11.site-packages.sqlalchemy.event.registry'
        except ImportError as e:
            print(f"Could not import registry: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.TurboSHAKE256 import *
            self.tools['TurboSHAKE256'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.TurboSHAKE256'
        except ImportError as e:
            print(f"Could not import TurboSHAKE256: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Hash.TupleHash256 import *
            self.tools['TupleHash256'] = 'thonlibs.libthon3.11.site-packages.Crypto.Hash.TupleHash256'
        except ImportError as e:
            print(f"Could not import TupleHash256: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.PublicKey._curve import *
            self.tools['_curve'] = 'thonlibs.libthon3.11.site-packages.Crypto.PublicKey._curve'
        except ImportError as e:
            print(f"Could not import _curve: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.Crypto.Util.Counter import *
            self.tools['Counter'] = 'thonlibs.libthon3.11.site-packages.Crypto.Util.Counter'
        except ImportError as e:
            print(f"Could not import Counter: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.dtypes import *
            self.tools['dtypes'] = 'thonlibs.libthon3.11.site-packages.numpy.dtypes'
        except ImportError as e:
            print(f"Could not import dtypes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.__config__ import *
            self.tools['__config__'] = 'thonlibs.libthon3.11.site-packages.numpy.__config__'
        except ImportError as e:
            print(f"Could not import __config__: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._configtool import *
            self.tools['_configtool'] = 'thonlibs.libthon3.11.site-packages.numpy._configtool'
        except ImportError as e:
            print(f"Could not import _configtool: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._expired_attrs_2_0 import *
            self.tools['_expired_attrs_2_0'] = 'thonlibs.libthon3.11.site-packages.numpy._expired_attrs_2_0'
        except ImportError as e:
            print(f"Could not import _expired_attrs_2_0: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._pytesttester import *
            self.tools['_pytesttester'] = 'thonlibs.libthon3.11.site-packages.numpy._pytesttester'
        except ImportError as e:
            print(f"Could not import _pytesttester: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._distributor_init import *
            self.tools['_distributor_init'] = 'thonlibs.libthon3.11.site-packages.numpy._distributor_init'
        except ImportError as e:
            print(f"Could not import _distributor_init: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._globals import *
            self.tools['_globals'] = 'thonlibs.libthon3.11.site-packages.numpy._globals'
        except ImportError as e:
            print(f"Could not import _globals: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.random._pickle import *
            self.tools['_pickle'] = 'thonlibs.libthon3.11.site-packages.numpy.random._pickle'
        except ImportError as e:
            print(f"Could not import _pickle: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.v1.parse import *
            self.tools['parse'] = 'thonlibs.libthon3.11.site-packagesdantic.v1.parse'
        except ImportError as e:
            print(f"Could not import parse: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.random.tests.test_smoke import *
            self.tools['test_smoke'] = 'thonlibs.libthon3.11.site-packages.numpy.random.tests.test_smoke'
        except ImportError as e:
            print(f"Could not import test_smoke: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.random.tests.test_randomstate_regression import *
            self.tools['test_randomstate_regression'] = 'thonlibs.libthon3.11.site-packages.numpy.random.tests.test_randomstate_regression'
        except ImportError as e:
            print(f"Could not import test_randomstate_regression: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.random.tests.test_generator_mt19937_regressions import *
            self.tools['test_generator_mt19937_regressions'] = 'thonlibs.libthon3.11.site-packages.numpy.random.tests.test_generator_mt19937_regressions'
        except ImportError as e:
            print(f"Could not import test_generator_mt19937_regressions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.random.tests.test_extending import *
            self.tools['test_extending'] = 'thonlibs.libthon3.11.site-packages.numpy.random.tests.test_extending'
        except ImportError as e:
            print(f"Could not import test_extending: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.random.tests.test_seed_sequence import *
            self.tools['test_seed_sequence'] = 'thonlibs.libthon3.11.site-packages.numpy.random.tests.test_seed_sequence'
        except ImportError as e:
            print(f"Could not import test_seed_sequence: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._utils._pep440 import *
            self.tools['_pep440'] = 'thonlibs.libthon3.11.site-packages.numpy._utils._pep440'
        except ImportError as e:
            print(f"Could not import _pep440: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._utils._convertions import *
            self.tools['_convertions'] = 'thonlibs.libthon3.11.site-packages.numpy._utils._convertions'
        except ImportError as e:
            print(f"Could not import _convertions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._utils._inspect import *
            self.tools['_inspect'] = 'thonlibs.libthon3.11.site-packages.numpy._utils._inspect'
        except ImportError as e:
            print(f"Could not import _inspect: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._typing._scalars import *
            self.tools['_scalars'] = 'thonlibs.libthon3.11.site-packages.numpy._typing._scalars'
        except ImportError as e:
            print(f"Could not import _scalars: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._typing._char_codes import *
            self.tools['_char_codes'] = 'thonlibs.libthon3.11.site-packages.numpy._typing._char_codes'
        except ImportError as e:
            print(f"Could not import _char_codes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._typing._nested_sequence import *
            self.tools['_nested_sequence'] = 'thonlibs.libthon3.11.site-packages.numpy._typing._nested_sequence'
        except ImportError as e:
            print(f"Could not import _nested_sequence: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._typing._nbit_base import *
            self.tools['_nbit_base'] = 'thonlibs.libthon3.11.site-packages.numpy._typing._nbit_base'
        except ImportError as e:
            print(f"Could not import _nbit_base: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._typing._shape import *
            self.tools['_shape'] = 'thonlibs.libthon3.11.site-packages.numpy._typing._shape'
        except ImportError as e:
            print(f"Could not import _shape: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._typing._ufunc import *
            self.tools['_ufunc'] = 'thonlibs.libthon3.11.site-packages.numpy._typing._ufunc'
        except ImportError as e:
            print(f"Could not import _ufunc: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._typing._nbit import *
            self.tools['_nbit'] = 'thonlibs.libthon3.11.site-packages.numpy._typing._nbit'
        except ImportError as e:
            print(f"Could not import _nbit: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._typing._array_like import *
            self.tools['_array_like'] = 'thonlibs.libthon3.11.site-packages.numpy._typing._array_like'
        except ImportError as e:
            print(f"Could not import _array_like: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._typing._extended_precision import *
            self.tools['_extended_precision'] = 'thonlibs.libthon3.11.site-packages.numpy._typing._extended_precision'
        except ImportError as e:
            print(f"Could not import _extended_precision: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._typing._add_docstring import *
            self.tools['_add_docstring'] = 'thonlibs.libthon3.11.site-packages.numpy._typing._add_docstring'
        except ImportError as e:
            print(f"Could not import _add_docstring: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.fft.helper import *
            self.tools['helper'] = 'thonlibs.libthon3.11.site-packages.numpy.fft.helper'
        except ImportError as e:
            print(f"Could not import helper: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.fft._pocketfft import *
            self.tools['_pocketfft'] = 'thonlibs.libthon3.11.site-packages.numpy.fft._pocketfft'
        except ImportError as e:
            print(f"Could not import _pocketfft: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.fft._helper import *
            self.tools['_helper'] = 'thonlibs.libthon3.11.site-packages.numpy.fft._helper'
        except ImportError as e:
            print(f"Could not import _helper: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.fft.tests.test_pocketfft import *
            self.tools['test_pocketfft'] = 'thonlibs.libthon3.11.site-packages.numpy.fft.tests.test_pocketfft'
        except ImportError as e:
            print(f"Could not import test_pocketfft: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.fft.tests.test_helper import *
            self.tools['test_helper'] = 'thonlibs.libthon3.11.site-packages.numpy.fft.tests.test_helper'
        except ImportError as e:
            print(f"Could not import test_helper: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.lib2def import *
            self.tools['lib2def'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.lib2def'
        except ImportError as e:
            print(f"Could not import lib2def: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.exec_command import *
            self.tools['exec_command'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.exec_command'
        except ImportError as e:
            print(f"Could not import exec_command: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.line_endings import *
            self.tools['line_endings'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.line_endings'
        except ImportError as e:
            print(f"Could not import line_endings: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.msvccompiler import *
            self.tools['msvccompiler'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.msvccompiler'
        except ImportError as e:
            print(f"Could not import msvccompiler: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils._shell_utils import *
            self.tools['_shell_utils'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils._shell_utils'
        except ImportError as e:
            print(f"Could not import _shell_utils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.unixccompiler import *
            self.tools['unixccompiler'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.unixccompiler'
        except ImportError as e:
            print(f"Could not import unixccompiler: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.npy_pkg_config import *
            self.tools['npy_pkg_config'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.npy_pkg_config'
        except ImportError as e:
            print(f"Could not import npy_pkg_config: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.pathccompiler import *
            self.tools['pathccompiler'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.pathccompiler'
        except ImportError as e:
            print(f"Could not import pathccompiler: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.intelccompiler import *
            self.tools['intelccompiler'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.intelccompiler'
        except ImportError as e:
            print(f"Could not import intelccompiler: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.armccompiler import *
            self.tools['armccompiler'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.armccompiler'
        except ImportError as e:
            print(f"Could not import armccompiler: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.msvc9compiler import *
            self.tools['msvc9compiler'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.msvc9compiler'
        except ImportError as e:
            print(f"Could not import msvc9compiler: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.numpy_distribution import *
            self.tools['numpy_distribution'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.numpy_distribution'
        except ImportError as e:
            print(f"Could not import numpy_distribution: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fujitsuccompiler import *
            self.tools['fujitsuccompiler'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fujitsuccompiler'
        except ImportError as e:
            print(f"Could not import fujitsuccompiler: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_ccompiler_opt_conf import *
            self.tools['test_ccompiler_opt_conf'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_ccompiler_opt_conf'
        except ImportError as e:
            print(f"Could not import test_ccompiler_opt_conf: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_fcompiler_intel import *
            self.tools['test_fcompiler_intel'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_fcompiler_intel'
        except ImportError as e:
            print(f"Could not import test_fcompiler_intel: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_fcompiler import *
            self.tools['test_fcompiler'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_fcompiler'
        except ImportError as e:
            print(f"Could not import test_fcompiler: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_log import *
            self.tools['test_log'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_log'
        except ImportError as e:
            print(f"Could not import test_log: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.tests.utilities import *
            self.tools['utilities'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.tests.utilities'
        except ImportError as e:
            print(f"Could not import utilities: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_system_info import *
            self.tools['test_system_info'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_system_info'
        except ImportError as e:
            print(f"Could not import test_system_info: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_mingw32ccompiler import *
            self.tools['test_mingw32ccompiler'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_mingw32ccompiler'
        except ImportError as e:
            print(f"Could not import test_mingw32ccompiler: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_misc_util import *
            self.tools['test_misc_util'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_misc_util'
        except ImportError as e:
            print(f"Could not import test_misc_util: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_shell_utils import *
            self.tools['test_shell_utils'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_shell_utils'
        except ImportError as e:
            print(f"Could not import test_shell_utils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_npy_pkg_config import *
            self.tools['test_npy_pkg_config'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_npy_pkg_config'
        except ImportError as e:
            print(f"Could not import test_npy_pkg_config: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_exec_command import *
            self.tools['test_exec_command'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_exec_command'
        except ImportError as e:
            print(f"Could not import test_exec_command: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_fcompiler_nagfor import *
            self.tools['test_fcompiler_nagfor'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_fcompiler_nagfor'
        except ImportError as e:
            print(f"Could not import test_fcompiler_nagfor: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_fcompiler_gnu import *
            self.tools['test_fcompiler_gnu'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.tests.test_fcompiler_gnu'
        except ImportError as e:
            print(f"Could not import test_fcompiler_gnu: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.arm import *
            self.tools['arm'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.arm'
        except ImportError as e:
            print(f"Could not import arm: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.g95 import *
            self.tools['g95'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.g95'
        except ImportError as e:
            print(f"Could not import g95: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.pg import *
            self.tools['pg'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.pg'
        except ImportError as e:
            print(f"Could not import pg: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.compaq import *
            self.tools['compaq'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.compaq'
        except ImportError as e:
            print(f"Could not import compaq: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.none import *
            self.tools['none'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.none'
        except ImportError as e:
            print(f"Could not import none: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.hpux import *
            self.tools['hpux'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.hpux'
        except ImportError as e:
            print(f"Could not import hpux: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.intel import *
            self.tools['intel'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.intel'
        except ImportError as e:
            print(f"Could not import intel: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.gnu import *
            self.tools['gnu'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.gnu'
        except ImportError as e:
            print(f"Could not import gnu: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.nag import *
            self.tools['nag'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.nag'
        except ImportError as e:
            print(f"Could not import nag: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.ibm import *
            self.tools['ibm'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.ibm'
        except ImportError as e:
            print(f"Could not import ibm: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.absoft import *
            self.tools['absoft'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.absoft'
        except ImportError as e:
            print(f"Could not import absoft: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.lahey import *
            self.tools['lahey'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.lahey'
        except ImportError as e:
            print(f"Could not import lahey: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.fujitsu import *
            self.tools['fujitsu'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.fujitsu'
        except ImportError as e:
            print(f"Could not import fujitsu: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.sun import *
            self.tools['sun'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.sun'
        except ImportError as e:
            print(f"Could not import sun: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.pathf95 import *
            self.tools['pathf95'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.pathf95'
        except ImportError as e:
            print(f"Could not import pathf95: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.mips import *
            self.tools['mips'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.mips'
        except ImportError as e:
            print(f"Could not import mips: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.nv import *
            self.tools['nv'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.nv'
        except ImportError as e:
            print(f"Could not import nv: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.vast import *
            self.tools['vast'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.fcompiler.vast'
        except ImportError as e:
            print(f"Could not import vast: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.develop import *
            self.tools['develop'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.develop'
        except ImportError as e:
            print(f"Could not import develop: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.bdist_rpm import *
            self.tools['bdist_rpm'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.bdist_rpm'
        except ImportError as e:
            print(f"Could not import bdist_rpm: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.command.config_compiler import *
            self.tools['config_compiler'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.command.config_compiler'
        except ImportError as e:
            print(f"Could not import config_compiler: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.command.install_clib import *
            self.tools['install_clib'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.command.install_clib'
        except ImportError as e:
            print(f"Could not import install_clib: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.command.autodist import *
            self.tools['autodist'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.command.autodist'
        except ImportError as e:
            print(f"Could not import autodist: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.command.install_data import *
            self.tools['install_data'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.command.install_data'
        except ImportError as e:
            print(f"Could not import install_data: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.command.build_scripts import *
            self.tools['build_scripts'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.command.build_scripts'
        except ImportError as e:
            print(f"Could not import build_scripts: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.command.install_headers import *
            self.tools['install_headers'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.command.install_headers'
        except ImportError as e:
            print(f"Could not import install_headers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.distutils.command.build_clib import *
            self.tools['build_clib'] = 'thonlibs.libthon3.11.site-packages.numpy.distutils.command.build_clib'
        except ImportError as e:
            print(f"Could not import build_clib: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.testing.print_coercion_tables import *
            self.tools['print_coercion_tables'] = 'thonlibs.libthon3.11.site-packages.numpy.testing.print_coercion_tables'
        except ImportError as e:
            print(f"Could not import print_coercion_tables: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.testing._private.extbuild import *
            self.tools['extbuild'] = 'thonlibs.libthon3.11.site-packages.numpy.testing._private.extbuild'
        except ImportError as e:
            print(f"Could not import extbuild: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_utils import *
            self.tools['test_utils'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_utils'
        except ImportError as e:
            print(f"Could not import test_utils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.compat3k import *
            self.tools['py3k'] = 'thonlibs.libthon3.11.site-packages.numpy.compat3k'
        except ImportError as e:
            print(f"Could not import py3k: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.diagnose import *
            self.tools['diagnose'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.diagnose'
        except ImportError as e:
            print(f"Could not import diagnose: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.common_rules import *
            self.tools['common_rules'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.common_rules'
        except ImportError as e:
            print(f"Could not import common_rules: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.auxfuncs import *
            self.tools['auxfuncs'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.auxfuncs'
        except ImportError as e:
            print(f"Could not import auxfuncs: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py._isocbind import *
            self.tools['_isocbind'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py._isocbind'
        except ImportError as e:
            print(f"Could not import _isocbind: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.symbolic import *
            self.tools['symbolic'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.symbolic'
        except ImportError as e:
            print(f"Could not import symbolic: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.use_rules import *
            self.tools['use_rules'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.use_rules'
        except ImportError as e:
            print(f"Could not import use_rules: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py._backends._distutils import *
            self.tools['_distutils'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py._backends._distutils'
        except ImportError as e:
            print(f"Could not import _distutils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py._backends._backend import *
            self.tools['_backend'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py._backends._backend'
        except ImportError as e:
            print(f"Could not import _backend: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_kind import *
            self.tools['test_kind'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_kind'
        except ImportError as e:
            print(f"Could not import test_kind: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_mixed import *
            self.tools['test_mixed'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_mixed'
        except ImportError as e:
            print(f"Could not import test_mixed: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_routines import *
            self.tools['test_routines'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_routines'
        except ImportError as e:
            print(f"Could not import test_routines: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_isoc import *
            self.tools['test_isoc'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_isoc'
        except ImportError as e:
            print(f"Could not import test_isoc: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_symbolic import *
            self.tools['test_symbolic'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_symbolic'
        except ImportError as e:
            print(f"Could not import test_symbolic: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_modules import *
            self.tools['test_modules'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_modules'
        except ImportError as e:
            print(f"Could not import test_modules: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_quoted_character import *
            self.tools['test_quoted_character'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_quoted_character'
        except ImportError as e:
            print(f"Could not import test_quoted_character: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_return_integer import *
            self.tools['test_return_integer'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_return_integer'
        except ImportError as e:
            print(f"Could not import test_return_integer: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_f2cmap import *
            self.tools['test_f2cmap'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_f2cmap'
        except ImportError as e:
            print(f"Could not import test_f2cmap: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_return_complex import *
            self.tools['test_return_complex'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_return_complex'
        except ImportError as e:
            print(f"Could not import test_return_complex: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_value_attrspec import *
            self.tools['test_value_attrspec'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_value_attrspec'
        except ImportError as e:
            print(f"Could not import test_value_attrspec: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_docs import *
            self.tools['test_docs'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_docs'
        except ImportError as e:
            print(f"Could not import test_docs: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_callback import *
            self.tools['test_callback'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_callback'
        except ImportError as e:
            print(f"Could not import test_callback: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_parameter import *
            self.tools['test_parameter'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_parameter'
        except ImportError as e:
            print(f"Could not import test_parameter: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_return_character import *
            self.tools['test_return_character'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_return_character'
        except ImportError as e:
            print(f"Could not import test_return_character: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_array_from_pyobj import *
            self.tools['test_array_from_pyobj'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_array_from_pyobj'
        except ImportError as e:
            print(f"Could not import test_array_from_pyobj: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_return_logical import *
            self.tools['test_return_logical'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_return_logical'
        except ImportError as e:
            print(f"Could not import test_return_logical: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_character import *
            self.tools['test_character'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_character'
        except ImportError as e:
            print(f"Could not import test_character: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_size import *
            self.tools['test_size'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_size'
        except ImportError as e:
            print(f"Could not import test_size: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_common import *
            self.tools['test_common'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_common'
        except ImportError as e:
            print(f"Could not import test_common: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_assumed_shape import *
            self.tools['test_assumed_shape'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_assumed_shape'
        except ImportError as e:
            print(f"Could not import test_assumed_shape: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_string import *
            self.tools['test_string'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_string'
        except ImportError as e:
            print(f"Could not import test_string: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_data import *
            self.tools['test_data'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_data'
        except ImportError as e:
            print(f"Could not import test_data: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_block_docstring import *
            self.tools['test_block_docstring'] = 'thonlibs.libthon3.11.site-packages.numpy.f2py.tests.test_block_docstring'
        except ImportError as e:
            print(f"Could not import test_block_docstring: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.tests.test_configtool import *
            self.tools['test_configtool'] = 'thonlibs.libthon3.11.site-packages.numpy.tests.test_configtool'
        except ImportError as e:
            print(f"Could not import test_configtool: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.tests.test_lazyloading import *
            self.tools['test_lazyloading'] = 'thonlibs.libthon3.11.site-packages.numpy.tests.test_lazyloading'
        except ImportError as e:
            print(f"Could not import test_lazyloading: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.tests.test_numpy_config import *
            self.tools['test_numpy_config'] = 'thonlibs.libthon3.11.site-packages.numpy.tests.test_numpy_config'
        except ImportError as e:
            print(f"Could not import test_numpy_config: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.tests.test_reloading import *
            self.tools['test_reloading'] = 'thonlibs.libthon3.11.site-packages.numpy.tests.test_reloading'
        except ImportError as e:
            print(f"Could not import test_reloading: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.tests.test_matlib import *
            self.tools['test_matlib'] = 'thonlibs.libthon3.11.site-packages.numpy.tests.test_matlib'
        except ImportError as e:
            print(f"Could not import test_matlib: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.tests.test__all__ import *
            self.tools['test__all__'] = 'thonlibs.libthon3.11.site-packages.numpy.tests.test__all__'
        except ImportError as e:
            print(f"Could not import test__all__: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.tests.test_numpy_version import *
            self.tools['test_numpy_version'] = 'thonlibs.libthon3.11.site-packages.numpy.tests.test_numpy_version'
        except ImportError as e:
            print(f"Could not import test_numpy_version: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.tests.test_scripts import *
            self.tools['test_scripts'] = 'thonlibs.libthon3.11.site-packages.numpy.tests.test_scripts'
        except ImportError as e:
            print(f"Could not import test_scripts: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.scimath import *
            self.tools['scimath'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.scimath'
        except ImportError as e:
            print(f"Could not import scimath: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.array_utils import *
            self.tools['array_utils'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.array_utils'
        except ImportError as e:
            print(f"Could not import array_utils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._user_array_impl import *
            self.tools['_user_array_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._user_array_impl'
        except ImportError as e:
            print(f"Could not import _user_array_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._utils_impl import *
            self.tools['_utils_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._utils_impl'
        except ImportError as e:
            print(f"Could not import _utils_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._nanfunctions_impl import *
            self.tools['_nanfunctions_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._nanfunctions_impl'
        except ImportError as e:
            print(f"Could not import _nanfunctions_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._twodim_base_impl import *
            self.tools['_twodim_base_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._twodim_base_impl'
        except ImportError as e:
            print(f"Could not import _twodim_base_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._shape_base_impl import *
            self.tools['_shape_base_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._shape_base_impl'
        except ImportError as e:
            print(f"Could not import _shape_base_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.recfunctions import *
            self.tools['recfunctions'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.recfunctions'
        except ImportError as e:
            print(f"Could not import recfunctions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._ufunclike_impl import *
            self.tools['_ufunclike_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._ufunclike_impl'
        except ImportError as e:
            print(f"Could not import _ufunclike_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.npyio import *
            self.tools['npyio'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.npyio'
        except ImportError as e:
            print(f"Could not import npyio: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.user_array import *
            self.tools['user_array'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.user_array'
        except ImportError as e:
            print(f"Could not import user_array: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._histograms_impl import *
            self.tools['_histograms_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._histograms_impl'
        except ImportError as e:
            print(f"Could not import _histograms_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._arrayterator_impl import *
            self.tools['_arrayterator_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._arrayterator_impl'
        except ImportError as e:
            print(f"Could not import _arrayterator_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.introspect import *
            self.tools['introspect'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.introspect'
        except ImportError as e:
            print(f"Could not import introspect: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.stride_tricks import *
            self.tools['stride_tricks'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.stride_tricks'
        except ImportError as e:
            print(f"Could not import stride_tricks: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._index_tricks_impl import *
            self.tools['_index_tricks_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._index_tricks_impl'
        except ImportError as e:
            print(f"Could not import _index_tricks_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._arraypad_impl import *
            self.tools['_arraypad_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._arraypad_impl'
        except ImportError as e:
            print(f"Could not import _arraypad_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._type_check_impl import *
            self.tools['_type_check_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._type_check_impl'
        except ImportError as e:
            print(f"Could not import _type_check_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._scimath_impl import *
            self.tools['_scimath_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._scimath_impl'
        except ImportError as e:
            print(f"Could not import _scimath_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib._arraysetops_impl import *
            self.tools['_arraysetops_impl'] = 'thonlibs.libthon3.11.site-packages.numpy.lib._arraysetops_impl'
        except ImportError as e:
            print(f"Could not import _arraysetops_impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_polynomial import *
            self.tools['test_polynomial'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_polynomial'
        except ImportError as e:
            print(f"Could not import test_polynomial: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_histograms import *
            self.tools['test_histograms'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_histograms'
        except ImportError as e:
            print(f"Could not import test_histograms: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_twodim_base import *
            self.tools['test_twodim_base'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_twodim_base'
        except ImportError as e:
            print(f"Could not import test_twodim_base: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_io import *
            self.tools['test_io'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_io'
        except ImportError as e:
            print(f"Could not import test_io: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_shape_base import *
            self.tools['test_shape_base'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_shape_base'
        except ImportError as e:
            print(f"Could not import test_shape_base: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_arrayterator import *
            self.tools['test_arrayterator'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_arrayterator'
        except ImportError as e:
            print(f"Could not import test_arrayterator: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_stride_tricks import *
            self.tools['test_stride_tricks'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_stride_tricks'
        except ImportError as e:
            print(f"Could not import test_stride_tricks: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_type_check import *
            self.tools['test_type_check'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_type_check'
        except ImportError as e:
            print(f"Could not import test_type_check: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test__version import *
            self.tools['test__version'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test__version'
        except ImportError as e:
            print(f"Could not import test__version: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_arraypad import *
            self.tools['test_arraypad'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_arraypad'
        except ImportError as e:
            print(f"Could not import test_arraypad: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_index_tricks import *
            self.tools['test_index_tricks'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_index_tricks'
        except ImportError as e:
            print(f"Could not import test_index_tricks: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_ufunclike import *
            self.tools['test_ufunclike'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_ufunclike'
        except ImportError as e:
            print(f"Could not import test_ufunclike: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_packbits import *
            self.tools['test_packbits'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_packbits'
        except ImportError as e:
            print(f"Could not import test_packbits: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test__iotools import *
            self.tools['test__iotools'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test__iotools'
        except ImportError as e:
            print(f"Could not import test__iotools: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_mixins import *
            self.tools['test_mixins'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_mixins'
        except ImportError as e:
            print(f"Could not import test_mixins: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_arraysetops import *
            self.tools['test_arraysetops'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_arraysetops'
        except ImportError as e:
            print(f"Could not import test_arraysetops: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_recfunctions import *
            self.tools['test_recfunctions'] = 'thonlibs.libthon3.11.site-packages.numpy.lib.tests.test_recfunctions'
        except ImportError as e:
            print(f"Could not import test_recfunctions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.linalg.linalg import *
            self.tools['linalg'] = 'thonlibs.libthon3.11.site-packages.numpy.linalg.linalg'
        except ImportError as e:
            print(f"Could not import linalg: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.test_runtime import *
            self.tools['test_runtime'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.test_runtime'
        except ImportError as e:
            print(f"Could not import test_runtime: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.test_typing import *
            self.tools['test_typing'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.test_typing'
        except ImportError as e:
            print(f"Could not import test_typing: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.test_isfile import *
            self.tools['test_isfile'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.test_isfile'
        except ImportError as e:
            print(f"Could not import test_isfile: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.ndarray_conversion import *
            self.tools['ndarray_conversion'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.ndarray_conversion'
        except ImportError as e:
            print(f"Could not import ndarray_conversion: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.ndarray_shape_manipulation import *
            self.tools['ndarray_shape_manipulation'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.ndarray_shape_manipulation'
        except ImportError as e:
            print(f"Could not import ndarray_shape_manipulation: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.array_like import *
            self.tools['array_like'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.array_like'
        except ImportError as e:
            print(f"Could not import array_like: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.scalars import *
            self.tools['scalars'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.scalars'
        except ImportError as e:
            print(f"Could not import scalars: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.modules import *
            self.tools['modules'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.modules'
        except ImportError as e:
            print(f"Could not import modules: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.multiarray import *
            self.tools['multiarray'] = 'thonlibs.libthon3.11.site-packages.numpy._core.multiarray'
        except ImportError as e:
            print(f"Could not import multiarray: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.flatiter import *
            self.tools['flatiter'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.flatiter'
        except ImportError as e:
            print(f"Could not import flatiter: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.array_constructors import *
            self.tools['array_constructors'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.array_constructors'
        except ImportError as e:
            print(f"Could not import array_constructors: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.nditer import *
            self.tools['nditer'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.nditer'
        except ImportError as e:
            print(f"Could not import nditer: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.bitwise_ops import *
            self.tools['bitwise_ops'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.bitwise_ops'
        except ImportError as e:
            print(f"Could not import bitwise_ops: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.simple import *
            self.tools['simple'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.simple'
        except ImportError as e:
            print(f"Could not import simple: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.lib_utils import *
            self.tools['lib_utils'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.lib_utils'
        except ImportError as e:
            print(f"Could not import lib_utils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.simple_py3 import *
            self.tools['simple_py3'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.simple_py3'
        except ImportError as e:
            print(f"Could not import simple_py3: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.comparisons import *
            self.tools['comparisons'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.comparisons'
        except ImportError as e:
            print(f"Could not import comparisons: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.arrayterator import *
            self.tools['arrayterator'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.arrayterator'
        except ImportError as e:
            print(f"Could not import arrayterator: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.shape import *
            self.tools['shape'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.shape'
        except ImportError as e:
            print(f"Could not import shape: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.ma import *
            self.tools['ma'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.ma'
        except ImportError as e:
            print(f"Could not import ma: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.ndarray_misc import *
            self.tools['ndarray_misc'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.ndarray_misc'
        except ImportError as e:
            print(f"Could not import ndarray_misc: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.literal import *
            self.tools['literal'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.literal'
        except ImportError as e:
            print(f"Could not import literal: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.numerictypes import *
            self.tools['numerictypes'] = 'thonlibs.libthon3.11.site-packages.numpy._core.numerictypes'
        except ImportError as e:
            print(f"Could not import numerictypes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.arithmetic import *
            self.tools['arithmetic'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.arithmetic'
        except ImportError as e:
            print(f"Could not import arithmetic: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.numeric import *
            self.tools['numeric'] = 'thonlibs.libthon3.11.site-packages.numpy._core.numeric'
        except ImportError as e:
            print(f"Could not import numeric: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.ufunc_config import *
            self.tools['ufunc_config'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.ufunc_config'
        except ImportError as e:
            print(f"Could not import ufunc_config: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.lib_version import *
            self.tools['lib_version'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.lib_version'
        except ImportError as e:
            print(f"Could not import lib_version: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.warnings_and_errors import *
            self.tools['warnings_and_errors'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.warnings_and_errors'
        except ImportError as e:
            print(f"Could not import warnings_and_errors: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.index_tricks import *
            self.tools['index_tricks'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.index_tricks'
        except ImportError as e:
            print(f"Could not import index_tricks: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.mod import *
            self.tools['mod'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.mod'
        except ImportError as e:
            print(f"Could not import mod: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.ufunclike import *
            self.tools['ufunclike'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.ufunclike'
        except ImportError as e:
            print(f"Could not import ufunclike: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.dtype import *
            self.tools['dtype'] = 'thonlibs.libthon3.11.site-packages.numpy.typing.tests.data.pass.dtype'
        except ImportError as e:
            print(f"Could not import dtype: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._pyinstaller.tests.test_pyinstaller import *
            self.tools['test_pyinstaller'] = 'thonlibs.libthon3.11.site-packages.numpy._pyinstaller.tests.test_pyinstaller'
        except ImportError as e:
            print(f"Could not import test_pyinstaller: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._pyinstaller.testsinstaller-smoke import *
            self.tools['pyinstaller-smoke'] = 'thonlibs.libthon3.11.site-packages.numpy._pyinstaller.testsinstaller-smoke'
        except ImportError as e:
            print(f"Could not import pyinstaller-smoke: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.matrixlib.tests.test_interaction import *
            self.tools['test_interaction'] = 'thonlibs.libthon3.11.site-packages.numpy.matrixlib.tests.test_interaction'
        except ImportError as e:
            print(f"Could not import test_interaction: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.matrixlib.tests.test_masked_matrix import *
            self.tools['test_masked_matrix'] = 'thonlibs.libthon3.11.site-packages.numpy.matrixlib.tests.test_masked_matrix'
        except ImportError as e:
            print(f"Could not import test_masked_matrix: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.matrixlib.tests.test_defmatrix import *
            self.tools['test_defmatrix'] = 'thonlibs.libthon3.11.site-packages.numpy.matrixlib.tests.test_defmatrix'
        except ImportError as e:
            print(f"Could not import test_defmatrix: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.matrixlib.tests.test_matrix_linalg import *
            self.tools['test_matrix_linalg'] = 'thonlibs.libthon3.11.site-packages.numpy.matrixlib.tests.test_matrix_linalg'
        except ImportError as e:
            print(f"Could not import test_matrix_linalg: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.umath import *
            self.tools['umath'] = 'thonlibs.libthon3.11.site-packages.numpy._core.umath'
        except ImportError as e:
            print(f"Could not import umath: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.shape_base import *
            self.tools['shape_base'] = 'thonlibs.libthon3.11.site-packages.numpy._core.shape_base'
        except ImportError as e:
            print(f"Could not import shape_base: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.getlimits import *
            self.tools['getlimits'] = 'thonlibs.libthon3.11.site-packages.numpy._core.getlimits'
        except ImportError as e:
            print(f"Could not import getlimits: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core._dtype import *
            self.tools['_dtype'] = 'thonlibs.libthon3.11.site-packages.numpy._core._dtype'
        except ImportError as e:
            print(f"Could not import _dtype: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.function_base import *
            self.tools['function_base'] = 'thonlibs.libthon3.11.site-packages.numpy._core.function_base'
        except ImportError as e:
            print(f"Could not import function_base: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.core._multiarray_umath import *
            self.tools['_multiarray_umath'] = 'thonlibs.libthon3.11.site-packages.numpy.core._multiarray_umath'
        except ImportError as e:
            print(f"Could not import _multiarray_umath: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core._dtype_ctypes import *
            self.tools['_dtype_ctypes'] = 'thonlibs.libthon3.11.site-packages.numpy._core._dtype_ctypes'
        except ImportError as e:
            print(f"Could not import _dtype_ctypes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.printoptions import *
            self.tools['printoptions'] = 'thonlibs.libthon3.11.site-packages.numpy._core.printoptions'
        except ImportError as e:
            print(f"Could not import printoptions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core._type_aliases import *
            self.tools['_type_aliases'] = 'thonlibs.libthon3.11.site-packages.numpy._core._type_aliases'
        except ImportError as e:
            print(f"Could not import _type_aliases: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core._ufunc_config import *
            self.tools['_ufunc_config'] = 'thonlibs.libthon3.11.site-packages.numpy._core._ufunc_config'
        except ImportError as e:
            print(f"Could not import _ufunc_config: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core._add_newdocs_scalars import *
            self.tools['_add_newdocs_scalars'] = 'thonlibs.libthon3.11.site-packages.numpy._core._add_newdocs_scalars'
        except ImportError as e:
            print(f"Could not import _add_newdocs_scalars: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.strings import *
            self.tools['strings'] = 'thonlibs.libthon3.11.site-packages.numpy._core.strings'
        except ImportError as e:
            print(f"Could not import strings: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core._string_helpers import *
            self.tools['_string_helpers'] = 'thonlibs.libthon3.11.site-packages.numpy._core._string_helpers'
        except ImportError as e:
            print(f"Could not import _string_helpers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.cversions import *
            self.tools['cversions'] = 'thonlibs.libthon3.11.site-packages.numpy._core.cversions'
        except ImportError as e:
            print(f"Could not import cversions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core._asarray import *
            self.tools['_asarray'] = 'thonlibs.libthon3.11.site-packages.numpy._core._asarray'
        except ImportError as e:
            print(f"Could not import _asarray: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._exceptions import *
            self.tools['_exceptions'] = 'thonlibs.libthon3.11.site-packages.httpcore._exceptions'
        except ImportError as e:
            print(f"Could not import _exceptions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core._machar import *
            self.tools['_machar'] = 'thonlibs.libthon3.11.site-packages.numpy._core._machar'
        except ImportError as e:
            print(f"Could not import _machar: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.memmap import *
            self.tools['memmap'] = 'thonlibs.libthon3.11.site-packages.numpy._core.memmap'
        except ImportError as e:
            print(f"Could not import memmap: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core._methods import *
            self.tools['_methods'] = 'thonlibs.libthon3.11.site-packages.numpy._core._methods'
        except ImportError as e:
            print(f"Could not import _methods: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_numerictypes import *
            self.tools['test_numerictypes'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_numerictypes'
        except ImportError as e:
            print(f"Could not import test_numerictypes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_scalarinherit import *
            self.tools['test_scalarinherit'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_scalarinherit'
        except ImportError as e:
            print(f"Could not import test_scalarinherit: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_cython import *
            self.tools['test_cython'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_cython'
        except ImportError as e:
            print(f"Could not import test_cython: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_cpu_features import *
            self.tools['test_cpu_features'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_cpu_features'
        except ImportError as e:
            print(f"Could not import test_cpu_features: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests._locales import *
            self.tools['_locales'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests._locales'
        except ImportError as e:
            print(f"Could not import _locales: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_print import *
            self.tools['test_print'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_print'
        except ImportError as e:
            print(f"Could not import test_print: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_errstate import *
            self.tools['test_errstate'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_errstate'
        except ImportError as e:
            print(f"Could not import test_errstate: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test__exceptions import *
            self.tools['test__exceptions'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test__exceptions'
        except ImportError as e:
            print(f"Could not import test__exceptions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_custom_dtypes import *
            self.tools['test_custom_dtypes'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_custom_dtypes'
        except ImportError as e:
            print(f"Could not import test_custom_dtypes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_protocols import *
            self.tools['test_protocols'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_protocols'
        except ImportError as e:
            print(f"Could not import test_protocols: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_multithreading import *
            self.tools['test_multithreading'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_multithreading'
        except ImportError as e:
            print(f"Could not import test_multithreading: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_hashtable import *
            self.tools['test_hashtable'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_hashtable'
        except ImportError as e:
            print(f"Could not import test_hashtable: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_casting_unittests import *
            self.tools['test_casting_unittests'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_casting_unittests'
        except ImportError as e:
            print(f"Could not import test_casting_unittests: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_getlimits import *
            self.tools['test_getlimits'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_getlimits'
        except ImportError as e:
            print(f"Could not import test_getlimits: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_scalar_methods import *
            self.tools['test_scalar_methods'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_scalar_methods'
        except ImportError as e:
            print(f"Could not import test_scalar_methods: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_indexerrors import *
            self.tools['test_indexerrors'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_indexerrors'
        except ImportError as e:
            print(f"Could not import test_indexerrors: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_machar import *
            self.tools['test_machar'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_machar'
        except ImportError as e:
            print(f"Could not import test_machar: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_conversion_utils import *
            self.tools['test_conversion_utils'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_conversion_utils'
        except ImportError as e:
            print(f"Could not import test_conversion_utils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.ma.tests.test_arrayobject import *
            self.tools['test_arrayobject'] = 'thonlibs.libthon3.11.site-packages.numpy.ma.tests.test_arrayobject'
        except ImportError as e:
            print(f"Could not import test_arrayobject: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_dtype import *
            self.tools['test_dtype'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_dtype'
        except ImportError as e:
            print(f"Could not import test_dtype: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_umath_accuracy import *
            self.tools['test_umath_accuracy'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_umath_accuracy'
        except ImportError as e:
            print(f"Could not import test_umath_accuracy: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_umath import *
            self.tools['test_umath'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_umath'
        except ImportError as e:
            print(f"Could not import test_umath: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_argparse import *
            self.tools['test_argparse'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_argparse'
        except ImportError as e:
            print(f"Could not import test_argparse: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests._natype import *
            self.tools['_natype'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests._natype'
        except ImportError as e:
            print(f"Could not import _natype: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_indexing import *
            self.tools['test_indexing'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_indexing'
        except ImportError as e:
            print(f"Could not import test_indexing: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_scalar_ctors import *
            self.tools['test_scalar_ctors'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_scalar_ctors'
        except ImportError as e:
            print(f"Could not import test_scalar_ctors: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_simd_module import *
            self.tools['test_simd_module'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_simd_module'
        except ImportError as e:
            print(f"Could not import test_simd_module: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_extint128 import *
            self.tools['test_extint128'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_extint128'
        except ImportError as e:
            print(f"Could not import test_extint128: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_cpu_dispatcher import *
            self.tools['test_cpu_dispatcher'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_cpu_dispatcher'
        except ImportError as e:
            print(f"Could not import test_cpu_dispatcher: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_limited_api import *
            self.tools['test_limited_api'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_limited_api'
        except ImportError as e:
            print(f"Could not import test_limited_api: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_arraymethod import *
            self.tools['test_arraymethod'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_arraymethod'
        except ImportError as e:
            print(f"Could not import test_arraymethod: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_nep50_promotions import *
            self.tools['test_nep50_promotions'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_nep50_promotions'
        except ImportError as e:
            print(f"Could not import test_nep50_promotions: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_dlpack import *
            self.tools['test_dlpack'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_dlpack'
        except ImportError as e:
            print(f"Could not import test_dlpack: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_array_api_info import *
            self.tools['test_array_api_info'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_array_api_info'
        except ImportError as e:
            print(f"Could not import test_array_api_info: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_ufunc import *
            self.tools['test_ufunc'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_ufunc'
        except ImportError as e:
            print(f"Could not import test_ufunc: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_arrayprint import *
            self.tools['test_arrayprint'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_arrayprint'
        except ImportError as e:
            print(f"Could not import test_arrayprint: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_unicode import *
            self.tools['test_unicode'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_unicode'
        except ImportError as e:
            print(f"Could not import test_unicode: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_abc import *
            self.tools['test_abc'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_abc'
        except ImportError as e:
            print(f"Could not import test_abc: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_defchararray import *
            self.tools['test_defchararray'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_defchararray'
        except ImportError as e:
            print(f"Could not import test_defchararray: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_casting_floatingpoint_errors import *
            self.tools['test_casting_floatingpoint_errors'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_casting_floatingpoint_errors'
        except ImportError as e:
            print(f"Could not import test_casting_floatingpoint_errors: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_memmap import *
            self.tools['test_memmap'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_memmap'
        except ImportError as e:
            print(f"Could not import test_memmap: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_longdouble import *
            self.tools['test_longdouble'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_longdouble'
        except ImportError as e:
            print(f"Could not import test_longdouble: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_simd import *
            self.tools['test_simd'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_simd'
        except ImportError as e:
            print(f"Could not import test_simd: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy._core.tests.test_strings import *
            self.tools['test_strings'] = 'thonlibs.libthon3.11.site-packages.numpy._core.tests.test_strings'
        except ImportError as e:
            print(f"Could not import test_strings: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.ma.mrecords import *
            self.tools['mrecords'] = 'thonlibs.libthon3.11.site-packages.numpy.ma.mrecords'
        except ImportError as e:
            print(f"Could not import mrecords: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.ma.testutils import *
            self.tools['testutils'] = 'thonlibs.libthon3.11.site-packages.numpy.ma.testutils'
        except ImportError as e:
            print(f"Could not import testutils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.ma.timer_comparison import *
            self.tools['timer_comparison'] = 'thonlibs.libthon3.11.site-packages.numpy.ma.timer_comparison'
        except ImportError as e:
            print(f"Could not import timer_comparison: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.ma.tests.test_subclassing import *
            self.tools['test_subclassing'] = 'thonlibs.libthon3.11.site-packages.numpy.ma.tests.test_subclassing'
        except ImportError as e:
            print(f"Could not import test_subclassing: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.ma.tests.test_extras import *
            self.tools['test_extras'] = 'thonlibs.libthon3.11.site-packages.numpy.ma.tests.test_extras'
        except ImportError as e:
            print(f"Could not import test_extras: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.ma.tests.test_mrecords import *
            self.tools['test_mrecords'] = 'thonlibs.libthon3.11.site-packages.numpy.ma.tests.test_mrecords'
        except ImportError as e:
            print(f"Could not import test_mrecords: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.legendre import *
            self.tools['legendre'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.legendre'
        except ImportError as e:
            print(f"Could not import legendre: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.polyutils import *
            self.tools['polyutils'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.polyutils'
        except ImportError as e:
            print(f"Could not import polyutils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.hermite import *
            self.tools['hermite'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.hermite'
        except ImportError as e:
            print(f"Could not import hermite: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.hermite_e import *
            self.tools['hermite_e'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.hermite_e'
        except ImportError as e:
            print(f"Could not import hermite_e: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial._polybase import *
            self.tools['_polybase'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial._polybase'
        except ImportError as e:
            print(f"Could not import _polybase: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.polynomial import *
            self.tools['polynomial'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.polynomial'
        except ImportError as e:
            print(f"Could not import polynomial: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.laguerre import *
            self.tools['laguerre'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.laguerre'
        except ImportError as e:
            print(f"Could not import laguerre: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_classes import *
            self.tools['test_classes'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_classes'
        except ImportError as e:
            print(f"Could not import test_classes: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_laguerre import *
            self.tools['test_laguerre'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_laguerre'
        except ImportError as e:
            print(f"Could not import test_laguerre: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_symbol import *
            self.tools['test_symbol'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_symbol'
        except ImportError as e:
            print(f"Could not import test_symbol: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_hermite import *
            self.tools['test_hermite'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_hermite'
        except ImportError as e:
            print(f"Could not import test_hermite: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_chebyshev import *
            self.tools['test_chebyshev'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_chebyshev'
        except ImportError as e:
            print(f"Could not import test_chebyshev: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_printing import *
            self.tools['test_printing'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_printing'
        except ImportError as e:
            print(f"Could not import test_printing: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_legendre import *
            self.tools['test_legendre'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_legendre'
        except ImportError as e:
            print(f"Could not import test_legendre: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_polyutils import *
            self.tools['test_polyutils'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_polyutils'
        except ImportError as e:
            print(f"Could not import test_polyutils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_hermite_e import *
            self.tools['test_hermite_e'] = 'thonlibs.libthon3.11.site-packages.numpy.polynomial.tests.test_hermite_e'
        except ImportError as e:
            print(f"Could not import test_hermite_e: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.depends import *
            self.tools['depends'] = 'thonlibs.libthon3.11.site-packages.setuptools.depends'
        except ImportError as e:
            print(f"Could not import depends: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.lib2to3_ex import *
            self.tools['lib2to3_ex'] = 'thonlibs.libthon3.11.site-packages.setuptools.lib2to3_ex'
        except ImportError as e:
            print(f"Could not import lib2to3_ex: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests26compat import *
            self.tools['py26compat'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests26compat'
        except ImportError as e:
            print(f"Could not import py26compat: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools27compat import *
            self.tools['py27compat'] = 'thonlibs.libthon3.11.site-packages.setuptools27compat'
        except ImportError as e:
            print(f"Could not import py27compat: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools31compat import *
            self.tools['py31compat'] = 'thonlibs.libthon3.11.site-packages.setuptools31compat'
        except ImportError as e:
            print(f"Could not import py31compat: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.script template (dev) import *
            self.tools['script template (dev)'] = 'thonlibs.libthon3.11.site-packages.setuptools.script template (dev)'
        except ImportError as e:
            print(f"Could not import script template (dev): {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.script template import *
            self.tools['script template'] = 'thonlibs.libthon3.11.site-packages.setuptools.script template'
        except ImportError as e:
            print(f"Could not import script template: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.site-patch import *
            self.tools['site-patch'] = 'thonlibs.libthon3.11.site-packages.setuptools.site-patch'
        except ImportError as e:
            print(f"Could not import site-patch: {e}")
            
        try:
            from memo-desktop.node_modules.dmg-builder.vendor.mac_alias.alias import *
            self.tools['alias'] = 'memo-desktop.node_modules.dmg-builder.vendor.mac_alias.alias'
        except ImportError as e:
            print(f"Could not import alias: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.bdist_wininst import *
            self.tools['bdist_wininst'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.bdist_wininst'
        except ImportError as e:
            print(f"Could not import bdist_wininst: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.install_egg_info import *
            self.tools['install_egg_info'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.install_egg_info'
        except ImportError as e:
            print(f"Could not import install_egg_info: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.install_scripts import *
            self.tools['install_scripts'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.install_scripts'
        except ImportError as e:
            print(f"Could not import install_scripts: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.register import *
            self.tools['register'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.register'
        except ImportError as e:
            print(f"Could not import register: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.rotate import *
            self.tools['rotate'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.rotate'
        except ImportError as e:
            print(f"Could not import rotate: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.saveopts import *
            self.tools['saveopts'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.saveopts'
        except ImportError as e:
            print(f"Could not import saveopts: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.setopt import *
            self.tools['setopt'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.setopt'
        except ImportError as e:
            print(f"Could not import setopt: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.command.upload_docs import *
            self.tools['upload_docs'] = 'thonlibs.libthon3.11.site-packages.setuptools.command.upload_docs'
        except ImportError as e:
            print(f"Could not import upload_docs: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.test_bdist_egg import *
            self.tools['test_bdist_egg'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.test_bdist_egg'
        except ImportError as e:
            print(f"Could not import test_bdist_egg: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.test_develop import *
            self.tools['test_develop'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.test_develop'
        except ImportError as e:
            print(f"Could not import test_develop: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.test_dist_info import *
            self.tools['test_dist_info'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.test_dist_info'
        except ImportError as e:
            print(f"Could not import test_dist_info: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.test_markerlib import *
            self.tools['test_markerlib'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.test_markerlib'
        except ImportError as e:
            print(f"Could not import test_markerlib: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.test_svn import *
            self.tools['test_svn'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.test_svn'
        except ImportError as e:
            print(f"Could not import test_svn: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.setuptools.tests.test_test import *
            self.tools['test_test'] = 'thonlibs.libthon3.11.site-packages.setuptools.tests.test_test'
        except ImportError as e:
            print(f"Could not import test_test: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages._markerlib.markers import *
            self.tools['markers'] = 'thonlibs.libthon3.11.site-packages._markerlib.markers'
        except ImportError as e:
            print(f"Could not import markers: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa._distutils_hack.override import *
            self.tools['override'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa._distutils_hack.override'
        except ImportError as e:
            print(f"Could not import override: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.pkg_resources.tests.test_find_distributions import *
            self.tools['test_find_distributions'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.pkg_resources.tests.test_find_distributions'
        except ImportError as e:
            print(f"Could not import test_find_distributions: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.pkg_resources.tests.test_markers import *
            self.tools['test_markers'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.pkg_resources.tests.test_markers'
        except ImportError as e:
            print(f"Could not import test_markers: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.pkg_resources.tests.test_pkg_resources import *
            self.tools['test_pkg_resources'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.pkg_resources.tests.test_pkg_resources'
        except ImportError as e:
            print(f"Could not import test_pkg_resources: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.pkg_resources.tests.test_working_set import *
            self.tools['test_working_set'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.pkg_resources.tests.test_working_set'
        except ImportError as e:
            print(f"Could not import test_working_set: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._entry_points import *
            self.tools['_entry_points'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._entry_points'
        except ImportError as e:
            print(f"Could not import _entry_points: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._imp import *
            self.tools['_imp'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._imp'
        except ImportError as e:
            print(f"Could not import _imp: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._importlib import *
            self.tools['_importlib'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._importlib'
        except ImportError as e:
            print(f"Could not import _importlib: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.importlib_metadata._itertools import *
            self.tools['_itertools'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.importlib_metadata._itertools'
        except ImportError as e:
            print(f"Could not import _itertools: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._normalization import *
            self.tools['_normalization'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._normalization'
        except ImportError as e:
            print(f"Could not import _normalization: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._path import *
            self.tools['_path'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._path'
        except ImportError as e:
            print(f"Could not import _path: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._reqs import *
            self.tools['_reqs'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._reqs'
        except ImportError as e:
            print(f"Could not import _reqs: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._shutil import *
            self.tools['_shutil'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._shutil'
        except ImportError as e:
            print(f"Could not import _shutil: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._static import *
            self.tools['_static'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._static'
        except ImportError as e:
            print(f"Could not import _static: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.zipp.glob import *
            self.tools['glob'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.zipp.glob'
        except ImportError as e:
            print(f"Could not import glob: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.installer import *
            self.tools['installer'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.installer'
        except ImportError as e:
            print(f"Could not import installer: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.launch import *
            self.tools['launch'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.launch'
        except ImportError as e:
            print(f"Could not import launch: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.modified import *
            self.tools['modified'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.modified'
        except ImportError as e:
            print(f"Could not import modified: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.monkey import *
            self.tools['monkey'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.monkey'
        except ImportError as e:
            print(f"Could not import monkey: {e}")
            
        try:
            from .cache.uv.sdists-v6pi.socketio-client.0.7.2.xltyDdGjrKXXB9sOqai7i.src.socketIO_client.namespaces import *
            self.tools['namespaces'] = '.cache.uv.sdists-v6pi.socketio-client.0.7.2.xltyDdGjrKXXB9sOqai7i.src.socketIO_client.namespaces'
        except ImportError as e:
            print(f"Could not import namespaces: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.unicode_utils import *
            self.tools['unicode_utils'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.unicode_utils'
        except ImportError as e:
            print(f"Could not import unicode_utils: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.wheel import *
            self.tools['wheel'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.wheel'
        except ImportError as e:
            print(f"Could not import wheel: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.windows_support import *
            self.tools['windows_support'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.windows_support'
        except ImportError as e:
            print(f"Could not import windows_support: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils._log import *
            self.tools['_log'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils._log'
        except ImportError as e:
            print(f"Could not import _log: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils._macos_compat import *
            self.tools['_macos_compat'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils._macos_compat'
        except ImportError as e:
            print(f"Could not import _macos_compat: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils._modified import *
            self.tools['_modified'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils._modified'
        except ImportError as e:
            print(f"Could not import _modified: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.cmd import *
            self.tools['cmd'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.cmd'
        except ImportError as e:
            print(f"Could not import cmd: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.cygwinccompiler import *
            self.tools['cygwinccompiler'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.cygwinccompiler'
        except ImportError as e:
            print(f"Could not import cygwinccompiler: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.dep_util import *
            self.tools['dep_util'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.dep_util'
        except ImportError as e:
            print(f"Could not import dep_util: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.dir_util import *
            self.tools['dir_util'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.dir_util'
        except ImportError as e:
            print(f"Could not import dir_util: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.fancy_getopt import *
            self.tools['fancy_getopt'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.fancy_getopt'
        except ImportError as e:
            print(f"Could not import fancy_getopt: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.file_util import *
            self.tools['file_util'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.file_util'
        except ImportError as e:
            print(f"Could not import file_util: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.spawn import *
            self.tools['spawn'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.spawn'
        except ImportError as e:
            print(f"Could not import spawn: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.sysconfig import *
            self.tools['sysconfig'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.sysconfig'
        except ImportError as e:
            print(f"Could not import sysconfig: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.versionpredicate import *
            self.tools['versionpredicate'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.versionpredicate'
        except ImportError as e:
            print(f"Could not import versionpredicate: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.zosccompiler import *
            self.tools['zosccompiler'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.zosccompiler'
        except ImportError as e:
            print(f"Could not import zosccompiler: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.command._framework_compat import *
            self.tools['_framework_compat'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.command._framework_compat'
        except ImportError as e:
            print(f"Could not import _framework_compat: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.command.bdist_dumb import *
            self.tools['bdist_dumb'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.command.bdist_dumb'
        except ImportError as e:
            print(f"Could not import bdist_dumb: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.command.check import *
            self.tools['check'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.command.check'
        except ImportError as e:
            print(f"Could not import check: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.command.clean import *
            self.tools['clean'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.command.clean'
        except ImportError as e:
            print(f"Could not import clean: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.compat39 import *
            self.tools['py39'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.compat39'
        except ImportError as e:
            print(f"Could not import py39: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.support import *
            self.tools['support'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.support'
        except ImportError as e:
            print(f"Could not import support: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_archive_util import *
            self.tools['test_archive_util'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_archive_util'
        except ImportError as e:
            print(f"Could not import test_archive_util: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_bdist import *
            self.tools['test_bdist'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_bdist'
        except ImportError as e:
            print(f"Could not import test_bdist: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_bdist_dumb import *
            self.tools['test_bdist_dumb'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_bdist_dumb'
        except ImportError as e:
            print(f"Could not import test_bdist_dumb: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_bdist_rpm import *
            self.tools['test_bdist_rpm'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_bdist_rpm'
        except ImportError as e:
            print(f"Could not import test_bdist_rpm: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_build import *
            self.tools['test_build'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_build'
        except ImportError as e:
            print(f"Could not import test_build: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_build_clib import *
            self.tools['test_build_clib'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_build_clib'
        except ImportError as e:
            print(f"Could not import test_build_clib: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_build_py import *
            self.tools['test_build_py'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_build_py'
        except ImportError as e:
            print(f"Could not import test_build_py: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_build_scripts import *
            self.tools['test_build_scripts'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_build_scripts'
        except ImportError as e:
            print(f"Could not import test_build_scripts: {e}")
            
        try:
            from .cache.uv.archive-v0.ewElvJ7lbFnivoa93_pQm.setuptools._distutils.tests.test_ccompiler import *
            self.tools['test_ccompiler'] = '.cache.uv.archive-v0.ewElvJ7lbFnivoa93_pQm.setuptools._distutils.tests.test_ccompiler'
        except ImportError as e:
            print(f"Could not import test_ccompiler: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_check import *
            self.tools['test_check'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_check'
        except ImportError as e:
            print(f"Could not import test_check: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_clean import *
            self.tools['test_clean'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_clean'
        except ImportError as e:
            print(f"Could not import test_clean: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_cmd import *
            self.tools['test_cmd'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_cmd'
        except ImportError as e:
            print(f"Could not import test_cmd: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_config_cmd import *
            self.tools['test_config_cmd'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_config_cmd'
        except ImportError as e:
            print(f"Could not import test_config_cmd: {e}")
            
        try:
            from .cache.uv.archive-v0.ewElvJ7lbFnivoa93_pQm.setuptools._distutils.tests.test_cygwinccompiler import *
            self.tools['test_cygwinccompiler'] = '.cache.uv.archive-v0.ewElvJ7lbFnivoa93_pQm.setuptools._distutils.tests.test_cygwinccompiler'
        except ImportError as e:
            print(f"Could not import test_cygwinccompiler: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_dir_util import *
            self.tools['test_dir_util'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_dir_util'
        except ImportError as e:
            print(f"Could not import test_dir_util: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_extension import *
            self.tools['test_extension'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_extension'
        except ImportError as e:
            print(f"Could not import test_extension: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_file_util import *
            self.tools['test_file_util'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_file_util'
        except ImportError as e:
            print(f"Could not import test_file_util: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_install import *
            self.tools['test_install'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_install'
        except ImportError as e:
            print(f"Could not import test_install: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_install_data import *
            self.tools['test_install_data'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_install_data'
        except ImportError as e:
            print(f"Could not import test_install_data: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_install_headers import *
            self.tools['test_install_headers'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_install_headers'
        except ImportError as e:
            print(f"Could not import test_install_headers: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_install_lib import *
            self.tools['test_install_lib'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_install_lib'
        except ImportError as e:
            print(f"Could not import test_install_lib: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_install_scripts import *
            self.tools['test_install_scripts'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_install_scripts'
        except ImportError as e:
            print(f"Could not import test_install_scripts: {e}")
            
        try:
            from .cache.uv.archive-v0.ewElvJ7lbFnivoa93_pQm.setuptools._distutils.tests.test_mingwccompiler import *
            self.tools['test_mingwccompiler'] = '.cache.uv.archive-v0.ewElvJ7lbFnivoa93_pQm.setuptools._distutils.tests.test_mingwccompiler'
        except ImportError as e:
            print(f"Could not import test_mingwccompiler: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_modified import *
            self.tools['test_modified'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_modified'
        except ImportError as e:
            print(f"Could not import test_modified: {e}")
            
        try:
            from .cache.uv.archive-v0.ewElvJ7lbFnivoa93_pQm.setuptools._distutils.tests.test_msvccompiler import *
            self.tools['test_msvccompiler'] = '.cache.uv.archive-v0.ewElvJ7lbFnivoa93_pQm.setuptools._distutils.tests.test_msvccompiler'
        except ImportError as e:
            print(f"Could not import test_msvccompiler: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_spawn import *
            self.tools['test_spawn'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_spawn'
        except ImportError as e:
            print(f"Could not import test_spawn: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_sysconfig import *
            self.tools['test_sysconfig'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_sysconfig'
        except ImportError as e:
            print(f"Could not import test_sysconfig: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_text_file import *
            self.tools['test_text_file'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_text_file'
        except ImportError as e:
            print(f"Could not import test_text_file: {e}")
            
        try:
            from .cache.uv.archive-v0.ewElvJ7lbFnivoa93_pQm.setuptools._distutils.tests.test_unixccompiler import *
            self.tools['test_unixccompiler'] = '.cache.uv.archive-v0.ewElvJ7lbFnivoa93_pQm.setuptools._distutils.tests.test_unixccompiler'
        except ImportError as e:
            print(f"Could not import test_unixccompiler: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.tests.test_util import *
            self.tools['test_util'] = 'thonlibs.libthon3.11.site-packages.qrcode.tests.test_util'
        except ImportError as e:
            print(f"Could not import test_util: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_versionpredicate import *
            self.tools['test_versionpredicate'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.test_versionpredicate'
        except ImportError as e:
            print(f"Could not import test_versionpredicate: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.unix_compat import *
            self.tools['unix_compat'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.tests.unix_compat'
        except ImportError as e:
            print(f"Could not import unix_compat: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.autocommand.autoasync import *
            self.tools['autoasync'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.autocommand.autoasync'
        except ImportError as e:
            print(f"Could not import autoasync: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.autocommand.autocommand import *
            self.tools['autocommand'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.autocommand.autocommand'
        except ImportError as e:
            print(f"Could not import autocommand: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.autocommand.automain import *
            self.tools['automain'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.autocommand.automain'
        except ImportError as e:
            print(f"Could not import automain: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.autocommand.autoparse import *
            self.tools['autoparse'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.autocommand.autoparse'
        except ImportError as e:
            print(f"Could not import autoparse: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.inflect.compat38 import *
            self.tools['py38'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.inflect.compat38'
        except ImportError as e:
            print(f"Could not import py38: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.importlib_metadata._adapters import *
            self.tools['_adapters'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.importlib_metadata._adapters'
        except ImportError as e:
            print(f"Could not import _adapters: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.importlib_metadata._functools import *
            self.tools['_functools'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.importlib_metadata._functools'
        except ImportError as e:
            print(f"Could not import _functools: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.importlib_metadata._meta import *
            self.tools['_meta'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.importlib_metadata._meta'
        except ImportError as e:
            print(f"Could not import _meta: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.importlib_metadata._text import *
            self.tools['_text'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.importlib_metadata._text'
        except ImportError as e:
            print(f"Could not import _text: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.compat311 import *
            self.tools['py311'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.compat311'
        except ImportError as e:
            print(f"Could not import py311: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.jaraco.text.layouts import *
            self.tools['layouts'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.jaraco.text.layouts'
        except ImportError as e:
            print(f"Could not import layouts: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.jaraco.text.show-newlines import *
            self.tools['show-newlines'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.jaraco.text.show-newlines'
        except ImportError as e:
            print(f"Could not import show-newlines: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.jaraco.text.strip-prefix import *
            self.tools['strip-prefix'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.jaraco.text.strip-prefix'
        except ImportError as e:
            print(f"Could not import strip-prefix: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.jaraco.text.to-dvorak import *
            self.tools['to-dvorak'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.jaraco.text.to-dvorak'
        except ImportError as e:
            print(f"Could not import to-dvorak: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.jaraco.text.to-qwerty import *
            self.tools['to-qwerty'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.jaraco.text.to-qwerty'
        except ImportError as e:
            print(f"Could not import to-qwerty: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.more_itertools.more import *
            self.tools['more'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.more_itertools.more'
        except ImportError as e:
            print(f"Could not import more: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging._manylinux import *
            self.tools['_manylinux'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging._manylinux'
        except ImportError as e:
            print(f"Could not import _manylinux: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging._musllinux import *
            self.tools['_musllinux'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging._musllinux'
        except ImportError as e:
            print(f"Could not import _musllinux: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging._parser import *
            self.tools['_parser'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging._parser'
        except ImportError as e:
            print(f"Could not import _parser: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging._structures import *
            self.tools['_structures'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging._structures'
        except ImportError as e:
            print(f"Could not import _structures: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging._tokenizer import *
            self.tools['_tokenizer'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging._tokenizer'
        except ImportError as e:
            print(f"Could not import _tokenizer: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.metadata import *
            self.tools['metadata'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.metadata'
        except ImportError as e:
            print(f"Could not import metadata: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging.specifiers import *
            self.tools['specifiers'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.vendored.packaging.specifiers'
        except ImportError as e:
            print(f"Could not import specifiers: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.platformdirs.windows import *
            self.tools['windows'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.platformdirs.windows'
        except ImportError as e:
            print(f"Could not import windows: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.tomli._re import *
            self.tools['_re'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.tomli._re'
        except ImportError as e:
            print(f"Could not import _re: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._decorators import *
            self.tools['_decorators'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._decorators'
        except ImportError as e:
            print(f"Could not import _decorators: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._functions import *
            self.tools['_functions'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._functions'
        except ImportError as e:
            print(f"Could not import _functions: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._importhook import *
            self.tools['_importhook'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._importhook'
        except ImportError as e:
            print(f"Could not import _importhook: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._memo import *
            self.tools['_memo'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._memo'
        except ImportError as e:
            print(f"Could not import _memo: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._pytest_plugin import *
            self.tools['_pytest_plugin'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._pytest_plugin'
        except ImportError as e:
            print(f"Could not import _pytest_plugin: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._suppression import *
            self.tools['_suppression'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._suppression'
        except ImportError as e:
            print(f"Could not import _suppression: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._transformer import *
            self.tools['_transformer'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._transformer'
        except ImportError as e:
            print(f"Could not import _transformer: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._union_transformer import *
            self.tools['_union_transformer'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.typeguard._union_transformer'
        except ImportError as e:
            print(f"Could not import _union_transformer: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel._setuptools_logging import *
            self.tools['_setuptools_logging'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel._setuptools_logging'
        except ImportError as e:
            print(f"Could not import _setuptools_logging: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.wheelfile import *
            self.tools['wheelfile'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.wheelfile'
        except ImportError as e:
            print(f"Could not import wheelfile: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.cli.pack import *
            self.tools['pack'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.cli.pack'
        except ImportError as e:
            print(f"Could not import pack: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.cli.unpack import *
            self.tools['unpack'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel.cli.unpack'
        except ImportError as e:
            print(f"Could not import unpack: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.compat310 import *
            self.tools['py310'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.compat310'
        except ImportError as e:
            print(f"Could not import py310: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.command.dist_info import *
            self.tools['dist_info'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.command.dist_info'
        except ImportError as e:
            print(f"Could not import dist_info: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.compat312 import *
            self.tools['py312'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.compat312'
        except ImportError as e:
            print(f"Could not import py312: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config.expand import *
            self.tools['expand'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config.expand'
        except ImportError as e:
            print(f"Could not import expand: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config._validate_pyproject.extra_validations import *
            self.tools['extra_validations'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config._validate_pyproject.extra_validations'
        except ImportError as e:
            print(f"Could not import extra_validations: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config._validate_pyproject.fastjsonschema_exceptions import *
            self.tools['fastjsonschema_exceptions'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config._validate_pyproject.fastjsonschema_exceptions'
        except ImportError as e:
            print(f"Could not import fastjsonschema_exceptions: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config._validate_pyproject.formats import *
            self.tools['formats'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.config._validate_pyproject.formats'
        except ImportError as e:
            print(f"Could not import formats: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.contexts import *
            self.tools['contexts'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.contexts'
        except ImportError as e:
            print(f"Could not import contexts: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.mod_with_constant import *
            self.tools['mod_with_constant'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.mod_with_constant'
        except ImportError as e:
            print(f"Could not import mod_with_constant: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.script-with-bom import *
            self.tools['script-with-bom'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.script-with-bom'
        except ImportError as e:
            print(f"Could not import script-with-bom: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_bdist_deprecations import *
            self.tools['test_bdist_deprecations'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_bdist_deprecations'
        except ImportError as e:
            print(f"Could not import test_bdist_deprecations: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_bdist_wheel import *
            self.tools['test_bdist_wheel'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_bdist_wheel'
        except ImportError as e:
            print(f"Could not import test_bdist_wheel: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_build_meta import *
            self.tools['test_build_meta'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_build_meta'
        except ImportError as e:
            print(f"Could not import test_build_meta: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_core_metadata import *
            self.tools['test_core_metadata'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_core_metadata'
        except ImportError as e:
            print(f"Could not import test_core_metadata: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_depends import *
            self.tools['test_depends'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_depends'
        except ImportError as e:
            print(f"Could not import test_depends: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_distutils_adoption import *
            self.tools['test_distutils_adoption'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_distutils_adoption'
        except ImportError as e:
            print(f"Could not import test_distutils_adoption: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_extern import *
            self.tools['test_extern'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_extern'
        except ImportError as e:
            print(f"Could not import test_extern: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_find_py_modules import *
            self.tools['test_find_py_modules'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_find_py_modules'
        except ImportError as e:
            print(f"Could not import test_find_py_modules: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_glob import *
            self.tools['test_glob'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_glob'
        except ImportError as e:
            print(f"Could not import test_glob: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_logging import *
            self.tools['test_logging'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_logging'
        except ImportError as e:
            print(f"Could not import test_logging: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_namespaces import *
            self.tools['test_namespaces'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_namespaces'
        except ImportError as e:
            print(f"Could not import test_namespaces: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_setopt import *
            self.tools['test_setopt'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_setopt'
        except ImportError as e:
            print(f"Could not import test_setopt: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_setuptools import *
            self.tools['test_setuptools'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_setuptools'
        except ImportError as e:
            print(f"Could not import test_setuptools: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_shutil_wrapper import *
            self.tools['test_shutil_wrapper'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_shutil_wrapper'
        except ImportError as e:
            print(f"Could not import test_shutil_wrapper: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_unicode_utils import *
            self.tools['test_unicode_utils'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_unicode_utils'
        except ImportError as e:
            print(f"Could not import test_unicode_utils: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_virtualenv import *
            self.tools['test_virtualenv'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_virtualenv'
        except ImportError as e:
            print(f"Could not import test_virtualenv: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_wheel import *
            self.tools['test_wheel'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.test_wheel'
        except ImportError as e:
            print(f"Could not import test_wheel: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.textwrap import *
            self.tools['textwrap'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.textwrap'
        except ImportError as e:
            print(f"Could not import textwrap: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.config.test_expand import *
            self.tools['test_expand'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.config.test_expand'
        except ImportError as e:
            print(f"Could not import test_expand: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.config.test_pyprojecttoml_dynamic_deps import *
            self.tools['test_pyprojecttoml_dynamic_deps'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.config.test_pyprojecttoml_dynamic_deps'
        except ImportError as e:
            print(f"Could not import test_pyprojecttoml_dynamic_deps: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.config.test_setupcfg import *
            self.tools['test_setupcfg'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.config.test_setupcfg'
        except ImportError as e:
            print(f"Could not import test_setupcfg: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.config.downloads.preload import *
            self.tools['preload'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.config.downloads.preload'
        except ImportError as e:
            print(f"Could not import preload: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.socketio.tests.performance_test import *
            self.tools['performance_test'] = 'thonlibs.libthon3.11.site-packages.socketio.tests.performance_test'
        except ImportError as e:
            print(f"Could not import performance_test: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa._rwlock import *
            self.tools['_rwlock'] = 'thonlibs.libthon3.11.site-packages.ecdsa._rwlock'
        except ImportError as e:
            print(f"Could not import _rwlock: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa._sha3 import *
            self.tools['_sha3'] = 'thonlibs.libthon3.11.site-packages.ecdsa._sha3'
        except ImportError as e:
            print(f"Could not import _sha3: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.curves import *
            self.tools['curves'] = 'thonlibs.libthon3.11.site-packages.ecdsa.curves'
        except ImportError as e:
            print(f"Could not import curves: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.ssh import *
            self.tools['ssh'] = 'thonlibs.libthon3.11.site-packages.ecdsa.ssh'
        except ImportError as e:
            print(f"Could not import ssh: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.test_curves import *
            self.tools['test_curves'] = 'thonlibs.libthon3.11.site-packages.ecdsa.test_curves'
        except ImportError as e:
            print(f"Could not import test_curves: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.test_der import *
            self.tools['test_der'] = 'thonlibs.libthon3.11.site-packages.ecdsa.test_der'
        except ImportError as e:
            print(f"Could not import test_der: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.test_ellipticcurve import *
            self.tools['test_ellipticcurve'] = 'thonlibs.libthon3.11.site-packages.ecdsa.test_ellipticcurve'
        except ImportError as e:
            print(f"Could not import test_ellipticcurve: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.test_jacobi import *
            self.tools['test_jacobi'] = 'thonlibs.libthon3.11.site-packages.ecdsa.test_jacobi'
        except ImportError as e:
            print(f"Could not import test_jacobi: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.test_malformed_sigs import *
            self.tools['test_malformed_sigs'] = 'thonlibs.libthon3.11.site-packages.ecdsa.test_malformed_sigs'
        except ImportError as e:
            print(f"Could not import test_malformed_sigs: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.test_numbertheory import *
            self.tools['test_numbertheory'] = 'thonlibs.libthon3.11.site-packages.ecdsa.test_numbertheory'
        except ImportError as e:
            print(f"Could not import test_numbertheory: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.test_rw_lock import *
            self.tools['test_rw_lock'] = 'thonlibs.libthon3.11.site-packages.ecdsa.test_rw_lock'
        except ImportError as e:
            print(f"Could not import test_rw_lock: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.ecdsa.test_sha3 import *
            self.tools['test_sha3'] = 'thonlibs.libthon3.11.site-packages.ecdsa.test_sha3'
        except ImportError as e:
            print(f"Could not import test_sha3: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcash._ripemd160 import *
            self.tools['_ripemd160'] = 'thonlibs.libthon3.11.site-packages.bitcash._ripemd160'
        except ImportError as e:
            print(f"Could not import _ripemd160: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.bitcash.crypto import *
            self.tools['crypto'] = 'thonlibs.libthon3.11.site-packages.bitcash.crypto'
        except ImportError as e:
            print(f"Could not import crypto: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.test_curve import *
            self.tools['test_curve'] = 'thonlibs.libthon3.11.site-packages.tests.test_curve'
        except ImportError as e:
            print(f"Could not import test_curve: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.tests.network.test_meta import *
            self.tools['test_meta'] = 'thonlibs.libthon3.11.site-packages.tests.network.test_meta'
        except ImportError as e:
            print(f"Could not import test_meta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.coincurve.flags import *
            self.tools['flags'] = 'thonlibs.libthon3.11.site-packages.coincurve.flags'
        except ImportError as e:
            print(f"Could not import flags: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._discovery import *
            self.tools['_discovery'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._discovery'
        except ImportError as e:
            print(f"Could not import _discovery: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compat.numpy import *
            self.tools['numpy'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compat.numpy'
        except ImportError as e:
            print(f"Could not import numpy: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.cygwin import *
            self.tools['cygwin'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.cygwin'
        except ImportError as e:
            print(f"Could not import cygwin: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.zos import *
            self.tools['zos'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.zos'
        except ImportError as e:
            print(f"Could not import zos: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.tests.test_base import *
            self.tools['test_base'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.tests.test_base'
        except ImportError as e:
            print(f"Could not import test_base: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.tests.test_cygwin import *
            self.tools['test_cygwin'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.tests.test_cygwin'
        except ImportError as e:
            print(f"Could not import test_cygwin: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.tests.test_mingw import *
            self.tools['test_mingw'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.tests.test_mingw'
        except ImportError as e:
            print(f"Could not import test_mingw: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.tests.test_msvc import *
            self.tools['test_msvc'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.tests.test_msvc'
        except ImportError as e:
            print(f"Could not import test_msvc: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.tests.test_unix import *
            self.tools['test_unix'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._distutils.compilers.C.tests.test_unix'
        except ImportError as e:
            print(f"Could not import test_unix: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel._bdist_wheel import *
            self.tools['_bdist_wheel'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools._vendor.wheel._bdist_wheel'
        except ImportError as e:
            print(f"Could not import _bdist_wheel: {e}")
            
        try:
            from .cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.integration.test_pbr import *
            self.tools['test_pbr'] = '.cache.uv.archive-v0.eQ6-JdWRSLT2PDxKvxPPa.setuptools.tests.integration.test_pbr'
        except ImportError as e:
            print(f"Could not import test_pbr: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.annotated_types.test_cases import *
            self.tools['test_cases'] = 'thonlibs.libthon3.11.site-packages.annotated_types.test_cases'
        except ImportError as e:
            print(f"Could not import test_cases: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.typing_inspection.introspection import *
            self.tools['introspection'] = 'thonlibs.libthon3.11.site-packages.typing_inspection.introspection'
        except ImportError as e:
            print(f"Could not import introspection: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.typing_inspection.typing_objects import *
            self.tools['typing_objects'] = 'thonlibs.libthon3.11.site-packages.typing_inspection.typing_objects'
        except ImportError as e:
            print(f"Could not import typing_objects: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.h11._readers import *
            self.tools['_readers'] = 'thonlibs.libthon3.11.site-packages.h11._readers'
        except ImportError as e:
            print(f"Could not import _readers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.h11._receivebuffer import *
            self.tools['_receivebuffer'] = 'thonlibs.libthon3.11.site-packages.h11._receivebuffer'
        except ImportError as e:
            print(f"Could not import _receivebuffer: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.h11._state import *
            self.tools['_state'] = 'thonlibs.libthon3.11.site-packages.h11._state'
        except ImportError as e:
            print(f"Could not import _state: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL._util import *
            self.tools['_util'] = 'thonlibs.libthon3.11.site-packages.PIL._util'
        except ImportError as e:
            print(f"Could not import _util: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.h11._writers import *
            self.tools['_writers'] = 'thonlibs.libthon3.11.site-packages.h11._writers'
        except ImportError as e:
            print(f"Could not import _writers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._api import *
            self.tools['_api'] = 'thonlibs.libthon3.11.site-packages.httpcore._api'
        except ImportError as e:
            print(f"Could not import _api: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpx._transports.asgi import *
            self.tools['asgi'] = 'thonlibs.libthon3.11.site-packages.httpx._transports.asgi'
        except ImportError as e:
            print(f"Could not import asgi: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sniffio._impl import *
            self.tools['_impl'] = 'thonlibs.libthon3.11.site-packages.sniffio._impl'
        except ImportError as e:
            print(f"Could not import _impl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.sniffio._tests.test_sniffio import *
            self.tools['test_sniffio'] = 'thonlibs.libthon3.11.site-packages.sniffio._tests.test_sniffio'
        except ImportError as e:
            print(f"Could not import test_sniffio: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio.from_thread import *
            self.tools['from_thread'] = 'thonlibs.libthon3.11.site-packages.anyio.from_thread'
        except ImportError as e:
            print(f"Could not import from_thread: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio.lowlevel import *
            self.tools['lowlevel'] = 'thonlibs.libthon3.11.site-packages.anyio.lowlevel'
        except ImportError as e:
            print(f"Could not import lowlevel: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio.to_interpreter import *
            self.tools['to_interpreter'] = 'thonlibs.libthon3.11.site-packages.anyio.to_interpreter'
        except ImportError as e:
            print(f"Could not import to_interpreter: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio.to_process import *
            self.tools['to_process'] = 'thonlibs.libthon3.11.site-packages.anyio.to_process'
        except ImportError as e:
            print(f"Could not import to_process: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio.to_thread import *
            self.tools['to_thread'] = 'thonlibs.libthon3.11.site-packages.anyio.to_thread'
        except ImportError as e:
            print(f"Could not import to_thread: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio._core._asyncio_selector_thread import *
            self.tools['_asyncio_selector_thread'] = 'thonlibs.libthon3.11.site-packages.anyio._core._asyncio_selector_thread'
        except ImportError as e:
            print(f"Could not import _asyncio_selector_thread: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio._core._contextmanagers import *
            self.tools['_contextmanagers'] = 'thonlibs.libthon3.11.site-packages.anyio._core._contextmanagers'
        except ImportError as e:
            print(f"Could not import _contextmanagers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio.abc._resources import *
            self.tools['_resources'] = 'thonlibs.libthon3.11.site-packages.anyio.abc._resources'
        except ImportError as e:
            print(f"Could not import _resources: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio._core._signals import *
            self.tools['_signals'] = 'thonlibs.libthon3.11.site-packages.anyio._core._signals'
        except ImportError as e:
            print(f"Could not import _signals: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio.abc._subprocesses import *
            self.tools['_subprocesses'] = 'thonlibs.libthon3.11.site-packages.anyio.abc._subprocesses'
        except ImportError as e:
            print(f"Could not import _subprocesses: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._synchronization import *
            self.tools['_synchronization'] = 'thonlibs.libthon3.11.site-packages.httpcore._synchronization'
        except ImportError as e:
            print(f"Could not import _synchronization: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio.abc._tasks import *
            self.tools['_tasks'] = 'thonlibs.libthon3.11.site-packages.anyio.abc._tasks'
        except ImportError as e:
            print(f"Could not import _tasks: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio.abc._testing import *
            self.tools['_testing'] = 'thonlibs.libthon3.11.site-packages.anyio.abc._testing'
        except ImportError as e:
            print(f"Could not import _testing: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio._core._typedattr import *
            self.tools['_typedattr'] = 'thonlibs.libthon3.11.site-packages.anyio._core._typedattr'
        except ImportError as e:
            print(f"Could not import _typedattr: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio.streams.buffered import *
            self.tools['buffered'] = 'thonlibs.libthon3.11.site-packages.anyio.streams.buffered'
        except ImportError as e:
            print(f"Could not import buffered: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio.streams.file import *
            self.tools['file'] = 'thonlibs.libthon3.11.site-packages.anyio.streams.file'
        except ImportError as e:
            print(f"Could not import file: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio.streams.memory import *
            self.tools['memory'] = 'thonlibs.libthon3.11.site-packages.anyio.streams.memory'
        except ImportError as e:
            print(f"Could not import memory: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio.streams.stapled import *
            self.tools['stapled'] = 'thonlibs.libthon3.11.site-packages.anyio.streams.stapled'
        except ImportError as e:
            print(f"Could not import stapled: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anyio.streams.tls import *
            self.tools['tls'] = 'thonlibs.libthon3.11.site-packages.anyio.streams.tls'
        except ImportError as e:
            print(f"Could not import tls: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.httpcore._ssl import *
            self.tools['_ssl'] = 'thonlibs.libthon3.11.site-packages.httpcore._ssl'
        except ImportError as e:
            print(f"Could not import _ssl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.alias_generators import *
            self.tools['alias_generators'] = 'thonlibs.libthon3.11.site-packagesdantic.alias_generators'
        except ImportError as e:
            print(f"Could not import alias_generators: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.aliases import *
            self.tools['aliases'] = 'thonlibs.libthon3.11.site-packagesdantic.aliases'
        except ImportError as e:
            print(f"Could not import aliases: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.annotated_handlers import *
            self.tools['annotated_handlers'] = 'thonlibs.libthon3.11.site-packagesdantic.annotated_handlers'
        except ImportError as e:
            print(f"Could not import annotated_handlers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.v1.datetime_parse import *
            self.tools['datetime_parse'] = 'thonlibs.libthon3.11.site-packagesdantic.v1.datetime_parse'
        except ImportError as e:
            print(f"Could not import datetime_parse: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.v1.env_settings import *
            self.tools['env_settings'] = 'thonlibs.libthon3.11.site-packagesdantic.v1.env_settings'
        except ImportError as e:
            print(f"Could not import env_settings: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.functional_serializers import *
            self.tools['functional_serializers'] = 'thonlibs.libthon3.11.site-packagesdantic.functional_serializers'
        except ImportError as e:
            print(f"Could not import functional_serializers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.functional_validators import *
            self.tools['functional_validators'] = 'thonlibs.libthon3.11.site-packagesdantic.functional_validators'
        except ImportError as e:
            print(f"Could not import functional_validators: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.v1.generics import *
            self.tools['generics'] = 'thonlibs.libthon3.11.site-packagesdantic.v1.generics'
        except ImportError as e:
            print(f"Could not import generics: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.root_model import *
            self.tools['root_model'] = 'thonlibs.libthon3.11.site-packagesdantic.root_model'
        except ImportError as e:
            print(f"Could not import root_model: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.validate_call_decorator import *
            self.tools['validate_call_decorator'] = 'thonlibs.libthon3.11.site-packagesdantic.validate_call_decorator'
        except ImportError as e:
            print(f"Could not import validate_call_decorator: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._core_utils import *
            self.tools['_core_utils'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._core_utils'
        except ImportError as e:
            print(f"Could not import _core_utils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._dataclasses import *
            self.tools['_dataclasses'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._dataclasses'
        except ImportError as e:
            print(f"Could not import _dataclasses: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._decorators_v1 import *
            self.tools['_decorators_v1'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._decorators_v1'
        except ImportError as e:
            print(f"Could not import _decorators_v1: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._discriminated_union import *
            self.tools['_discriminated_union'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._discriminated_union'
        except ImportError as e:
            print(f"Could not import _discriminated_union: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._docs_extraction import *
            self.tools['_docs_extraction'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._docs_extraction'
        except ImportError as e:
            print(f"Could not import _docs_extraction: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._forward_ref import *
            self.tools['_forward_ref'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._forward_ref'
        except ImportError as e:
            print(f"Could not import _forward_ref: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._git import *
            self.tools['_git'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._git'
        except ImportError as e:
            print(f"Could not import _git: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._import_utils import *
            self.tools['_import_utils'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._import_utils'
        except ImportError as e:
            print(f"Could not import _import_utils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._internal_dataclass import *
            self.tools['_internal_dataclass'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._internal_dataclass'
        except ImportError as e:
            print(f"Could not import _internal_dataclass: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._known_annotated_metadata import *
            self.tools['_known_annotated_metadata'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._known_annotated_metadata'
        except ImportError as e:
            print(f"Could not import _known_annotated_metadata: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._mock_val_ser import *
            self.tools['_mock_val_ser'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._mock_val_ser'
        except ImportError as e:
            print(f"Could not import _mock_val_ser: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._model_construction import *
            self.tools['_model_construction'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._model_construction'
        except ImportError as e:
            print(f"Could not import _model_construction: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._namespace_utils import *
            self.tools['_namespace_utils'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._namespace_utils'
        except ImportError as e:
            print(f"Could not import _namespace_utils: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._schema_gather import *
            self.tools['_schema_gather'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._schema_gather'
        except ImportError as e:
            print(f"Could not import _schema_gather: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._schema_generation_shared import *
            self.tools['_schema_generation_shared'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._schema_generation_shared'
        except ImportError as e:
            print(f"Could not import _schema_generation_shared: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._serializers import *
            self.tools['_serializers'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._serializers'
        except ImportError as e:
            print(f"Could not import _serializers: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._signature import *
            self.tools['_signature'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._signature'
        except ImportError as e:
            print(f"Could not import _signature: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic._internal._validate_call import *
            self.tools['_validate_call'] = 'thonlibs.libthon3.11.site-packagesdantic._internal._validate_call'
        except ImportError as e:
            print(f"Could not import _validate_call: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.deprecated.copy_internals import *
            self.tools['copy_internals'] = 'thonlibs.libthon3.11.site-packagesdantic.deprecated.copy_internals'
        except ImportError as e:
            print(f"Could not import copy_internals: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.experimental.arguments_schema import *
            self.tools['arguments_schema'] = 'thonlibs.libthon3.11.site-packagesdantic.experimental.arguments_schema'
        except ImportError as e:
            print(f"Could not import arguments_schema: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.experimental.pipeline import *
            self.tools['pipeline'] = 'thonlibs.libthon3.11.site-packagesdantic.experimental.pipeline'
        except ImportError as e:
            print(f"Could not import pipeline: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.plugin._loader import *
            self.tools['_loader'] = 'thonlibs.libthon3.11.site-packagesdantic.plugin._loader'
        except ImportError as e:
            print(f"Could not import _loader: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.plugin._schema_validator import *
            self.tools['_schema_validator'] = 'thonlibs.libthon3.11.site-packagesdantic.plugin._schema_validator'
        except ImportError as e:
            print(f"Could not import _schema_validator: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packagesdantic.v1.annotated_types import *
            self.tools['annotated_types'] = 'thonlibs.libthon3.11.site-packagesdantic.v1.annotated_types'
        except ImportError as e:
            print(f"Could not import annotated_types: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._constants import *
            self.tools['_constants'] = 'thonlibs.libthon3.11.site-packages.anthropic._constants'
        except ImportError as e:
            print(f"Could not import _constants: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._files import *
            self.tools['_files'] = 'thonlibs.libthon3.11.site-packages.anthropic._files'
        except ImportError as e:
            print(f"Could not import _files: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._legacy_response import *
            self.tools['_legacy_response'] = 'thonlibs.libthon3.11.site-packages.anthropic._legacy_response'
        except ImportError as e:
            print(f"Could not import _legacy_response: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._qs import *
            self.tools['_qs'] = 'thonlibs.libthon3.11.site-packages.anthropic._qs'
        except ImportError as e:
            print(f"Could not import _qs: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._resource import *
            self.tools['_resource'] = 'thonlibs.libthon3.11.site-packages.anthropic._resource'
        except ImportError as e:
            print(f"Could not import _resource: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._response import *
            self.tools['_response'] = 'thonlibs.libthon3.11.site-packages.anthropic._response'
        except ImportError as e:
            print(f"Could not import _response: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._decoders.jsonl import *
            self.tools['jsonl'] = 'thonlibs.libthon3.11.site-packages.anthropic._decoders.jsonl'
        except ImportError as e:
            print(f"Could not import jsonl: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._utils._datetime_parse import *
            self.tools['_datetime_parse'] = 'thonlibs.libthon3.11.site-packages.anthropic._utils._datetime_parse'
        except ImportError as e:
            print(f"Could not import _datetime_parse: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._utils._logs import *
            self.tools['_logs'] = 'thonlibs.libthon3.11.site-packages.anthropic._utils._logs'
        except ImportError as e:
            print(f"Could not import _logs: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._utils._proxy import *
            self.tools['_proxy'] = 'thonlibs.libthon3.11.site-packages.anthropic._utils._proxy'
        except ImportError as e:
            print(f"Could not import _proxy: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._utils._reflection import *
            self.tools['_reflection'] = 'thonlibs.libthon3.11.site-packages.anthropic._utils._reflection'
        except ImportError as e:
            print(f"Could not import _reflection: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic._utils._resources_proxy import *
            self.tools['_resources_proxy'] = 'thonlibs.libthon3.11.site-packages.anthropic._utils._resources_proxy'
        except ImportError as e:
            print(f"Could not import _resources_proxy: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.lib._extras._common import *
            self.tools['_common'] = 'thonlibs.libthon3.11.site-packages.anthropic.lib._extras._common'
        except ImportError as e:
            print(f"Could not import _common: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.lib._extras._google_auth import *
            self.tools['_google_auth'] = 'thonlibs.libthon3.11.site-packages.anthropic.lib._extras._google_auth'
        except ImportError as e:
            print(f"Could not import _google_auth: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.lib.vertex._beta import *
            self.tools['_beta'] = 'thonlibs.libthon3.11.site-packages.anthropic.lib.vertex._beta'
        except ImportError as e:
            print(f"Could not import _beta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.lib.vertex._beta_messages import *
            self.tools['_beta_messages'] = 'thonlibs.libthon3.11.site-packages.anthropic.lib.vertex._beta_messages'
        except ImportError as e:
            print(f"Could not import _beta_messages: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.lib.bedrock._stream import *
            self.tools['_stream'] = 'thonlibs.libthon3.11.site-packages.anthropic.lib.bedrock._stream'
        except ImportError as e:
            print(f"Could not import _stream: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.lib.bedrock._stream_decoder import *
            self.tools['_stream_decoder'] = 'thonlibs.libthon3.11.site-packages.anthropic.lib.bedrock._stream_decoder'
        except ImportError as e:
            print(f"Could not import _stream_decoder: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.lib.streaming._beta_types import *
            self.tools['_beta_types'] = 'thonlibs.libthon3.11.site-packages.anthropic.lib.streaming._beta_types'
        except ImportError as e:
            print(f"Could not import _beta_types: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.lib.streaming._messages import *
            self.tools['_messages'] = 'thonlibs.libthon3.11.site-packages.anthropic.lib.streaming._messages'
        except ImportError as e:
            print(f"Could not import _messages: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.resources.beta.beta import *
            self.tools['beta'] = 'thonlibs.libthon3.11.site-packages.anthropic.resources.beta.beta'
        except ImportError as e:
            print(f"Could not import beta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.resources.beta.files import *
            self.tools['files'] = 'thonlibs.libthon3.11.site-packages.anthropic.resources.beta.files'
        except ImportError as e:
            print(f"Could not import files: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.anthropic_beta_param import *
            self.tools['anthropic_beta_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.anthropic_beta_param'
        except ImportError as e:
            print(f"Could not import anthropic_beta_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.base64_pdf_source_param import *
            self.tools['base64_pdf_source_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.base64_pdf_source_param'
        except ImportError as e:
            print(f"Could not import base64_pdf_source_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta_api_error import *
            self.tools['beta_api_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta_api_error'
        except ImportError as e:
            print(f"Could not import beta_api_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta_authentication_error import *
            self.tools['beta_authentication_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta_authentication_error'
        except ImportError as e:
            print(f"Could not import beta_authentication_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta_billing_error import *
            self.tools['beta_billing_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta_billing_error'
        except ImportError as e:
            print(f"Could not import beta_billing_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta_error import *
            self.tools['beta_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta_error'
        except ImportError as e:
            print(f"Could not import beta_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta_error_response import *
            self.tools['beta_error_response'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta_error_response'
        except ImportError as e:
            print(f"Could not import beta_error_response: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta_gateway_timeout_error import *
            self.tools['beta_gateway_timeout_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta_gateway_timeout_error'
        except ImportError as e:
            print(f"Could not import beta_gateway_timeout_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta_invalid_request_error import *
            self.tools['beta_invalid_request_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta_invalid_request_error'
        except ImportError as e:
            print(f"Could not import beta_invalid_request_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta_not_found_error import *
            self.tools['beta_not_found_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta_not_found_error'
        except ImportError as e:
            print(f"Could not import beta_not_found_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta_overloaded_error import *
            self.tools['beta_overloaded_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta_overloaded_error'
        except ImportError as e:
            print(f"Could not import beta_overloaded_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta_permission_error import *
            self.tools['beta_permission_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta_permission_error'
        except ImportError as e:
            print(f"Could not import beta_permission_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta_rate_limit_error import *
            self.tools['beta_rate_limit_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta_rate_limit_error'
        except ImportError as e:
            print(f"Could not import beta_rate_limit_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.cache_control_ephemeral_param import *
            self.tools['cache_control_ephemeral_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.cache_control_ephemeral_param'
        except ImportError as e:
            print(f"Could not import cache_control_ephemeral_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.cache_creation import *
            self.tools['cache_creation'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.cache_creation'
        except ImportError as e:
            print(f"Could not import cache_creation: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.citation_char_location import *
            self.tools['citation_char_location'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.citation_char_location'
        except ImportError as e:
            print(f"Could not import citation_char_location: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.citation_char_location_param import *
            self.tools['citation_char_location_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.citation_char_location_param'
        except ImportError as e:
            print(f"Could not import citation_char_location_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.citation_content_block_location import *
            self.tools['citation_content_block_location'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.citation_content_block_location'
        except ImportError as e:
            print(f"Could not import citation_content_block_location: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.citation_content_block_location_param import *
            self.tools['citation_content_block_location_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.citation_content_block_location_param'
        except ImportError as e:
            print(f"Could not import citation_content_block_location_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.citation_page_location import *
            self.tools['citation_page_location'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.citation_page_location'
        except ImportError as e:
            print(f"Could not import citation_page_location: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.citation_page_location_param import *
            self.tools['citation_page_location_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.citation_page_location_param'
        except ImportError as e:
            print(f"Could not import citation_page_location_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.citation_search_result_location_param import *
            self.tools['citation_search_result_location_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.citation_search_result_location_param'
        except ImportError as e:
            print(f"Could not import citation_search_result_location_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.citations_config_param import *
            self.tools['citations_config_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.citations_config_param'
        except ImportError as e:
            print(f"Could not import citations_config_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.citations_search_result_location import *
            self.tools['citations_search_result_location'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.citations_search_result_location'
        except ImportError as e:
            print(f"Could not import citations_search_result_location: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.completion import *
            self.tools['completion'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.completion'
        except ImportError as e:
            print(f"Could not import completion: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.content_block_delta_event import *
            self.tools['content_block_delta_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.content_block_delta_event'
        except ImportError as e:
            print(f"Could not import content_block_delta_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.content_block_source_content_param import *
            self.tools['content_block_source_content_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.content_block_source_content_param'
        except ImportError as e:
            print(f"Could not import content_block_source_content_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.content_block_source_param import *
            self.tools['content_block_source_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.content_block_source_param'
        except ImportError as e:
            print(f"Could not import content_block_source_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.content_block_start_event import *
            self.tools['content_block_start_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.content_block_start_event'
        except ImportError as e:
            print(f"Could not import content_block_start_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.content_block_stop_event import *
            self.tools['content_block_stop_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.content_block_stop_event'
        except ImportError as e:
            print(f"Could not import content_block_stop_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.document_block_param import *
            self.tools['document_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.document_block_param'
        except ImportError as e:
            print(f"Could not import document_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.image_block_param import *
            self.tools['image_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.image_block_param'
        except ImportError as e:
            print(f"Could not import image_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.input_json_delta import *
            self.tools['input_json_delta'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.input_json_delta'
        except ImportError as e:
            print(f"Could not import input_json_delta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.message import *
            self.tools['message'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.message'
        except ImportError as e:
            print(f"Could not import message: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.message_delta_event import *
            self.tools['message_delta_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.message_delta_event'
        except ImportError as e:
            print(f"Could not import message_delta_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.message_delta_usage import *
            self.tools['message_delta_usage'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.message_delta_usage'
        except ImportError as e:
            print(f"Could not import message_delta_usage: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.message_start_event import *
            self.tools['message_start_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.message_start_event'
        except ImportError as e:
            print(f"Could not import message_start_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.message_stop_event import *
            self.tools['message_stop_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.message_stop_event'
        except ImportError as e:
            print(f"Could not import message_stop_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.message_stream_event import *
            self.tools['message_stream_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.message_stream_event'
        except ImportError as e:
            print(f"Could not import message_stream_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.message_tokens_count import *
            self.tools['message_tokens_count'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.message_tokens_count'
        except ImportError as e:
            print(f"Could not import message_tokens_count: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.model_info import *
            self.tools['model_info'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.model_info'
        except ImportError as e:
            print(f"Could not import model_info: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.model_list_params import *
            self.tools['model_list_params'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.model_list_params'
        except ImportError as e:
            print(f"Could not import model_list_params: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.model_param import *
            self.tools['model_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.model_param'
        except ImportError as e:
            print(f"Could not import model_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.plain_text_source_param import *
            self.tools['plain_text_source_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.plain_text_source_param'
        except ImportError as e:
            print(f"Could not import plain_text_source_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.raw_content_block_delta import *
            self.tools['raw_content_block_delta'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.raw_content_block_delta'
        except ImportError as e:
            print(f"Could not import raw_content_block_delta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.raw_content_block_delta_event import *
            self.tools['raw_content_block_delta_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.raw_content_block_delta_event'
        except ImportError as e:
            print(f"Could not import raw_content_block_delta_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.raw_content_block_stop_event import *
            self.tools['raw_content_block_stop_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.raw_content_block_stop_event'
        except ImportError as e:
            print(f"Could not import raw_content_block_stop_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.raw_message_delta_event import *
            self.tools['raw_message_delta_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.raw_message_delta_event'
        except ImportError as e:
            print(f"Could not import raw_message_delta_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.raw_message_start_event import *
            self.tools['raw_message_start_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.raw_message_start_event'
        except ImportError as e:
            print(f"Could not import raw_message_start_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.raw_message_stop_event import *
            self.tools['raw_message_stop_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.raw_message_stop_event'
        except ImportError as e:
            print(f"Could not import raw_message_stop_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.raw_message_stream_event import *
            self.tools['raw_message_stream_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.raw_message_stream_event'
        except ImportError as e:
            print(f"Could not import raw_message_stream_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.redacted_thinking_block import *
            self.tools['redacted_thinking_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.redacted_thinking_block'
        except ImportError as e:
            print(f"Could not import redacted_thinking_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.redacted_thinking_block_param import *
            self.tools['redacted_thinking_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.redacted_thinking_block_param'
        except ImportError as e:
            print(f"Could not import redacted_thinking_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.search_result_block_param import *
            self.tools['search_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.search_result_block_param'
        except ImportError as e:
            print(f"Could not import search_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.signature_delta import *
            self.tools['signature_delta'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.signature_delta'
        except ImportError as e:
            print(f"Could not import signature_delta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.stop_reason import *
            self.tools['stop_reason'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.stop_reason'
        except ImportError as e:
            print(f"Could not import stop_reason: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.text_block import *
            self.tools['text_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.text_block'
        except ImportError as e:
            print(f"Could not import text_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.text_block_param import *
            self.tools['text_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.text_block_param'
        except ImportError as e:
            print(f"Could not import text_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.text_delta import *
            self.tools['text_delta'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.text_delta'
        except ImportError as e:
            print(f"Could not import text_delta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.thinking_block import *
            self.tools['thinking_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.thinking_block'
        except ImportError as e:
            print(f"Could not import thinking_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.thinking_block_param import *
            self.tools['thinking_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.thinking_block_param'
        except ImportError as e:
            print(f"Could not import thinking_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.thinking_config_disabled_param import *
            self.tools['thinking_config_disabled_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.thinking_config_disabled_param'
        except ImportError as e:
            print(f"Could not import thinking_config_disabled_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.thinking_config_enabled_param import *
            self.tools['thinking_config_enabled_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.thinking_config_enabled_param'
        except ImportError as e:
            print(f"Could not import thinking_config_enabled_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.thinking_config_param import *
            self.tools['thinking_config_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.thinking_config_param'
        except ImportError as e:
            print(f"Could not import thinking_config_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.thinking_delta import *
            self.tools['thinking_delta'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.thinking_delta'
        except ImportError as e:
            print(f"Could not import thinking_delta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.tool_bash_20250124_param import *
            self.tools['tool_bash_20250124_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.tool_bash_20250124_param'
        except ImportError as e:
            print(f"Could not import tool_bash_20250124_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.tool_choice_any_param import *
            self.tools['tool_choice_any_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.tool_choice_any_param'
        except ImportError as e:
            print(f"Could not import tool_choice_any_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.tool_choice_auto_param import *
            self.tools['tool_choice_auto_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.tool_choice_auto_param'
        except ImportError as e:
            print(f"Could not import tool_choice_auto_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.tool_choice_none_param import *
            self.tools['tool_choice_none_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.tool_choice_none_param'
        except ImportError as e:
            print(f"Could not import tool_choice_none_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.tool_choice_param import *
            self.tools['tool_choice_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.tool_choice_param'
        except ImportError as e:
            print(f"Could not import tool_choice_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.tool_choice_tool_param import *
            self.tools['tool_choice_tool_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.tool_choice_tool_param'
        except ImportError as e:
            print(f"Could not import tool_choice_tool_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.tool_param import *
            self.tools['tool_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.tool_param'
        except ImportError as e:
            print(f"Could not import tool_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.tool_result_block_param import *
            self.tools['tool_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.tool_result_block_param'
        except ImportError as e:
            print(f"Could not import tool_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.tool_text_editor_20250124_param import *
            self.tools['tool_text_editor_20250124_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.tool_text_editor_20250124_param'
        except ImportError as e:
            print(f"Could not import tool_text_editor_20250124_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.tool_text_editor_20250429_param import *
            self.tools['tool_text_editor_20250429_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.tool_text_editor_20250429_param'
        except ImportError as e:
            print(f"Could not import tool_text_editor_20250429_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.tool_text_editor_20250728_param import *
            self.tools['tool_text_editor_20250728_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.tool_text_editor_20250728_param'
        except ImportError as e:
            print(f"Could not import tool_text_editor_20250728_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.tool_use_block import *
            self.tools['tool_use_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.tool_use_block'
        except ImportError as e:
            print(f"Could not import tool_use_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.tool_use_block_param import *
            self.tools['tool_use_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.tool_use_block_param'
        except ImportError as e:
            print(f"Could not import tool_use_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.url_image_source_param import *
            self.tools['url_image_source_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.url_image_source_param'
        except ImportError as e:
            print(f"Could not import url_image_source_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.url_pdf_source_param import *
            self.tools['url_pdf_source_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.url_pdf_source_param'
        except ImportError as e:
            print(f"Could not import url_pdf_source_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.usage import *
            self.tools['usage'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.usage'
        except ImportError as e:
            print(f"Could not import usage: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_base64_pdf_block_param import *
            self.tools['beta_base64_pdf_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_base64_pdf_block_param'
        except ImportError as e:
            print(f"Could not import beta_base64_pdf_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_base64_pdf_source import *
            self.tools['beta_base64_pdf_source'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_base64_pdf_source'
        except ImportError as e:
            print(f"Could not import beta_base64_pdf_source: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_base64_pdf_source_param import *
            self.tools['beta_base64_pdf_source_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_base64_pdf_source_param'
        except ImportError as e:
            print(f"Could not import beta_base64_pdf_source_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_output_block import *
            self.tools['beta_bash_code_execution_output_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_output_block'
        except ImportError as e:
            print(f"Could not import beta_bash_code_execution_output_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_output_block_param import *
            self.tools['beta_bash_code_execution_output_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_output_block_param'
        except ImportError as e:
            print(f"Could not import beta_bash_code_execution_output_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_result_block import *
            self.tools['beta_bash_code_execution_result_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_result_block'
        except ImportError as e:
            print(f"Could not import beta_bash_code_execution_result_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_result_block_param import *
            self.tools['beta_bash_code_execution_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_result_block_param'
        except ImportError as e:
            print(f"Could not import beta_bash_code_execution_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_tool_result_block import *
            self.tools['beta_bash_code_execution_tool_result_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_tool_result_block'
        except ImportError as e:
            print(f"Could not import beta_bash_code_execution_tool_result_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_tool_result_block_param import *
            self.tools['beta_bash_code_execution_tool_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_tool_result_block_param'
        except ImportError as e:
            print(f"Could not import beta_bash_code_execution_tool_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_tool_result_error import *
            self.tools['beta_bash_code_execution_tool_result_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_tool_result_error'
        except ImportError as e:
            print(f"Could not import beta_bash_code_execution_tool_result_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_tool_result_error_param import *
            self.tools['beta_bash_code_execution_tool_result_error_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_bash_code_execution_tool_result_error_param'
        except ImportError as e:
            print(f"Could not import beta_bash_code_execution_tool_result_error_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_cache_control_ephemeral_param import *
            self.tools['beta_cache_control_ephemeral_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_cache_control_ephemeral_param'
        except ImportError as e:
            print(f"Could not import beta_cache_control_ephemeral_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_cache_creation import *
            self.tools['beta_cache_creation'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_cache_creation'
        except ImportError as e:
            print(f"Could not import beta_cache_creation: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_char_location import *
            self.tools['beta_citation_char_location'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_char_location'
        except ImportError as e:
            print(f"Could not import beta_citation_char_location: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_char_location_param import *
            self.tools['beta_citation_char_location_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_char_location_param'
        except ImportError as e:
            print(f"Could not import beta_citation_char_location_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_config import *
            self.tools['beta_citation_config'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_config'
        except ImportError as e:
            print(f"Could not import beta_citation_config: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_content_block_location import *
            self.tools['beta_citation_content_block_location'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_content_block_location'
        except ImportError as e:
            print(f"Could not import beta_citation_content_block_location: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_content_block_location_param import *
            self.tools['beta_citation_content_block_location_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_content_block_location_param'
        except ImportError as e:
            print(f"Could not import beta_citation_content_block_location_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_page_location import *
            self.tools['beta_citation_page_location'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_page_location'
        except ImportError as e:
            print(f"Could not import beta_citation_page_location: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_page_location_param import *
            self.tools['beta_citation_page_location_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_page_location_param'
        except ImportError as e:
            print(f"Could not import beta_citation_page_location_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_search_result_location import *
            self.tools['beta_citation_search_result_location'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_search_result_location'
        except ImportError as e:
            print(f"Could not import beta_citation_search_result_location: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_search_result_location_param import *
            self.tools['beta_citation_search_result_location_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citation_search_result_location_param'
        except ImportError as e:
            print(f"Could not import beta_citation_search_result_location_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citations_config_param import *
            self.tools['beta_citations_config_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_citations_config_param'
        except ImportError as e:
            print(f"Could not import beta_citations_config_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_output_block import *
            self.tools['beta_code_execution_output_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_output_block'
        except ImportError as e:
            print(f"Could not import beta_code_execution_output_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_output_block_param import *
            self.tools['beta_code_execution_output_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_output_block_param'
        except ImportError as e:
            print(f"Could not import beta_code_execution_output_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_result_block import *
            self.tools['beta_code_execution_result_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_result_block'
        except ImportError as e:
            print(f"Could not import beta_code_execution_result_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_result_block_param import *
            self.tools['beta_code_execution_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_result_block_param'
        except ImportError as e:
            print(f"Could not import beta_code_execution_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_20250522_param import *
            self.tools['beta_code_execution_tool_20250522_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_20250522_param'
        except ImportError as e:
            print(f"Could not import beta_code_execution_tool_20250522_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_20250825_param import *
            self.tools['beta_code_execution_tool_20250825_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_20250825_param'
        except ImportError as e:
            print(f"Could not import beta_code_execution_tool_20250825_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_result_block import *
            self.tools['beta_code_execution_tool_result_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_result_block'
        except ImportError as e:
            print(f"Could not import beta_code_execution_tool_result_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_result_block_content import *
            self.tools['beta_code_execution_tool_result_block_content'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_result_block_content'
        except ImportError as e:
            print(f"Could not import beta_code_execution_tool_result_block_content: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_result_block_param import *
            self.tools['beta_code_execution_tool_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_result_block_param'
        except ImportError as e:
            print(f"Could not import beta_code_execution_tool_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_result_block_param_content_param import *
            self.tools['beta_code_execution_tool_result_block_param_content_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_result_block_param_content_param'
        except ImportError as e:
            print(f"Could not import beta_code_execution_tool_result_block_param_content_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_result_error import *
            self.tools['beta_code_execution_tool_result_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_result_error'
        except ImportError as e:
            print(f"Could not import beta_code_execution_tool_result_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_result_error_code import *
            self.tools['beta_code_execution_tool_result_error_code'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_result_error_code'
        except ImportError as e:
            print(f"Could not import beta_code_execution_tool_result_error_code: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_result_error_param import *
            self.tools['beta_code_execution_tool_result_error_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_code_execution_tool_result_error_param'
        except ImportError as e:
            print(f"Could not import beta_code_execution_tool_result_error_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_container import *
            self.tools['beta_container'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_container'
        except ImportError as e:
            print(f"Could not import beta_container: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_container_upload_block import *
            self.tools['beta_container_upload_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_container_upload_block'
        except ImportError as e:
            print(f"Could not import beta_container_upload_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_container_upload_block_param import *
            self.tools['beta_container_upload_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_container_upload_block_param'
        except ImportError as e:
            print(f"Could not import beta_container_upload_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_content_block_source_content_param import *
            self.tools['beta_content_block_source_content_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_content_block_source_content_param'
        except ImportError as e:
            print(f"Could not import beta_content_block_source_content_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_content_block_source_param import *
            self.tools['beta_content_block_source_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_content_block_source_param'
        except ImportError as e:
            print(f"Could not import beta_content_block_source_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_document_block import *
            self.tools['beta_document_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_document_block'
        except ImportError as e:
            print(f"Could not import beta_document_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_file_document_source_param import *
            self.tools['beta_file_document_source_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_file_document_source_param'
        except ImportError as e:
            print(f"Could not import beta_file_document_source_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_file_image_source_param import *
            self.tools['beta_file_image_source_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_file_image_source_param'
        except ImportError as e:
            print(f"Could not import beta_file_image_source_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_image_block_param import *
            self.tools['beta_image_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_image_block_param'
        except ImportError as e:
            print(f"Could not import beta_image_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_input_json_delta import *
            self.tools['beta_input_json_delta'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_input_json_delta'
        except ImportError as e:
            print(f"Could not import beta_input_json_delta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_mcp_tool_result_block import *
            self.tools['beta_mcp_tool_result_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_mcp_tool_result_block'
        except ImportError as e:
            print(f"Could not import beta_mcp_tool_result_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_mcp_tool_use_block import *
            self.tools['beta_mcp_tool_use_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_mcp_tool_use_block'
        except ImportError as e:
            print(f"Could not import beta_mcp_tool_use_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_mcp_tool_use_block_param import *
            self.tools['beta_mcp_tool_use_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_mcp_tool_use_block_param'
        except ImportError as e:
            print(f"Could not import beta_mcp_tool_use_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_message import *
            self.tools['beta_message'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_message'
        except ImportError as e:
            print(f"Could not import beta_message: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_message_delta_usage import *
            self.tools['beta_message_delta_usage'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_message_delta_usage'
        except ImportError as e:
            print(f"Could not import beta_message_delta_usage: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_message_param import *
            self.tools['beta_message_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_message_param'
        except ImportError as e:
            print(f"Could not import beta_message_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_message_tokens_count import *
            self.tools['beta_message_tokens_count'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_message_tokens_count'
        except ImportError as e:
            print(f"Could not import beta_message_tokens_count: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_model_info import *
            self.tools['beta_model_info'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_model_info'
        except ImportError as e:
            print(f"Could not import beta_model_info: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_plain_text_source import *
            self.tools['beta_plain_text_source'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_plain_text_source'
        except ImportError as e:
            print(f"Could not import beta_plain_text_source: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_plain_text_source_param import *
            self.tools['beta_plain_text_source_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_plain_text_source_param'
        except ImportError as e:
            print(f"Could not import beta_plain_text_source_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_content_block_delta import *
            self.tools['beta_raw_content_block_delta'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_content_block_delta'
        except ImportError as e:
            print(f"Could not import beta_raw_content_block_delta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_content_block_delta_event import *
            self.tools['beta_raw_content_block_delta_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_content_block_delta_event'
        except ImportError as e:
            print(f"Could not import beta_raw_content_block_delta_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_content_block_stop_event import *
            self.tools['beta_raw_content_block_stop_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_content_block_stop_event'
        except ImportError as e:
            print(f"Could not import beta_raw_content_block_stop_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_message_delta_event import *
            self.tools['beta_raw_message_delta_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_message_delta_event'
        except ImportError as e:
            print(f"Could not import beta_raw_message_delta_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_message_start_event import *
            self.tools['beta_raw_message_start_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_message_start_event'
        except ImportError as e:
            print(f"Could not import beta_raw_message_start_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_message_stop_event import *
            self.tools['beta_raw_message_stop_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_message_stop_event'
        except ImportError as e:
            print(f"Could not import beta_raw_message_stop_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_message_stream_event import *
            self.tools['beta_raw_message_stream_event'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_raw_message_stream_event'
        except ImportError as e:
            print(f"Could not import beta_raw_message_stream_event: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_redacted_thinking_block import *
            self.tools['beta_redacted_thinking_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_redacted_thinking_block'
        except ImportError as e:
            print(f"Could not import beta_redacted_thinking_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_redacted_thinking_block_param import *
            self.tools['beta_redacted_thinking_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_redacted_thinking_block_param'
        except ImportError as e:
            print(f"Could not import beta_redacted_thinking_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_request_document_block_param import *
            self.tools['beta_request_document_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_request_document_block_param'
        except ImportError as e:
            print(f"Could not import beta_request_document_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_request_mcp_server_tool_configuration_param import *
            self.tools['beta_request_mcp_server_tool_configuration_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_request_mcp_server_tool_configuration_param'
        except ImportError as e:
            print(f"Could not import beta_request_mcp_server_tool_configuration_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_request_mcp_server_url_definition_param import *
            self.tools['beta_request_mcp_server_url_definition_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_request_mcp_server_url_definition_param'
        except ImportError as e:
            print(f"Could not import beta_request_mcp_server_url_definition_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_request_mcp_tool_result_block_param import *
            self.tools['beta_request_mcp_tool_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_request_mcp_tool_result_block_param'
        except ImportError as e:
            print(f"Could not import beta_request_mcp_tool_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_search_result_block_param import *
            self.tools['beta_search_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_search_result_block_param'
        except ImportError as e:
            print(f"Could not import beta_search_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_signature_delta import *
            self.tools['beta_signature_delta'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_signature_delta'
        except ImportError as e:
            print(f"Could not import beta_signature_delta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_stop_reason import *
            self.tools['beta_stop_reason'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_stop_reason'
        except ImportError as e:
            print(f"Could not import beta_stop_reason: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_block import *
            self.tools['beta_text_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_block'
        except ImportError as e:
            print(f"Could not import beta_text_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_block_param import *
            self.tools['beta_text_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_block_param'
        except ImportError as e:
            print(f"Could not import beta_text_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_delta import *
            self.tools['beta_text_delta'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_delta'
        except ImportError as e:
            print(f"Could not import beta_text_delta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_create_result_block import *
            self.tools['beta_text_editor_code_execution_create_result_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_create_result_block'
        except ImportError as e:
            print(f"Could not import beta_text_editor_code_execution_create_result_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_create_result_block_param import *
            self.tools['beta_text_editor_code_execution_create_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_create_result_block_param'
        except ImportError as e:
            print(f"Could not import beta_text_editor_code_execution_create_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_str_replace_result_block import *
            self.tools['beta_text_editor_code_execution_str_replace_result_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_str_replace_result_block'
        except ImportError as e:
            print(f"Could not import beta_text_editor_code_execution_str_replace_result_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_str_replace_result_block_param import *
            self.tools['beta_text_editor_code_execution_str_replace_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_str_replace_result_block_param'
        except ImportError as e:
            print(f"Could not import beta_text_editor_code_execution_str_replace_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_tool_result_block import *
            self.tools['beta_text_editor_code_execution_tool_result_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_tool_result_block'
        except ImportError as e:
            print(f"Could not import beta_text_editor_code_execution_tool_result_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_tool_result_block_param import *
            self.tools['beta_text_editor_code_execution_tool_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_tool_result_block_param'
        except ImportError as e:
            print(f"Could not import beta_text_editor_code_execution_tool_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_tool_result_error import *
            self.tools['beta_text_editor_code_execution_tool_result_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_tool_result_error'
        except ImportError as e:
            print(f"Could not import beta_text_editor_code_execution_tool_result_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_tool_result_error_param import *
            self.tools['beta_text_editor_code_execution_tool_result_error_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_tool_result_error_param'
        except ImportError as e:
            print(f"Could not import beta_text_editor_code_execution_tool_result_error_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_view_result_block import *
            self.tools['beta_text_editor_code_execution_view_result_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_view_result_block'
        except ImportError as e:
            print(f"Could not import beta_text_editor_code_execution_view_result_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_view_result_block_param import *
            self.tools['beta_text_editor_code_execution_view_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_text_editor_code_execution_view_result_block_param'
        except ImportError as e:
            print(f"Could not import beta_text_editor_code_execution_view_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_thinking_block import *
            self.tools['beta_thinking_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_thinking_block'
        except ImportError as e:
            print(f"Could not import beta_thinking_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_thinking_block_param import *
            self.tools['beta_thinking_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_thinking_block_param'
        except ImportError as e:
            print(f"Could not import beta_thinking_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_thinking_config_disabled_param import *
            self.tools['beta_thinking_config_disabled_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_thinking_config_disabled_param'
        except ImportError as e:
            print(f"Could not import beta_thinking_config_disabled_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_thinking_config_enabled_param import *
            self.tools['beta_thinking_config_enabled_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_thinking_config_enabled_param'
        except ImportError as e:
            print(f"Could not import beta_thinking_config_enabled_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_thinking_config_param import *
            self.tools['beta_thinking_config_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_thinking_config_param'
        except ImportError as e:
            print(f"Could not import beta_thinking_config_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_thinking_delta import *
            self.tools['beta_thinking_delta'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_thinking_delta'
        except ImportError as e:
            print(f"Could not import beta_thinking_delta: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_bash_20241022_param import *
            self.tools['beta_tool_bash_20241022_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_bash_20241022_param'
        except ImportError as e:
            print(f"Could not import beta_tool_bash_20241022_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_bash_20250124_param import *
            self.tools['beta_tool_bash_20250124_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_bash_20250124_param'
        except ImportError as e:
            print(f"Could not import beta_tool_bash_20250124_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_choice_any_param import *
            self.tools['beta_tool_choice_any_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_choice_any_param'
        except ImportError as e:
            print(f"Could not import beta_tool_choice_any_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_choice_auto_param import *
            self.tools['beta_tool_choice_auto_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_choice_auto_param'
        except ImportError as e:
            print(f"Could not import beta_tool_choice_auto_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_choice_none_param import *
            self.tools['beta_tool_choice_none_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_choice_none_param'
        except ImportError as e:
            print(f"Could not import beta_tool_choice_none_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_choice_param import *
            self.tools['beta_tool_choice_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_choice_param'
        except ImportError as e:
            print(f"Could not import beta_tool_choice_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_choice_tool_param import *
            self.tools['beta_tool_choice_tool_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_choice_tool_param'
        except ImportError as e:
            print(f"Could not import beta_tool_choice_tool_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_computer_use_20241022_param import *
            self.tools['beta_tool_computer_use_20241022_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_computer_use_20241022_param'
        except ImportError as e:
            print(f"Could not import beta_tool_computer_use_20241022_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_computer_use_20250124_param import *
            self.tools['beta_tool_computer_use_20250124_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_computer_use_20250124_param'
        except ImportError as e:
            print(f"Could not import beta_tool_computer_use_20250124_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_param import *
            self.tools['beta_tool_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_param'
        except ImportError as e:
            print(f"Could not import beta_tool_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_result_block_param import *
            self.tools['beta_tool_result_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_result_block_param'
        except ImportError as e:
            print(f"Could not import beta_tool_result_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_text_editor_20241022_param import *
            self.tools['beta_tool_text_editor_20241022_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_text_editor_20241022_param'
        except ImportError as e:
            print(f"Could not import beta_tool_text_editor_20241022_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_text_editor_20250124_param import *
            self.tools['beta_tool_text_editor_20250124_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_text_editor_20250124_param'
        except ImportError as e:
            print(f"Could not import beta_tool_text_editor_20250124_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_text_editor_20250429_param import *
            self.tools['beta_tool_text_editor_20250429_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_text_editor_20250429_param'
        except ImportError as e:
            print(f"Could not import beta_tool_text_editor_20250429_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_text_editor_20250728_param import *
            self.tools['beta_tool_text_editor_20250728_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_text_editor_20250728_param'
        except ImportError as e:
            print(f"Could not import beta_tool_text_editor_20250728_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_use_block import *
            self.tools['beta_tool_use_block'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_use_block'
        except ImportError as e:
            print(f"Could not import beta_tool_use_block: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_use_block_param import *
            self.tools['beta_tool_use_block_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_tool_use_block_param'
        except ImportError as e:
            print(f"Could not import beta_tool_use_block_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_url_image_source_param import *
            self.tools['beta_url_image_source_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_url_image_source_param'
        except ImportError as e:
            print(f"Could not import beta_url_image_source_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_url_pdf_source_param import *
            self.tools['beta_url_pdf_source_param'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_url_pdf_source_param'
        except ImportError as e:
            print(f"Could not import beta_url_pdf_source_param: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_usage import *
            self.tools['beta_usage'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.beta_usage'
        except ImportError as e:
            print(f"Could not import beta_usage: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.deleted_file import *
            self.tools['deleted_file'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.deleted_file'
        except ImportError as e:
            print(f"Could not import deleted_file: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.file_list_params import *
            self.tools['file_list_params'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.file_list_params'
        except ImportError as e:
            print(f"Could not import file_list_params: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.file_metadata import *
            self.tools['file_metadata'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.file_metadata'
        except ImportError as e:
            print(f"Could not import file_metadata: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.file_upload_params import *
            self.tools['file_upload_params'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.file_upload_params'
        except ImportError as e:
            print(f"Could not import file_upload_params: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.messages.batch_create_params import *
            self.tools['batch_create_params'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.messages.batch_create_params'
        except ImportError as e:
            print(f"Could not import batch_create_params: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.messages.batch_list_params import *
            self.tools['batch_list_params'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.messages.batch_list_params'
        except ImportError as e:
            print(f"Could not import batch_list_params: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_deleted_message_batch import *
            self.tools['beta_deleted_message_batch'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_deleted_message_batch'
        except ImportError as e:
            print(f"Could not import beta_deleted_message_batch: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch import *
            self.tools['beta_message_batch'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch'
        except ImportError as e:
            print(f"Could not import beta_message_batch: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch_canceled_result import *
            self.tools['beta_message_batch_canceled_result'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch_canceled_result'
        except ImportError as e:
            print(f"Could not import beta_message_batch_canceled_result: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch_errored_result import *
            self.tools['beta_message_batch_errored_result'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch_errored_result'
        except ImportError as e:
            print(f"Could not import beta_message_batch_errored_result: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch_expired_result import *
            self.tools['beta_message_batch_expired_result'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch_expired_result'
        except ImportError as e:
            print(f"Could not import beta_message_batch_expired_result: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch_individual_response import *
            self.tools['beta_message_batch_individual_response'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch_individual_response'
        except ImportError as e:
            print(f"Could not import beta_message_batch_individual_response: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch_request_counts import *
            self.tools['beta_message_batch_request_counts'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch_request_counts'
        except ImportError as e:
            print(f"Could not import beta_message_batch_request_counts: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch_result import *
            self.tools['beta_message_batch_result'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch_result'
        except ImportError as e:
            print(f"Could not import beta_message_batch_result: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch_succeeded_result import *
            self.tools['beta_message_batch_succeeded_result'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.beta.messages.beta_message_batch_succeeded_result'
        except ImportError as e:
            print(f"Could not import beta_message_batch_succeeded_result: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.messages.deleted_message_batch import *
            self.tools['deleted_message_batch'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.messages.deleted_message_batch'
        except ImportError as e:
            print(f"Could not import deleted_message_batch: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch import *
            self.tools['message_batch'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch'
        except ImportError as e:
            print(f"Could not import message_batch: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch_canceled_result import *
            self.tools['message_batch_canceled_result'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch_canceled_result'
        except ImportError as e:
            print(f"Could not import message_batch_canceled_result: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch_errored_result import *
            self.tools['message_batch_errored_result'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch_errored_result'
        except ImportError as e:
            print(f"Could not import message_batch_errored_result: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch_expired_result import *
            self.tools['message_batch_expired_result'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch_expired_result'
        except ImportError as e:
            print(f"Could not import message_batch_expired_result: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch_individual_response import *
            self.tools['message_batch_individual_response'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch_individual_response'
        except ImportError as e:
            print(f"Could not import message_batch_individual_response: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch_request_counts import *
            self.tools['message_batch_request_counts'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch_request_counts'
        except ImportError as e:
            print(f"Could not import message_batch_request_counts: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch_result import *
            self.tools['message_batch_result'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch_result'
        except ImportError as e:
            print(f"Could not import message_batch_result: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch_succeeded_result import *
            self.tools['message_batch_succeeded_result'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.messages.message_batch_succeeded_result'
        except ImportError as e:
            print(f"Could not import message_batch_succeeded_result: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.shared.api_error_object import *
            self.tools['api_error_object'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.shared.api_error_object'
        except ImportError as e:
            print(f"Could not import api_error_object: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.shared.authentication_error import *
            self.tools['authentication_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.shared.authentication_error'
        except ImportError as e:
            print(f"Could not import authentication_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.shared.billing_error import *
            self.tools['billing_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.shared.billing_error'
        except ImportError as e:
            print(f"Could not import billing_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.shared.error_object import *
            self.tools['error_object'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.shared.error_object'
        except ImportError as e:
            print(f"Could not import error_object: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.shared.error_response import *
            self.tools['error_response'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.shared.error_response'
        except ImportError as e:
            print(f"Could not import error_response: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.shared.gateway_timeout_error import *
            self.tools['gateway_timeout_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.shared.gateway_timeout_error'
        except ImportError as e:
            print(f"Could not import gateway_timeout_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.shared.invalid_request_error import *
            self.tools['invalid_request_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.shared.invalid_request_error'
        except ImportError as e:
            print(f"Could not import invalid_request_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.shared.not_found_error import *
            self.tools['not_found_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.shared.not_found_error'
        except ImportError as e:
            print(f"Could not import not_found_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.shared.overloaded_error import *
            self.tools['overloaded_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.shared.overloaded_error'
        except ImportError as e:
            print(f"Could not import overloaded_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.shared.permission_error import *
            self.tools['permission_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.shared.permission_error'
        except ImportError as e:
            print(f"Could not import permission_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.anthropic.types.shared.rate_limit_error import *
            self.tools['rate_limit_error'] = 'thonlibs.libthon3.11.site-packages.anthropic.types.shared.rate_limit_error'
        except ImportError as e:
            print(f"Could not import rate_limit_error: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.flask_sqlalchemy.table import *
            self.tools['table'] = 'thonlibs.libthon3.11.site-packages.flask_sqlalchemy.table'
        except ImportError as e:
            print(f"Could not import table: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.LUT import *
            self.tools['LUT'] = 'thonlibs.libthon3.11.site-packages.qrcode.LUT'
        except ImportError as e:
            print(f"Could not import LUT: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.console_scripts import *
            self.tools['console_scripts'] = 'thonlibs.libthon3.11.site-packages.qrcode.console_scripts'
        except ImportError as e:
            print(f"Could not import console_scripts: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.release import *
            self.tools['release'] = 'thonlibs.libthon3.11.site-packages.qrcode.release'
        except ImportError as e:
            print(f"Could not import release: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.compat.etree import *
            self.tools['etree'] = 'thonlibs.libthon3.11.site-packages.qrcode.compat.etree'
        except ImportError as e:
            print(f"Could not import etree: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.compat.png import *
            self.tools['png'] = 'thonlibs.libthon3.11.site-packages.qrcode.compat.png'
        except ImportError as e:
            print(f"Could not import png: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.image.styles.moduledrawers.pil import *
            self.tools['pil'] = 'thonlibs.libthon3.11.site-packages.qrcode.image.styles.moduledrawers.pil'
        except ImportError as e:
            print(f"Could not import pil: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.image.pure import *
            self.tools['pure'] = 'thonlibs.libthon3.11.site-packages.qrcode.image.pure'
        except ImportError as e:
            print(f"Could not import pure: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.image.styledpil import *
            self.tools['styledpil'] = 'thonlibs.libthon3.11.site-packages.qrcode.image.styledpil'
        except ImportError as e:
            print(f"Could not import styledpil: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.image.styles.moduledrawers.svg import *
            self.tools['svg'] = 'thonlibs.libthon3.11.site-packages.qrcode.image.styles.moduledrawers.svg'
        except ImportError as e:
            print(f"Could not import svg: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.image.styles.colormasks import *
            self.tools['colormasks'] = 'thonlibs.libthon3.11.site-packages.qrcode.image.styles.colormasks'
        except ImportError as e:
            print(f"Could not import colormasks: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.tests.consts import *
            self.tools['consts'] = 'thonlibs.libthon3.11.site-packages.qrcode.tests.consts'
        except ImportError as e:
            print(f"Could not import consts: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.tests.test_example import *
            self.tools['test_example'] = 'thonlibs.libthon3.11.site-packages.qrcode.tests.test_example'
        except ImportError as e:
            print(f"Could not import test_example: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.tests.test_qrcode import *
            self.tools['test_qrcode'] = 'thonlibs.libthon3.11.site-packages.qrcode.tests.test_qrcode'
        except ImportError as e:
            print(f"Could not import test_qrcode: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.tests.test_qrcode_pil import *
            self.tools['test_qrcode_pil'] = 'thonlibs.libthon3.11.site-packages.qrcode.tests.test_qrcode_pil'
        except ImportError as e:
            print(f"Could not import test_qrcode_pil: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.tests.test_qrcode_pypng import *
            self.tools['test_qrcode_pypng'] = 'thonlibs.libthon3.11.site-packages.qrcode.tests.test_qrcode_pypng'
        except ImportError as e:
            print(f"Could not import test_qrcode_pypng: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.tests.test_qrcode_svg import *
            self.tools['test_qrcode_svg'] = 'thonlibs.libthon3.11.site-packages.qrcode.tests.test_qrcode_svg'
        except ImportError as e:
            print(f"Could not import test_qrcode_svg: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.qrcode.tests.test_release import *
            self.tools['test_release'] = 'thonlibs.libthon3.11.site-packages.qrcode.tests.test_release'
        except ImportError as e:
            print(f"Could not import test_release: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.AvifImagePlugin import *
            self.tools['AvifImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.AvifImagePlugin'
        except ImportError as e:
            print(f"Could not import AvifImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.BdfFontFile import *
            self.tools['BdfFontFile'] = 'thonlibs.libthon3.11.site-packages.PIL.BdfFontFile'
        except ImportError as e:
            print(f"Could not import BdfFontFile: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.BufrStubImagePlugin import *
            self.tools['BufrStubImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.BufrStubImagePlugin'
        except ImportError as e:
            print(f"Could not import BufrStubImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ContainerIO import *
            self.tools['ContainerIO'] = 'thonlibs.libthon3.11.site-packages.PIL.ContainerIO'
        except ImportError as e:
            print(f"Could not import ContainerIO: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.CurImagePlugin import *
            self.tools['CurImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.CurImagePlugin'
        except ImportError as e:
            print(f"Could not import CurImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.DcxImagePlugin import *
            self.tools['DcxImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.DcxImagePlugin'
        except ImportError as e:
            print(f"Could not import DcxImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ExifTags import *
            self.tools['ExifTags'] = 'thonlibs.libthon3.11.site-packages.PIL.ExifTags'
        except ImportError as e:
            print(f"Could not import ExifTags: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.FliImagePlugin import *
            self.tools['FliImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.FliImagePlugin'
        except ImportError as e:
            print(f"Could not import FliImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.FontFile import *
            self.tools['FontFile'] = 'thonlibs.libthon3.11.site-packages.PIL.FontFile'
        except ImportError as e:
            print(f"Could not import FontFile: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.FpxImagePlugin import *
            self.tools['FpxImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.FpxImagePlugin'
        except ImportError as e:
            print(f"Could not import FpxImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.FtexImagePlugin import *
            self.tools['FtexImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.FtexImagePlugin'
        except ImportError as e:
            print(f"Could not import FtexImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.GbrImagePlugin import *
            self.tools['GbrImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.GbrImagePlugin'
        except ImportError as e:
            print(f"Could not import GbrImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.GdImageFile import *
            self.tools['GdImageFile'] = 'thonlibs.libthon3.11.site-packages.PIL.GdImageFile'
        except ImportError as e:
            print(f"Could not import GdImageFile: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.GimpGradientFile import *
            self.tools['GimpGradientFile'] = 'thonlibs.libthon3.11.site-packages.PIL.GimpGradientFile'
        except ImportError as e:
            print(f"Could not import GimpGradientFile: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.GimpPaletteFile import *
            self.tools['GimpPaletteFile'] = 'thonlibs.libthon3.11.site-packages.PIL.GimpPaletteFile'
        except ImportError as e:
            print(f"Could not import GimpPaletteFile: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.GribStubImagePlugin import *
            self.tools['GribStubImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.GribStubImagePlugin'
        except ImportError as e:
            print(f"Could not import GribStubImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.Hdf5StubImagePlugin import *
            self.tools['Hdf5StubImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.Hdf5StubImagePlugin'
        except ImportError as e:
            print(f"Could not import Hdf5StubImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.IcnsImagePlugin import *
            self.tools['IcnsImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.IcnsImagePlugin'
        except ImportError as e:
            print(f"Could not import IcnsImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.IcoImagePlugin import *
            self.tools['IcoImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.IcoImagePlugin'
        except ImportError as e:
            print(f"Could not import IcoImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImImagePlugin import *
            self.tools['ImImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.ImImagePlugin'
        except ImportError as e:
            print(f"Could not import ImImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageChops import *
            self.tools['ImageChops'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageChops'
        except ImportError as e:
            print(f"Could not import ImageChops: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageFilter import *
            self.tools['ImageFilter'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageFilter'
        except ImportError as e:
            print(f"Could not import ImageFilter: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageGrab import *
            self.tools['ImageGrab'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageGrab'
        except ImportError as e:
            print(f"Could not import ImageGrab: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageMath import *
            self.tools['ImageMath'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageMath'
        except ImportError as e:
            print(f"Could not import ImageMath: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageMode import *
            self.tools['ImageMode'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageMode'
        except ImportError as e:
            print(f"Could not import ImageMode: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageMorph import *
            self.tools['ImageMorph'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageMorph'
        except ImportError as e:
            print(f"Could not import ImageMorph: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageOps import *
            self.tools['ImageOps'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageOps'
        except ImportError as e:
            print(f"Could not import ImageOps: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImagePalette import *
            self.tools['ImagePalette'] = 'thonlibs.libthon3.11.site-packages.PIL.ImagePalette'
        except ImportError as e:
            print(f"Could not import ImagePalette: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageSequence import *
            self.tools['ImageSequence'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageSequence'
        except ImportError as e:
            print(f"Could not import ImageSequence: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageShow import *
            self.tools['ImageShow'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageShow'
        except ImportError as e:
            print(f"Could not import ImageShow: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageStat import *
            self.tools['ImageStat'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageStat'
        except ImportError as e:
            print(f"Could not import ImageStat: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImageTransform import *
            self.tools['ImageTransform'] = 'thonlibs.libthon3.11.site-packages.PIL.ImageTransform'
        except ImportError as e:
            print(f"Could not import ImageTransform: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.ImtImagePlugin import *
            self.tools['ImtImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.ImtImagePlugin'
        except ImportError as e:
            print(f"Could not import ImtImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.IptcImagePlugin import *
            self.tools['IptcImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.IptcImagePlugin'
        except ImportError as e:
            print(f"Could not import IptcImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.Jpeg2KImagePlugin import *
            self.tools['Jpeg2KImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.Jpeg2KImagePlugin'
        except ImportError as e:
            print(f"Could not import Jpeg2KImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.McIdasImagePlugin import *
            self.tools['McIdasImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.McIdasImagePlugin'
        except ImportError as e:
            print(f"Could not import McIdasImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.MicImagePlugin import *
            self.tools['MicImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.MicImagePlugin'
        except ImportError as e:
            print(f"Could not import MicImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.MpegImagePlugin import *
            self.tools['MpegImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.MpegImagePlugin'
        except ImportError as e:
            print(f"Could not import MpegImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.MpoImagePlugin import *
            self.tools['MpoImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.MpoImagePlugin'
        except ImportError as e:
            print(f"Could not import MpoImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.PaletteFile import *
            self.tools['PaletteFile'] = 'thonlibs.libthon3.11.site-packages.PIL.PaletteFile'
        except ImportError as e:
            print(f"Could not import PaletteFile: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.PalmImagePlugin import *
            self.tools['PalmImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.PalmImagePlugin'
        except ImportError as e:
            print(f"Could not import PalmImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.PcdImagePlugin import *
            self.tools['PcdImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.PcdImagePlugin'
        except ImportError as e:
            print(f"Could not import PcdImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.PcfFontFile import *
            self.tools['PcfFontFile'] = 'thonlibs.libthon3.11.site-packages.PIL.PcfFontFile'
        except ImportError as e:
            print(f"Could not import PcfFontFile: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.PcxImagePlugin import *
            self.tools['PcxImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.PcxImagePlugin'
        except ImportError as e:
            print(f"Could not import PcxImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.PdfImagePlugin import *
            self.tools['PdfImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.PdfImagePlugin'
        except ImportError as e:
            print(f"Could not import PdfImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.PdfParser import *
            self.tools['PdfParser'] = 'thonlibs.libthon3.11.site-packages.PIL.PdfParser'
        except ImportError as e:
            print(f"Could not import PdfParser: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.PixarImagePlugin import *
            self.tools['PixarImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.PixarImagePlugin'
        except ImportError as e:
            print(f"Could not import PixarImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.PngImagePlugin import *
            self.tools['PngImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.PngImagePlugin'
        except ImportError as e:
            print(f"Could not import PngImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.PsdImagePlugin import *
            self.tools['PsdImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.PsdImagePlugin'
        except ImportError as e:
            print(f"Could not import PsdImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.SunImagePlugin import *
            self.tools['SunImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.SunImagePlugin'
        except ImportError as e:
            print(f"Could not import SunImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.TarIO import *
            self.tools['TarIO'] = 'thonlibs.libthon3.11.site-packages.PIL.TarIO'
        except ImportError as e:
            print(f"Could not import TarIO: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.TgaImagePlugin import *
            self.tools['TgaImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.TgaImagePlugin'
        except ImportError as e:
            print(f"Could not import TgaImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.XVThumbImagePlugin import *
            self.tools['XVThumbImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.XVThumbImagePlugin'
        except ImportError as e:
            print(f"Could not import XVThumbImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.XbmImagePlugin import *
            self.tools['XbmImagePlugin'] = 'thonlibs.libthon3.11.site-packages.PIL.XbmImagePlugin'
        except ImportError as e:
            print(f"Could not import XbmImagePlugin: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL._binary import *
            self.tools['_binary'] = 'thonlibs.libthon3.11.site-packages.PIL._binary'
        except ImportError as e:
            print(f"Could not import _binary: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL._deprecate import *
            self.tools['_deprecate'] = 'thonlibs.libthon3.11.site-packages.PIL._deprecate'
        except ImportError as e:
            print(f"Could not import _deprecate: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL._tkinter_finder import *
            self.tools['_tkinter_finder'] = 'thonlibs.libthon3.11.site-packages.PIL._tkinter_finder'
        except ImportError as e:
            print(f"Could not import _tkinter_finder: {e}")
            
        try:
            from thonlibs.libthon3.11.site-packages.PIL.report import *
            self.tools['report'] = 'thonlibs.libthon3.11.site-packages.PIL.report'
        except ImportError as e:
            print(f"Could not import report: {e}")
            
        try:
            from .cache.uv.sdists-v6pi.socketio-client.0.7.2.xltyDdGjrKXXB9sOqai7i.src.socketIO_client.logs import *
            self.tools['logs'] = '.cache.uv.sdists-v6pi.socketio-client.0.7.2.xltyDdGjrKXXB9sOqai7i.src.socketIO_client.logs'
        except ImportError as e:
            print(f"Could not import logs: {e}")
            
        try:
            from .cache.uv.sdists-v6pi.socketio-client.0.7.2.xltyDdGjrKXXB9sOqai7i.src.socketIO_client.symmetries import *
            self.tools['symmetries'] = '.cache.uv.sdists-v6pi.socketio-client.0.7.2.xltyDdGjrKXXB9sOqai7i.src.socketIO_client.symmetries'
        except ImportError as e:
            print(f"Could not import symmetries: {e}")
            
        try:
            from .cache.uv.sdists-v6pi.socketio-client.0.7.2.xltyDdGjrKXXB9sOqai7i.src.socketIO_client.heartbeats import *
            self.tools['heartbeats'] = '.cache.uv.sdists-v6pi.socketio-client.0.7.2.xltyDdGjrKXXB9sOqai7i.src.socketIO_client.heartbeats'
        except ImportError as e:
            print(f"Could not import heartbeats: {e}")
            
        try:
            from .cache.uv.sdists-v6pi.socketio-client.0.7.2.xltyDdGjrKXXB9sOqai7i.src.socketIO_client.parsers import *
            self.tools['parsers'] = '.cache.uv.sdists-v6pi.socketio-client.0.7.2.xltyDdGjrKXXB9sOqai7i.src.socketIO_client.parsers'
        except ImportError as e:
            print(f"Could not import parsers: {e}")
            
        try:
            from .cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.tests.test_backend_finding import *
            self.tools['test_backend_finding'] = '.cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.tests.test_backend_finding'
        except ImportError as e:
            print(f"Could not import test_backend_finding: {e}")
            
        try:
            from .cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.tests.test_pool_01 import *
            self.tools['test_pool_01'] = '.cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.tests.test_pool_01'
        except ImportError as e:
            print(f"Could not import test_pool_01: {e}")
            
        try:
            from .cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.socketpool.backend_gevent import *
            self.tools['backend_gevent'] = '.cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.socketpool.backend_gevent'
        except ImportError as e:
            print(f"Could not import backend_gevent: {e}")
            
        try:
            from .cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.socketpool.backend_thread import *
            self.tools['backend_thread'] = '.cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.socketpool.backend_thread'
        except ImportError as e:
            print(f"Could not import backend_thread: {e}")
            
        try:
            from .cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.socketpool.backend_eventlet import *
            self.tools['backend_eventlet'] = '.cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.socketpool.backend_eventlet'
        except ImportError as e:
            print(f"Could not import backend_eventlet: {e}")
            
        try:
            from .cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.socketpool.conn import *
            self.tools['conn'] = '.cache.uv.sdists-v6pi.socketpool.0.5.3.pTCKzIbeA6QBsW3slXeEH.src.socketpool.conn'
        except ImportError as e:
            print(f"Could not import conn: {e}")
            
        try:
            from .cache.uv.sdists-v6pisha3.1.0.2.ntHPTr-hSogxThDVxZzCE.src.sha3 import *
            self.tools['sha3'] = '.cache.uv.sdists-v6pisha3.1.0.2.ntHPTr-hSogxThDVxZzCE.src.sha3'
        except ImportError as e:
            print(f"Could not import sha3: {e}")
            
        try:
            from .cache.uv.sdists-v6pisha3.1.0.2.ntHPTr-hSogxThDVxZzCE.src.Modules._sha3.cleanup import *
            self.tools['cleanup'] = '.cache.uv.sdists-v6pisha3.1.0.2.ntHPTr-hSogxThDVxZzCE.src.Modules._sha3.cleanup'
        except ImportError as e:
            print(f"Could not import cleanup: {e}")
            
        try:
            from thonlibs.bin.activate_this import *
            self.tools['activate_this'] = 'thonlibs.bin.activate_this'
        except ImportError as e:
            print(f"Could not import activate_this: {e}")
            
        try:
            from memo-desktop.node_modules.dmg-builder.vendor.dmgbuild.badge import *
            self.tools['badge'] = 'memo-desktop.node_modules.dmg-builder.vendor.dmgbuild.badge'
        except ImportError as e:
            print(f"Could not import badge: {e}")
            
        try:
            from memo-desktop.node_modules.dmg-builder.vendor.dmgbuild.colors import *
            self.tools['colors'] = 'memo-desktop.node_modules.dmg-builder.vendor.dmgbuild.colors'
        except ImportError as e:
            print(f"Could not import colors: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.update-gyp import *
            self.tools['update-gyp'] = 'memo-desktop.node_modules.node-gyp.update-gyp'
        except ImportError as e:
            print(f"Could not import update-gyp: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyp.gyp_main import *
            self.tools['gyp_main'] = 'memo-desktop.node_modules.node-gyp.gyp.gyp_main'
        except ImportError as e:
            print(f"Could not import gyp_main: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyp.test_gyp import *
            self.tools['test_gyp'] = 'memo-desktop.node_modules.node-gyp.gyp.test_gyp'
        except ImportError as e:
            print(f"Could not import test_gyp: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyp.tools.graphviz import *
            self.tools['graphviz'] = 'memo-desktop.node_modules.node-gyp.gyp.tools.graphviz'
        except ImportError as e:
            print(f"Could not import graphviz: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyp.tools.pretty_gyp import *
            self.tools['pretty_gyp'] = 'memo-desktop.node_modules.node-gyp.gyp.tools.pretty_gyp'
        except ImportError as e:
            print(f"Could not import pretty_gyp: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyp.tools.pretty_sln import *
            self.tools['pretty_sln'] = 'memo-desktop.node_modules.node-gyp.gyp.tools.pretty_sln'
        except ImportError as e:
            print(f"Could not import pretty_sln: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyp.tools.pretty_vcproj import *
            self.tools['pretty_vcproj'] = 'memo-desktop.node_modules.node-gyp.gyp.tools.pretty_vcproj'
        except ImportError as e:
            print(f"Could not import pretty_vcproj: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.common_test import *
            self.tools['common_test'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.common_test'
        except ImportError as e:
            print(f"Could not import common_test: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.easy_xml import *
            self.tools['easy_xml'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.easy_xml'
        except ImportError as e:
            print(f"Could not import easy_xml: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.flock_tool import *
            self.tools['flock_tool'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.flock_tool'
        except ImportError as e:
            print(f"Could not import flock_tool: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.input_test import *
            self.tools['input_test'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.input_test'
        except ImportError as e:
            print(f"Could not import input_test: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSToolFile import *
            self.tools['MSVSToolFile'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSToolFile'
        except ImportError as e:
            print(f"Could not import MSVSToolFile: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSUserFile import *
            self.tools['MSVSUserFile'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSUserFile'
        except ImportError as e:
            print(f"Could not import MSVSUserFile: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSUtil import *
            self.tools['MSVSUtil'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSUtil'
        except ImportError as e:
            print(f"Could not import MSVSUtil: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSVersion import *
            self.tools['MSVSVersion'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.MSVSVersion'
        except ImportError as e:
            print(f"Could not import MSVSVersion: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.ninja_syntax import *
            self.tools['ninja_syntax'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.ninja_syntax'
        except ImportError as e:
            print(f"Could not import ninja_syntax: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.simple_copy import *
            self.tools['simple_copy'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.simple_copy'
        except ImportError as e:
            print(f"Could not import simple_copy: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.xcode_ninja import *
            self.tools['xcode_ninja'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.xcode_ninja'
        except ImportError as e:
            print(f"Could not import xcode_ninja: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.xml_fix import *
            self.tools['xml_fix'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.xml_fix'
        except ImportError as e:
            print(f"Could not import xml_fix: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.analyzer import *
            self.tools['analyzer'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.analyzer'
        except ImportError as e:
            print(f"Could not import analyzer: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.compile_commands_json import *
            self.tools['compile_commands_json'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.compile_commands_json'
        except ImportError as e:
            print(f"Could not import compile_commands_json: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.dump_dependency_json import *
            self.tools['dump_dependency_json'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.dump_dependency_json'
        except ImportError as e:
            print(f"Could not import dump_dependency_json: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.eclipse import *
            self.tools['eclipse'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.eclipse'
        except ImportError as e:
            print(f"Could not import eclipse: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.gypd import *
            self.tools['gypd'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.gypd'
        except ImportError as e:
            print(f"Could not import gypd: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.gypsh import *
            self.tools['gypsh'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.gypsh'
        except ImportError as e:
            print(f"Could not import gypsh: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.msvs_test import *
            self.tools['msvs_test'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.msvs_test'
        except ImportError as e:
            print(f"Could not import msvs_test: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.ninja_test import *
            self.tools['ninja_test'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.ninja_test'
        except ImportError as e:
            print(f"Could not import ninja_test: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.xcode_test import *
            self.tools['xcode_test'] = 'memo-desktop.node_modules.node-gyp.gyplib.gyp.generator.xcode_test'
        except ImportError as e:
            print(f"Could not import xcode_test: {e}")
            
        try:
            from memo-desktop.node_modules.node-gyp.test.fixtures.test-charmap import *
            self.tools['test-charmap'] = 'memo-desktop.node_modules.node-gyp.test.fixtures.test-charmap'
        except ImportError as e:
            print(f"Could not import test-charmap: {e}")
            
    def get_available_tools(self):
        """Get list of available tools"""
        return list(self.tools.keys())
        
    def execute_tool_function(self, tool_name, function_name, *args, **kwargs):
        """Execute a function from a specific tool"""
        if tool_name in self.tools:
            try:
                # Dynamic function execution would go here
                pass
            except Exception as e:
                return {"error": f"Could not execute {function_name} in {tool_name}: {e}"}
        return {"error": f"Tool {tool_name} not found"}

if __name__ == "__main__":
    controller = MasterController()
    print(f"Master Controller initialized with {len(controller.get_available_tools())} tools")
