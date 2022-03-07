try:
    import os
    import sys
    import unittest

    sys.path.append(os.path.join(os.path.dirname(__file__), "../../../.."))
except ImportError as e:
    sys.exit(str(e))
else:
    from backend.janten_master.src.controller.resource_controller import (
        ResourceController,
    )
    from backend.janten_master.src.controller.pai import (
        Pai,
    )


class TestResourceController(unittest.TestCase):
    """convert_to_path()のテスト"""

    def test_convert_to_path(self):
        """convert_to_path()をテストするメソッド

        テスト項目:
            引数が正しい場合、牌IDに対応したパスが返される。

        """
        controller = self._create_resource_controller()
        result = controller.convert_to_path(Pai.MAN_01)
        self.assertEqual(result, "dummy/man1-66-90-l.png")

    def _create_resource_controller(self):
        return ResourceController("dummy")


if __name__ == "__main__":
    unittest.main()
