#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from cli import PowerCLI

def main():
    with PowerCLI() as app:
        app.run()

if __name__ == "__main__":
    main()