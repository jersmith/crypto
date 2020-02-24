#!/usr/bin/env python3

import sys
import commando

commands = commando.new('cipher (encrypt|decrypt) [key]', sys.argv)

print(commands)
