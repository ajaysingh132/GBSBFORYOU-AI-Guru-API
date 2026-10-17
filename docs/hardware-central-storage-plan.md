# Hardware, Central Storage and Data Governance Plan

## Objective

Operate four workstations from a central, access-controlled data store. Keep the authoritative copy of approved files in one location, minimize unnecessary local copies, and maintain a separate recoverable backup.

## Proposed initial design

- 3 general workstations: 16–32 GB RAM and 512 GB–1 TB SSD.
- 1 engineering workstation: 32–64 GB RAM and 1 TB SSD, suitable for code and data preparation; do not assume it can train a large model from scratch.
- 1 four-bay NAS or equivalent central file server.
- Four NAS-grade 4 TB drives in a suitable redundant configuration, subject to vendor compatibility checks.
- Two separate backup drives or a separately located backup target.
- Gigabit/2.5GbE switch and appropriate cabling.
- UPS for NAS/network equipment.
- Per-user accounts, least-privilege permissions, encryption where supported, audit logs, versioned backups, and periodic restore tests.

## Capacity and RAID notes

Four 4 TB drives provide 16 TB raw decimal capacity. With RAID 5, roughly one drive's capacity is used for parity, leaving about 12 TB decimal before filesystem overhead (approximately 10.9 TiB). Actual usable capacity depends on configuration.

RAID protects against some drive failures but is not a backup. Maintain a separate backup and test restoration. If the project grows beyond the backup target's capacity, expand backup capacity before adding more source data.

## Folder layout

~~~text
GBSBFORYOU-CENTRAL/
├── 00_ADMIN/                 # policies, budget, approvals
├── 01_RESEARCH/              # papers, notes, reference records
├── 02_LANGUAGE_DATA/         # source inventory, approved data, cleaned data
├── 03_MODEL_DEVELOPMENT/     # code, tokenizer, configs, logs
├── 04_MODEL_CHECKPOINTS/     # large model checkpoints; access-controlled
├── 05_EVALUATION/            # held-out test data, reports
├── 06_AI_AGENTS/             # profiles, task records, outputs
├── 07_GBSBFORYOU_PROJECTS/   # separate folders per project
├── 08_RELEASES/              # reviewed release artifacts
└── 09_TEMPORARY/             # automatically purged working files
~~~

## Data-handling rules

1. Central storage holds the authoritative copy; local downloads are working copies only.
2. Never store API keys, passwords, or private credentials in the repository or shared folders.
3. Do not ingest personal, sensitive, or restricted data without a documented lawful basis and approval.
4. Every dataset needs source, date, language, license, allowed use, size, quality status, and version recorded.
5. Large checkpoints may be copied temporarily to a training environment for performance; record the location and remove the copy after verification.
6. Configure a retention period for temporary files and test deletion rules before applying them to valuable data.
7. Keep at least one backup offline or isolated from routine workstation access.
8. Test recovery on a schedule; do not assume a successful backup job proves that files can be restored.
9. Do not sync all research data into GitHub. Use Git for code and small metadata; keep large datasets and private materials in controlled storage.
10. Separate project permissions; a contributor or AI agent should access only the folders required for its assigned work.

## Planning budget

The main first-year budget includes a ₹2.15 lakh planning allowance for central storage, backup, network, UPS, and setup. This is not a purchase order. Obtain three written quotes and confirm warranty, drive compatibility, capacity, taxes, and delivery to Bhopal before purchase.

Retail examples observed during budget preparation:
- Synology DS423 4-bay enclosure listing: https://www.primeabgb.com/online-price-reviews-india/synology-diskstation-ds423-4-bay-nas-enclosure/
- QNAP TS-464 8 GB listing: https://www.mdcomputers.in/product/qnap-nas-enclosure-ts-464-8g
- WD Red Plus 4 TB NAS drive listing: https://www.golchha.com/

Prices and stock can change. The final bill of materials should record quote date, GST, shipping, warranty, and seller.
