# coding=utf-8
from MaKaC.webinterface.pages.conferences import WPConfModifAC

from indico.core.plugins import IndicoPlugin, IndicoPluginBlueprint
from indico.core import signals
from MaKaC.services.interface.rpc.handlers import endpointMap, importModule
import indicoaffiliation.filters
import indicoaffiliation.fileimport

blueprint = IndicoPluginBlueprint('indicoaffiliation', __name__)


class IndicoAffiliatitonPlugin(IndicoPlugin):
    """Indico Affiliation Plugin

    """
    configurable = False

    def init(self):
        super(IndicoAffiliatitonPlugin, self).init()

        # Inject the JS and CSS, should be in limited pages
        pages = [WPConfModifAC]
        for page in pages:
            self.inject_js('indicoaffiliation_js', page)
            self.inject_css('indicoaffiliation_css', page)

        endpointMap["affiliation"]=importModule("indicoaffiliation.indicoaffiliation.rpc.services")

    def register_assets(self):
        self.register_js_bundle('indicoaffiliation_js', 'js/indicoaffiliation.js','js/lib/hogan-3.0.2.js')
        self.register_css_bundle('indicoaffiliation_css', 'css/indicoaffiliation.css','css/typeahead.css')
        

    def get_blueprints(self):
        return blueprint

    @signals.app_created.connect
    def _config(app, **kwargs):
        pass

