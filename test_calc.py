from mylib.calc import add, sub, mul, div, power
from CALCLI import cli

# import the click runner for testing
from click.testing import CliRunner
import pytest


@pytest.fixture
# test add
def test_add_cmd():
    runner = CliRunner()
    result = runner.invoke(cli, ["add", "2", "3"])
    assert result.exit_code == 0
    assert result.output == "2.0 + 3.0 = 5.0\n"


# test sub
def test_sub_cmd():
    runner = CliRunner()
    result = runner.invoke(cli, ["sub", "2", "3"])
    assert result.exit_code == 0
    assert result.output == "2.0 - 3.0 = -1.0\n"


# test mul
def test_mul_cmd():
    runner = CliRunner()
    result = runner.invoke(cli, ["mul", "2", "3"])
    assert result.exit_code == 0
    assert result.output == "2.0 * 3.0 = 6.0\n"


# test div
def test_div_cmd():
    runner = CliRunner()
    result = runner.invoke(cli, ["div", "2", "3"])
    assert result.exit_code == 0
    assert result.output == "2.0 / 3.0 = 0.6666666666666666\n"


# test power
def test_power_cmd():
    runner = CliRunner()
    result = runner.invoke(cli, ["power", "2", "3"])
    assert result.exit_code == 0
    assert result.output == "2.0 ** 3.0 = 8.0\n"


# tes


def test_add():
    assert add(2, 3) == 5

    # write a test for each function in calc.py


def test_sub():
    assert sub(2, 3) == -1


def test_mul():
    assert mul(2, 3) == 6


def test_div():
    assert div(2, 3) == 0.6666666666666666


def test_power():
    assert power(2, 3) == 8


# write a test for the help command
def test_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "A calculator module" in result.output
    assert "Add two numbers" in result.output
    assert "Subtract two numbers" in result.output
    assert "Multiply two numbers" in result.output
    assert "Divide two numbers" in result.output
    assert "Raise a to the power of b" in result.output
