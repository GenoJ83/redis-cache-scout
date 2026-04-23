from src.hotkey.tracker import HotKeyTracker

def test_hotkey_tracking():
    t = HotKeyTracker()
    t.record_access("user:1")
    t.record_access("user:1")
    t.record_access("user:2")
    top = t.top_hot_keys(1)
    assert top[0] == ("user:1", 2)
