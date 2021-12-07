import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"
import ReactEcharts from "echarts-for-react"


interface EVENT_DATA{
  event_data:Map<string,object>;
}
class StreamlitEchartsEvents extends StreamlitComponentBase<EVENT_DATA> {
  

  public render = (): ReactNode => {
      // Arguments that are passed to the plugin in Python are accessible
      // via `this.props.args`.
      const options =JSON.parse(this.props.args["options"])
      const events_dict=JSON.parse(this.props.args["events"])
      const params_dict=JSON.parse(this.props.args["keys"])


      //event_values store events data ,which in echarts, params.*, 
      //filtered by 'keys' 
      const event_values:any={}
      const PARAM_KEYS=Object.keys(params_dict)  
      
      //event_handler. in event, we stored property of user-designed params .
      function handle_event(params:any){     
        for (var p in params){          
            if (PARAM_KEYS.indexOf(p)!==-1){
              event_values[p]=params[p]
            }
                
        }       

      //converting object to json
        let data=JSON.stringify(event_values)    
      //return value to python side    
        Streamlit.setComponentValue(data)
      }
   
      //return event_handler to event
      for ( let event  in events_dict){
        events_dict[event]=handle_event           
      }

      return (
          <ReactEcharts
            option={options}
            notMerge={true}
            lazyUpdate={true}            
            onEvents= {events_dict}
          />
        
      )
  }

 
}


export default withStreamlitConnection(StreamlitEchartsEvents)
