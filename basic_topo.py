from mininet.net import Mininet
from mininet.node import Host
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.topo import Topo

from set_env import set_env

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'h1', cls=Host, ip='10.0.0.1' )
        h2 = self.addHost( 'h2', cls=Host, ip='10.0.0.2' )
        leftSwitch = self.addSwitch( 's3' )

        # Add links
        self.addLink( h1, leftSwitch )
        self.addLink( leftSwitch, h2 )


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
