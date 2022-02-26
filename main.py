from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()

dicionario_termos = {
    # '- desastre:':'http://www.planalto.gov.br/ccivil_03/_ato2007-2010/2010/lei/l12334.htm',
    'Evento perigoso:': 'https://www.in.gov.br/en/web/dou/-/portaria-n-6.730-de-9-de-marco-de-2020-247538988',
    'gestão de desastres:': 'https://www.in.gov.br/en/web/dou/-/instrucao-normativa-n-36-de-4-de-dezembro-de-2020-292423788',
    'gestão de risco de desastres:': 'https://www.in.gov.br/en/web/dou/-/instrucao-normativa-n-36-de-4-de-dezembro-de-2020-292423788',
    'ameaça:': 'https://www.in.gov.br/en/web/dou/-/instrucao-normativa-n-36-de-4-de-dezembro-de-2020-292423788',
    'plano de contingência -': 'https://www.in.gov.br/en/web/dou/-/decreto-n-10.593-de-24-de-dezembro-de-2020-296427343',
    # 'risco': 'https://www.in.gov.br/en/web/dou/-/decreto-n-10.593-de-24-de-dezembro-de-2020-296427343'
    '- risco de desastre:': 'https://www.in.gov.br/en/web/dou/-/instrucao-normativa-n-36-de-4-de-dezembro-de-2020-292423788',
    '- vulnerabilidade:': 'https://www.in.gov.br/en/web/dou/-/instrucao-normativa-n-36-de-4-de-dezembro-de-2020-292423788'
}

def check_norma(dicionario_termos):
    result = []
    for termo,link in dicionario_termos.items():
        try:
            obj = {}
            r = session.get(link)
            artigos = r.html.find('.dou-paragraph')
            identifica = r.html.find('.identifica')
            ementa = r.html.find('.ementa')

            for i in range(len(artigos)):

                if termo in artigos[i].text:
                    norma = identifica[0].text
                    texto_ementa = ementa[0].text
                    trecho_termo = artigos[i].text

            obj['norma'] = norma
            obj['texto_ementa'] = texto_ementa
            obj['trecho_termo'] = trecho_termo

            result.append(obj)

        except:
            print(f'erro: {termo}')
            pass
    
    return result


result = check_norma(dicionario_termos)
print(result)

# df = pd.DataFrame()

# for item in result:
#     df['norma'] = item['norma']
#     df['texto_ementa'] = item['texto_ementa']
#     df['trecho_termo'] = item['trecho_termo']

# df.to_csv('terminology_table.csv')
# print(df.head())