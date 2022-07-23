from parser.parsing import _organize


def test_organize():
    # test simple example
    test_buff = "func main()\n\treturn 0\nend"
    expected = "func main (  ) \n \t return 0\nend"
    assert _organize(test_buff) == expected

    # test function with multiple args
    test_buff = "func main(a u256, b u256, c u256)\n\treturn 0\nend"
    expected = "func main ( a u256 ,  b u256 ,  c u256 ) \n \t return 0\nend"
    assert _organize(test_buff) == expected

    # test function with multiple args and multiple lines
    test_buff = "func main(a u256,\n\tb u256,\n\tc u256)\n\treturn 1\nend"
    expected = "func main ( a u256 , b u256 , c u256 ) \n \t return 1\nend"
    assert _organize(test_buff) == expected
