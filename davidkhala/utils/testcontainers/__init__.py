import os


def persistent():
    os.environ["TESTCONTAINERS_RYUK_DISABLED"] = "true"
