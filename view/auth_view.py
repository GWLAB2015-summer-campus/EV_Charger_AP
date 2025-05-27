from kivymd.uix.floatlayout import MDFloatLayout
from log_helper import log

class AuthView(MDFloatLayout):
    _auth = None
    def set_auth(self, auth):
        from models import Certificate, _Private_Key, _CertChain, _Cert
        print(auth)
        if auth is not None:
            self._auth = auth
            #private key
            # self.ids.private_key_x.text = str(auth.private_key.x)[:min(len(str(auth.private_key.x)), 28)]
            # self.ids.private_key_y.text = str(auth.private_key.y)[:min(len(str(auth.private_key.y)), 28)]
            # self.ids.private_key_curve.text = auth.private_key.curve
            # self.ids.private_value.text = str(auth.private_key.private_value)[:min(len(str(auth.private_key.private_value)), 28)]

            #contract chain
            self.ids.contract_cn.text = auth.contract_cert.leaf.cn
            self.ids.contract_o.text = auth.contract_cert.leaf.o
            self.ids.contract_ou.text = auth.contract_cert.leaf.ou

            #cps chain
            self.ids.cps_cn.text = auth.cps_cert.leaf.cn
            self.ids.cps_o.text = auth.cps_cert.leaf.o
            self.ids.cps_ou.text = auth.cps_cert.leaf.ou

            self.remove_widget(self.ids.auth_empty)