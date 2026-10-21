# H7 mutation audit

Baseline: {"exit_code": 0, "states": 32, "transition_rows": 92, "invariant_errors": 0, "tests_passed": 14, "tests_total": 14, "stdout_file": "/workspace/scratch/a6ca59e05764/ct000-audit-v5/evidence/mutations/baseline.stdout.txt", "author_accepts": true}

| Case | Targets | Category | H7 errors | H7 tests | Exit | Author criterion |
|---|---|---|---:|---|---:|---|
| M01_no_capacity_lock | T13 | unsafe_action | 0 | 14/14 | 0 | ACCEPT |
| M02_reaper_without_guard | T19, T20 | unsafe_action | 0 | 14/14 | 0 | ACCEPT |
| M03_unbounded_but_word_tran | T17 | unsafe_action | 0 | 14/14 | 0 | ACCEPT |
| M04_resend_unsafe | T24 | unsafe_action | 0 | 14/14 | 0 | ACCEPT |
| M05_cancel_without_revoke | T90 | unsafe_action | 0 | 14/14 | 0 | ACCEPT |
| M06_discard_late_evidence | T70 | unsafe_action | 0 | 14/14 | 0 | ACCEPT |
| M07_claim_guard_always_true | T10, T11, T12, T13 | unsafe_guard_definition | 0 | 14/14 | 0 | ACCEPT |
| M08_absent_means_not_done | T64 | unsafe_guard_definition | 0 | 14/14 | 0 | ACCEPT |
| M09_invalid_holder_and_timer | state:Đang chạy | unsafe_state_metadata | 0 | 14/14 | 0 | ACCEPT |
| M10_terminal_without_cleanup | T41 | unsafe_action | 0 | 14/14 | 0 | ACCEPT |
| M11_remove_all_value_definitions | Bảng Giá trị:all rows | missing_guard_definitions | 0 | 14/14 | 0 | ACCEPT |
| C01_delete_T13 | T13 | positive_control | 6 | 11/14 | 0 | REJECT |
| C02_empty_holder | state:Đang chạy | positive_control | 1 | 14/14 | 0 | REJECT |
| C03_unbounded_without_word_tran | T17 | positive_control | 1 | 14/14 | 0 | REJECT |

Totals: {"unsafe_mutations": 11, "unsafe_accepted": 11, "controls": 3, "controls_rejected": 3, "all_process_exit_codes_zero": true}

Audit verdict: {"exit_code": 1, "failure_reasons": ["unsafe_mutation_accepted", "H7_reported_failure_but_exited_zero"], "scope": "Static checker audit only; a clean baseline is not deployment or live PostgreSQL PASS."}

Original source snapshots unchanged: True

The accepted mutations demonstrate blind spots in the checker, not that those malicious mutations are present in the source.
No deployment, PostgreSQL write, remote write, or change to the original H7 Python code was performed.
