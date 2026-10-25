#!/usr/bin/env python3
import argparse, html, json
from pathlib import Path

REQUIRED={"meta":["title","author","coverage"],"orientation":["thesis","problem"]}
def validate(data):
    errors=[]
    for section,fields in REQUIRED.items():
        value=data.get(section)
        if not isinstance(value,dict): errors.append(f"{section} must be an object"); continue
        for field in fields:
            if not str(value.get(field,"")).strip(): errors.append(f"{section}.{field} is required")
    if not isinstance(data.get("chapters"),list) or not data["chapters"]: errors.append("chapters must be a non-empty array")
    for key in ("coverage_map","overview","concepts","formulations","critique","reality","actions","glossary","notes"):
        data.setdefault(key,[])
        if not isinstance(data[key],list): errors.append(f"{key} must be an array")
    concept_ids=[]
    for i,item in enumerate(data.get("concepts",[])):
        cid=str(item.get("id","")).strip()
        if not cid: errors.append(f"concepts[{i}].id is required")
        elif cid in concept_ids: errors.append(f"duplicate concept id: {cid}")
        concept_ids.append(cid)
    known=set(concept_ids)
    for i,item in enumerate(data.get("concepts",[])):
        for j,rel in enumerate(item.get("relations",[]) or []):
            target=str(rel.get("target_id","")).strip()
            if not target: errors.append(f"concepts[{i}].relations[{j}].target_id is required")
            elif target not in known: errors.append(f"unknown concept relation target: {target}")
    if str(data.get("meta",{}).get("coverage","")).lower()=="complete":
        coverage=data.get("coverage_map",[])
        if not coverage: errors.append("coverage_map is required when meta.coverage is complete")
        if any(str(row.get("status","")).lower() not in {"read","excluded"} for row in coverage):
            errors.append("complete coverage cannot contain pending or unreadable ranges")
    if errors: raise ValueError("Invalid book data:\n- "+"\n- ".join(errors))

def main():
    p=argparse.ArgumentParser(description="Render an offline interactive book reader from JSON")
    p.add_argument("--data",required=True,type=Path);p.add_argument("--output",required=True,type=Path);p.add_argument("--template",type=Path)
    a=p.parse_args();data=json.loads(a.data.read_text(encoding="utf-8-sig"));validate(data)
    template=a.template or Path(__file__).resolve().parents[1]/"assets"/"reader-template.html"
    source=template.read_text(encoding="utf-8");payload=json.dumps(data,ensure_ascii=False).replace("</","<\\/")
    result=source.replace("{{BOOK_TITLE}}",html.escape(str(data["meta"]["title"]))).replace("{{ACCENT}}",str(data["meta"].get("theme",{}).get("accent","#9E2A24"))).replace("{{BOOK_DATA}}",payload)
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(result,encoding="utf-8");print(f"Rendered {a.output.resolve()}")
if __name__=="__main__": main()
