"""
Test deterministic replay functionality.

Execute deterministic run twice in same test and verify:
- Outputs are identical
- Trace/hash is identical
- No nondeterminism
- No execution-order dependence
"""

import hashlib
from spectrum.replay import run
from spectrum.verify import verify


def test_replay_deterministic_single_run():
    """
    Test that running the same input twice produces identical output.
    """
    input_data = b"test input"
    
    # Run twice
    output1 = run(input_data)
    output2 = run(input_data)
    
    # Must be bit-identical
    assert output1 == output2
    assert len(output1) == len(output2)
    assert type(output1) == type(output2)


def test_replay_deterministic_multiple_inputs():
    """
    Test determinism across multiple different inputs.
    """
    inputs = [
        b"",
        b"a",
        b"test",
        b"longer test input with more data",
        b"\x00\x01\x02\x03",
        b"unicode: \xc3\xa9\xc3\xa0\xc3\xb4",
    ]
    
    for input_data in inputs:
        output1 = run(input_data)
        output2 = run(input_data)
        
        # Each input produces deterministic output
        assert output1 == output2


def test_replay_trace_hash_identical():
    """
    Test that trace/hash is identical across runs.
    
    The output itself is a cryptographic hash, so we verify
    that the same input always produces the same hash.
    """
    input_data = b"deterministic test"
    
    # Run multiple times
    outputs = [run(input_data) for _ in range(10)]
    
    # All outputs must be identical
    first_output = outputs[0]
    for output in outputs[1:]:
        assert output == first_output
    
    # Verify the hash itself is deterministic
    expected_hash = hashlib.sha256(input_data).digest()
    assert first_output == expected_hash


def test_replay_no_execution_order_dependence():
    """
    Test that execution order does not affect results.
    
    Run operations in different orders and verify results remain identical.
    """
    input_a = b"input_a"
    input_b = b"input_b"
    input_c = b"input_c"
    
    # Order 1: A, B, C
    output_a1 = run(input_a)
    output_b1 = run(input_b)
    output_c1 = run(input_c)
    
    # Order 2: C, B, A
    output_c2 = run(input_c)
    output_b2 = run(input_b)
    output_a2 = run(input_a)
    
    # Order 3: B, A, C
    output_b3 = run(input_b)
    output_a3 = run(input_a)
    output_c3 = run(input_c)
    
    # All corresponding outputs must be identical
    assert output_a1 == output_a2 == output_a3
    assert output_b1 == output_b2 == output_b3
    assert output_c1 == output_c2 == output_c3


def test_verify_correct_output():
    """
    Test verification of correct output.
    """
    input_data = b"verify test"
    output = run(input_data)
    
    # Verification should succeed
    assert verify(input_data, output) is True


def test_verify_incorrect_output():
    """
    Test verification rejects incorrect output.
    """
    input_data = b"verify test"
    wrong_output = b"wrong output"
    
    # Verification should fail
    assert verify(input_data, wrong_output) is False


def test_verify_deterministic():
    """
    Test that verification is itself deterministic.
    """
    input_data = b"deterministic verify"
    output = run(input_data)
    
    # Verify multiple times
    results = [verify(input_data, output) for _ in range(10)]
    
    # All results must be identical
    assert all(results)
    assert len(set(results)) == 1  # All same value


def test_replay_no_side_effects():
    """
    Test that run() has no side effects.
    
    Running the function should not modify any external state.
    """
    input_data = b"side effect test"
    
    # Get initial output
    output1 = run(input_data)
    
    # Run many more times
    for _ in range(100):
        output = run(input_data)
        assert output == output1
    
    # First output should still be valid
    assert verify(input_data, output1)


def test_replay_byte_level_determinism():
    """
    Test determinism at the byte level.
    
    Every single byte of the output must be identical.
    """
    input_data = b"byte level test"
    
    output1 = run(input_data)
    output2 = run(input_data)
    
    # Check length
    assert len(output1) == len(output2)
    
    # Check every byte
    for i in range(len(output1)):
        assert output1[i] == output2[i]
    
    # Check as bytes
    assert output1 == output2


def test_replay_empty_input():
    """
    Test determinism with empty input.
    """
    input_data = b""
    
    output1 = run(input_data)
    output2 = run(input_data)
    
    assert output1 == output2
    assert verify(input_data, output1)


def test_replay_large_input():
    """
    Test determinism with large input.
    """
    # Large input: 1MB
    input_data = b"x" * (1024 * 1024)
    
    output1 = run(input_data)
    output2 = run(input_data)
    
    assert output1 == output2
    assert verify(input_data, output1)
