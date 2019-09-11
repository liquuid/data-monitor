import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("db2.csv", sep="|")

is_escritorio = df.Nome == 'escritorio'
is_sala = df.Nome == 'sala'
is_banheiro = df.Nome == 'banheiro'
is_gu = df.Nome == 'gu'
import pdb; pdb.set_trace()

fig = go.Figure()
fig.add_trace(go.Scatter(
                x=df[is_escritorio].Date,
                y=df[is_escritorio]['Temp'],
                name="escritorio - Temp",
                line_color='deepskyblue',
                opacity=0.8))

fig.add_trace(go.Scatter(
                x=df[is_escritorio].Date,
                y=df[is_escritorio]['Humi'],
                name="escritorio - Humidade",
                line_color='dimgray',
                opacity=0.8))


fig.add_trace(go.Scatter(
                x=df[is_sala].Date,
                y=df[is_sala]['Temp'],
                name="sala - Temp",
                line_color='#ff0000',
                opacity=0.8))

fig.add_trace(go.Scatter(
                x=df[is_sala].Date,
                y=df[is_sala]['Humi'],
                name="sala - Humidade",
                line_color='#990000',
                opacity=0.8))

fig.add_trace(go.Scatter(
                x=df[is_banheiro].Date,
                y=df[is_banheiro]['Temp'],
                name="banheiro - Temp",
                line_color='#00ff00',
                opacity=0.8))

fig.add_trace(go.Scatter(
                x=df[is_banheiro].Date,
                y=df[is_banheiro]['Humi'],
                name="banheiro - Humidade",
                line_color='#009900',
                opacity=0.8))

fig.add_trace(go.Scatter(
                x=df[is_gu].Date,
                y=df[is_gu]['Temp'],
                name="gu - Temp",
                line_color='#0000FF',
                opacity=0.8))

fig.add_trace(go.Scatter(
                x=df[is_gu].Date,
                y=df[is_gu]['Humi'],
                name="gu - Humidade",
                line_color='#000099',
                opacity=0.8))        


# Use date string to set xaxis range
#fig.update_layout(xaxis_range=['2019-09-11','2019-09-11'],
#                  title_text="Manually Set Date Range")
fig.show()
