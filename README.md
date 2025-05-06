# 🏧 Simulador de Caixa Eletrônico em Python

Este é um projeto simples em Python que simula o funcionamento de um **caixa eletrônico**.  
O usuário informa o valor desejado para saque e o programa retorna a quantidade de cédulas de cada valor necessária para compor esse saque.

---

## ❓ Como funciona

- O usuário digita o valor do saque.
- O programa calcula a menor quantidade possível de cédulas (R$100, R$50, R$20, R$10, R$5, R$2 e R$1).
- O resultado mostra quantas cédulas de cada valor serão entregues.

---

## 🔁 Funcionalidades

- Saques múltiplos no mesmo programa.
- Validação de entradas (sem valores negativos ou não numéricos).
- Código modular com função separada para o cálculo.
- Mensagens claras para o usuário.

---

## ▶️ Como executar

1. Certifique-se de ter o **Python instalado** (versão 3.x).
2. Clone este repositório ou copie o código para um arquivo `.py`.
3. Execute no terminal ou em uma IDE como VSCode, PyCharm ou Thonny:

```bash
python caixa_eletronico.py
Digite o valor para saque (0 para sair): R$ 276

💸 Cédulas entregues:
➡️ 2 cédula(s) de R$ 100
➡️ 1 cédula(s) de R$ 50
➡️ 1 cédula(s) de R$ 20
➡️ 1 cédula(s) de R$ 5
➡️ 1 cédula(s) de R$ 1

