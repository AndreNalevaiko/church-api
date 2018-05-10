import logging

from church_api.model import Budget
from church_api.config import API_VERSION

# actions = create_actions_blueprint(BankReceive, api_version=API_VERSION)

logger = logging.getLogger(__name__)


def create_api(api):
    api.create_api(Budget,
                   methods=['GET', 'POST'],
                   url_prefix='/%s' % API_VERSION,
                   results_per_page=10,
                   primary_key='id',
                   preprocessors={
                   },
                   postprocessors={
                   })