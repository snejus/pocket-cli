import configparser
import os


class Configs:
    _section_name = "pocket"

    def __init__(self):
        path = self._get_file_path()

        self._config_parser = configparser.ConfigParser()

        if not os.path.exists(path):
            return

        self._config_parser.readfp(open(path))

    def get(self, name):
        try:
            value = self._config_parser.get(self._section_name, name)
        except (configparser.NoSectionError, configparser.NoOptionError):
            value = None

        return value

    def set(self, name, value):
        if not self._config_parser.has_section(self._section_name):
            self._config_parser.add_section(self._section_name)
        self._config_parser.set(self._section_name, name, str(value))

    def write(self):
        self._config_parser.write(open(self._get_file_path(), "w"))

    def _get_file_path(self):
        return "{}/.pocket-config".format(os.path.expanduser("~"))
