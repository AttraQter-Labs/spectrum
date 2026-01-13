"""
Example canonical engines.
"""

from spectrum.engines.registry import register_engine


def add_one_engine(state):
    return state["x"] + 1


register_engine(
    name="add_one",
    version="1.0.0",
    fn=add_one_engine,
    description="Adds one to integer x"
)
