def unique_node_ids(nodes):
    """Return unique node identifiers (deterministic).

    Removes duplicates while preserving order.
    This simple implementation is sufficient for MVP
    verification and test alignment.
    """
    return list(dict.fromkeys(nodes))
  
