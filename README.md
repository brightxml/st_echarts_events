## Streamlit Echarts Events
a bi-directional streamlit components with pyecharts plots

 return event value from js-side to python-side。if no events designed, just display a chart.


### Installation

```python
pip install streamlit-ehcarts-events
```

## Usage
only three steps using it , generate a pyecharts object, passing interested events and parameters

#### inputs:
**chart**: pyecharts object
**events**: list , echarts events, eg. ['click','dblclick']
**params**: list , events value for echarts events,declared in [echarts API DOC](https://echarts.apache.org/en/api.html#events), eg. ['name','data','value']

 #### outputs:
return status and values.
**status**
0: get a value
-1: get no value or an error occurs.
 **return_data**
python dictionary, key is params,value is value for params.


## Example
```python
from pyecharts.charts import Bar
from st_echarts_events import st_echarts_events

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])

import streamlit as st
st.header("Pyecharts Events Feedback Test")    
chart=bar
events=['click']   
params=['name','value','data']
status,return_data = st_echarts_events(chart=chart,events=events,params=params)    
st.markdown("Return data : %s " % return_data)
```

if you want test the package, deploy environment like this:[streamlit template](https://github.com/streamlit/component-template)

## Notes:
if no data. return 'no data.'
if error, return error message.
map are not working well so far, need further implement.


