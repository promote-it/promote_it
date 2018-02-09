#!/usr/bin/env python

import yaml
import logging

class PromoteItConfig(object):

    def __init__(self):
        self.config_file = None
        self.env_config_file = None
        self.config = {}
        self.logger = logging.getLogger("config")


    def initialize(self, config_file, env_config_file):
        self.config_file = config_file
        self.env_config_file = env_config_file
        self.load_config_files()


    def load_config_files(self):
        self.logger.info("Loading config file %s" % self.config_file)
        config = yaml.load(open(self.config_file, 'r'))
        if (config is None):
            config = {}

        self.logger.info("Loading env config file %s" % self.env_config_file)
        env_config = yaml.load(open(self.env_config_file, 'r'))
        if (env_config is None):
            env_config = {}

        self.config = {**config, **env_config}

    def get(self, source):
        source_config = self.config.get(source)
        return source_config


    def print(self):
        self.logger.info(self.config)


    def print_sections(self):
        for section in self.config:
            self.logger.info(section)

if __name__ == "__main__":
    config = PromoteItConfig()
    config.initialize("promote_it.yml", "dev_promote_it.yml")
    config.print()
    config.print_sections()