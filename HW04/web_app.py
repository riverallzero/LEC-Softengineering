from flask import Flask
import pandas as pd
import plotly.express as px

app = Flask(__name__)


@app.route("/")
def home():
    resp_text = ""
    resp_text += ("<html>\n")
    resp_text += ("<body>\n")
    resp_text += "<br><br><br><br><br><br><br><br>"
    resp_text += "<font size=18><center><h><strong>2012~2021년도 도시별 인구 트리맵</strong></h></center></font>\n"
    resp_text += "<font size=10><center><p>( /population/year )</p></center>\n<br></font>"
    resp_text += ("</body>\n")
    resp_text += ("</html>\n")

    return resp_text


@app.route("/population/<year>")
def population(year):
    df = pd.read_csv('do_population.csv', encoding='cp949')

    year = int(year)

    year_list = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
    if year not in year_list:
        resp_text = ""
        resp_text += "<br><br><br><br><br><br>"
        resp_text += "<center><font size=10><h><strong>연도를 다시 입력하세요 (2012~2021)</strong></h></font></center>"

    else:
        sex = []
        for r in df['항목']:
            sex.append(r[:2])
        df.insert(2, 'sex', sex)

        del df['항목']

        df.rename(columns={'시점': 'year', '행정구역(시군구)별': 'location', '데이터': 'value'}, inplace=True)

        loc = []
        for l in df['location']:
            loc.append(l)

        del df['location']

        df.insert(0, 'location', loc)

        df_year = df[f'{year}']

        vals = []
        for data in df_year:
            vals.append(round(data/10000))

        locs = []
        for loc in df['location']:
            locs.append(loc)

        sexs = []
        for sex in df['sex']:
            sexs.append(sex)

        df = pd.DataFrame(
            dict(vals=vals, locs=locs, sexs=sexs)
        )

        df['인구(만)명'] = f'{year}년도 인구 [(만)명]'

        fig = px.treemap(
            df,
            path=['인구(만)명', 'locs', 'sexs', 'vals'],
            values='vals',
            color='vals'
        )

        fig.update_traces(root_color='gold')
        fig.update_layout(
            margin=dict(t=25, l=25, r=25),
            title_font=dict(family='Arial', size=35),
            font=dict(size=25, family='Verdana'),
        )

        fig_html = fig.to_html()

        resp_text = ""
        resp_text += "<html>\n"
        resp_text += "<body>\n"
        resp_text += "<br>"
        resp_text += f"<font size=8><center><h><strong>{year}년도 도시별 인구 트리맵</strong></h></center></font>\n"
        resp_text += f"{fig_html}"
        resp_text += "</body>\n"
        resp_text += "</html>\n"

    return resp_text

app.run(host='0.0.0.0', debug=True)