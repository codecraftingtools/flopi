#!/usr/bin/env python3

import flopi

flopi.set_logging_level_for("a", flopi.WARNING)
#flopi.set_logging_level(flopi.WARNING)

log = flopi.get_logger()
log2 = flopi.get_logger("a")
log.info("info1", end="")
log.info("info2")
log2.info("infoa")
log.error("webb")
