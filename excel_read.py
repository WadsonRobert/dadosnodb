import pandas as pd

#A LEITURA E O TRATAMENTO DO ARQUIVO EXCEL

def read_excel(file_path):

    df = pd.read_excel(file_path)
    df.fillna('', inplace=True)
    df = df.drop(columns=['id'])
    df.replace(r'^\s*$', '', regex=True, inplace=True)
    df.to_excel('dados_tratados.xlsx', index=False)

    return df

df = read_excel('logs_com_erros.xlsx')




