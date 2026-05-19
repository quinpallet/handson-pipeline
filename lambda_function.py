import json
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# バージョン情報（v2.0.0 に更新）
VERSION = os.environ.get('APP_VERSION', '2.0.0')

def lambda_handler(event, context):
    """
    HTTP API レスポンス関数 v2.0.0
    レスポンスにタイムスタンプと環境情報を追加
    """
    logger.info(f"v2.0.0 - Request received: {json.dumps(event)}")
    http_method = event.get('requestContext', {}).get('http', {}).get('method', 'UNKNOWN')
    path = event.get('requestContext', {}).get('http', {}).get('path', '/')
    # v2.0.0: タイムスタンプと環境変数を追加
    response_body = {
        "message": "Hello from CodePipeline Demo! (v2.0.0)",
        "version": VERSION,
        "method": http_method,
        "path": path,
        "timestamp": datetime.now().isoformat(),
        "environment": os.environ.get('ENVIRONMENT', 'handson'),
        "status": "ok"
    }
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "X-App-Version": VERSION
        },
        "body": json.dumps(response_body, ensure_ascii=False)
    }

