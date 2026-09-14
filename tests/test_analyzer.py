from netscope.analyzer import identify_http


def test_identify_http():
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Server: TestServer/1.0\r\n"
        "\r\n"
    )

    result = identify_http(response)

    assert result is not None
    assert result.service == "HTTP"
    assert result.version == "TestServer/1.0"
