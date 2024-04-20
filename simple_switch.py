from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER , MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet


class ExampleSwitch13(app_manager.RyuApp):
    OFP_VERSIONS=[ofproto_v1_3.OFP_VERSION] #using openflow version 1.3

    def __init__(self, *args, **kwargs):
       super(ExampleSwitch13,self).__init__(*args,**kwargs)
       #initialize mac  address table
       self.mac_to_port={}

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER) #registers method as a event handler for the EventOFSwitchFeatures 
    def switch_features_handler(self,event):
        """
        this event will be called when a new switch connects to the node and
        features are being negotiated.  CONFIG_DISPATCHER indicates that the 
        handler should be invokved during the switch configurations stage.
        """
        databath =event.msg.datapath #recieves the datapath obj
        ofproto =datapath.ofproto #ofproto = openflow protocol version used by switch
        parser=datapath.ofproto_parser  #retrieves the parser object associated with openflow
        
        #install table miss flow entry
        match = parser.OFPMatch()
        actions= [parser.OFPActionOutput(ofproto.OFPIT_APPLY_ACTIONS,actions)]  # A list containing a single action, which is to send the packet to the controller 

        self.add_flow(datapath,0,match,actions) 
        #This line calls the add_flow method to install a flow entry on the switch. It passes the datapath object, priority 0, the match criteria,
        #and the actions to be executed when a packet matches the criteria.

            
                                                 
