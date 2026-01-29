from itsdangerous import URLSafeTimedSerializer
secret_key="code9"
salt='Otpverify'
# serialization
def endata(data):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.dumps(data,salt=salt)
#deserialization
def dndata(data):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.loads(data,salt=salt)