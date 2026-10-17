# GBSBFORYOU Native Language Model v0.1 — First-Year Budget

**Budget date:** 17 October 2026  
**Currency:** INR  
**Period:** 12 months  
**Status:** Planning estimate for expert/institutional review; not a vendor quotation, payroll offer, or grant sanction.

## Executive budget

| Category | First-year estimate |
|---|---:|
| Four human supervisors — gross salary budget | ₹40,20,000 |
| Employer/statutory/benefit provision (15% planning allowance) | ₹6,03,000 |
| Shared AI agent tooling/API allowance | ₹1,80,000 |
| Internet | ₹36,000 |
| Electricity and routine power cost | ₹60,000 |
| GPU/cloud compute reserve | ₹5,00,000 |
| Four workstations/computers | ₹3,15,000 |
| Monitors and peripherals | ₹50,000 |
| Central NAS, disks, separate backup, network and UPS | ₹2,15,000 |
| Dataset preparation, legal/license review, and data tooling | ₹1,50,000 |
| External expert review/workshops | ₹1,50,000 |
| Research/partner travel | ₹1,00,000 |
| Hosting, domain, monitoring, security and backup software allowance | ₹50,000 |
| **Subtotal before contingency** | **₹64,34,000** |
| Contingency (10%) | ₹6,42,900 |
| **Total first-year planning budget** | **₹70,71,900** |

**Rounded planning request: ₹70.72 lakh (about ₹70.7 lakh) for 12 months.**

This total excludes office rent, founder/director salary, taxes not captured in supplier prices, major legal proceedings, and compute demand above the ₹5 lakh reserve. If operated remotely or through a host institution, rent can be avoided or separately provided in-kind.

## A. Human supervisor salary assumptions

These are planning allowances for experienced technical roles in a small project, not verified offers or a guarantee of local market salary. Before grant submission, obtain local salary benchmarks and recruitment estimates.

| Role | Monthly gross assumption | 12-month gross |
|---|---:|---:|
| H1 — Research & Architecture Supervisor | ₹80,000 | ₹9,60,000 |
| H2 — Data & Indian Language Supervisor | ₹60,000 | ₹7,20,000 |
| H3 — Model Engineering Supervisor | ₹1,25,000 | ₹15,00,000 |
| H4 — Quality, Safety & Documentation Supervisor | ₹70,000 | ₹8,40,000 |
| **Total** | **₹3,35,000/month** | **₹40,20,000** |

A 15% provision (₹6.03 lakh/year) is reserved for employer costs, benefits, statutory contributions, recruitment or payroll overhead as applicable. The exact requirement must be confirmed by a payroll/accounting professional for the final employment structure.

The project director/founder is not assigned a salary in this draft. Add one only if the applicant organization, grant rules, and approved work plan permit it.

## B. Twelve AI roles are not twelve salaried staff

The twelve A1–A12 entries are task roles for AI-assisted workflows. The budget therefore uses a **shared ₹15,000/month allowance** for model/API use, workflow execution, and related tooling—not a fictitious salary for each agent. The actual cost could be lower with local scripts and free tiers, or higher if paid inference is used heavily. Each provider and usage cap must be documented before activation.

## C. Computer and storage bill of materials

| Item | Quantity | Budget assumption | Total |
|---|---:|---:|---:|
| Standard office workstation, 16–32 GB RAM, 512 GB–1 TB SSD | 3 | ₹55,000 each | ₹1,65,000 |
| Engineering workstation for coding/data processing (not assumed to train a large model locally) | 1 | ₹1,50,000 | ₹1,50,000 |
| Monitors, keyboard/mouse, peripherals | 4 sets | Combined allowance | ₹50,000 |
| Central storage and backup package | 1 | NAS, 4 NAS-grade drives, two separate backup drives, switch/cables, UPS/setup | ₹2,15,000 |

Observed retail examples checked for this planning draft:
- Synology DS423 4-bay enclosure listed at about ₹44,436 by PrimeABGB: https://www.primeabgb.com/online-price-reviews-india/synology-diskstation-ds423-4-bay-nas-enclosure/
- QNAP TS-464 8 GB 4-bay NAS listed at about ₹72,400 by MDComputers: https://www.mdcomputers.in/product/qnap-nas-enclosure-ts-464-8g
- WD Red Plus 4 TB NAS drive listing observed around ₹20,603: https://www.golchha.com/ (search exact model WD Red Plus 4TB before ordering; listing and availability may change).

Prices are time-sensitive; stock, delivery to Bhopal, GST and invoice conditions must be confirmed. Obtain at least three written quotations before procurement. A RAID array is not a backup. Configure access controls, UPS, versioned backup, and at least one offline or separately located copy. Four 4 TB drives in RAID 5 provide roughly 12 TB decimal before filesystem overhead; actual usable capacity depends on configuration.

The engineering workstation is for development and data preparation; **the budget does not assume it can train a large language model from scratch**. The ₹5 lakh GPU reserve is provisional. First request compute estimates and eligibility review through IndiaAI Compute or a qualified academic/incubator partner; do not commit cloud spend without written approval.

## D. Operating assumptions

- Remote-first; no office rent included.
- Free/open-source tools prioritized.
- Four human supervisors assumed full-time for 12 months.
- No separate salary assigned to AI agent profiles.
- One shared AI/tooling allowance, subject to usage caps.
- Dataset purchases are not assumed; the data/legal allowance covers review and preparation, not blanket rights to third-party data.
- GPU compute is a capped reserve, not a quote or guaranteed allocation.
- Contingency is not permission to spend; each use requires approval.

## E. Funding plan: seek modular support

The full ₹70.8 lakh estimate should not be presented as though a single government scheme will necessarily fund it. Seek a combination of prototype grant or incubator support for a narrowly defined pilot, subsidized/in-kind GPU compute, university or research-lab mentorship and evaluation, hardware/cloud credits, and further funding only after a reproducible pilot and independent evaluation.

Official scheme ceilings and eligibility can change. Check the latest official guidelines before applying:
- IndiaAI Compute Portal: https://compute.indiaai.gov.in/
- DST NIDHI-PRAYAS 2.0: https://nidhi.dst.gov.in/prayas2-0/
- NIDHI-PRAYAS 2.0 guidelines: https://nidhi.dst.gov.in/document/nidhi-prayas-2-0-program-guidelines/

## F. Approval gates before money is committed

1. H1 validates architecture and estimates GPU hours.
2. H2 validates candidate dataset rights and preparation costs.
3. H3 supplies a bill of materials and reproducible compute benchmark.
4. H4 reviews risk, licensing, security and evaluation design.
5. Project director approves final procurement and spending caps.
6. Any funder-specific budget is reconciled to the funder's permitted cost heads before submission.
