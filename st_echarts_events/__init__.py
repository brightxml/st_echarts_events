import os
from typing import List
import streamlit.components.v1 as components
from pyecharts.charts.chart import Base
import demjson
import  streamlit as st
# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("st_echarts_events"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "st_echarts_events",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_echarts_events", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.

def st_echarts_events(chart:Base,events:List=['click'],params:List=['name']):
    """Create a new instance of "st_echarts_events".

    Parameters
    ----------
    chart: pyecharts
        an pyecharts object, like Bar().
    events: list
        events in echarts, see official API. eg.['click']
    params:list
        property of events, eg. ['name','data']
    Returns
        status, return_data
        status:
         0: get a value
        -1: get no value or an error occurs.
        return_data:
        python dictionary, key is params,value is value for params.
    
    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    import  json
    options=chart.dump_options_with_quotes()
    events_dict={k:k for k in events} if params else {'click':None}
    params_dict={k:k for k in params  } if params else {'name':None}
    
    
    events_data = _component_func(
        options=options,
        events=json.dumps(events_dict),
        keys=json.dumps(params_dict)
    )
            
    if events_data:
        try:
            events_dict_data=demjson.decode(events_data) 
            status=0
            return_data=events_dict_data
        except Exception as e:
            status=-1
            return_data=e
    else:
        status=-1
        return_data='no data.'
    return status,return_data
    
      


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run st_echarts_events/__init__.py`

if not _RELEASE:    
    from pyecharts.charts import Bar

    bar = Bar()
    bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    
    import streamlit as st
    st.header("Pyecharts Events Feedback Test")    
    chart=bar
    events=['click']   
    status,msg = st_echarts_events(chart=chart,events=events,params=['name','value','data'])    
    st.markdown("return data : %s " % msg)
    st.json(chart.get_options())
    

