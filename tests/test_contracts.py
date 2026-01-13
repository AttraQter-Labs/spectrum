from spectrum.contracts import Contract
from spectrum.api.contracted_execute import execute_with_contract


def add_one(state):
    return state["x"] + 1


def test_contract_accepts_valid_input():
    contract = Contract(
        name="add-one",
        input_keys=("x",),
        output_type=int,
    )

    record = execute_with_contract(
        engine="contract-test",
        state={"x": 1},
        contract=contract,
        fn=add_one,
    )

    assert record.output == 2


def test_contract_rejects_missing_key():
    contract = Contract(
        name="add-one",
        input_keys=("x",),
        output_type=int,
    )

    try:
        execute_with_contract(
            engine="contract-test",
            state={},
            contract=contract,
            fn=add_one,
        )
        assert False
    except KeyError:
        pass


def test_contract_rejects_wrong_output_type():
    contract = Contract(
        name="bad-output",
        input_keys=("x",),
        output_type=str,
    )

    try:
        execute_with_contract(
            engine="contract-test",
            state={"x": 1},
            contract=contract,
            fn=add_one,
        )
        assert False
    except TypeError:
        pass
