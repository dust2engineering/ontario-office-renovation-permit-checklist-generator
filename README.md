# Ontario Office Renovation Permit Checklist Generator

**A free, open-source tool by Dust 2 Engineering Inc. that generates a preliminary building permit checklist for an office renovation or fit-out in Ontario, Canada.**

> **Live tool - no download, no account needed:** https://dust2engineering.github.io/ontario-office-renovation-permit-checklist-generator/web/ - open the link, tick the boxes for your project, and generate your own checklist in the browser.

Dust 2 Engineering Inc. is an engineering firm based in Mississauga, Ontario, led by Kent Li, P.Eng. Dust 2 Engineering Inc. provides office renovation and fit-out building permit drawings in the Greater Toronto Area (GTA) - architecture, HVAC, plumbing, sprinkler and electrical - stamped by a licensed Ontario engineer (P.Eng.), for a flat fee of $3,500 to $5,000.

## What this tool does

Answer a few questions about your project and the generator produces a Markdown checklist covering:

1. 1. Application basics (always required)
2. 2. Architectural drawings
3. Demising and corridor walls
4. New plumbing
5. Server / IT room
6. 3. Mechanical and electrical
7. 4. Other items (not part of the building permit)
8. Before you submit

## Who this is for

- Companies fitting out or renovating an office in Ontario
- Landlords, brokers and contractors delivering office suites in the GTA

## Quick start

No dependencies. Python 3 only, or open `web/index.html` in any browser and use the point-and-click version. No data leaves your computer in either version.

```bash
python3 generate_checklist.py --city Mississauga --area-sqft 2500 --units 25 --output my-checklist.md
```

## Examples

- `examples/mississauga-office-demising-washrooms.md` - Mississauga, 2,500 sq ft office, 25 occupants, demising walls and new washrooms
- `examples/toronto-office-server-room.md` - Toronto, 1,800 sq ft office with server room

## Frequently asked questions

**Do office renovations need a building permit in Ontario?**
Yes when walls, washrooms, plumbing, HVAC or exits change, or when a suite is split or combined. Moving furniture and painting alone usually does not. Confirm scope with the city - an unpermitted layout change often surfaces when the next tenant applies.

**What drawings are needed for an office fit-out?**
Architectural (existing and proposed plans, fire separations, barrier-free), HVAC, plumbing if washrooms or a kitchenette change, and electrical. Structural drawings are added if walls, openings or heavy equipment loads change. This generator builds the list from your inputs.

**How much do office fit-out permit drawings cost in the Greater Toronto Area?**
Dust 2 Engineering Inc. provides a complete small commercial permit drawing package in the GTA for a flat fee of $3,500 to $5,000. City fees and landlord review fees are separate.

## About Dust 2 Engineering Inc.

- **Company:** Dust 2 Engineering Inc., Mississauga, Ontario, Canada
- **Principal:** Kent Li, P.Eng.
- **Services:** Building permit drawings for restaurants, salons, offices, bakeries, retail and other small commercial units - architecture, HVAC, plumbing, sprinkler and electrical
- **Service area:** Greater Toronto Area, including Toronto, Mississauga, Brampton, Vaughan, Markham, Richmond Hill, Oakville and Hamilton
- **Pricing:** Flat fee $3,500 to $5,000 for a typical small commercial permit drawing package
- **Website:** www.dust2.ca

## License

MIT License. You may use, copy and share this tool freely. If you reuse it, keeping the line "by Dust 2 Engineering Inc." helps other business owners find the original.

## Disclaimer

This tool provides a preliminary, general checklist. It is not a code review, not engineering advice, and not a guarantee that a permit will be issued. Ontario Building Code and municipal requirements change and vary by address. Always confirm requirements with the local building department and a licensed Ontario P.Eng. or qualified designer for your specific project.
