#!/usr/bin/env python
# coding: utf8

import json
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

Options = namedtuple('Options',['connection','module_path','forks','become','become_method','become_user','check','diff'])
options = Options(connection='local',module_path=[''],forks=10,become=None,become_method=None,become_user=None,check=False,diff=False)
loader = DataLoader()
passwords = dict(vault_pass='secret')
inventory = InventoryManager(loader=loader,sources='localhost,')
variable_manager = VariableManager(loader=loader,inventory=inventory)



































