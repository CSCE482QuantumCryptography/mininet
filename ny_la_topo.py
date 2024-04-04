from mininet.net import Mininet
from mininet.node import Host
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.topo import Topo

from set_env import set_env

class MyTopo( Topo ):
    "Topology example for New Yok host communicating to Los Angeles host, total latency ~110ms."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        NY_host = self.addHost( 'NY_host', cls=Host, ip='10.0.0.1' )
        LA_host = self.addHost( 'LA_host', cls=Host, ip='10.0.0.2' )
        sw = self.addSwitch( 'sw2' )

        # Add links
        self.addLink( NY_host, sw, cls=TCLink, delay="55ms")
        self.addLink( sw, LA_host, cls=TCLink, delay="55ms")
    


topos = { 'mytopo': ( lambda: MyTopo() ) }

def run():
    "Create and run the network."
    topo = MyTopo()
    net = Mininet(topo)
    
    net.start()

    set_env(net.hosts[0])
    set_env(net.hosts[1])

    CLI(net)

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
