class Errors:
    def ok(body):
        return { "statusCode": 200, "body": body }
    def badRequest(msg):
        return { "statusCode": 400, "body": { "msg": msg } }