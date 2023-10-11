# Testing Strategy

## General Considerations

To keep the scope of the interop runner focused and prevent any overlap with existing testing there's a few things to do or not do:

* QUIC capabilities - especially those already tested by the QUIC interop runner should not be tested here as it overlaps with the QUIC interop runner, and will double-test implementations.

* Performance and latency measures are out of scope for the time being.

* Fuzz-testing or testing of other failures like corrupted data, loss etc is out of scope for now.

## Tests

> [!NOTE]
> Should these tests be split by implementation capability - so each is done for WebTransport vs RAW QUIC, and for Relay/Producer/Consumer? MoQ Transport should be the same over both.

Implementations should also test to see if they think a given interop test is a pass or fail, and throw non-zero exit (how? TBD).

### Handshake

When a handshake is successfully negotiated, that a QUIC connection using the right ALPN was successful and a "SETUP" message was completed. 

### Termination

That for a successful connection a termination signal is sent, acknowledged and the connection closed.

### Subscription

A consumer sends a subscription request that is acknowledged. 
