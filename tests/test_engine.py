"""Comprehensive tests for the deterministic computation engine.

These tests validate:
1. Exact determinism across multiple runs
2. Replay equality
3. Safe error handling (division by zero)
4. Pure function behavior (no side effects)
"""

import pytest
from api.public import run_deterministic, replay
from engine.core import add, subtract, multiply, divide


class TestBasicOperations:
    """Test individual arithmetic operations."""
    
    def test_add_deterministic(self):
        """Test that addition is deterministic."""
        a, b = 5.0, 3.0
        result1 = add(a, b)
        result2 = add(a, b)
        result3 = add(a, b)
        
        assert result1 == result2 == result3 == 8.0
    
    def test_subtract_deterministic(self):
        """Test that subtraction is deterministic."""
        a, b = 10.0, 4.0
        result1 = subtract(a, b)
        result2 = subtract(a, b)
        result3 = subtract(a, b)
        
        assert result1 == result2 == result3 == 6.0
    
    def test_multiply_deterministic(self):
        """Test that multiplication is deterministic."""
        a, b = 3.0, 7.0
        result1 = multiply(a, b)
        result2 = multiply(a, b)
        result3 = multiply(a, b)
        
        assert result1 == result2 == result3 == 21.0
    
    def test_divide_deterministic(self):
        """Test that division is deterministic."""
        a, b = 20.0, 4.0
        result1 = divide(a, b)
        result2 = divide(a, b)
        result3 = divide(a, b)
        
        assert result1 == result2 == result3 == 5.0
    
    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError deterministically."""
        with pytest.raises(ValueError, match="Division by zero"):
            divide(10.0, 0.0)
        
        # Verify it raises the same error consistently
        with pytest.raises(ValueError, match="Division by zero"):
            divide(10.0, 0.0)
        
        with pytest.raises(ValueError, match="Division by zero"):
            divide(5.0, 0.0)


class TestInstructionExecution:
    """Test instruction execution and determinism."""
    
    def test_single_instruction_deterministic(self):
        """Test single instruction execution is deterministic."""
        instructions = [{'operation': 'add', 'a': 5, 'b': 3}]
        
        results1, log1 = run_deterministic(instructions)
        results2, log2 = run_deterministic(instructions)
        results3, log3 = run_deterministic(instructions)
        
        # All results should be identical
        assert results1 == results2 == results3
        assert log1 == log2 == log3
        
        # Check the actual values
        assert len(results1) == 1
        assert results1[0]['result'] == 8
        assert results1[0]['operation'] == 'add'
        assert results1[0]['operands'] == {'a': 5, 'b': 3}
        assert results1[0]['step'] == 0
    
    def test_multiple_instructions_deterministic(self):
        """Test multiple instruction execution is deterministic."""
        instructions = [
            {'operation': 'add', 'a': 10, 'b': 5},
            {'operation': 'subtract', 'a': 20, 'b': 7},
            {'operation': 'multiply', 'a': 3, 'b': 4},
            {'operation': 'divide', 'a': 100, 'b': 4}
        ]
        
        results1, log1 = run_deterministic(instructions)
        results2, log2 = run_deterministic(instructions)
        results3, log3 = run_deterministic(instructions)
        
        # All results should be identical
        assert results1 == results2 == results3
        assert log1 == log2 == log3
        
        # Verify step-by-step results
        assert len(results1) == 4
        assert results1[0]['result'] == 15  # 10 + 5
        assert results1[1]['result'] == 13  # 20 - 7
        assert results1[2]['result'] == 12  # 3 * 4
        assert results1[3]['result'] == 25  # 100 / 4
    
    def test_complex_sequence_deterministic(self):
        """Test complex sequence of operations maintains determinism."""
        instructions = [
            {'operation': 'multiply', 'a': 2.5, 'b': 4.0},
            {'operation': 'divide', 'a': 50.0, 'b': 2.0},
            {'operation': 'add', 'a': 100.5, 'b': 0.5},
            {'operation': 'subtract', 'a': 1000.0, 'b': 999.0}
        ]
        
        # Run 10 times to ensure consistency
        all_results = []
        all_logs = []
        
        for _ in range(10):
            results, log = run_deterministic(instructions)
            all_results.append(results)
            all_logs.append(log)
        
        # All runs should produce identical results
        first_results = all_results[0]
        for results in all_results[1:]:
            assert results == first_results
        
        # All logs should be identical
        first_log = all_logs[0]
        for log in all_logs[1:]:
            assert log == first_log


class TestReplay:
    """Test replay functionality and determinism."""
    
    def test_replay_matches_original(self):
        """Test that replay produces identical results."""
        instructions = [
            {'operation': 'add', 'a': 15, 'b': 25},
            {'operation': 'multiply', 'a': 6, 'b': 7}
        ]
        
        original_results, log = run_deterministic(instructions)
        replayed_results = replay(log)
        
        # Replayed results should match original exactly
        assert replayed_results == original_results
    
    def test_replay_consistency(self):
        """Test that replay is consistent across multiple replays."""
        instructions = [
            {'operation': 'divide', 'a': 100, 'b': 5},
            {'operation': 'subtract', 'a': 50, 'b': 10}
        ]
        
        _, log = run_deterministic(instructions)
        
        # Replay multiple times
        replay1 = replay(log)
        replay2 = replay(log)
        replay3 = replay(log)
        
        # All replays should be identical
        assert replay1 == replay2 == replay3
    
    def test_replay_complex_log(self):
        """Test replay with complex operations."""
        instructions = [
            {'operation': 'add', 'a': 1.5, 'b': 2.5},
            {'operation': 'subtract', 'a': 10.0, 'b': 3.5},
            {'operation': 'multiply', 'a': 2.5, 'b': 4.0},
            {'operation': 'divide', 'a': 100.0, 'b': 8.0}
        ]
        
        original_results, log = run_deterministic(instructions)
        
        # Replay 5 times
        for _ in range(5):
            replayed = replay(log)
            assert replayed == original_results
    
    def test_replay_with_division_by_zero(self):
        """Test that replay handles division by zero deterministically."""
        instructions = [
            {'operation': 'add', 'a': 5, 'b': 3},
            {'operation': 'divide', 'a': 10, 'b': 0}  # Will fail
        ]
        
        # Original execution should fail
        with pytest.raises(ValueError, match="Division by zero"):
            run_deterministic(instructions)
        
        # If we had a partial log (only the first instruction)
        partial_log = [{
            'step': 0,
            'operation': 'add',
            'operands': {'a': 5, 'b': 3},
            'result': 8
        }]
        
        # Replay should work for the partial log
        replayed = replay(partial_log)
        assert len(replayed) == 1
        assert replayed[0]['result'] == 8


class TestDeterminismGuarantees:
    """Test specific determinism guarantees."""
    
    def test_no_side_effects(self):
        """Test that operations have no side effects."""
        instructions = [
            {'operation': 'add', 'a': 5, 'b': 3},
            {'operation': 'multiply', 'a': 2, 'b': 4}
        ]
        
        # Run once
        results1, log1 = run_deterministic(instructions)
        
        # Modify the returned results (should not affect subsequent runs)
        results1[0]['result'] = 999
        log1[0]['result'] = 999
        
        # Run again
        results2, log2 = run_deterministic(instructions)
        
        # Second run should not be affected by modifications to first run
        assert results2[0]['result'] == 8  # Not 999
        assert log2[0]['result'] == 8  # Not 999
    
    def test_input_independence(self):
        """Test that modifying input doesn't affect stored state."""
        instructions = [{'operation': 'add', 'a': 5, 'b': 3}]
        
        results1, _ = run_deterministic(instructions)
        
        # Modify the input instructions
        instructions[0]['a'] = 100
        
        # Run with different instructions
        results2, _ = run_deterministic(instructions)
        
        # Results should reflect the actual inputs
        assert results1[0]['result'] == 8   # 5 + 3
        assert results2[0]['result'] == 103  # 100 + 3
    
    def test_bit_identical_float_operations(self):
        """Test that float operations are bit-identical across runs."""
        instructions = [
            {'operation': 'divide', 'a': 1.0, 'b': 3.0},  # Results in repeating decimal
            {'operation': 'multiply', 'a': 0.1, 'b': 0.2}  # Potential floating point issues
        ]
        
        # Run multiple times and collect results
        results_list = []
        for _ in range(20):
            results, _ = run_deterministic(instructions)
            results_list.append(results)
        
        # All results should be bit-identical
        first = results_list[0]
        for results in results_list[1:]:
            # Check that even floating point representations are identical
            assert results[0]['result'] == first[0]['result']
            assert results[1]['result'] == first[1]['result']
            # Use repr to check bit-identical representation
            assert repr(results[0]['result']) == repr(first[0]['result'])
            assert repr(results[1]['result']) == repr(first[1]['result'])


class TestErrorHandling:
    """Test error handling and edge cases."""
    
    def test_invalid_operation(self):
        """Test that invalid operations raise appropriate errors."""
        instructions = [{'operation': 'power', 'a': 2, 'b': 3}]
        
        with pytest.raises(ValueError, match="Unknown operation"):
            run_deterministic(instructions)
    
    def test_missing_operands(self):
        """Test that missing operands raise appropriate errors."""
        instructions = [{'operation': 'add', 'a': 5}]  # Missing 'b'
        
        with pytest.raises(KeyError):
            run_deterministic(instructions)
    
    def test_division_by_zero_in_sequence(self):
        """Test division by zero in a sequence of operations."""
        instructions = [
            {'operation': 'add', 'a': 5, 'b': 3},
            {'operation': 'divide', 'a': 10, 'b': 0},  # Should fail here
            {'operation': 'multiply', 'a': 2, 'b': 4}  # Should not execute
        ]
        
        with pytest.raises(ValueError, match="Division by zero"):
            run_deterministic(instructions)
    
    def test_empty_instructions(self):
        """Test that empty instruction list works correctly."""
        instructions = []
        
        results, log = run_deterministic(instructions)
        
        assert results == []
        assert log == []
