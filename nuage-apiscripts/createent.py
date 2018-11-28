# we assume we have the setup_logging() and start_csproot_session() methods
# showed in the previous example

from vspk import v4_0 as vspk
setup_logging()
csproot = start_csproot_session()

# Create a new enterprise object. The only mandatory parameter is the name,
# so we give it directly to the contructor
new_enterprise = vspk.NUEnterprise(name="new-corp")

# Create the enterprise on VSD.
csproot.create_child(new_enterprise)

# Create a new domain object.
new_domain = vspk.NUDomain()
# The attributes can also be set on the object directly
new_domain.name = "new-dom"

# Create the domain on VSD.
new_enterprise.create_child(new_domain)
