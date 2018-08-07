"""AUCR openstack plugin route page handler."""
# coding=utf-8
from flask import Blueprint
from flask import session, redirect, url_for, render_template, request
from flask_login import current_user, login_required
from app.plugins.openstack.client import create_nova_keypair, get_nova_server_list
openstack_page = Blueprint('openstack', __name__, template_folder='templates')


@openstack_page.route('/openstack_dashboard', methods=['GET', 'POST'])
@login_required
def openstack_dashboard():
    """Chat room. The user's name and room must be stored in the session."""
    test = get_nova_server_list()
    server_dict = {}
    current_page_menu = {}
    current_page_menu["dashboard"] = {"link": "openstack.openstack_dashboard", "name": "Dashboard"}
    current_page_menu["test"] = {"link": "openstack.openstack_dashboard", "name": "Test"}
    for items in get_nova_server_list():
        table_dict = {}
        table_dict["name"] = items.human_id
        table_dict["status"] = items.status
        table_dict["id"] = items.id
        networks_list = items.networks
        if "public" in networks_list:
            table_dict["externalip"] = items.networks["public"][1]
        else:
            table_dict["externalip"] = ""
        if "private" in items.networks:
            table_dict["externalip"] = items.networks["private"][2]
            table_dict["internalip"] = items.networks["private"][0]
        else:
            table_dict["internalip"] = ""
        server_dict[str(items.human_id)] = table_dict
    return render_template("openstack_dashboard.html", test=test, table_dict=server_dict,
                           current_page_menu=current_page_menu)
