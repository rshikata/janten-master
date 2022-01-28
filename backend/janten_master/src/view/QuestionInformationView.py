try:
    import os
    import sys
    from rest_framework.views import APIView
    from django.http import JsonResponse

    sys.path.append(os.path.join(os.path.dirname(__file__), "../../../.."))
except ImportError as e:
    sys.exit(str(e))
else:
    from backend.janten_master.src.controller.mahjong_information_controller import (
        MahjongInformationController,
    )


class QuestionInformationView(APIView):
    """HTTPリクエストを受け取り、問題情報をHTTPレスポンスとして返す。"""

    def get(self, request):
        """GET通信処理
        Args:
        request (HttpRequest): HttpRequestオブジェクト

        Returns:
        JsonResponse: Responseオブジェクト
        """

        operator = MahjongInformationController()
        response_json, status = operator.get_qestion_information()
        return JsonResponse(response_json, status=status)
