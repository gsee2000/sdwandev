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

# Create a new enterprise object. The only mandatory parameter is the name,
# so we give it directly to the contructor
new_enterprise = vspk.NUEnterprise(name="new-corp8")

# Create the enterprise on VSD.
csproot.create_child(new_enterprise)

# Create a new domain object.
new_domain = vspk.NUDomain()
# The attributes can also be set on the object directly
new_domain.name = "new-dom"
#new_domain.template_id = "98088286-9bc5-4898-b5e5-ea7e8d99ff98"

# Create the domain on VSD.
new_enterprise.create_child(new_domain)

