import gradio as gr

def add(num1, num2):
    return num1 + num2

interface = gr.Interface(
    fn = add,
    inputs = ['number', 'number'],
    outputs = 'number',
    title = '계산기',
    description =  '숫자 두 개를 입력하세요',
    flagging_mode = 'never'
)

interface.launch()