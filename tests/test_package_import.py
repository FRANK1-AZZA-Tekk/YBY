def test_yby_package_imports():
    import yby

    assert yby is not None


def test_yby_ui_and_router_imports():
    from yby.router import HybridRouter
    from yby.ui import build_status_view

    assert HybridRouter is not None
    assert build_status_view(battery_percent=100, temperature_c=25.0)
