#!/usr/bin/env python

import os
import subprocess

PKG_NAME = "foo"
TARGET = "thumbv7em-none-eabi"
THRESHOLD = 1000


def build():
    cmd = f"cargo build --release --target {TARGET}"
    print(subprocess.check_output("echo $RUSTUP_TOOLCHAIN", shell=True))
    subprocess.check_output(cmd, shell=True)


def check():
    toolchain = os.getenv("RUSTUP_TOOLCHAIN")
    filepath = f"./target-{toolchain}/{TARGET}/release/{PKG_NAME}"
    filesize = os.path.getsize(filepath)
    return filesize > THRESHOLD


if __name__ == "__main__":
    build()
    exit(check())
