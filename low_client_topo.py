from mininet.net import Mininet
from mininet.node import Host
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.topo import Topo

from set_env import set_env


class MyTopo( Topo ):
    "Topology example for host communicating to with multiple clients simultaneously, total clients: 10"

    def build( self ):
        "Create custom topo."

        hosts = []

        # Add hosts and switches
        for k in range(10):
            hosts.append(self.addHost('h' + str(k), cls=Host, ip='10.0.0.'+str(k+1)))

        sw = self.addSwitch( 'sw0' )

        # Add links
        for k in range(1, 10):
            self.addLink(hosts[k], sw, cls=TCLink, delay="10ms")
        
        self.addLink(hosts[0], sw, cls=TCLink, delay="10ms")
        


topos = { 'mytopo': ( lambda: MyTopo() ) }

def run():
    "Create and run the network."
    topo = MyTopo()
    net = Mininet(topo)
    
    net.start()

    for k in range(len(net.hosts)):
        set_env(net.hosts[k])

    net.hosts[0].cmd("h0 cd server")
    net.hosts[0].cmd("h0 ./server -src 10.0.0.1:9080")

    for host in range(1, 10):
        net.hosts[host].cmd(str(net.hosts[host]) + " cd client")
        net.hosts[host].cmd(str(net.hosts[host]) + " ./client -dst 10.0.0.1:9080")

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
