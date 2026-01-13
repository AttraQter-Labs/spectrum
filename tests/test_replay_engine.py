from fractions import Fraction
from spectrum.lattice.node import LatticeNode
from spectrum.serialization.canonical import serialize_nodes, hash_nodes
from spectrum.replay.replay import replay_nodes


def test_replay_identity():
    nodes = (
        LatticeNode(id=0, state_vector=(Fraction(0),), parents=set()),
        LatticeNode(id=1, state_vector=(Fraction(1),), parents={0}),
    )

    serialized = serialize_nodes(nodes)
    replayed = replay_nodes(serialized)

    assert nodes == replayed


def test_replay_hash_stability():
    nodes = (
        LatticeNode(id=2, state_vector=(Fraction(3,2),), parents={1}),
        LatticeNode(id=1, state_vector=(Fraction(1),), parents=set()),
    )

    h1 = hash_nodes(nodes)
    h2 = hash_nodes(replay_nodes(serialize_nodes(nodes)))

    assert h1 == h2
