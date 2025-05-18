import inspect
from typing import Generator

import pytest
from _pytest.fixtures import SubRequest
from click.testing import CliRunner


@pytest.fixture
def cli_runner(request: SubRequest) -> CliRunner:
    """Instance of `click.testing.CliRunner`, configurable with `@pytest.mark.click_setup`.

    @pytest.mark.click_setup(charset="cp1251")
    def test_something(cli_runner):
        ...
    """
    runner_kwargs = {}
    marker = request.node.get_closest_marker("click_setup")
    # get kwargs when invoked as: @pytest.mark.click_setup(mix_stderr=False)
    if marker:
        # pass all runtime to kwargs
        runner_kwargs = marker.kwargs
        if (
            "mix_stderr" not in inspect.signature(CliRunner).parameters
        ):  # we are on click >= 8.2
            # remove kwargs that are not in signature
            runner_kwargs.pop("mix_stderr", None)

    return CliRunner(**runner_kwargs)


@pytest.fixture
def isolated_cli_runner(cli_runner: CliRunner) -> Generator[CliRunner, None, None]:
    """Instance of `click.testing.CliRunner` with automagically `isolated_filesystem()` called."""
    with cli_runner.isolated_filesystem():
        yield cli_runner


@pytest.mark.click_setup(mix_stderr=False)  # needes click < 8.2.0
def test_cli(
    isolated_cli_runner,  # run in fresh new temp directory (useful if cwd changes)
):
    from biskotakigold.cli import main

    ARGS, KWARGS = None, dict()
    result = isolated_cli_runner.invoke(
        main,
        args=ARGS,
        input=None,
        env=None,
        catch_exceptions=False,
        **KWARGS,
    )
    assert result.exit_code == 0
    assert result.stdout == ''
