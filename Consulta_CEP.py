import urllib.request
import json

def consulta_CEP(CEP):
    url = f"https://viacep.com.br/ws/{CEP}/json/"
    try:
        with urllib.request.urlopen(url) as buscaCEP:
            resultadoBusca = json.loads(buscaCEP.read().decode('utf-8'))
            if 'erro' in resultadoBusca and resultadoBusca['erro'] is True:
                print("CEP não encontrado no banco de dados\n")
            else:
                return resultadoBusca
    except urllib.error.HTTPError as codigoErro:
        if codigoErro.code == 400:
            print("Formato de CEP inválido\n")
        else: 
            print("Erro de comunicação\n")


CEP = input("\nCEP: ")
busca = consulta_CEP(CEP)
if busca:
    print("Logradouro:", busca["logradouro"])
    print("Complemento:", busca["complemento"])
    print("Bairro:", busca["bairro"])
    print("Localidade:", busca["localidade"])
    print("UF:", busca["uf"])
    print("IBGE:", busca["ibge"])
    print("GIA:", busca["gia"])
    print("DDD:", busca["ddd"])
    print("SIAFI:", busca["siafi"],"\n")

# Aprendizados:
# Usar with ao operar a url e para sair após erro
# Usar decodificador
# Usar urllib.error.HTTPError no except para códigos de erro
# Usar is True para verificar se existe no BD