# Testing Strategy

## General Considerations

To keep the scope of the interop runner focused and prevent any overlap with
existing testing there's a few things to do or not do:

* QUIC capabilities - especially those already tested by the QUIC interop runner
should not be tested here. This may also include future capabilities such as
multipath.

* Performance and latency measures are out of scope for the time being.

* Fuzz-testing or testing of other failures like corrupted data, loss etc is
out of scope for now.

## Tests

TODO: Should these tests be split by implementation capability - so each is done
for WebTransport vs RAW QUIC, and for Relay/Producer/Consumer?

### Handshake

When a handshake is successfully negotiated, that a QUIC connection using
the right ALPN was successful and a "SETUP" message was completed. 

### Termination

That for a successful connection a termination signal is sent, acknowledged and
the connection closed.

### Subscription

A consumer sends a subscription request that is acknowledged. 
