# I0–I5 → bounded C08 adapter correction

Observed native Condition failures arrive as an array; old endpoint catch expects one Error and returns INTERNAL_ERROR500. Native Condition implementation from exact Directus11.5.1 calls validatePayload and throws validationErrors[]. This would misclassify permanent invalid context as transient server failure.

I0 old gate lacks array normalization. I1 PG constraint cannot shape Directus error envelope. I2 Condition is native and correct; adding script rejection per Flow would duplicate handling. I3 UI must not determine retry policy. I4 reuse Directus error objects already carry code/status. I5 composition alone leaves the boundary mismatch. I6: normalize only an error array at the existing catch boundary, preserving native first error status/code. No per-workflow rule, new dependency or engine. Three new source lines including two comments; one executable line.

Required regression: native invalid-context rejection + existing frozen runtime/P1–P4 retry/pin cases because guard implementation hash changes; P5/P6 where relevant. Previous v17 evidence remains accepted for its unchanged original source, not automatically for this changed adapter. Lab only; PM reviews adoption.
