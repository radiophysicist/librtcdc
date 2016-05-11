import pyrtcdc

peer = pyrtcdc.PeerConnection(None, None, stun_server='stun.services.mozilla.com')
offer = peer.generate_offer()
