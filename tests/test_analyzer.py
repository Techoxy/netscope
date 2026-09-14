from netscope.analyzer import (
    identify_ftp,
    identify_http,
    identify_service,
    identify_ssh,
)


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
    response = "SSH-2.0-NetScope-Test"

    result = identify_ssh(response)

    assert result is not None
    assert result.service == "SSH"
    assert result.version == "2.0"
    assert result.banner == response


def test_identify_service_http():
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Server: TestServer/1.0\r\n"
        "\r\n"
    )

    result = identify_service(response)

    assert result is not None
    assert result.service == "HTTP"


def test_identify_service_ssh():
    result = identify_service("SSH-2.0-NetScope-Test")

    assert result is not None
    assert result.service == "SSH"


def test_identify_service_unknown():
    result = identify_service("UNKNOWN-PROTOCOL")

    assert result is None
def test_identify_ftp():
    response = "220 NetScope FTP Test Server"

    result = identify_ftp(response)

    assert result is not None
    assert result.service == "FTP"
    assert result.banner == response


def test_identify_service_ftp():
    result = identify_service("220 NetScope FTP Test Server")

    assert result is not None
    assert result.service == "FTP"
