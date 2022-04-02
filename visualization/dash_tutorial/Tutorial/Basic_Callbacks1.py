from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
        # value: input태그에 기본적으로 들어갈 값, type:input태그 input의 종류를 설정할 수 있는 듯?
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


@app.callback(
    Output(component_id='my-output', component_property='children'), #내보낼 id, 어디에 내보낼지
    Input(component_id='my-input', component_property='value') # 받을 id, 받을 값.
)
def update_output_div(input_value): #함수명은 기능을 설명할 수 있도록 임의로 설정. 변수명은?
    # 변수의 인수 또한 임의로 설정가능(함수 내부에 사용하는 변수와 동일하게).
    # 인수는 Input의 입력을 받는 듯.
    # 데코레이터와 함수 사이에 빈 줄이 있으면 callback registration이 실패함.
    return f'Output: {input_value}'


if __name__ == '__main__':
    app.run_server(debug=True)