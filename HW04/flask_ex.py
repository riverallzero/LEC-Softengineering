from flask import Flask

app = Flask(__name__)

@app.route("/gugudan/<dan>")
def gugudan(dan):
    dan = int(dan)
    color = 'blue'

    resp_text = ''

    resp_text += ('<html>\n')
    resp_text += ('<body>\n')

    for i in range(9):
        resp_text += (f'<p>{dan} * {i + 1} = <font color={color}>{dan * (i + 1)}</font></p>\n')

    resp_text += ('</html>\n')
    resp_text += ('</body>\n')

    return resp_text


@app.route('/k2c/<k>')
def k2c(k):
    k = float(k)
    c = str(k - 273.15)

    # resp_text = ''
    # resp_text += '<p><strong>절대온도에서 섭씨온도 변환</strong></p>'
    # resp_text += f'<p>{k:.1f} <font color=blue>K</font> => {c:.1f} <font color=red>℃</font></p>'

    return c

app.run(host='0.0.0.0', debug=True)

# app.run() => 코드를 고쳤을 때 코드를 재실행 해야함
# app.run(debug=True) => 코드를 고치면 F5만 하면 내용이 변경됨
# app.run(host='0.0.0.0') => 호스트 번호가 강의실 자리 순서대로 나타남(즉, 접근 가능)
# http://127.0.0.1:5000 그냥 url에서는 오류가 뜸
# http://127.0.0.1:5000/gugudan/5 하고자하는 route를 써야함