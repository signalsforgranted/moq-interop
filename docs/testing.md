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

This list should align with the [interop matrix](https://docs.google.com/spreadsheets/d/1C6hf76McVBUfnt84Eb_fY5Gd2qaGn9XLy22BdkTjuCw/edit#gid=0).

| Test | Name | Description |
| 1 | Exchange Setup | Send a ClientSetup and receive a ServerSetup |
| 2 | Exchange Subscribe/Ok | Send a Subscribe and receive a Subsscribe Ok |
| 3 | Receive Object | Send or Receive an Object on an active subscription |
| 4 | Exchange Announce/Ok | Send an Announce and receive an AnnounceOK |
| 5 | Subscribe Hint | Send a Subscribe Hint for non-live edge and receive correct object |
| 6 | Unsubscribe | Unsubscribe from an active subsciption, terminating object flow |
| 7 | Goaway | Drain a connection after receiving a Goaway |

### Handshake - 1, 2, 4

When a handshake is successfully negotiated, that a QUIC connection using the right ALPN was successful and a "SETUP" message was completed. 

### Termination - 6, 7

That for a successful connection a termination signal is sent, acknowledged and the connection closed.

### Subscription - 2, 5, 6

A consumer sends a subscription request that is acknowledged, and later unsubscribed.

