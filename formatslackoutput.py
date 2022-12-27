'''
Created on Dec 26, 2022
@author: bilal.peerzade
'''

import pandas as pd
from collections import OrderedDict

class FormatSlackOutput:
  def formatSlackMessage(self,df):
    df = df.applymap(str)
    max_lengths = df.apply(lambda x: (x.str.len().max() if x.str.len().max() > len(x.name) else len(x.name)) if x.dtype == 'object' else len(x.name))
    separator = '+'
    for m in max_lengths:
      separator = separator+ (m+2) *'-' +'+'
    separator = separator +'\n'
    i=0
    header='|'
    for col in df.columns:
      header = header +col+ (max_lengths[i]+2-len(col)) *' '+'|'
      i+=1
    header = header +'\n'
    rows=''
    for element in df.values:
      i=0
      rows=rows+'|'
      for row in element:
        rows = rows+str(row)+(max_lengths[i]+2-len(str(row))) *' '+'|'
        i+=1
      rows=rows+'\n'
    output = separator+header+separator+rows+separator
    print(output)
    return output
    
def main():
    frmt = FormatSlackOutput()
    
    data = [{'PubId': '158554', 'Publisher': 'Playbuzz - oRTB', 'Todays spend': 1025, 'Yesterday spend': 1515, '% Diff': -32.35, 'Comparison': 'Today vs Yesterday', 'Region': 'EMEA', 'Pod': 'EMEA UK'}, {'PubId': '157333', 'Publisher': 'CafeMedia (via EB)', 'Todays spend': 3653, 'Yesterday spend': 5398, '% Diff': -32.33, 'Comparison': 'Today vs Yesterday', 'Region': 'NTAM', 'Pod': 'US East'},{'PubId': '158554', 'Publisher': 'Playbuzz - oRTB', 'Todays spend': 1025, 'Yesterday spend': 1515, '% Diff': -32.35, 'Comparison': 'Today vs Yesterday', 'Region': 'EMEA', 'Pod': 'EMEA UK'}, {'PubId': '157333', 'Publisher': 'CafeMedia (via EB)', 'Todays spend': 3653, 'Yesterday spend': 5398, '% Diff': -32.33, 'Comparison': 'Today vs Yesterday', 'Region': 'NTAM', 'Pod': 'US East'}]
    #data=[{"ID":1,"Name":"Alice","Age":25,"Address":{"Street":"123MainStreet","City":"NewYork","State":"NY"}},{"ID":2,"Name":"Bob","Age":30,"Address":{"Street":"456SecondStreet","City":"Chicago","State":"IL"}}]
    #data = {"cid":597,"pred":2,"tl":[1,1,1]}
    #data = ([OrderedDict([('advertiserId', 307), ('Type', 'bids'), ('CountINGX', 684554), ('CountGCP', 684682), ('CountDiff%', '-0.02')]), OrderedDict([('advertiserId', 307), ('Type', 'video'), ('CountINGX', 330727), ('CountGCP', 318334), ('CountDiff%', '3.89')]), OrderedDict([('advertiserId', 307), ('Type', 'burl'), ('CountINGX', 69695), ('CountGCP', 66627), ('CountDiff%', '4.60')])])
    #data = (((2021, 10, 20, 13, 0), 3623.19, '13/30/2010/raw/api/verifiedapi?&op=GETCONTENTSUMMARY', 'raw/api/verifiedapi', 'ETL'), ((2021, 10, 20, 14, 0), 3398.79, '14/30/2010/raw/api/verifiedapi?&op=GETCONTENTSUMMARY', 'raw/api/verifiedapi', 'ETL'), ((2021, 10, 20, 15, 0), 3098.86, '15/30/2010/raw/api/verifiedapi?&op=GETCONTENTSUMMARY', 'raw/api/verifiedapi', 'ETL'))
    #df = pd.DataFrame(data, columns=['timestamp', 'size', 'url', 'path', 'type'])
    df = pd.json_normalize(data)
    frmt.formatSlackMessage(df)
if __name__ == "__main__":
    main()
