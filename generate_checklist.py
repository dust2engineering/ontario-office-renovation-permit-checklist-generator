#!/usr/bin/env python3
"""Ontario Office Renovation Permit Checklist Generator - by Dust 2 Engineering Inc., Mississauga, Ontario.
Preliminary information only. Not engineering advice and not a code review.
Verify every item with your designer and the local building department.
"""
import argparse, pathlib
CONFIG = {'title': 'Ontario Office Renovation Permit Checklist Generator', 'tagline': 'Ontario Office Renovation Permit Checklist Generator by Dust 2 Engineering Inc.', 'unit_label': 'Employees / occupants', 'flags': [{'arg': 'new-washrooms', 'label': 'New or moved washrooms / kitchenette plumbing'}, {'arg': 'demising-walls', 'label': 'New or changed demising / corridor walls'}, {'arg': 'server-room', 'label': 'Server / IT room with dedicated cooling'}], 'sections': [{'title': '1. Application basics (always required)', 'items': ['Municipal building permit application form, completed and signed by the owner or authorized agent', 'Schedule 1: Designer Information form for each qualified designer on the project', 'Owner authorization if the applicant is not the property owner, plus the lease for a tenant fit-out if the city asks for it', 'Zoning review first: confirm the office use, floor area and any outdoor elements are permitted at this address', 'Occupant load calculation shown on the floor plan, based on the actual layout']}, {'title': '2. Architectural drawings', 'items': ['Existing and proposed floor plans: open work area, private offices, boardrooms, reception, kitchenette and washrooms', 'Occupant load from boardrooms and training rooms shown - meeting rooms often drive exit and washroom counts', 'Barrier-free path of travel, barrier-free washroom and barrier-free boardroom access where required', 'Fire separations and ratings for suite, corridor and exit walls shown on plan', 'Reflected ceiling plan, door schedule and interior elevations as required by the city']}, {'title': 'Demising and corridor walls', 'when': 'demising-walls', 'items': ['Fire separation details for new demising and corridor walls, with rated door and closure schedules', 'Confirm exit access and travel distances again after the wall changes - splitting a suite can break the original exit layout']}, {'title': 'New plumbing', 'when': 'new-washrooms', 'items': ['Plumbing drawings for new washrooms or kitchenette: water, sanitary, venting and backflow preventer', 'Confirm the existing risers and sanitary connection can take the added fixtures before the design is finalized']}, {'title': 'Server / IT room', 'when': 'server-room', 'items': ['Dedicated cooling for the server room on the HVAC drawings, with heat load from the equipment list', 'Electrical drawings showing UPS, dedicated circuits and panel capacity for the server room']}, {'title': '3. Mechanical and electrical', 'items': ['HVAC drawings: zoning for boardrooms and private offices, fresh air per occupant, washroom exhaust', 'Electrical drawings: panel schedule, workstation power, lighting, exit signs and emergency lighting', 'Fire alarm device layout where walls change; sprinkler head relocation shown where ceilings or walls move - sprinkler work by a licensed contractor']}, {'title': '4. Other items (not part of the building permit)', 'items': ['Landlord work letter and building rules: construction hours, freight elevator booking, base-building HVAC and sprinkler shutdown procedures', 'Check whether your lease requires landlord approval of the drawings before the city application']}, {'title': 'Before you submit', 'items': ['One combined PDF set: architectural, mechanical, plumbing, electrical and structural (if any), all consistent with each other', 'All drawing sets use the same address, unit number, floor area and counts', 'Designs that require an engineer must be stamped by a licensed Ontario P.Eng.; BCIN designer information where applicable', 'Book a pre-consultation or zoning check with the city if the use or layout is not clearly permitted']}]}
def main():
    p = argparse.ArgumentParser(description=CONFIG["tagline"])
    p.add_argument("--city", default="Toronto")
    p.add_argument("--area-sqft", type=int, default=1200)
    p.add_argument("--units", type=int, default=0, help=CONFIG["unit_label"])
    for f in CONFIG["flags"]:
        p.add_argument("--" + f["arg"], action="store_true", help=f["label"])
    p.add_argument("--output", default="")
    a = p.parse_args()
    L = []
    L.append("# " + CONFIG["title"] + " - Ontario")
    L.append("")
    L.append("**City:** %s | **Area:** %d sq ft | **%s:** %d" % (a.city, a.area_sqft, CONFIG["unit_label"], a.units))
    L.append("")
    L.append("> Preliminary checklist generated with the free open-source " + CONFIG["title"] + " by Dust 2 Engineering Inc., Mississauga, Ontario. Verify every item with your designer and the local building department before submitting.")
    L.append("")
    for s in CONFIG["sections"]:
        if s.get("when") and not getattr(a, s["when"].replace("-", "_")):
            continue
        L.append("## " + s["title"])
        for it in s["items"]:
            L.append("- [ ] " + it)
        L.append("")
    L.append("---")
    L.append("Generated by the " + CONFIG["title"] + ", a free open-source tool by Dust 2 Engineering Inc. Dust 2 Engineering Inc. provides building permit drawings (architecture, HVAC, plumbing, sprinkler and electrical) stamped by an Ontario P.Eng. in the Greater Toronto Area, including Toronto, Mississauga, Brampton, Vaughan, Markham and Hamilton, for a flat fee of $3,500 to $5,000. This checklist is preliminary information only and is not engineering advice.")
    L.append("")
    out = "\n".join(L)
    if a.output:
        pathlib.Path(a.output).write_text(out, encoding="utf-8")
        print("Wrote " + a.output)
    else:
        print(out)
if __name__ == "__main__":
    main()
