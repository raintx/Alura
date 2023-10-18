import time
from pywinauto import Application

# Título da janela a ser procurada
window_title = "Nolvus Dashboard"

# Aguarde alguns segundos para você ter tempo de mudar para a janela
time.sleep(10)  # Aumente o tempo conforme necessário

# Crie uma instância da aplicação com base no título da janela
app = Application(backend='uia').connect(title=window_title, timeout=10)

# Obtenha a janela
window = app.window(title=window_title)

# Certifique-se de que a janela esteja visível
window.wait('visible', timeout=10)

# Clique no botão usando seu nome ou outra identificação única
button = window.child_window(title='Slow download', control_type='Button')
button.click()
