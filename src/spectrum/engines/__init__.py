"""
Canonical engine registry.

This module defines which engines exist and enforces version sealing.
"""
from spectrum.engines.registry import (
    EngineSpec,
    ENGINE_REGISTRY,
    get_engine_spec,
)

__all__ = [
    "EngineSpec",
    "ENGINE_REGISTRY",
    "get_engine_spec",
]
