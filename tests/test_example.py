from example import main


def test_main(capsys):
    main()
    assert capsys.readouterr().out == "Hello, world!\n"
