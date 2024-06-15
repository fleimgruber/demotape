import pytest

from demotape import download_stream, generate_channellist, get_destpath

@pytest.fixture
def root_path():
    return "build"


@pytest.fixture
def test_channel():
    return {
        'name': 'Test Channel', 
        'url': 'https://1000338copo-app2749759488.r53.cdn.tv1.eu/1000518lf/1000338copo/live/app2749759488/w2928771075/live247.smil/playlist.m3u8'
    }


def test_download_stream(test_channel, root_path):
    dest_path = get_destpath(test_channel, root_path)
    download_stream(test_channel, dest_path)


def test_generate_channel_list():
    actual = generate_channellist()
    assert len(actual) == 23
