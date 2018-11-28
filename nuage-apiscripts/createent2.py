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

setup_logging()
csproot = start_csproot_session()

# Create an enterprise asynchronously
enterprise = vspk.NUEnterprise(name="Test Enterprise")
csproot.create_child(enterprise) 
