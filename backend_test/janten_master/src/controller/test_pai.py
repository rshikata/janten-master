try:
    import os
    import sys
    import unittest

    sys.path.append(os.path.join(os.path.dirname(__file__), "../../../.."))
except ImportError as e:
    sys.exit(str(e))
else:
    from backend.janten_master.src.controller.pai import (
        Pai,
    )


class TestPai(unittest.TestCase):
    def test_get_values1(self):
        """get_values()をテストするメソッド

        テスト項目:
            引数が正しい場合、value値が返される。
        """

        self.assertEqual(Pai.get_values("MAN_01"), Pai.MAN_01)

    def test_get_values2(self):
        """get_values()をテストするメソッド

        テスト項目:
            指定された引数に該当するデータが存在しない場合、例外(ValueError)が発生する。
        """
        with self.assertRaises(ValueError):
            Pai.get_values("test")


if __name__ == "__main__":
    unittest.main()
