import yaml

from modules.pytg.Manager import Manager
from modules.pytg.utils import manager

class AdminsManager(Manager):
    @staticmethod
    def initialize():
        AdminsManager.__instance = AdminsManager()

        return

    @staticmethod
    def load():
        return AdminsManager.__instance

    def is_user_admin(self, user_pointer):
        return user_pointer in manager("config").load_settings_file("admins")["admins"]
