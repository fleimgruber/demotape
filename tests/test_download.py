import pytest

from demotape import download_stream, generate_channellist, get_destpath

@pytest.fixture
def root_path():
    return "build"


@pytest.fixture
def test_channel_legacy():
    return {
        'name': 'Test Channel', 
        'url': 'https://1000338copo-app2749759488.r53.cdn.tv1.eu/1000518lf/1000338copo/live/app2749759488/w2928771075/live247.smil/playlist.m3u8'
    }


@pytest.fixture
def test_channel():
    return {
        'name': 'Test Channel', 
        'url': 'https://z4atvie10swse101.rtccdn.com/pidbv/smil:pidbv_1060.smil/playlist.m3u8'
    }


@pytest.fixture
def test_channel_justlive():
    return {
        'name': 'justlive', 
        'url': 'https://pidbv.justlive.tv/player.php?stream=bv1060'
    }


def test_download_stream_legacy(test_channel_legacy, root_path):
    dest_path = get_destpath(test_channel_legacy, root_path)
    download_stream(test_channel_legacy, dest_path)


def test_download_stream(test_channel, root_path):
    dest_path = get_destpath(test_channel, root_path)
    download_stream(test_channel, dest_path)


def test_download_stream_justlive(test_channel_justlive, root_path):
    dest_path = get_destpath(test_channel_justlive, root_path)
    download_stream(test_channel_justlive, dest_path)


def test_generate_channel_list():
    actual = generate_channellist()
    assert len(actual) == 23
