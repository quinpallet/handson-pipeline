import json
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# バージョン情報（デプロイ確認用）
VERSION = os.environ.get('APP_VERSION', '1.0.0')

def lambda_handler(event, context):
    """
    シンプルな HTTP API レスポンス関数
    CodePipeline による自動デプロイのデモ用
    """
    logger.info(f"Request received: {json.dumps(event)}")
    # HTTPメソッドの取得（API Gateway v2 の形式）
    http_method = event.get('requestContext', {}).get('http', {}).get('method', 'UNKNOWN')
    path = event.get('requestContext', {}).get('http', {}).get('path', '/')
    response_body = {
        "message": "Hello from CodePipeline Demo!",
        "version": VERSION,
        "method": http_method,
        "path": path,
        "status": "ok"
    }
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response_body, ensure_ascii=False)
    }
