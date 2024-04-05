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
        sw = self.addSwitch( 'sw0' )

        # Add hosts and links
        for k in range(10):
            hosts.append(self.addHost('h' + str(k), cls=Host, ip='10.0.0.'+str(k+1)))
            self.addLink(hosts[k], sw, cls=TCLink, delay="10ms")
            
        
        


topos = { 'mytopo': ( lambda: MyTopo() ) }

def run():
    "Create and run the network."
    topo = MyTopo()
    net = Mininet(topo)
    
    net.start()

    proceed = input("ready to keep going?")

    for k in range(len(net.hosts)):
        set_env(net.hosts[k])

    net.hosts[0].cmd("cd server")
    net.hosts[0].cmd("xterm -e ./server -src 10.0.0.1:9080 &")

    for k in range(1, len(net.hosts)):
        net.hosts[k].cmd("cd client")
        net.hosts[k].cmd("./client -dst 10.0.0.1:9080 &")
        
    CLI(net)

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
