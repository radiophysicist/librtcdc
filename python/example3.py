#!/usr/bin/env python
# -*- coding: utf-8 -*-#

def on_candidate(peer, candidate):
    print candidate


if __name__ == "__main__":
    print("Starting...")
    import pyrtcdc
    # Если stun_server не задать, то падает при инициализации PeerConnection
    # C ошибкой corrupted double-linked list
    peer = pyrtcdc.PeerConnection(on_candidate=on_candidate,
                                  stun_server='stun.ekiga.net')
    offer = peer.generate_offer()
    print("Exiting...")
