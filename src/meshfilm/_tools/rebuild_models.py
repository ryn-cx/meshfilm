"""Rebuild Pydantic models for the Meshfilm package."""

import logging

from good_ass_pydantic_integrator.utils import rebuild_models

import meshfilm

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    rebuild_models(meshfilm)
