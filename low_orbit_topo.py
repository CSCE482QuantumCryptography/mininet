from mininet.net import Mininet
from mininet.node import Host
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.topo import Topo

from set_env import set_env

class MyTopo( Topo ):
    "Topology example for host communicating to with low orbit satellite, total latency ~25ms"

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'h1', cls=Host, ip='10.0.0.1' )
        satellite = self.addHost( 'h2', cls=Host, ip='10.0.0.2' )
        sw = self.addSwitch( 'sw2' )

        # Add links
        self.addLink( h1, sw, cls=TCLink, delay="15ms", bw=300)
        self.addLink( sw, satellite, cls=TCLink, delay="10ms", loss=1, bw=300)
    


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
