#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# abstract_block.py
#   abstract building block
#   ブロックの抽象クラス
#

__version__ = '0.1'
__author__ = 'Mikio Nakano'
__copyright__ = 'C4A Research Institute, Inc.'

from typing import Dict, Any
from dialbb.util.logger import get_logger


class AbstractBlock:

    def __init__(self, *args):

        self.block_config, self.config, self.config_dir = args
        self.name = self.block_config.get("name", None)
        self._logger = get_logger(self.name)

    def process(self, input_data: Dict[str, Any], session_id: str) -> Dict[str, Any]:
        """
        todo
        :param input_data:
        :param session_id:
        :return:
        """

        raise NotImplementedError  # needs implementation

    # log functions  log関数
    def log_debug(self, message: str, session_id: str = "unknown") -> None:
        self._logger.debug(f"session: {session_id}, {message}")

    def log_info(self, message: str,  session_id: str = "unknown") -> None:
        self._logger.info(f"session: {session_id}, {message}")

    def log_warning(self, message: str, session_id: str = "unknown") -> None:
        self._logger.warning(f"session: {session_id}, {message}")

    def log_error(self, message: str, session_id: str = "unknown") -> None:
        self._logger.error(f"session: {session_id}, {message}")












