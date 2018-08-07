import os
from keystoneauth1 import loading
from keystoneauth1.identity import v3
from keystoneauth1 import session
# from keystoneclient.v3 import client
from novaclient import client


def nova_client_loader():
    loader = loading.get_plugin_loader('password')
    auth_url = os.environ["OPENSTACK_AUTH_URL"]
    user_domain_name = os.environ["OPENSTACK_USER_DOMAIN_NAME"]
    user_name = os.environ["OPENSTACK_USERNAME"]
    user_password = os.environ["OPENSTACK_PASSWORD"]
    project_domain_name = os.environ["OPENSTACK_PROJECT_DOMAIN_NAME"]
    project_name = os.environ["OPENSTACK_PROJECT_NAME"]
    project_id = os.environ["OPENSTACK_PROJECT_ID"]
    auth = loader.load_from_options(auth_url=auth_url,
                                    user_domain_name=user_domain_name,
                                    username=user_name,
                                    password=user_password,
                                    project_domain_name=project_domain_name,
                                    project_name=project_name,
                                    project_id=project_id)
    return auth


def create_nova_keypair(keypair_name, user_id):
    auth = nova_client_loader()
    sess = session.Session(auth=auth)
    nova = client.Client(version="2.10", session=sess)
    keypair_object = nova.keypairs.create(keypair_name, user_id=user_id)
    return keypair_object


def get_nova_server_list():
    auth = nova_client_loader()
    sess = session.Session(auth=auth)
    nova = client.Client(version="2.10", session=sess)
    server_list = nova.servers.list()
    return server_list
