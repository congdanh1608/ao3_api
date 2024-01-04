# from AO3 import app

# if __name__ == "__main__":
#     import unicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)



from flask import Flask, jsonify
from AO3 import Work

app = Flask(__name__)

@app.route('/works/<int:workid>', methods=['GET'])
def get_work(workid):
    try:
        # Tạo một đối tượng Work với workid
        work = Work(workid)

        # Gọi reload để tải thông tin về công việc
        work.reload()

        # Chuẩn bị dữ liệu để trả về dưới dạng JSON
        response_data = {
            'work_id': work.id,
            'title': work.title,
            'chapters': [
                {
                    'chapter_id': chapter.id,
                    'chapter_title': chapter.title,
                    # ... Các thông tin khác mà bạn muốn trả về
                }
                for chapter in work.chapters
            ]
        }

        return jsonify(response_data)

    except utils.InvalidIdError as e:
        return jsonify({'error': str(e)}), 404  # Trả về mã lỗi 404 nếu không tìm thấy công việc

if __name__ == '__main__':
    app.run(debug=True)

