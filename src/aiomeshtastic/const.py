# SPDX-FileCopyrightText: 2024-2025 @broglep
#
# SPDX-License-Identifier: MIT

import logging


class Undefined:
    def __nonzero__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "..."


UNDEFINED = Undefined()
LOGGER = logging.getLogger(__package__)
