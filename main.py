# from AO3 import app

# if __name__ == "__main__":
#     import unicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)



from flask import Flask, jsonify
from works import Work  

app = Flask(__name__)

@app.route('/works/<int:work_id>', methods=['GET'])
def get_work(work_id):
    try:
        work = Work(work_id)
        return jsonify(work.metadata)
    except Exception as e:
        return jsonify({'error': str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)

