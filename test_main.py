import pytest
from main import hello, main


def test_hello():
    """Test the hello function with a name."""
    result = hello("World")
    assert result == "Hello World"


def test_hello_with_different_name():
    """Test the hello function with a different name."""
    result = hello("Alice")
    assert result == "Hello Alice"


def test_hello_with_empty_string():
    """Test the hello function with an empty string."""
    result = hello("")
    assert result == "Hello "


def test_main(capsys):
    """Test the main function prints the correct output."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"