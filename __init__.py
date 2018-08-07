"""AUCR openstack plugin."""
# coding=utf-8
from app.plugins.openstack.routes import openstack_page
from app.plugins.openstack import routes


def load(app):
    """AUCR chat plugin flask app blueprint registration."""
    app.register_blueprint(openstack_page, url_prefix='/openstack')
