import numpy as np
import pandas as pd


def consulta_bc(codigo_bcb):
    '''
    
    Exemplos de código:
    433 - IPCA
    189 - IGPM'''
    url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(codigo_bcb)
    df = pd.read_json(url)
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df.set_index('data', inplace=True)
    return df