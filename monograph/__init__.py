

VERSION = '0.1.0'
CONFIG = {}
ETIQUETTE = None

try:
    import yaml
    from crossref.restful import Etiquette
    with open('config.yml', 'r') as fp:
        CONFIG = yaml.safe_load(fp)
        ETIQUETTE = Etiquette('Monograph', VERSION, CONFIG['monograph']['base_url'],
                              CONFIG['monograph']['contact_email'])
except FileNotFoundError:
    pass
except ModuleNotFoundError:
    pass
