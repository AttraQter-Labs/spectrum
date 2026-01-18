class LatticeState:
    """Deterministic lattice state (MVP stub).

    Placeholder for future lattice modeling.  Exists only
    to satisfy public API and test imports.
    """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        return f"<LatticeState args={self.args} kwargs={self.kwargs}>"
