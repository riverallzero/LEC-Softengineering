from flask import Flask, request, escape
import pandas as pd
import plotly.express as px
from flask_cors import CORS, cross_origin

app = Flask(__name__)


@app.route("/population", methods=['GET', 'POST'])
@cross_origin(origin="*")
def population():
    df = pd.read_csv('do_population.csv', encoding='cp949')

    if request.method == 'GET':
        year = request.args.get('year')
    else:
        year = request.form.get('year')

    year = int(escape(year))

    year_list = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
    if year not in year_list:

        return "연도를 다시 입력하세요 (2012~2021)"

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

        df['title'] = f'{year}년도 인구 (만)명'

        fig = px.treemap(
            df,
            path=['title', 'locs', 'sexs', 'vals'],
            values='vals',
            color='vals'
        )

        fig.update_layout(
            margin=dict(t=25, l=25, r=25),
            title_font=dict(family='Arial', size=25),
            font=dict(size=25, family='Verdana'),
        )

        fig_html = fig.to_html()

    return fig_html


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()