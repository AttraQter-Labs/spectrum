from spectrum.engines.examples import add_one_engine
from spectrum.contracts import Contract
from spectrum.api.engine_execute import execute_engine


def test_registered_engine_executes():
    contract = Contract(
        name="add-one",
        input_keys=("x",),
        output_type=int,
    )

    record = execute_engine(
        engine_name="add_one",
        engine_version="1.0.0",
        engine_fn=add_one_engine,
        contract=contract,
        state={"x": 2},
    )

    assert record.output == 3


def test_engine_mutation_detected():
    def tampered(state):
        return state["x"] + 2

    contract = Contract(
        name="add-one",
        input_keys=("x",),
        output_type=int,
    )

    try:
        execute_engine(
            engine_name="add_one",
            engine_version="1.0.0",
            engine_fn=tampered,
            contract=contract,
            state={"x": 2},
        )
        assert False
    except AssertionError:
        pass
