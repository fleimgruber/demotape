import re

import httpx


def test_bv1020():
    r = httpx.get("https://pidbv.justlive.tv/player.php?stream=bv1020")
    assert r


def test_bv1020_m3u8_parsing():
    r = httpx.get("https://pidbv.justlive.tv/player.php?stream=bv1020")
    pattern = re.compile(r"(https:\/\/[a-z0-9]*\.rtccdn\.com\/PIDBV\/smil:pidbv_1020\.smil\/playlist\.m3u8)")
    m = re.findall(pattern, r.text)
    assert m[0] == "https://z4defra12swse101.rtccdn.com/PIDBV/smil:pidbv_1020.smil/playlist.m3u8"
