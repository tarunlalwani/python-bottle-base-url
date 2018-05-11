import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

import bottle
from app import app
application = bottle.default_app()

mount_path = os.getenv("APP_MOUNT_PATH", "/")
application.config['APP_MOUNT_PATH'] = mount_path

application.mount(mount_path,  app)
bottle.BaseTemplate.defaults['APP_MOUNT_PATH'] = mount_path