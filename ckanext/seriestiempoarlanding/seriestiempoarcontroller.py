import ckan
import ckan.lib.base as base
from base import BaseController
import logging
logger = logging.getLogger(__name__)


class SeriesTiempoArController(BaseController):

    def test(self):
        return base.render('config/config_01_title.html')
