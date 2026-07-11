# TODO: Validate
"""Remove redundant Meshfilm files."""

import logging

from good_ass_pydantic_integrator.utils import remove_redundant_files

import meshfilm

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    remove_redundant_files(meshfilm)
