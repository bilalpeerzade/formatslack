Presenting data in a clear and organized manner can be a challenge on the Slack platform, as formatting options are limited. 

If you have data stored in JSON, dictionaries, lists, or dataframes that you want to share with your team in a tabular format, it can be frustrating to have code for specific use cases and present the data.

That's where our new library comes in! With our library, you can easily transform your data into a visually appealing table that is easy to read and understand. 

Simply input your data and let the library handle the rest – no need to worry about compatibility issues or spend time in writing code to format the output. 

Our library makes it easy to present your data in a professional and organized way, improving your team's productivity and collaboration on Slack.


USAGE

pip install formatSlackMessage 

example:

#import the installed library

from formatslackmessage import formatslackoutput

import pandas as pd

data=[{"ID":1,"Name":"Alice","Age":25,"Address":{"Street":"123MainStreet","City":"NewYork","State":"NY"}},{"ID":2,"Name":"Bob","Age":30,"Address":{"Street":"456SecondStreet","City":"Chicago","State":"IL"}}]

#convert the list of json to a df

df= pd.json_normalize(data)

#call the function to format your data to a tabular format

formatslackoutput.formatSlackMessage(df)

Output

+----+-------+-----+-----------------+--------------+---------------+
|ID  |Name   |Age  |Address.Street   |Address.City  |Address.State  |
+----+-------+-----+-----------------+--------------+---------------+
|1   |Alice  |25   |123MainStreet    |NewYork       |NY             |
|2   |Bob    |30   |456SecondStreet  |Chicago       |IL             |
+----+-------+-----+-----------------+--------------+---------------+
