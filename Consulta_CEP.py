import urllib.request
import json
import tkinter as tk

def consulta_CEP(CEP):
    url = f"https://viacep.com.br/ws/{CEP}/json/"
    try:
        with urllib.request.urlopen(url) as buscaCEP:
            resultadoBusca = json.loads(buscaCEP.read().decode('utf-8'))
            if 'erro' in resultadoBusca and resultadoBusca['erro'] is True:
                return "\nCEP não encontrado no banco de dados\n"
            else:
                return resultadoBusca
    except urllib.error.HTTPError as codigoErro:
        if codigoErro.code == 400:
            return "\nFormato de CEP inválido\n"
        else: 
            return "\nErro de comunicação\n"

def exibe_busca(CEP, caixa_pesquisa):
    busca = consulta_CEP(CEP)
    if isinstance(busca, dict):
        resultado = f"Logradouro: {busca['logradouro']}\n" \
                    f"Complemento: {busca['complemento']}\n" \
                    f"Bairro: {busca['bairro']}\n" \
                    f"Localidade: {busca['localidade']}\n" \
                    f"UF: {busca['uf']}\n" \
                    f"IBGE: {busca['ibge']}\n" \
                    f"GIA: {busca['gia']}\n" \
                    f"DDD: {busca['ddd']}\n" \
                    f"SIAFI: {busca['siafi']}\n"
    else:
        resultado = busca

    caixa_pesquisa.insert(tk.END, resultado)
    caixa_pesquisa.see(tk.END)

def interface_usuario():
    root = tk.Tk()
    root.title("Consulte seu CEP!")

    titulo = tk.Label(root, text="Consulte seu CEP!")
    titulo.pack(pady=10)

    entrada_CEP = tk.StringVar()
    campo_entrada = tk.Entry(root, textvariable=entrada_CEP, width=50)
    campo_entrada.pack(pady=10, ipadx=20)

    caixa_pesquisa = tk.Text(root, height=10, width=50)
    caixa_pesquisa.pack(pady=10)

    botao_pesquisa = tk.Button(root, text="Pesquisar", command=lambda: exibe_busca(entrada_CEP.get(), caixa_pesquisa))
    root.bind("<Return>", lambda event: exibe_busca(entrada_CEP.get(), caixa_pesquisa))
    botao_pesquisa.pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    interface_usuario()
