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


def test_identify_ssh():
    from netscope.analyzer import identify_ssh

    info = identify_ssh("SSH-2.0-NetScope-Test")

    assert info is not None
    assert info.service == "SSH"
    assert info.version == "2.0"
    assert info.banner == "SSH-2.0-NetScope-Test"
