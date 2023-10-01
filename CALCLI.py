#!/usr/bin/env python3
from mylib.calc import add, sub, mul, div, power
import click


@click.group()
def cli():
    """A calculator module"""


@cli.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_cmd(a, b):
    """Add two numbers"""
    # use colored output in f string
    click.echo(click.style(f"{a} + {b} = {add(a, b)}", fg="green"))


@cli.command("sub")
@click.argument("a", type=float)
@click.argument("b", type=float)
def sub_cmd(a, b):
    """Subtract two numbers"""
    click.echo(click.style(f"{a} - {b} = {sub(a, b)}", fg="red"))


@cli.command("mul")
@click.argument("a", type=float)
@click.argument("b", type=float)
def mul_cmd(a, b):
    """Multiply two numbers"""
    click.echo(click.style(f"{a} * {b} = {mul(a, b)}", fg="yellow"))


@cli.command("div")
@click.argument("a", type=float)
@click.argument("b", type=float)
def div_cmd(a, b):
    """Divide two numbers"""
    click.echo(click.style(f"{a} / {b} = {div(a, b)}", fg="blue"))


@cli.command("power")
@click.argument("a", type=float)
@click.argument("b", type=float)
def power_cmd(a, b):
    """Raise a to the power of b"""
    click.echo(click.style(f"{a} ** {b} = {power(a, b)}", fg="magenta"))


if __name__ == "__main__":
    cli()
