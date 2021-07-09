import functools
from io import open

from yaml import safe_load


class ConfigManager(object):
    @staticmethod
    def get_configs():
        """
        Returns a dict based on the contents of the conf.yaml file
        :return: dictionary with the config values
        """
        with open("./conf/conf.yaml", "r", encoding="utf-8") as config_file:
            config_values = safe_load(config_file)
            config_file.close()
        return config_values

    @staticmethod
    def get_db_connection_string():
        """
        Builds a basic connection string with the db parameters found in the config file
        :return: Connection String
        """
        config_values = ConfigManager.get_configs()
        get = functools.partial(config_values.get("db").get)
        user = get("user", None)
        password = get("password", "")
        host = get("host", "")
        port = get("port", "")
        db_name = get("db_name", None)

        assert user, "Invalid db user found in config"
        assert db_name, "Invalid db_name found in config"

        return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
