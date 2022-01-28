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


class AggregateResultsView(APIView):
    """HTTPリクエストを受け取り、集計結果をHTTPレスポンスとして返す。"""

    def get(self, request):
        """GET通信処理
        Args:
        request (HttpRequest): HttpRequestオブジェクト

        Returns:
        JsonResponse: Responseオブジェクト
        """

        operator = MahjongInformationController()
        response_json, status = operator.get_aggregate_results(
            request.query_params.get("id")
        )

        return JsonResponse(response_json, status=status)
