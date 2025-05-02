# -*- coding: utf-8 -*-
from configs.yaml import ConfigYaml


class ConfigManager(object):
    config_yaml = ConfigYaml()

    def add_config_context(self, context, bu=None, profile=None):
        userdata = context.config.userdata
        env_tag = userdata.get('env', 'test')

        if not hasattr(context, 'test_config'):
            context.test_config = self.config_yaml(
                'config_{}.yaml'.format(
                    env_tag
                )
            )
