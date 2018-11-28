from vspk import v5_0 as vspk

def setup_logging():
    import logging
    from vspk.utils import set_log_level
    set_log_level(logging.DEBUG, logging.StreamHandler())

def start_csproot_session():
    session = vspk.NUVSDSession(
        username='csproot',
        password='csproot',
        enterprise='csp',
        api_url="https://portalproxy.lab.local")
    try:
        session.start()
    except:
        logging.error('Failed to start the session')
    return session.user

# we assume we have the setup_logging() and start_csproot_session() methods
# showed in the previous example

from vspk import v5_0 as vspk
setup_logging()
csproot = start_csproot_session()

# Count will make a request to the backend to retrieve the number of enterprises
(_, _, nb_enterprises) = csproot.enterprises.count()
print 'Number of enterprises to retrieve = %s' % nb_enterprises

# Fetch will get all information of each enterprise from the server
csproot.enterprises.fetch()

for enterprise in csproot.enterprises:
    print enterprise.name
