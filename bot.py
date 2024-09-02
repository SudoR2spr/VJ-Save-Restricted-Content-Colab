# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from main import Bot
from flask import Flask, jsonify

# Home
@app.route('/')
def index():
    return 'Bot Is Alive'

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status='OK'), 200

if __name__ == "__main__":
    # Start Flask app in a separate thread
    def run_flask():
        app.run(host='0.0.0.0', port=8000)

    flask_thread = Thread(target=run_flask)
    flask_thread.start()

Bot().run()

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
