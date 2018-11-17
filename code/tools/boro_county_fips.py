def boro_county_fips(boro, tract,  block):
    st = '36'
    if boro == 1:
      return st + '061' + tract + block
    elif boro == 2:
      return st + '005' + tract + block
    elif boro == 3:
      return st + '047' + tract + block
    elif boro == 4:
      return st + '081' + tract + block
    elif boro == 5:
      return st + '085' + tract + block
    else:
      return 'X' + tract + block"""
