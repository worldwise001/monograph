import yaml
from crossref.restful import Etiquette

VERSION = '0.1.0'

with open('config.yml', 'r') as fp:
    CONFIG = yaml.safe_load(fp)

ETIQUETTE = Etiquette('Monograph', VERSION, CONFIG['monograph']['base_url'], CONFIG['monograph']['contact_email'])
