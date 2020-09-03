import logging

from modules.admins.AdminsManager import AdminsManager

def initialize():
    logging.info("Initializing admins module...")

    AdminsManager.initialize()

def connect():
    pass

def load_manager():
    return AdminsManager.load()

def depends_on():
    return ["config"]