# Incident and rollback checklist

1. **Hold:** stop expansion and unrelated changes. Name the incident operator.
2. **Identify:** record current image, configuration, impact, first observed time and request IDs.
3. **Contain:** disable the optional feature if that addresses the fault. Avoid changing multiple variables at once.
4. **Recover:** restore the recorded known-good image and compatible configuration using the rehearsed procedure.
5. **Verify:** run smoke checks, check the expected version, and inspect errors and latency over the agreed window.
6. **Communicate:** record impact, recovery time and remaining limitations for the affected people.
7. **Learn:** preserve sanitized evidence and create a corrective change with a regression test.

Rollback does not revoke leaked credentials, unsend messages, or reverse a database migration.
A credential leak needs revocation/rotation. Data damage may need a tested backup restore
or forward fix. Preserve evidence and obtain the appropriate operational authority.
