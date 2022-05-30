from typing import Any
from flow import Flow
from network import NetworkType

Node = Any


def maximal_flow(network: NetworkType, s: Node, t: Node) -> Flow:
    """
    Renvoie le flot maximal sur le réseau `network` entre la source `s` et la cible `t`.

    INPUT :

        - network, un réseau de type Network
        - s, le sommet source
        - t, le sommet cible

    OUTPUT : un objet Flow de valeur maximale sur le réseau.
    """
    # Initialisation par le flot vide
    F = Flow(network, s, t, check=False)
    
    # Tant qu'il y a des chaînes augmentantes on met à jour le flot
    chain = F.find_augmenting_path()
    while chain is not None:
        F.increase_augmenting_path(chain)
        chain = F.find_augmenting_path()
        
    return F