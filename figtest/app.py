from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(host="redis_1", port=6379)
redis.incr('started')
@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times. <p>The app started %s times.' % (redis.get('hits'), redis.get('started'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
