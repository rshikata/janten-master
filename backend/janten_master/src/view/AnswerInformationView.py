try:
    import os
    import sys
    from rest_framework.views import APIView
    from django.http import JsonResponse
    from rest_framework.response import Response

    sys.path.append(os.path.join(os.path.dirname(__file__), "../../../.."))
except ImportError as e:
    sys.exit(str(e))
else:
    from backend.janten_master.src.controller.mahjong_information_controller import (
        MahjongInformationController,
    )


class AnswerInformationView(APIView):
    """HTTPリクエストを受け取り、回答情報登録してHTTPレスポンスとして返す。"""

    def post(self, request):
        """POST通信処理
        Args:
        request (HttpRequest): HttpRequestオブジェクト

        Returns:
        JsonResponse: Responseオブジェクト
        """

        parameters = request.data
        operator = MahjongInformationController()
        question_id = parameters.get("question_id")
        player_name = parameters.get("player_name")
        answer_id = parameters.get("answer_pai")
        response_json, status = operator.register_answer_information(
            question_id, player_name, answer_id
        )

        return JsonResponse(response_json, status=status)
