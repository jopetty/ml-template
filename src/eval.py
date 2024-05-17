"""Evaluate models."""

import logging

import fire
import pyrootutils
from dotenv import load_dotenv

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%d-%m %H:%M:%S",
    level=logging.INFO,
)

PROJECT_ROOT = path = pyrootutils.find_root(
    search_from=__file__, indicator=".project-root"
)

load_dotenv()


def main():
    raise NotImplementedError


if __name__ == "__main__":
    fire.Fire(main)
