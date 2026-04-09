from src.cli.main import build_parser, main

def test_cli():
    p = build_parser()
    opts = p.parse_args(["--port", "6380", "--delimiter", "/"])
    assert opts.port == 6380
    assert opts.delimiter == "/"
    assert main(["--version"]) == 0
